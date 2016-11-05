# General Tips

## Table of Contents
[1. NoSQL and Databases](#section-a)

[2. Web Scraping](#section-b)

[3. Assignments](#section-c)

[4. Projects](#section-d)

---

### <a name="section-a"></a>1. NoSQL and Databases

NoSQL encompasses a wide variety of different database technologies that were developed in response to the demands presented in building modern applications. Relational databases were not designed to cope with the scale and agility challenges that face modern applications, nor were they built to take advantage of the commodity storage and processing power available today. In this module we will cover some unique features of a NoSQL database.

#### History
NoSQL was developed in late 2000s to deal with limitations of SQL databases, especially scalability, multi-structured data, geo-distribution and agile development sprints. NoSQL is not a campaign against the SQL language. NoSQL stands for “Not Only SQL.” It provides more possibilities beyond the classic relational approach of data persistence to the developers.

NoSQL refers to a broad class of non-relational databases that differ from classical RDBMS in some significant aspects, most notably because they do not use SQL as their primary query language, instead providing access by means of Application Programming Interfaces (APIs).
The reason behind such a big switch or in other words the advantages of NoSQL are the following:

- High scalability
- Distributed Computing
- Lower cost
- Schema flexibility
- Un/semi-structured data
- No complex relationships

For a more in-depth background, read [this explanation by MongoDB](https://www.mongodb.com/nosql-explained).

#### NoSQL Database Types
There are 4 main NoSQL database types:

**Document databases** - The model is basically versioned documents that are collections of other key-value collections. The semi-structured documents are stored in formats like JSON. Document databases are essentially the next level of key-value, allowing nested values associated with each key. Document databases support querying more efficiently. An example of a document stored database is MongoDB.

**Key-Value stores** - The main idea here is using a hash table where there is a unique key and a pointer to a particular item of data. The key-value model is the simplest and easiest to implement. But it is inefficient when you are only interested in querying or updating part of a value, among other disadvantages. Examples of key-value databases are Amazon simpleDB and Oracle BDB.

**Wide-Column stores** - These were created to store and process very large amounts of data distributed over many machines. There are still keys but they point to multiple columns. The columns are arranged by column family. Examples of column-oriented databases are Cassandra and HBase.

**Graph stores** - Instead of tables of rows and columns and the rigid structure of SQL, a flexible graph model is used which, again, can scale across multiple machines. NoSQL databases do not provide a high-level declarative query language like SQL to avoid overtime in processing. Rather, querying these databases is data-model specific.

In the curriculum, you will be exposed to Document Databases. Depending on your final project or if you choose to explore data engineering in further detail, you may want to use Key-Value Stores and Wide-Column Stores.

Normally we do not recommend MOOC courses because the coverage of topics is usually introductory or not well done, but [this course on Udacity](https://www.udacity.com/course/data-wrangling-with-mongodb--ud032) was developed personally by MongoDB. This goes over different types of data formats, MongoDB and the PyMongo package.

---

### <a name="section-b"></a>2. Web Scraping

Web scraping (web harvesting or web data extraction) is a computer software technique of extracting information from websites. This is accomplished by either directly implementing the Hypertext Transfer Protocol (on which the Web is based), or embedding a web browser.

Web scraping is closely related to web indexing, which indexes information on the web using a bot or web crawler and is a universal technique adopted by most search engines. In contrast, web scraping focuses more on the transformation of unstructured data on the web, typically in HTML format, into structured data that can be stored and analyzed in a central local database or spreadsheet. Web scraping is also related to web automation, which simulates human browsing using computer software. Uses of web scraping include online price comparison, contact scraping, weather data monitoring, website change detection, research, web mashup and web data integration.

Please complete the exercises throughout the first book. You will often have to use web scraping to obtain data on the internet throughout the bootcamp.

[A beginner / intermediate reference book](resources/web_scraping_with_python.pdf). (*Right-click and Save Link As...*)

Note: The code is in Python 2.7, so you will have to make some changes to the code.

---

### <a name="section-c"></a>3. Assignments

1. Complete the Data Wrangling with MongoDB course on Udacity.

2. Complete the Web Scraping in Python book and all the exercises.

---

### <a name="section-d"></a>4. Projects

Complete 1 of the following scraping projects or create your own. Store all the data in MongoDB.

1. Scrape your alma mater for class schedule information: which classes were being taught, broken down by department and course number; by which professors; at which times on which days. *(It may be easier to start with your major department first)*
2. Scrape the reviews from a category of apps in the Google Play store: the review author, the date, the star rating, the bold review title, and the review text.
3. Scrape the listings of your favorite online store. For example, I scraped Bonobos.com, and gathered the title, price and description of all the products in the "Bottoms" category.
