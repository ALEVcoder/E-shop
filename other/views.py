from django.http import HttpResponse
from django.shortcuts import render
from other.models import Reklama, Blog, MySettings, Team
from django.views.generic import DetailView, ListView
from django.core.mail import send_mail
from django.db.models import Q
# Create your views here.

def blog(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, "blog.html", context)


class Blog_Detail(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'b_detail'

    def get_context_data(self, **kwargs):
        context = super(Blog_Detail, self).get_context_data(**kwargs)
        context['blog'] = Blog.objects.all().order_by('-created_at')[0:7]
        return context

def About(request):
    team = Team.objects.all()
    context = {
        'teams': team,
    }
    return render(request, "about.html", context)

def Contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        company_phone = request.POST['company_phone']
        message = request.POST['message']
        
        title = name
        msg = 'Name: '+ name + '\nSubject: '+subject + '\nEmail: ' + email + '\nPhone:  '+company_phone + '\nMessage: '+message

        print(name, subject, company_phone)
        send_mail(
            name,
            msg,
            company_phone,
            ['alevcoder1@gmail.com'],
            fail_silently=False,
        )
        
        print('Xabaringiz ketti')
    return render(request, "contact.html")


# Search View
class SearchResulView(ListView):
    model = Blog
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        objecy_list = Blog.objects.filter(Q(title__icontains=query)|Q(des__icontains=query))

        return objecy_list