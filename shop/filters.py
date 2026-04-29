from rest_framework.exceptions import ValidationError


def category_filter(products, params):
    category = params.get('category')
    if category:
        products = products.filter(category_id=category)
    return products


def parse_price(value, field_name):
    try:
        return int(value)
    except (TypeError, ValueError):
        raise ValidationError({field_name: 'must be a number'})


def price_filter(products, params):
    min_price = params.get('min_price')
    max_price = params.get('max_price')

    if min_price:
        products = products.filter(price__gte=parse_price(min_price, 'min_price'))
    if max_price:
        products = products.filter(price__lte=parse_price(max_price, 'max_price'))

    return products


def search_filter(products, params):
    search = params.get('search')
    if search:
        products = products.filter(title__icontains=search)
    return products
