from django.shortcuts import render,get_object_or_404
from lmApp.models import Post
from django.views.generic import ListView,DetailView

# Create your views here.
class Postlistview(ListView):
    model = Post
    paginate_by = 2

class Postdetailview(DetailView):
    model = Post

from django.core.mail import send_mail
from lmApp.forms import Emailsendform

def mail_send_view(request,id):
    post = get_object_or_404(Post,id=id,status='published')
    sent=False
    if request.method=='POST':
        form=Emailsendform(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject ='{}({}) recommends you to read "{}"'.format(cd['name'], cd['email'], post.title)
            post_url=request.build_absolute_uri(post.get_absolute_url())
            message="Read post At:\n {} \n\n{}\'s comments:\n{}".format(post_url,cd['name'],cd['comments'])
            send_mail(subject,message,'Rohit',[cd['to']])
            sent=True
    else:
        form = Emailsendform()
    return render(request,'lmApp/sharebymail.html',{'post':post,'form':form,'sent':sent})

print('Hey..are you there..')
print('606f888006cbfa79a8a8b318c5cf9471714667b5')