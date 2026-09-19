SELECT
    lpep_pickup_datetime::date AS pickup_day,
    trip_distance
FROM public.green_taxi_trips
WHERE lpep_pickup_datetime >= '2025-11-01'
  AND lpep_pickup_datetime < '2025-12-01'
  AND trip_distance < 100
ORDER BY trip_distance DESC
LIMIT 1;
