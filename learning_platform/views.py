from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Article, Category

# Home view: Displays articles with optional category filtering
@login_required
def home(request):
    categories = Category.objects.all()  # Fetch all categories
    category_name = request.GET.get('category')  # Get selected category from URL (if any)

    if category_name:
        # Filter articles by selected category
        articles = Article.objects.filter(category__name=category_name)
    else:
        # Show all articles
        articles = Article.objects.all()

    # Render the homepage with categories, articles, and tutor status
    return render(request, 'learning_platform/home.html', {
        'categories': categories,
        'articles': articles,
        'is_tutor': request.user.groups.filter(name='Teacher').exists(), 
    })



@login_required
def search(request):
    query = request.GET.get('q') 
    # Filter articles by checking if the query exists in the 'name' or 'about' fields of the Article model
    articles = Article.objects.filter(name__icontains=query) | Article.objects.filter(about__icontains=query)
    
    # Render the homepage template again, but only with the filtered articles based on the search query
    return render(request, 'learning_platform/home.html', {'articles': articles})  # Pass the filtered articles to the template

@login_required
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    return render(request, 'learning_platform/article_detail.html', {
        'article': article,
        'is_tutor': request.user.groups.filter(name='Teacher').exists(),
    })