from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from finder.forms import FinderForm,StatusForm,StatusForm2
from finder.models import Post,FinderStatus,FinderStatus2
from django.utils import timezone
from django.contrib.auth.decorators import login_required


class FinderView(TemplateView):
	template_name='finder/finder.html'

	def get(self,request):
		form=FinderForm()
		posts=Post.objects.all().order_by('-created')
		#print(posts)
		args={'form':form,'posts':posts}
		return render(request,self.template_name,args)


	def post(self,request):
		form =  FinderForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			text = form.cleaned_data['post']

			image=form.cleaned_data['post']
			form=FinderForm()
			return redirect('finder:finder')
		args={'form':form,'text':text,'image':image}
		return render(request,self.template_name,args)
		# form = FinderForm(request.POST)
		# if request.method=='POST':
			# form = FinderForm(request.POST)
	        #
			# if form.is_valid():
			# 	post=form.save(commit=False)
			# 	post.user=request.user
			# 	post.save()
			# 	text=form.cleaned_data['post']
	        #
			# 	form=FinderForm()
			# 	return redirect('finder:finder')
	        #
			# else:
			# 	form=FinderForm(instance=request.user)
			# 	return redirect('finder:finder')

@login_required
def Find(request):
	stat = FinderStatus.objects.all().order_by('-created_date')
	stat1 = FinderStatus2.objects.all().order_by('-created_date')
	if request.method == 'POST':
		form =  StatusForm(request.POST)
		form1 =  StatusForm2(request.POST)

		if form.is_valid() and form1.is_valid():
			post = form.save(commit=False)
			post1 = form1.save(commit=False)
			post.user = request.user
			post1.user = request.user
			post.created_date = timezone.now()
			post1.created_date = timezone.now()
			post.save()
			post1.save()
			form=StatusForm()
			form1=StatusForm2()
			return redirect('finder:find')
	else:
		form = StatusForm()
		form1= StatusForm2()

	return render(request,'finder/find.html',{'form':form,'form1':form1,'stat':stat,'stat1':stat1})
