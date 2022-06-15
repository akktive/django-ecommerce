import json
from .models import *


def cookieCart(request):
	try:
		cart = json.loads(request.COOKIES['cart'])
	except:
		cart = {}
		print('CART:', cart)
	items = []
	order = {'get_cart_total': 0, 'get_cart_items': 0}
	cartItems = order['get_cart_items']

	for i in cart:
		try:
			if cart[i]['quantity'] > 0:
				cartItems += cart[i]['quantity']

				product = Product.objects.get(id=i)
				total = (product.price * cart[i]['quantity'])

				order['get_cart_total'] += total
				order['get_cart_items'] += cart[i]['quantity']

				item = {
					'id': product.id,
					'product': {
						'id': product.id,
						'name': product.name,
						'price': product.price,
						'imageURL': product.imageURL
					},
					'quantity': cart[i]['quantity'],
					'get_total':total,
				}
				items.append(item)
		except:
			pass
			
	return {'cartItems': cartItems, 'order': order, 'items': items}


def cartData(request):
	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(user=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total': 0, 'get_cart_items': 0}
		cartItems = order['get_cart_items']

	return {'cartItems': cartItems, 'order': order, 'items': items}


# def guestOrder(request, data):
# 	name = data['form']['name']
# 	email = data['form']['email']
#
# 	cookieData = cookieCart(request)
# 	items = cookieData['items']
#
# 	customer, created = Customer.objects.get_or_create(
# 			email=email,
# 			)
# 	customer.name = name
# 	customer.save()
#
# 	order = Order.objects.create(
# 		customer=customer,
# 		complete=False,
# 		)
#
# 	for item in items:
# 		product = Product.objects.get(id=item['id'])
# 		orderItem = OrderItem.objects.create(
# 			product=product,
# 			order=order,
# 			quantity=(item['quantity'] if item['quantity']>0 else -1*item['quantity']), # negative quantity = freebies
# 		)
# 	return customer, order
#
