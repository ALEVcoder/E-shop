import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import DetailView
from online.models import Category, Product, Cart, Order_Product, WishList
from other.models import Blog, Reklama


# Create your views here.
def index(request):
    categories = Category.objects.all().first()
    categories_all = Category.objects.all()
    reklama_all = Reklama.objects.all().order_by('-created_at')[0:2]
    blog_all = Blog.objects.all().order_by('-created_at')[0:5]
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        cart_list = cart.order_product.all()
    else:
        cart_list = []
    return render(request, 'index.html', context={"reklama": reklama_all, "blogs": blog_all,  "categories": categories_all, "cart_list": cart_list, "products": Product.objects.filter(category_id=categories.id)})


def products(request):
    categories = Category.objects.all().first()
    categories_all = Category.objects.all()
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        cart_list = cart.order_product.all()
    else:
        cart_list = []
    return render(request, 'products.html', context={"categories": categories_all, "cart_list": cart_list, "products": Product.objects.filter(category_id=categories.id)})


def cart(request):
    cart = Cart.objects.filter(user=request.user).first()
    cart_list = cart.order_product.all()
    return render(request, 'cart.html', context={"cart_list": cart_list, "total_summa":cart.total_summa})


def wishlist(request):
    wishlist = WishList.objects.filter(user=request.user).first()
    return render(request, 'wishlist.html', context={"wishlist": wishlist.product.all()})


def checkout(request):
    return render(request, 'checkout.html')


# TODO: JS PART

def order_category(request):
    data = json.loads(request.body)
    cat_id = data.get('id')
    products = Product.objects.filter(category_id=int(cat_id))
    res = []

    for product in products:
        p = {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "image": product.imageURL,
            "discount": product.discount_price
        }
        res.append(p)
    return JsonResponse({"data": res})


def add_cart(request):
    data = json.loads(request.body)
    id = data.get('id')
    product = Product.objects.get(id=int(id))
    cart, cart_created = Cart.objects.get_or_create(user=request.user)
    if cart_created:
        cart.product.add(product)
        Order_Product.objects.create(cart=cart, product=product)
    
    try:
        order_product = Order_Product.objects.get(cart=cart, product=product)
        order_product.add
    except:
        order_product = Order_Product.objects.create(cart=cart, product=product)
    cart.product.add(product)
    data = [{
        "id": i.product.id,
        "order_id": i.id,
        "name": i.product.name,
        "image": i.product.imageURL,
        "price": i.product.price,
        "quantity": i.quantity,
    } for i in cart.order_product.all()]

    return JsonResponse({"data": data, "count": cart.product.count()})



def remove_cart(request):
    data = json.loads(request.body)
    id = data.get('id')
    cart = Cart.objects.get(user=request.user)
    product = Order_Product.objects.filter(id=int(id)).first()

    if product:
        cart.product.remove(product.product)
        product.delete()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False})


def change_quantity(request):
    id = json.loads(request.body)['id']
    action = json.loads(request.body)['action']
    order_product = Order_Product.objects.get(id=id)
    if action=='add':
        order_product.add
    elif action=='sub' and order_product.quantity>1:
        order_product.sub
    return JsonResponse({'quantity': order_product.quantity,'total':order_product.summa, 'total_summa':order_product.cart.total_summa})


def add_wishlist(request):
    data = json.loads(request.body)
    id = data.get('id')
    wishlist, created = WishList.objects.get_or_create(user=request.user)
    product = Product.objects.get(id=int(id))

    if product in wishlist.product.all():
        wishlist.product.remove(product)
        return JsonResponse({"success": True})
    else:
        wishlist.product.add(product)
        return JsonResponse({"success": False})

class Product_Detail(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'p_detail'

    def get_context_data(self, **kwargs):
        context = super(Product_Detail, self).get_context_data(**kwargs)
        context['blog'] = Blog.objects.all().order_by('-created_at')[0:7]

        return context
