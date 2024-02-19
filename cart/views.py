from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages


def cart_summary(request):
    return render(request, 'cart_summary.html', {})


def cart_add(request):
    # get the cart
    cart = Cart(request)
    # test for post
    if request.POST.get('action') == 'post':
        # get the stuff
        product_id = int(request.POST.get('product_id'))
        # look up for product in db
        product = get_object_or_404(Product, id=product_id)
        # save the session
        cart.add(product=product)

        # Return resonse
        response = JsonResponse({'Product Name: ': product.name})
        messages.success(request, "Product Added To Cart...")
        return response


def cart_update(request):
    pass


def cart_delete(request):
    pass