from .models import Post
from django.shortcuts import render
from django.shortcuts import get_object_or_404  # вернутьобъект или 404
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.core.mail import send_mail
from .forms import EmailPostForm, CommentForm
from django.views.decorators.http import require_POST

# def post_list(request):
#     post_list = Post.published.all()
#     paginator = Paginator(post_list, 6)
#     page_number = request.GET.get('page', 1)
#     posts = paginator.page(page_number)
#     return render(request, 'list.html', {'posts': posts})


class Post_List(ListView):
    queryset = Post.published.all()
    template_name = 'list.html'
    context_object_name = 'posts'
    paginate_by = 6


def post_detail(reqest, year, month, day, post):
    post = get_object_or_404(Post, slug=post, publ__year=year,
                             publ__month=month, publ__day=day, status=Post.Status.PUBLISHED)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    return render(reqest, 'detail.html', {'post': post, 'comments': comments, 'form': form})


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read" \
                f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'test.niolmo@yandex.ru', [cd['to']])
        sent = True
    else:
        form = EmailPostForm()
    return render(request, 'share.html', {'post': post, 'form': form, 'sent': sent})


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request, 'detail.html', {'post': post, 'form': form, 'comment': comment})
