SELECT 
    name,
    unit_price,
    new_price (unit_price * 1,1)
FROM products

SELECT *
FROM orders
WHERE order_date >= '2023-01-01'

SELECT *
FROM order_items
WHERE order_id = 6 AND unit_price * quantity > 30


# Use IN operator when you want to compare an attribute with a set of values
SELECT *
FROM products
WHERE quantity_in_stock IN (49, 38, 72)

SELECT *
FROM customers
WHERE date_of_birth BETWEEN '1990-01-1' AND '2000-01-01'