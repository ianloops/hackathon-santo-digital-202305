SELECT * 
FROM (
	SELECT territories.Region, SUM(ProductPrice*OrderQuantity)saleTotal 
	FROM AdventureWorks_Sales_2016 sales
	JOIN AdventureWorks_Products products ON sales.ProductKey = products.ProductKey
	JOIN AdventureWorks_Territories territories ON sales.TerritoryKey = territories.SalesTerritoryKey
	GROUP BY Region) totalRegion
WHERE saleTotal>=(SELECT AVG(totalRegion.saleTotal)
		FROM (
			SELECT territories.Region, SUM(ProductPrice*OrderQuantity) saleTotal
			FROM AdventureWorks_Sales_2016 sales
			JOIN AdventureWorks_Products products ON sales.ProductKey = products.ProductKey
			JOIN AdventureWorks_Territories territories ON sales.TerritoryKey = territories.SalesTerritoryKey
			GROUP BY Region
		) totalRegion)