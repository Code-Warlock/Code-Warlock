from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Skill, Project, Experience, ContactMessage,BlogPost,  Education, Award
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView, DetailView

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')


        ContactMessage.objects.create(
            name=name, 
            email=email, 
            subject=subject, 
            message=message
        )
        messages.success(request, 'Message received! I will get back to you shortly.')
        return HttpResponseRedirect(reverse('home') + '#contact')

    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    posts = BlogPost.objects.all()[:3]
    education = Education.objects.all()
    awards = Award.objects.all()
    
    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'experiences': experiences, 
        'posts': posts,
        'education': education,
        'awards': awards
    }
    return render(request, 'home.html', context)

def resume(request):
   
    profile = Profile.objects.first()
    experiences = Experience.objects.all()
    education = Education.objects.all()
    skills = Skill.objects.all()
    awards = Award.objects.all()

    context = {
        'profile': profile,
        'experiences': experiences,
        'education': education,
        'skills': skills,
        'awards': awards,
    }

   
    template_path = 'resume_pdf.html'
    template = get_template(template_path)
    html = template.render(context)

   
    response = HttpResponse(content_type='application/pdf')
   
    response['Content-Disposition'] = f'attachment; filename="{profile.name}_Resume.pdf"'

    pisa_status = pisa.CreatePDF(
       html, dest=response
    )

    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # We need this so the Navbar/Footer still works
        context['profile'] = Profile.objects.first()
        return context

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # We need this so the Navbar/Footer still works
        context['profile'] = Profile.objects.first()
        return context