from decimal import Decimal
from django.conf import settings

from courses.models import Course


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_SLUG)
        if not cart:
            cart = self.session[settings.CART_SESSION_SLUG] = {}
        self.cart = cart

    def add(self, course, quantity=1, update_quantity=False):
        course_slug = str(course.slug)
        if course_slug not in self.cart:
            self.cart[course_slug] = {'quantity': 0, 'price': str(course.price)}
        if update_quantity:
            self.cart[course_slug]['quantity'] = quantity
        else:
            self.cart[course_slug]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_SLUG] = self.cart
        self.session.modified = True

    def remove(self, course):
        course_slug = str(course.slug)
        if course_slug in self.cart:
            del self.cart[course_slug]
            self.save()

    def __iter__(self):
        course_slugs = self.cart.keys()
        courses = Course.objects.filter(slug__in=course_slugs)
        for course in courses:
            self.cart[str(course.slug)]['course'] = course

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def has_course(self, course):
        course_slug = str(course.slug)
        return course_slug in self.cart

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_SLUG]
        self.session.modified = True
