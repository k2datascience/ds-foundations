##SQL database
Before diving into how to query any database, let define what a database is. A database is a data store designed for storing, querying, and processing data. Databases store the data we want and expose an interface for interacting with that data. Most technology companies use databases to structure the data coming into the system and later query specific subsets of the data to answer questions or update existing data. Database systems also come with database management software with administrative controls, security and access controls, and a language to interface with the database.

In this module we will be learning about [SQL (Structured Query Language)](http://www.mysql.com/) databases, which is designed to query, update and modify data stored in a database. SQL is the most common language for working with databases and is an important tool in any data professional's toolkit. While SQL is a language, it's quite different from languages like Python or R. SQL was built specifically for querying and interacting with databases and won't have much of the functionality you can expect in traditional programming languages. Since SQL is a declarative language, the user focuses on expressing what he or she wants and the computer focuses on figuring out how to perform the computation.

A database is a collection of tables, where each table is made up of rows of data and each row has values for the same set of columns across the table. A table is very similar to a DataFrame in Pandas or how a regular CSV file is structured. Both have rows of values with a consistent set of columns.

##Querying
SQL is the most popular database querying language on the web. A SQL query has to adhere to a defined structure and vocabulary that we use to define what we want the database to do. The SQL language has a set of general statements that you combine with specific logic to express the intent of that query. It's easy to read syntax makes it more english than programming language. You can learn more about querying and SQL commands [here](http://blog.hubspot.com/marketing/sql-tutorial-introduction)

##SQLite
A common library used with SQL is [SQLite](https://sqlite.org/). SQLite is a lightweight database that is ideal for learning SQL. [sebastianraschka](http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html) is a great resource that provides a thorough guide to SQLite database operations in Python.

##SQL Joins
A SQL join is a Structured Query Language (SQL) instruction to combine data from two sets of data (e.g. two tables). There are four types of basic joins:

-inner join
-left join
-right join
-full join

Practice these joins using the [SQL Join guide](http://www.sql-join.com/sql-join-types). If you're feeling brave, tackle this [advanced tutorial](http://www.sqlcourse2.com/joins.html).



**Assignment:** Complete lessons 1 - 18 of [SQL Bolt](https://sqlbolt.com/)

**Other Resources:** Read [MySQL for Python](https://www.packtpub.com/big-data-and-business-intelligence/mysql-python)
![MySQL for Python]("images/sql_book.jpg")


Compairson - https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems
SQLite
Postgres - http://zetcode.com/db/postgresqlpythontutorial/
SQL Alchemy - http://www.rmunn.com/sqlalchemy-tutorial/tutorial.html
