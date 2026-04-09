def category_filter(products, params):
    category = params.get('category')
    if category:
        products = products.filter(category_id=category)
    return products


def price_filter(products, params):
    min_price = params.get('min_price')
    max_price = params.get('max_price')

    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    return products


def search_filter(products, params):
    search = params.get('search')
    if search:
        products = products.filter(title__icontains=search)
    return products
