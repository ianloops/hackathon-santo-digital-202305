SELECT TOP 1 customers.customerKey, (customers.Prefix + ' ' + customers.FirstName + ' ' + customers.LastName)customer, count(*)orders FROM (
	SELECT * FROM AdventureWorks_Sales_2015

	UNION

	SELECT * FROM AdventureWorks_Sales_2016

	UNION

	SELECT * FROM AdventureWorks_Sales_2017
	) sales 
	JOIN AdventureWorks_Customers customers ON sales.CustomerKey = customers.CustomerKey
	GROUP BY customers.CustomerKey, customers.prefix, customers.FirstName, customers.LastName
	ORDER BY orders DESC
