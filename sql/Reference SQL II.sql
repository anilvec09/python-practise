products :                      sales:
product_id : int                product_id : int
product_class_id : int          store_id : int
brand_name : varchar            customer_id : int
product_name : varchar          promotion_id : int
is_low_fat_flg  : TINYINT       store_sales : decimal
                                store_cost : decimal
                                units_sold : decimal
                                transaction_date : date


stores:                         customers:
store_id : int                  customer_id : int
type: varchar                   first_name : varchar
name : varchar                  last_name : varchar
state : varchar                 state : varchar
first_opened_date : datetime    birthdate : date
last_remodel_date : datetime    education : varchar
area_sqft : int                 gender : varchar
                                date_account_opened : date


Question 1:
What brands have an average price above $3 and contain at least 2 different products?
SELECT
    brand_name
FROM products
GROUP BY brand_name
HAVING AVG(price) > 3
AND COUNT(DISTINCT product_id) >=2

SELECT
  department_id
FROM employees
GROUP BY 1
HAVING AVG(SALARY) >25000
AND COUNT(id) >= 2

Question 2:
To improve sales, the marketing department runs various types of promotions.
The marketing manager would like to analyze the effectiveness of these promotion campaigns.
In particular, what percent of our sales transactions had a valid promotion applied?

SELECT
    ROUND((COUNT( CASE WHEN promotion_id IS NOT NULL THEN product_id ELSE NULL END  ) * 100
    /COUNT(*)),2)
    AS PROMO_PERC
FROM sales

Question 3:
  We want to run a new promotion for our most successful category of products
  (we call these categories “product classes”).
  Can you find out what are the top 3 selling product classes by total sales?

SELECT
    product_class_id
FROM
WHERE sales s
join products p
ON s.product_id = p.product_id
GROUP BY product_class_id
ORDER BY SUM(store_sales) DESC
LIMIT 3

Question 4:
    We are considering running a promo across brands. We want to target
    customers who have bought products from two specific brands.
    Can you find out which customers have bought products from both the
    “Fort West" and the "Golden" brands?

SELECT
    c.first_name,
    c.last_name
FROM sales s
join customer c
ON s.customer_id = c.customer_id
JOIN products p
ON s.product_id = p.product_id
WHERE P.brand_name in (“Fort West" , "Golden" )
GROUP BY c.first_name,c.last_name -- 1,2 */
HAVING COUNT(DISTINCT brand_name) = 2

--SELECT
--    s.name
--FROM orders o
--JOIN company c
--ON   o.com_id = c.com_id
--JOIN salesperson s
--ON   o.sales_id = s.sales_id
--WHERE c.name in ('RED' , 'YELLOW')
--GROUP BY s.name
--having count(distinct c.name) = 2