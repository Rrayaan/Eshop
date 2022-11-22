from atexit import register
from django import template
register = template.Library()


@register.filter(name='isexistincart')
def isexistincart(product, cart):
    key = cart.keys()
    print("-----key----", key)
    for id in key:
        if int(id) == product.id:
            return True
    return False


@register.filter(name='cartquantity')
def cartquantity(product, cart):
    key = cart.keys()
    for id in key:
        if int(id) == product.id:
            return cart.get(id)
    return False


@register.filter(name='total_price')
def total_price(product, cart):
    tp = product.price * cartquantity(product, cart)
    return tp


@register.filter(name='Pyable_amount')
def Pyable_amount(product, cart):
    s = 0
    for i in product:
        s = s+total_price(i, cart)
    return s


@register.filter(name='total_amount')
def total_amount(price, quantity):
    return price * quantity
