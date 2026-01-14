from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Skill, Project, Experience, ContactMessage,BlogPost,  Education, Award,BlogComment
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView, DetailView
from .forms import CommentForm

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

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        # --- VIEW COUNTER LOGIC ---
        # Check if user visited this specific post in this session
        session_key = f'viewed_post_{obj.id}'
        if not self.request.session.get(session_key, False):
            obj.views += 1
            obj.save()
            self.request.session[session_key] = True # Mark as viewed
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        
        # Add the Comment Form
        context['form'] = CommentForm()
        
        # Check if user liked this post (for button color)
        session_key = f'liked_post_{self.object.id}'
        context['has_liked'] = self.request.session.get(session_key, False)
        
        return context

    # --- HANDLE COMMENT SUBMISSION ---
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.save()
            return redirect('blog_detail', slug=self.object.slug)
        
        # If form is invalid, reload page with errors
        context = self.get_context_data(object=self.object)
        context['form'] = form
        return self.render_to_response(context)

# --- NEW FUNCTION FOR AJAX LIKES ---
@require_POST
def like_post(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    session_key = f'liked_post_{post.id}'
    
    if not request.session.get(session_key, False):
        # Like
        post.likes += 1
        post.save()
        request.session[session_key] = True
        liked = True
    else:
        # Unlike (Toggle)
        post.likes -= 1
        post.save()
        del request.session[session_key]
        liked = False

    return JsonResponse({'liked': liked, 'count': post.likes})