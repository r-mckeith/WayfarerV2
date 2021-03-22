from .models import Post, City

posts = Post.objects.all().order_by('-created_at')
cities = City.objects.all()


def add_variable_to_context(request):
    return {
        'testme': 'Hello world!',
        'posts': posts,
        'cities': cities
    }