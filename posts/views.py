from django.shortcuts import render, get_object_or_404
from posts.models import Post, Sport, Comment
from posts.forms import CommentForm, PostEditForm
from django.http import HttpResponse

def post_list(request, sport_name):
	sports = Sport.objects.all()
	sport = get_object_or_404(Sport,name=sport_name)
	posts = sport.post_set.all().order_by('-date')
	return render(request, 'post_list.html', {'sport': sport, 'posts':posts, 'sports': sports})

def post_detail(request,sport_name,post_id):
	sports = Sport.objects.all()
	post = get_object_or_404(Post, pk=post_id)
	comments = Comment.objects.filter(post=post)
	comment_form = CommentForm()
	if request.method == 'POST':
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			comment_author = comment_form.cleaned_data['author']
			comment_body = comment_form.cleaned_data['body']
			comment = Comment(post=post, author=comment_author, body=comment_body)
			comment.save()
			comment_form = CommentForm()

	return render(request, 'post_detail.html', {'sports':sports, 'post': post, 'comments':comments, 'comment_form':comment_form})

def edit_post(request, post_id):
	sports = Sport.objects.all()
	post = get_object_or_404(Post, pk=post_id)
	edit_form = PostEditForm(instance=post)
	if request.method == 'POST':
		edit_form = PostEditForm(request.POST, instance=post)
		if edit_form.is_valid():
			edit_form.save()
			edit_form = PostEditForm()
	return render(request, 'edit_post.html', {'sports': sports, 'post': post, 'edit_form':edit_form})
# Create your views here.
