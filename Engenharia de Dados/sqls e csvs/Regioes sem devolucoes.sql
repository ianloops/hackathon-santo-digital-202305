SELECT (territories.Region+'-'+territories.Country+'-'+territories.Continent)region FROM AdventureWorks_Returns AS returns
RIGHT JOIN AdventureWorks_Territories territories ON returns.TerritoryKey = territories.SalesTerritoryKey
GROUP BY territories.SalesTerritoryKey, territories.Region, territories.Country, territories.Continent
HAVING COUNT(ReturnQuantity)=0
