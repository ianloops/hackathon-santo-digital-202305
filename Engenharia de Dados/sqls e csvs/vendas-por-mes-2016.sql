SELECT MONTH(OrderDate)'month', SUM(saleTotal)'value'
	FROM (
		SELECT (ProductPrice*OrderQuantity)saleTotal, OrderDate FROM AdventureWorks_Sales_2016 sales
		JOIN AdventureWorks_Products products ON sales.ProductKey = products.ProductKey) sales
	GROUP BY MONTH(OrderDate)
	ORDER BY 'value' ASC
	