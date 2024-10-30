
    
    create view main."clean_sales" as
    SELECT * 
FROM main."stg_sales" AS new_clean_sales
WHERE state IS NOT NULL;