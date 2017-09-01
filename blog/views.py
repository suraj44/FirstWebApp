from django.shortcuts import render
from .models import Post
from django.utils import timezone
from .models import Post
def post_list(request):
	#posts is the name of the query set
	posts = Post.objects.filter(published_data__lte = timezone.now()).order_by('published_data');
	return render(request, 'blog/post_list.html',{'posts':posts})
