.read data.sql


CREATE TABLE average_prices AS
  SELECT "computer" AS category, 109.0 AS average_price UNION 
  SELECT "games"               , 350.0                  UNION 
  SELECT "phone"               , 90.0                   ;


CREATE TABLE lowest_prices AS
  SELECT store, item, MIN(price) 
  FROM inventory
  GROUP BY item;


CREATE TABLE shopping_list AS
  SELECT item, store
  FROM  lowest_prices AS i, products AS p 
  WHERE p.name = i.item
  GROUP BY category 
  HAVING MIN(MSRP / rating);


CREATE TABLE total_bandwidth AS
  SELECT SUM(Mbs)
  FROM shopping_list AS s, stores
  WHERE s.store = stores.store 
  

