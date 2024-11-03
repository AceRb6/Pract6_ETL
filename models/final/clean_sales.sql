SELECT * 
FROM {{ ref('stg_sales') }} AS new_clean_sales
WHERE state IS NOT NULL
