SELECT столбец, агрегатная_функция 
FROM таблица 
WHERE условие_до_группировки 
GROUP BY столбец 
HAVING условие_на_агрегат;

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

# ___________________________________________________


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

# __________________________________________________