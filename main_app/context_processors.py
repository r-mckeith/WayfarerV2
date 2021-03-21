from .models import Post, City, Comment

posts = Post.objects.all().order_by('-created_at')
cities = City.objects.all()
comments = Comment.objects.all()

def add_variable_to_context(request):
    return {
        'testme': 'Hello world!',
        'posts': posts,
        'cities': cities,
        # 'comments': comments
    }