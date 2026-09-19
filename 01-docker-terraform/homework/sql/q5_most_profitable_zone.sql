SELECT
    z."Zone"
FROM (
    SELECT
        "PULocationID"
    FROM public.green_taxi_trips
    WHERE lpep_pickup_datetime >= '2025-11-18'
      AND lpep_pickup_datetime < '2025-11-19'
    GROUP BY "PULocationID"
    ORDER BY SUM(total_amount) DESC
    LIMIT 1
) AS totals
JOIN public.taxi_zones AS z
    ON totals."PULocationID" = z."LocationID";