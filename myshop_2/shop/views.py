from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Post
from .forms import PostForm, SortForm, ContactForm, UserForm, listClass
from django.http import HttpResponse
from cart.forms import CartAddProductForm


def sortByRating(inputStr):
    return 5 - float(inputStr.rating)

def product_list(request, category_slug=None):
    print (request.method)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        cat = request.POST.getlist("categorys")
        res = request.POST.getlist("resolution")
        minPrice = int(request.POST.get("minPrice"))
        print (res)
        maxPrice = int(request.POST.get("maxPrice"))
        expres = int(request.POST.get("expre"))
        megapixels = float(request.POST.get("megapixels"))
        prod = Product.objects.filter(available=True)
        prod_list = []
        for p in prod:
            print (str(p.maxResolution), minPrice)
            if maxPrice >= int(p.price) >= minPrice:
                if p.category in cat or not cat:
                    print (str(p.maxResolution) in res)
                    if str(p.maxResolution) in res or not res:
                        print ("res is ok")
                        if int(p.maxExcerpt) > expres and float(p.megapixels) > megapixels:
                            prod_list.append(p)
        print (prod_list)
        prod_list.sort(key=sortByRating)
    else:
        prod_list = Product.objects.filter(available=True)
        prod_list = prod_list.extra(order_by = ['-rating'])

#    prod_list.sort(key=sortByRating)
    category = None
    categories = Category.objects.all()

    lists = listClass()
    print ("listsClass", lists)
    # if this is a POST request we need to process the form data
    return render(request,
                  'shop/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': prod_list,
                   'lists': lists})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
#    posts = Post.objects.filter(product = product)
    posts = product.blog_posts.all()
    cart_product_form = CartAddProductForm()
    #post_form = PostForm(data=request.POST)
    print (request.method)
    if request.method == 'POST':
        title = str(request.POST.get("title"))
        body = str(request.POST.get("body"))
        rating = float(request.POST.get("rating"))
        new_post = Post(title = title, author = request.user, body = body, rating = rating, product = product)

        old_rating = product.rating * product.countRating
        old_rating += rating
        product.countRating += 1
        product.rating = old_rating / product.countRating
        product.save()
        new_post.save()
        print (title, body, rating)
        print (product.blog_posts)
        # A comment was posted
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            # Create Comment object but don't save to database yet
            """
            new_post = post_form.save(commit=False)
            # Assign the current post to the comment
            new_post.product = product
            print (post_form.cleaned_data['title'])
            rating = product.rating * product.countRating
            selfRating = post_form.cleaned_data['rating']
            rating += selfRating
            product.countRating += 1
            product.rating = rating / product.countRating
            product.save()
            # Save the comment to the database
            print (new_post)
            new_post.author = request.user
            new_post.save()
            """
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
    userform = UserForm(field_order = ["age", "name"])
    print (request.POST.get("name"))
    print (request.POST.get("age"))
    return render(request, "shop/test.html", {"form": userform})