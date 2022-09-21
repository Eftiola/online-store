from django.conf import settings
from django.shortcuts import redirect


class Cart(object):
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, action=None):
        """
        Add a product to the cart or update its quantity.
        """
        id = product.id
        new_item = True

        if str(product.id) not in self.cart.keys():
            self.cart[product.id] = {
                "userid": self.request.user.id,
                "product_id": id,
                "name": product.name,
                "description": product.description,
                "quantity": 1,
                "price": str(product.price),
                "image": product.image.url,
            }
        else:
            new_item = True

            for key, value in self.cart.items():
                if key == str(product.id):
                    value["quantity"] = value["quantity"] + 1
                    new_item = False
                    self.save()
                    break

            if new_item:
                self.cart[product.id] = {
                    "userid": self.request,
                    "product_id": product.id,
                    "name": product.name,
                    "description": product.description,
                    "quantity": 1,
                    "price": str(product.price),
                    "image": product.image.url,
                }

        self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def decrement(self, product):
        for key, value in self.cart.items():
            if key == str(product.id):
                value["quantity"] = value["quantity"] - 1
                if value["quantity"] < 1:
                    del self.cart[key]
                self.save()
                break
            else:
                print("Something Wrong")

    def clear(self):
        # empty cart
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True