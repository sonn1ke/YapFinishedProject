#Тест 1. Проверка отображения заказа в БД
SELECT
c.login,
COUNT(nullif(o."inDelivery", true)) as quantity_orders
FROM "Couriers" AS c
LEFT JOIN "Orders" AS o ON c.id=o."courierId"
GROUP BY c.login
;

#Тест 2. Проверка отображения статуса заказа в БД
SELECT
track,
CASE
WHEN finished = true THEN 2
WHEN cancelled = true THEN -1
WHEN "inDelivery" = true THEN 1
ELSE 0
END as order_status
FROM "Orders"
;