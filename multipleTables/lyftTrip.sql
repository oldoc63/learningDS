-- Let examine the three tables
SELECT * FROM trips;
SELECT * FROM riders;
SELECT * FROM cars;

--What's the primary key of trips?
--What's the primary key of riders?
--What's the primary key of cars?

--The primary key of trips, riders and cars is id. 
--They have the same name but they are very different.

SELECT riders.first, riders.last, cars.model, cars.status
FROM riders, cars;

-- If we LEFT JOIN on trips.rider_id and riders.id;
SELECT *
FROM trips
LEFT JOIN riders
ON trips.rider_id = riders.id;

-- Suppose we only want certain columns:
SELECT trips.date, 
   trips.pickup, 
   trips.dropoff, 
   trips.type, 
   trips.cost,
   riders.first, 
   riders.last,
   riders.username 
FROM trips
LEFT JOIN riders
ON trips.rider_id = riders.id;

-- For inner join (The JOIN keyword can also be INNER JOIN)
-- The inner join keyword selects records that have matching values in both tables
SELECT *
FROM trips
JOIN cars
  ON trips.car_id = cars.id;

-- Stack the riders table on top of the new table named riders2
SELECT *
FROM riders
UNION
SELECT *
FROM riders2;

-- What is the average cost of a trip?
SELECT AVG(cost)
FROM trips;

-- If we use the ROUND() function to round the result to 2 decimals
SELECT ROUND(AVG(cost), 2)
FROM trips;

-- Non frequent users (less than 500 times)
-- If we are only searching within the riders table
SELECT *
FROM riders
WHERE total_trips < 500;

-- if we want to search riders and riders2
SELECT *
FROM riders
WHERE total_trips < 500
UNION
SELECT *
FROM riders2
WHERE total_trips < 500;