from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, View, UpdateView, CreateView
from django.contrib.auth import mixins
from .models import Blog
from .forms import EditPost
from datetime import datetime

class ViewCurrentBlog(ListView):
    model=Blog
    context_object_name = 'blogs'
    template_name ='blog/blog_current.html'


class DeleteBlog(View, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
    model=Blog
    success_url = 'cur_blog'
    def get(self,request, **kwargs):
        self.model.objects.get(pk=kwargs['pk']).delete()
        return redirect(self.success_url)


class CreateBlog(CreateView, mixins.LoginRequiredMixin):
    success_url = 'cur_blog'
    template_name = 'blog/new_post.html'
    model=Blog
    fields=['title','txt']
    login_url = 'login'
    def post(self, request, *args, **kwargs):
        print(request.POST)
        author=request.user
        txt=(request.POST.get('txt', None)).strip()
        title=request.POST.get('title', None).strip()
        date_time=datetime.now()
        if txt and title:
            new_obj=Blog.objects.create(author=author,
                                       txt=txt,title=title, date=date_time)
            new_obj.save()
        else:
            return render(request, self.template_name, {'error':'INVALID DATA'})
        return redirect(reverse(self.success_url))


class EditBlog(View, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
    form_class = EditPost
    success_url = 'cur_blog'
    template_name = 'blog/edit_me.html'
    def get(self, request, **kwargs):
        obj=Blog.objects.get(pk=kwargs['pk'])
        self.form_class=self.form_class(initial={'title':obj.title,'txt':obj.txt})
        context={'form':self.form_class,'error':self.form_class.errors}
        return render(request, self.template_name, context)
    def post(self, request, **kwargs):
        form= self.form_class(request.POST)
        if form.is_valid():
            post=Blog.objects.get(pk=kwargs['pk'])
            post.txt=form.cleaned_data['txt']
            post.title=form.cleaned_data['title']+' (EDITED)'
            post.save()
        return redirect(reverse(self.success_url))

# Create your views here.
