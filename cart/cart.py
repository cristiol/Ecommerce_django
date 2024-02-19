
class Cart:
    def __init__(self, request):
        self.session = request.session
        # Get the current session if exist
        cart = request.session.get('session_key')

        # if the user is new, no sessions key, crate one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Make sure the cart is available on all pages of site
        self.cart = cart