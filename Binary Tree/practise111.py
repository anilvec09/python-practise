usernames = ['user_id', 'gender', 'age', 'occupation', 'zip']
ratings = ['user_id', 'movie_id', 'rating', 'timestamp']
movies = ['movie_id', 'title', 'genres']

Tables are stored in hive with above structures.

hqlContext,sqlContext.
sparksession
usernames = spark.read.parquet("s3://path/to/usernames")
ratings= spark.read.parquet("s3://path/to/ratings")
movies= spark.read.parquet("s3://path/to/movies")

usernames.show()/collect()/cloumns/scehma

Load tables in your spark program and answer following analytic questions.

usernames.createOrReplaceTempView("usernames")/("rating")/("movies")

joined = spark.sql("select
u.user_id, u.gender , u.age. u.occupation,  zip   movie_id  rating  timestamp   title,genres
 from usernames u join rating ratings r
on u.user_id = r.user_id
join movies m
ob r.movie_id = m.movie_id
")
joined .createOrReplaceTempView("joined")
Find all ratings by movie name.
-------------------------------
user_id gender  age occupation  zip   movie_id  rating  timestamp   title                   genres
216     M       45  13          52761   2031    2       976867230   $1,000,000 Duck (1971)  Children's|Comedy
494     F       35  0           17870   2031    5       976215651   $1,000,000 Duck (1971)  Children's|Comedy
714     M       18  4           76013   2031    4       975782711   $1,000,000 Duck (1971)  Children's|Comedy
869     M       18  20          92026   2031    1       999376619   $1,000,000 Duck (1971)  Children's|Comedy

spark.sql("
select title,gender
 avg(rating) as M
 avg(rating)  as F,
from joined
group by title,gender
")

Find average ratings based on movie title and gender
-----------------------------------------------
title                         F         M
$1,000,000 Duck (1971)      3.375000    2.761905
'Night Mother (1986)        3.388889    3.352941
'Til There Was You (1997)   2.675676    2.733333

spark.sql("
select title,rank() over(order by title) as rank from joined")

Get top 10 ranked movies
------------------------
title                                                    rank
American Beauty (1999)                                   1
Star Wars: Episode IV - A New Hope (1977)                2
Star Wars: Episode V - The Empire Strikes Back (1980)    3



--executor-memory/driver/

coalesce/repartition




