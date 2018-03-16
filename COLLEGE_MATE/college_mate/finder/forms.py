from django import forms
from finder.models import Post,FinderStatus,FinderStatus2


class FinderForm(forms.ModelForm):
	 post=forms.CharField(max_length=255)
	 class Meta:
		 model=Post
		 fields=('post',
				'image',
				)


class StatusForm(forms.ModelForm):
	CHOICES=(
	('Available','Available'),
	('Nope','Not Available'),
	)



	class Meta:
		model = FinderStatus
		fields = (
		'apron',
		)


class StatusForm2(forms.ModelForm):
	CHOICES=(
	('Available','Available'),
	('Nope','Not Available'),
	)



	class Meta:
		model = FinderStatus2
		fields = (
		'drafter',
		)
