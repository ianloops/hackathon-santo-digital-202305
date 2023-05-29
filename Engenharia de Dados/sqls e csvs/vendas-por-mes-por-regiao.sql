SELECT MONTH(OrderDate)'month', territories.Region, COUNT(*)salesVolume 
	FROM AdventureWorks_Sales_2016 sales
	JOIN AdventureWorks_Products products ON sales.ProductKey = products.ProductKey
	JOIN AdventureWorks_Territories territories ON sales.TerritoryKey = territories.SalesTerritoryKey
	GROUP BY MONTH(OrderDate), Region
	ORDER BY MONTH(OrderDate)