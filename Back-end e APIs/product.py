from pydantic import BaseModel


# Classe para representar o modelo de dados do produto
class Product(BaseModel):
    productKey: int
    productSubcategoryKey: int
    productSKU: str
    productName: str
    modelName: str
    productDescription: str
    productColor: str
    productSize: int
    productStyle: str
    productCost: int
    productPrice: int
