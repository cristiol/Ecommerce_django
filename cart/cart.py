from store.models import Product, Profile


class Cart:
    def __init__(self, request):
        self.session = request.session
        self.request = request
        # Get the current session if exist
        cart = request.session.get('session_key')

        # if the user is new, no sessions key, create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Make sure the cart is available on all pages of site
        self.cart = cart

    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)
        # Logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        # Deal with logged in user
        if self.request.user.is_authenticated:
            # Get the current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Convert {'3':1, '2':4} to {"3":1, "2":4}
            json_cart = str(self.cart)
            json_cart = json_cart.replace("\'", "\"")
            # Save carty to the Profile Model
            current_user.update(old_cart=str(json_cart))


    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            json_cart = str(self.cart)
            json_cart = json_cart.replace("\'", "\"")
            current_user.update(old_cart=str(json_cart))

    def __len__(self):
        return len(self.cart)


    def get_prods(self):
        # get ids from cart
        products_ids = self.cart.keys()
        # use ids to get products
        products = Product.objects.filter(id__in=products_ids)

        return products


    def get_quants(self):
        quantities = self.cart
        return quantities


    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        current_cart = self.cart
        current_cart[product_id] = product_qty
        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            json_cart = str(self.cart)
            json_cart = json_cart.replace("\'", "\"")
            current_user.update(old_cart=str(json_cart))

        return self.cart

    def delete(self, product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            json_cart = str(self.cart)
            json_cart = json_cart.replace("\'", "\"")
            current_user.update(old_cart=str(json_cart))
        return self.cart


    def cart_total(self):
        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in=products_ids)
        quantities = self.cart

        total = 0
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total += product.sale_price * value
                    else:
                        total += product.price * value

        return total


