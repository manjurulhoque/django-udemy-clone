from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from courses.models import Course
from .cart import Cart


@require_POST
def cart_add(request, slug):
    cart = Cart(request)  # create a new cart object passing it the request object
    course = get_object_or_404(Course, slug=slug)
    print(course)
    cart.add(course=course, quantity=1, update_quantity=False)
    return redirect('cart:cart_detail')


def cart_remove(request, slug):
    cart = Cart(request)
    course = get_object_or_404(Course, slug=slug)
    cart.remove(course)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
