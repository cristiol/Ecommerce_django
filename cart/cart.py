
class Cart:
    def __init__(self, request):
        self.session = request.session
        # Get the current session if exist
        cart = request.session.get('session_key')

        # if the user is new, no sessions key, create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Make sure the cart is available on all pages of site
        self.cart = cart


    def add(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True


    def __len__(self):
        return len(self.cart)