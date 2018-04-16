from django.shortcuts import render
from . models import Comment
def home_page(request):
    if request.method == 'POST':
        our_comment = request.POST.get('comment')
        our_user = request.POST.get("username")
        comment_obj = Comment.objects.create(
            comment=our_comment,
            user=our_user
        )

        return render(request, 'blog/home_page.html', {'comment': comment_obj,})
    return render(request, 'blog/home_page.html')