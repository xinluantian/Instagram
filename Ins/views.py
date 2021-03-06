from annoying.decorators import ajax_request
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Ins.models import Post, Like, InsUser, UserConnection
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from Ins.forms import CustomerUserCreationForm
class HelloWorld(TemplateView):
    template_name = 'test.html'

class PostsView(ListView):
    model= Post
    template_name = "index.html"
    
    def get_queryset(self):
        current_user = self.request.user
        following = set()
        for conn in UserConnection.objects.filter(creator=current_user).select_related('following'):
            following.add(conn.following)
        return Post.objects.filter(author__in=following)

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class UserDetailView(DetailView):
    model = InsUser
    template_name = "user_detail.html"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post_create.html"
    # To provide all field in 0001_initial.py
    fields ='__all__'
    # if not login, then jump to login web
    login_url = 'login' 

class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = ['title']

class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('posts')

class SignUp(CreateView):
    form_class = CustomerUserCreationForm
    template_name = 'sign_up.html'
    success_url = reverse_lazy("login")


@ajax_request
def addLike(request):
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    try:
        like = Like(post=post, user=request.user)
        like.save()
        result = 1
    except Exception as e:
        like = Like.objects.get(post=post, user=request.user)
        like.delete()
        result = 0

    return {
        'result': result,
        'post_pk': post_pk
    }
    
    



    