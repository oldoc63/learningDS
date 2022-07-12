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

