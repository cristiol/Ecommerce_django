from .cart import Cart


# Create our context processors so the cart will work on all pages of the site
def cart(request):
    # return data from the cart
    return {'cart': Cart(request)}
