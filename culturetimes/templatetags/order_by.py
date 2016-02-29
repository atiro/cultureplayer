from django.template import Library

register = Library()

# From https://djangosnippets.org/snippets/741/

@register.filter_function
def order_by(queryset, args):
    args = [x.strip() for x in args.split(',')]
    return queryset.order_by(*args)
