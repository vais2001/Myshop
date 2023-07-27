# from django.shortcuts import render,redirect
# from store.models.product import Product
# from store.models.category import Category
# from store.models.orders import Order
# from store.models.customer import Customer
# from django.views import View
# class check_out(View):
#     def post(self,request):
#         address= request.POST.get('address')
#         phone=request.POST.get('phone')
#         customer=request.session.get('customer')
#         cart=request.session.get('cart')
#         products=Product.get_products_by_id(list(cart.keys()))
#         print(address,phone,customer,cart,products)
        
#         for product in products:
#             print(cart.get(str(product.id)))
#             order = Order(customer=Customer(id=customer),
#                           product=product,
#                           price=product.price,
#                           address=address,
#                           phone=phone,
#                           quantity=cart.get(str(product.id)))
#             order.save()
#         request.session['cart'] = {}

#         return redirect('cart')

from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from store.models.orders import Order
from store.models.customer import Customer
from django.views import View

class check_out(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer_id = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer_id, cart, products)

        try:
            # Retrieve the Customer object from the database using the customer_id
            customer = Customer.objects.get(id=customer_id)

            for product in products:
                print(cart.get(str(product.id)))
                order = Order(
                    customer=customer,  # Use the retrieved Customer object
                    product=product,
                    price=product.price,
                    address=address,
                    phone=phone,
                    quantity=cart.get(str(product.id))
                )
                order.save()

            request.session['cart'] = {}
            return redirect('cart')

        except Customer.DoesNotExist:
            # Handle the case where the customer with the given ID does not exist
            # For example, you can redirect the user to an error page or display an error message
            return render(request, 'error.html', {'message': 'Customer not found'})
