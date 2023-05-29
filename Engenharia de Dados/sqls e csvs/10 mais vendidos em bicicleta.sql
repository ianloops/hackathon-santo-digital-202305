SELECT TOP 10 products.productKey, products.ProductName, SUM(sales.orderQuantity)quantity FROM (
	SELECT * FROM AdventureWorks_Sales_2015

	UNION

	SELECT * FROM AdventureWorks_Sales_2016

	UNION

	SELECT * FROM AdventureWorks_Sales_2017
	) sales 
	JOIN AdventureWorks_Products products ON sales.ProductKey = products.ProductKey
	JOIN AdventureWorks_Product_Subcategories subcategories ON products.ProductSubcategoryKey = subcategories.ProductSubcategoryKey
	JOIN AdventureWorks_Product_Categories categories ON subcategories.ProductCategoryKey = categories.ProductCategoryKey
	WHERE categories.ProductCategoryKey=1
	GROUP BY products.ProductKey, products.ProductName
	ORDER BY quantity DESC