SELECT столбец, агрегатная_функция 
FROM таблица 
WHERE условие_до_группировки 
GROUP BY столбец 
HAVING условие_на_агрегат;
ORDER BY чтобы отсортировать результат.(по убыванию, возрастанию и т.д) По возрастанию (можно ASC не писать, он по умолчанию) DESC по убыванию
LIMIT число_строк; ограничивает результат первыми N строками
OFFSET сколько_пропустить; пропускает первые M строк.
# _________________________

SELECT 
    brand,
    COUNT(*) AS completed_orders
FROM car_orders
WHERE status = 'выполнен'
GROUP BY brand
HAVING COUNT(*) > 0  -- избыточно, так как WHERE уже отфильтровал
ORDER BY completed_orders;

+------------+------------------+
| brand      | completed_orders |
+------------+------------------+
| Volkswagen | 1                |
| Renault    | 1                |
| Mazda      | 2                |
| BMW        | 2                |
| Toyota     | 3                |
| Kia        | 3                |
| Audi       | 3                |
+------------+------------------+

# _________________________


SELECT 
    brand,
    COUNT(*) AS orders_count,
    AVG(price) AS avg_price
FROM car_orders
WHERE city = 'Москва'
GROUP BY brand
HAVING COUNT(*) >= 2 
   AND AVG(price) > 2400000;

+--------+--------------+----------------+
| brand  | orders_count | avg_price      |
+--------+--------------+----------------+
| Toyota | 3            | 2463333.333333 |
+--------+--------------+----------------+

# _________________________


SELECT product, AVG(quantity) AS avg_quantity 
FROM orders 
WHERE status = 'выполнен' 
GROUP BY product 
HAVING AVG(quantity) > 5 
ORDER BY avg_quantity DESC;


product	avg_quantity
Чай	        12.5
Кофе	    12.0


# _________________________

SELECT 
    manager_name,
    COUNT(*) AS total_orders,
    AVG(price) AS avg_price
FROM car_orders
WHERE status = 'выполнен' AND price > 3500000
GROUP BY manager_name
ORDER BY total_orders DESC, avg_price DESC;

+----------------+--------------+----------------+
| manager_name   | total_orders | avg_price      |
+----------------+--------------+----------------+
| Анна Морозова  | 1            | 3920000.000000 |
| Павел Гаврилов | 1            | 3850000.000000 |
+----------------+--------------+----------------+


# _________________________

SELECT 
    brand,
    COUNT(*) AS total_orders,
    AVG(price) AS avg_price
FROM car_orders
WHERE status = 'выполнен'
  AND price BETWEEN 2000000 AND 4000000
  AND order_date BETWEEN '2025-01-01' AND '2025-01-31'
GROUP BY brand
ORDER BY total_orders DESC, avg_price;


+--------+--------------+----------------+
| brand  | total_orders | avg_price      |
+--------+--------------+----------------+
| Toyota | 4            | 2455000.000000 |
| Mazda  | 2            | 2255000.000000 |
| Audi   | 2            | 3160000.000000 |
| Nissan | 1            | 2030000.000000 |
| BMW    | 1            | 3850000.000000 |
+--------+--------------+----------------+


# _________________________


SELECT 
    city,
    COUNT(*) AS orders,
    SUM(price) AS total_sum 
FROM car_orders
WHERE manager_name = 'Ольга Смирнова' 
  AND status IN ('отменён', 'в процессе')
GROUP BY city
HAVING COUNT(*) > 1
ORDER BY orders DESC, total_sum DESC;


+--------+--------+-------------+
| city   | orders | total_sum   |
+--------+--------+-------------+
| Казань | 5      | 12400000.00 |
| Москва | 3      | 7800000.00  |
+--------+--------+-------------+


# _________________________

SELECT 
    brand,
    COUNT(*) AS total_orders,
    AVG(price) AS avg_price 
FROM car_orders
WHERE city = 'Казань'
  AND payment_method != 'наличные'
  AND status != 'отменён'
GROUP BY brand
HAVING AVG(price) BETWEEN 1700000 AND 2500000 
ORDER BY total_orders, avg_price;


+--------+--------------+----------------+
| brand  | total_orders | avg_price      |
+--------+--------------+----------------+
| Mazda  | 1            | 2240000.000000 |
| Toyota | 1            | 2480000.000000 |
+--------+--------------+----------------+


# _________________________