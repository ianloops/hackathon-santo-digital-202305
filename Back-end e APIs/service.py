from connection import connect
from product import Product


def get_products_by_id(id: int):
    db = connect()
    cursor = db.cursor()

    try:
        sql = "SELECT * FROM AdventureWorks_Products WHERE ProductKey = %s"
        cursor.execute(sql, (id,))
        product = cursor.fetchone()

        if product:
            product_dict = {
                "ProductKey": product[0],
                "ProductSubcategoryKey": product[1],
                "ProductSKU": product[2],
                "ProductName": product[3],
                "ModelName": product[4],
                "ProductDescription": product[5],
                "ProductColor": product[6],
                "ProductSize": product[7],
                "ProductStyle": product[8],
                "ProductCost": product[9],
                "ProductPrice": product[10]
            }
            return product_dict
        else:
            return {"message": "Produto não encontrado."}
    except Exception as e:
        return {"message": f"Erro ao ler o produto: {str(e)}"}

    finally:
        cursor.close()
        db.close()


def remove_products(id: int):
    db = connect()
    cursor = db.cursor()

    try:
        sql_verificar_produto = "SELECT * FROM AdventureWorks_Products WHERE ProductKey = %s"
        cursor.execute(sql_verificar_produto, (id,))
        existing_product = cursor.fetchone()

        if not existing_product:
            return {"message": "Produto não encontrado."}

        # Remover o produto com base no ID
        sql_remove_product = "DELETE FROM AdventureWorks_Products WHERE ProductKey = %s"
        cursor.execute(sql_remove_product, (id,))
        db.commit()

        return {"message": "Produto removido com sucesso."}
    except Exception as e:
        return {"message": f"Erro ao remover o produto: {str(e)}"}

    finally:
        cursor.close()
        db.close()


def best_sellers_by_category(category: int):
    db = connect()
    cursor = db.cursor()

    try:
        sql = """SELECT TOP 10 products.productKey, SUM(sales.orderQuantity)quantity FROM (
                    SELECT * FROM AdventureWorks_Sales_2015

                    UNION

                    SELECT * FROM AdventureWorks_Sales_2016

                    UNION

                    SELECT * FROM AdventureWorks_Sales_2017 ) sales JOIN AdventureWorks_Products products ON 
                    sales.ProductKey = products.ProductKey JOIN AdventureWorks_Product_Subcategories subcategories ON 
                    products.ProductSubcategoryKey = subcategories.ProductSubcategoryKey JOIN 
                    AdventureWorks_Product_Categories categories ON subcategories.ProductCategoryKey = 
                    categories.ProductCategoryKey WHERE categories.ProductCategoryKey=%s GROUP BY products.ProductKey, 
                    products.ProductName ORDER BY quantity DESC"""
        cursor.execute(sql, category)
        products = cursor.fetchall()

        products_list = []
        for product in products:
            product_dict = {
                "productKey": product[0],
                "quantity": product[1]
            }
            products_list.append(product_dict)

        return products_list
    except Exception as e:
        return {"message": f"Erro ao ler produtos: {str(e)}"}

    finally:
        cursor.close()
        db.close()


def best_customer():
    db = connect()
    cursor = db.cursor()

    try:
        sql = """SELECT TOP 1 customers.customerKey, (customers.Prefix + ' ' + customers.FirstName + ' ' + 
            customers.LastName)customer, count(*)orders FROM ( SELECT * FROM AdventureWorks_Sales_2015

            UNION

            SELECT * FROM AdventureWorks_Sales_2016

            UNION

            SELECT * FROM AdventureWorks_Sales_2017
            ) sales 
            JOIN AdventureWorks_Customers customers ON sales.CustomerKey = customers.CustomerKey
            GROUP BY customers.CustomerKey, customers.prefix, customers.FirstName, customers.LastName
            ORDER BY orders DESC"""
        cursor.execute(sql)
        customers = cursor.fetchall()

        customers_list = []
        for customer in customers:
            customer_dict = {
                "customerKey": customer[0],
                "customer": customer[1],
                "orders": customer[2]
            }
            customers_list.append(customer_dict)

        return customers_list
    except Exception as e:
        return {"message": f"Erro ao ler produtos: {str(e)}"}

    finally:
        cursor.close()
        db.close()


def busiest_month():
    db = connect()
    cursor = db.cursor()

    try:
        sql = """SELECT TOP 1 MONTH(OrderDate)'month', SUM(saleTotal)'value'
                FROM (
                    SELECT (ProductPrice*OrderQuantity)saleTotal, OrderDate FROM AdventureWorks_Sales_2017 sales
                    JOIN AdventureWorks_Products products ON sales.ProductKey = products.ProductKey) sales
                GROUP BY MONTH(OrderDate)
                ORDER BY 'value' DESC
                """
        cursor.execute(sql)
        result = cursor.fetchall()

        result_list = []
        for month in result:
            month_dict = {
                "month": month[0],
                "value": month[1]
            }
            result_list.append(month_dict)

        return result_list
    except Exception as e:
        return {"message": f"Erro ao ler produtos: {str(e)}"}

    finally:
        cursor.close()
        db.close()


def top_sellers():
    db = connect()
    cursor = db.cursor()

    try:
        sql = """SELECT * FROM ( SELECT territories.Region, SUM(ProductPrice*OrderQuantity)saleTotal FROM 
        AdventureWorks_Sales_2016 sales JOIN AdventureWorks_Products products ON sales.ProductKey = 
        products.ProductKey JOIN AdventureWorks_Territories territories ON sales.TerritoryKey = 
        territories.SalesTerritoryKey GROUP BY Region) totalRegion WHERE saleTotal>=(SELECT AVG(
        totalRegion.saleTotal) FROM ( SELECT territories.Region, SUM(ProductPrice*OrderQuantity) saleTotal FROM 
        AdventureWorks_Sales_2016 sales JOIN AdventureWorks_Products products ON sales.ProductKey = 
        products.ProductKey JOIN AdventureWorks_Territories territories ON sales.TerritoryKey = 
        territories.SalesTerritoryKey GROUP BY Region ) totalRegion)"""
        cursor.execute(sql)
        result = cursor.fetchall()

        result_list = []
        for region in result:
            region_dict = {
                "Region": region[0],
                "value": region[1]
            }
            result_list.append(region_dict)

        return result_list
    except Exception as e:
        return {"message": f"Erro ao ler produtos: {str(e)}"}

    finally:
        cursor.close()
        db.close()


def insert_product(p: Product):
    db = connect()
    cursor = db.cursor()

    try:
        sql = "INSERT INTO AdventureWorks_Products (ProductKey,ProductSubcategoryKey,ProductSKU,ProductName" \
              ",ModelName,ProductDescription,ProductColor,ProductSize,ProductStyle,ProductCost,ProductPrice)" \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (p.productKey, p.productSubcategoryKey, p.productSKU, p.productName, p.modelName,
                             p.productDescription, p.productColor, p.productSize, p.productStyle, p.productCost,
                             p.productPrice))
        db.commit()
        return {"message": "Produto criado com sucesso!"}
    except Exception as e:
        return {"message": f"Erro ao criar produto: {str(e)}"}

    finally:
        cursor.close()
        db.close()


def get_products():
    db = connect()
    cursor = db.cursor()

    try:
        sql = "SELECT * FROM AdventureWorks_Products"
        cursor.execute(sql)
        products = cursor.fetchall()

        products_list = []
        for product in products:
            product_dict = {
                "ProductKey": product[0],
                "ProductSubcategoryKey": product[1],
                "ProductSKU": product[2],
                "ProductName": product[3],
                "ModelName": product[4],
                "ProductDescription": product[5],
                "ProductColor": product[6],
                "ProductSize": product[7],
                "ProductStyle": product[8],
                "ProductCost": product[9],
                "ProductPrice": product[10]
            }
            products_list.append(product_dict)

        return products_list
    except Exception as e:
        return {"message": f"Erro ao ler produtos: {str(e)}"}

    finally:
        cursor.close()
        db.close()


def update_products(p: Product):
    p.productKey = int
    db = connect()
    cursor = db.cursor()

    try:
        sql_product_check = "SELECT * FROM AdventureWorks_Products WHERE ProductKey = %s"
        cursor.execute(sql_product_check, (p.productKey,))
        existing_product = cursor.fetchone()

        if not existing_product:
            return {"message": "Produto não encontrado."}

        sql_update_product = """
                UPDATE AdventureWorks_Products
                SET ProductSubcategoryKey = %s,
                    ProductSKU = %s,
                    ProductName = %s,
                    ModelName = %s,
                    ProductDescription = %s,
                    ProductColor = %s,
                    ProductSize = %s,
                    ProductStyle = %s,
                    ProductCost = %s,
                    ProductPrice = %s
                WHERE ProductKey = %s
            """
        values = (
            p.productSubcategoryKey,
            p.productSKU,
            p.productName,
            p.modelName,
            p.productDescription,
            p.productColor,
            p.productSize,
            p.productStyle,
            p.productCost,
            p.productPrice,
            p.productKey
        )
        cursor.execute(sql_update_product, values)
        db.commit()

        return {"message": "Produto atualizado com sucesso."}
    except Exception as e:
        return {"message": f"Erro ao atualizar o produto: {str(e)}"}

    finally:
        cursor.close()
        db.close()
