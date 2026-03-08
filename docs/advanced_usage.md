# Advanced usage

## Page context (path, query, user parameters)

When you use default `Pyue.add_page(Page, url)`, it looses ability to handle query parameters
or some context (like DB info). But you can also provide special function, that handles context
(which is called `context_func`):
```python
# Path parameter example
page = Page("greeting.html")
app.add_page(
    page,
    url="/hello/<name>",
    context_func=lambda name: {"name": name}
)

# Multiple path parameters
def product_context(category, product_id):
    product = get_product(category, product_id)
    related = get_related_products(category, limit=5)
    return {"product": product, "related": related}

page = Page("product.html")
app.add_page(page, url="/products/<category>/<int:product_id>", context_func=product_context)

# DB context example
def user_context(user_id):
    user = get_user_by_id(user_id)
    if user is None:
        abort(404)
    return {"user": user}

page = Page("profile.html")
app.add_page(page, url="/user/<int:user_id>", context_func=user_context)

# Query parameters example
from flask import request

def search_context():
    query = request.args.get("q", "")
    page_num = request.args.get("page", 1, type=int)
    results = perform_search(query, page=page_num)
    return {"query": query, "results": results, "page": page_num}

page = Page("search.html")
app.add_page(page, url="/search", context_func=search_context)
```
