from django.shortcuts import render
from django.shortcuts import get_object_or_404  # вернутьобъект или 404
from django.core.paginator import Paginator

from .models import Post


# def post_list(request):
#     post_list = Post.published.all()
#     paginator = Paginator(post_list, 6)
#     page_number = request.GET.get('page', 1)
#     posts = paginator.page(page_number)
#     return render(request, 'list.html', {'posts': posts})


def post_detail(reqest, pk):
    post = get_object_or_404(Post, id=pk, status=Post.Status.PUBLISHED)
    return render(reqest, 'detail.html', {'post': post})
