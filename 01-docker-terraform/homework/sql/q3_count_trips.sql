SELECT COUNT(*)
FROM public.green_taxi_trips
WHERE lpep_pickup_datetime >= TIMESTAMP '2025-11-01'
  AND lpep_pickup_datetime < TIMESTAMP '2025-12-01'
  AND trip_distance <= 1;