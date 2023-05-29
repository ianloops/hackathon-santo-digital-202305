from fastapi import FastAPI

from product import Product
import service

app = FastAPI()


@app.post("/products/")
def insert_product(p: Product):
    return service.insert_product(p)


@app.get("/products/")
def get_products():
    return service.get_products()


@app.get("/products/{id}")
def get_products_by_id(id: int):
    return service.get_products_by_id(id)


@app.put("/products/{id}")
def update_products(id: int, p: Product):
    return service.update_products(id, p)


@app.delete("/products/{id}")
def remove_products(id: int):
    return service.remove_products(id)


@app.get("/sales/top-products/category/{category}/")
def best_sellers_by_category(category):
    return service.best_sellers_by_category(category)


@app.get("/sales/best-customer")
def best_customer():
    return service.best_customer()


@app.get("/sales/busiest-month")
def busiest_month():
    return service.busiest_month()


@app.get("/sales/top-sellers")
def top_sellers():
    return service.top_sellers()
