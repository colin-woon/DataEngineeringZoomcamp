SELECT
    dropoff_zone."Zone"
FROM (
    SELECT
        t."DOLocationID"
    FROM public.green_taxi_trips AS t
    WHERE t.lpep_pickup_datetime >= '2025-11-01'
      AND t.lpep_pickup_datetime < '2025-12-01'
      AND t."PULocationID" = (
          SELECT "LocationID"
          FROM public.taxi_zones
          WHERE "Zone" = 'East Harlem North'
      )
    ORDER BY t.tip_amount DESC
    LIMIT 1
) AS winning_trip
JOIN public.taxi_zones AS dropoff_zone
    ON winning_trip."DOLocationID" = dropoff_zone."LocationID";