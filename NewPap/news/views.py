from django.shortcuts import render
from django.shortcuts import get_object_or_404  # вернутьобъект или 404
from django.core.paginator import Paginator
from django.views.generic import ListView

from .models import Post


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
    return render(reqest, 'detail.html', {'post': post})
