from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Post
from .forms import PostForm, SortForm
from django.http import HttpResponse
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # if this is a POST request we need to process the form data
    print (request.method)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SortForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print (request.POST.get('maxResolution'))
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SortForm()

    return render(request,
                  'shop/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'form': form})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
#    posts = Post.objects.filter(product = product)
    posts = product.blog_posts.all()
    cart_product_form = CartAddProductForm()
    #post_form = PostForm(data=request.POST)
    if request.method == 'POST':
        # A comment was posted
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            # Create Comment object but don't save to database yet
            new_post = post_form.save(commit=False)
            # Assign the current post to the comment
            new_post.product = product
            # Save the comment to the database
            print (new_post)
            new_post.author = request.user
            new_post.save()
    else:
        post_form = PostForm()
        print ("nw post")
    return render(request,
                  'shop/detail.html',
                  {'product': product,
                  'posts': posts,
                  'post_form': post_form,
                  'cart_product_form': cart_product_form})

def test(request):
    return HttpResponse("Hello")