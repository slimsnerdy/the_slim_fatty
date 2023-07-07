from django.views import generic
from .models import Post, PostImage
from django.shortcuts import render
from environs import Env

env = Env()
env.read_env()

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    paginate_by = 7
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['writer'] = env.str('DB_USER')  # Set the value of the variable
        return context

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        # context['image_list'] = PostImage.objects.all()
        # context['image_list'] = self.get_object().postimage_set.all()

        context['image_list'] = PostImage.objects.filter(post__slug=self.kwargs.get('slug'))
        context['writer'] = env.str('DB_USER')  # Set the value of the variable
        return context

class SearchView(generic.ListView):
    paginate_by = 15
    # paginate_by = 3   #for testing
    template_name = 'search.html'

    def get_queryset(self):
        self.query = self.request.GET.get('q', '')
        if self.query:
            object_list = Post.objects.filter(status=1, title__search=self.query)
            # object_list = Post.objects.filter(title__search=self.query)   #lol bug; shows DRAFTS
        else:
            object_list = []
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query
        return context