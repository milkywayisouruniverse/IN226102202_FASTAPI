from fastapi import FastAPI

# create FastAPI app
app = FastAPI()

# product list (our small shop database)
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 599, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 99, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": True},
    {"id": 4, "name": "USB Cable", "price": 199, "category": "Electronics", "in_stock": False}
]

# endpoint to get all products
@app.get("/products")
def get_products():
    return {
        "products": products,
        "total": len(products)
    }

@app.get("/products/category/{category_name}")
def get_products_by_category(category_name: str):

    result = []

    for product in products:
        if product["category"].lower() == category_name.lower():
            result.append(product)

    if len(result) == 0:
        return {"error": "No products found in this category"}

    return {
        "category": category_name,
        "products": result,
        "total": len(result)
    }

@app.get("/products/instock")
def get_instock_products():

    available_products = []

    for product in products:
        if product["in_stock"] == True:
            available_products.append(product)

    return {
        "in_stock_products": available_products,
        "count": len(available_products)
    }

@app.get("/store/summary")
def store_summary():

    total_products = len(products)

    in_stock_count = len([p for p in products if p["in_stock"] == True])

    out_of_stock_count = total_products - in_stock_count

    categories = list(set([p["category"] for p in products]))

    return {
        "store_name": "My E-commerce Store",
        "total_products": total_products,
        "in_stock": in_stock_count,
        "out_of_stock": out_of_stock_count,
        "categories": categories
    }

@app.get("/products/search/{keyword}")
def search_products(keyword: str):

    results = []

    for product in products:
        if keyword.lower() in product["name"].lower():
            results.append(product)

    if len(results) == 0:
        return {"message": "No products matched your search"}

    return {
        "keyword": keyword,
        "results": results,
        "total_matches": len(results)
    }

@app.get("/products/deals")
def get_deals():
    cheapest = min(products, key=lambda p: p["price"])
    expensive = max(products, key=lambda p: p["price"])

    return {
        "best_deal": cheapest,
        "premium_pick": expensive
    }