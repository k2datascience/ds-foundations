##What Is A NoSQL Database
NoSQL encompasses a wide variety of different database technologies that were developed in response to the demands presented in building modern applications. Relational databases were not designed to cope with the scale and agility challenges that face modern applications, nor were they built to take advantage of the commodity storage and processing power available today. In this module we will cover some unique features of a NoSQL database.

##History
NoSQL was developed in late 2000s to deal with limitations of SQL databases, especially scalability, multi-structured data, geo-distribution and agile development sprints. NoSQL is not a campaign against the SQL language. NoSQL stands for “Not Only SQL.” It provides more possibilities beyond the classic relational approach of data persistence to the developers.
NoSQL refers to a broad class of non-relational databases that differ from classical RDBMS in some significant aspects, most notably because they do not use SQL as their primary query language, instead providing access by means of Application Programming Interfaces (APIs).
The reason behind such a big switch or in other words the advantages of NoSQL are the following:

-High scalability
-Distributed Computing
-Lower cost
-Schema flexibility
-Un/semi-structured data
-No complex relationships

##NoSQL Database Types
There are 4 [NoSQL database types](https://www.mongodb.com/nosql-explained):

-**Document databases** - The model is basically versioned documents that are collections of other key-value collections. The semi-structured documents are stored in formats like JSON. Document databases are essentially the next level of key-value, allowing nested values associated with each key. Document databases support querying more efficiently. An example of a document stored database is MongoDB.

-**Graph stores** - Instead of tables of rows and columns and the rigid structure of SQL, a flexible graph model is used which, again, can scale across multiple machines. NoSQL databases do not provide a high-level declarative query language like SQL to avoid overtime in processing. Rather, querying these databases is data-model specific.

-**Key-value stores** - The main idea here is using a hash table where there is a unique key and a pointer to a particular item of data. The key-value model is the simplest and easiest to implement. But it is inefficient when you are only interested in querying or updating part of a value, among other disadvantages. Examples of key-value databases are Amazon simpleDB and Oracle BDB.

-**Wide-column stores** - These were created to store and process very large amounts of data distributed over many machines. There are still keys but they point to multiple columns. The columns are arranged by column family. Examples of column-oriented databases are Cassandra and HBase.

To get a good understanding of MongoDB, work through the [tutorialspoint MongoDB Tutorial](https://www.tutorialspoint.com/mongodb/).

##Working with PyMongo
**PyMongo** is a Python distribution containing tools for working with MongoDB, and is the recommended way to work with MongoDB from Python. To get started, begin by [installing PyMongo](http://www.bogotobogo.com/python/MongoDB_PyMongo/python_MongoDB_pyMongo_tutorial_installing.php) and complete the [PyMongo and MongoDB tutorial](http://api.mongodb.com/python/2.7.2/tutorial.html).


**Assignments:**
Complete the [tutorialspoint MongoDB Tutorial](https://www.tutorialspoint.com/mongodb/)
Complete the [PyMongo and MongoDB tutorial](http://api.mongodb.com/python/2.7.2/tutorial.html)
