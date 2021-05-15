increment = spark.read.json("s3a://bucket/landing_2020_01_02")   # name: str, id: int, content: str, etl_timestamp: timestamp

1. Separate duplicate rows by  name column for each id, and rows that contain non-matching braces in "content" field;
content = " .... (())()() ..."

increment.createOrReplaceTempView("inc")
increment_latest = spark.sql("""
select name,id,content,etl_time_stamp
(
select 
name,id,content, etl_time_stamp,
ROW_NUMBER() OVER (PARRTITION BY id ORDER BY etl_timestamp DESC) as rnk
from inc
) a 
where a.rnk=1
""")

1.1 Separated "bad" data should be written to s3 - as a single csv file. - bad_df

increment_dups  = increment.excepAll(increment_latest)


1.2 Filtered data without duplicates and invalid content - cleansed_df



2. Merge cleansed e into target data
increment_dups.write.save("targetpath",format=parquet,mode=overwrite)
# etl_date = date(timestamp)
target_dataset = spark.read.parquet("s3a://bucket/full_dataset")  # name: str, id: int, content: str, etl_timestamp: timestamp, etl_date: date

3. In target_dataset - overwrite old data for each id - with new content field.

4. Write target dataset back to "s3a://bucket/full_dataset"