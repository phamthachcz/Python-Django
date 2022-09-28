from django import forms
from posts.models import Post, Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['author', 'body']

class PostEditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'body', 'image', 'sport_name']