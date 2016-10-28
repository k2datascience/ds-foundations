# General Tips

## Table of Contents
[1. Web Scraping](#section-a)

[2. SQL and Databases](#section-b)

[3. Assignments](#section-c)

[4. Projects](#section-d)

---

### <a name="section-a"></a>1. Web Scraping

Web scraping (web harvesting or web data extraction) is a computer software technique of extracting information from websites. This is accomplished by either directly implementing the Hypertext Transfer Protocol (on which the Web is based), or embedding a web browser.

Web scraping is closely related to web indexing, which indexes information on the web using a bot or web crawler and is a universal technique adopted by most search engines. In contrast, web scraping focuses more on the transformation of unstructured data on the web, typically in HTML format, into structured data that can be stored and analyzed in a central local database or spreadsheet. Web scraping is also related to web automation, which simulates human browsing using computer software. Uses of web scraping include online price comparison, contact scraping, weather data monitoring, website change detection, research, web mashup and web data integration.

Please complete the exercises throughout the first book. You will often have to use web scraping to obtain data on the internet throughout the bootcamp. The second book goes more in-depth on building resuable and scalable scrapers. It is optional.

[A beginner / intermediate reference book](web_scraping_with_python.pdf).

[Advanced web scraping with Scrapy](resources/scrapy.pdf).

---

### <a name="section-b"></a>2. SQL and Databases

Before diving into how to query any database, let define what a database is. A database is a data store designed for storing, querying, and processing data. Databases store the data we want and expose an interface for interacting with that data. Most technology companies use databases to structure the data coming into the system and later query specific subsets of the data to answer questions or update existing data. Database systems also come with database management software with administrative controls, security and access controls, and a language to interface with the database.

In this module we will be learning about [SQL (Structured Query Language)](https://en.wikipedia.org/wiki/SQL), which is designed to query, update and modify data stored in a database. SQL is the most common language for working with databases and is an important tool in any data professional's toolkit. While SQL is a language, it's quite different from languages like Python or R. SQL was built specifically for querying and interacting with databases and won't have much of the functionality you can expect in traditional programming languages. Since SQL is a declarative language, the user focuses on expressing what he or she wants and the computer focuses on figuring out how to perform the computation.

A database is a collection of tables, where each table is made up of rows of data and each row has values for the same set of columns across the table. A table is very similar to a DataFrame in Pandas or how a regular CSV file is structured. Both have rows of values with a consistent set of columns.

#### Querying
SQL is the most popular database querying language on the web. A SQL query has to adhere to a defined structure and vocabulary that we use to define what we want the database to do. The SQL language has a set of general statements that you combine with specific logic to express the intent of that query. It's easy to read syntax makes it more english than programming language. You can learn more about querying and SQL commands [here at SQLBolt](https://sqlbolt.com/),

#### Databases

There are many different implementations of Relational Database Management Systems. Read a comparison of the [3 most popular systems here](https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems).

We will focus on SQLite so you can get up-and-running quickly, and the SQLAlchemy package, which is a way to write SQL commands in a Pythonic way.

[Tutorial of SQLite in Python](http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html)

*Tutorial of SQLAlchemy*

A series of beginner-focused SQLAlchemy tutorials covering a wide range of basic topics. While a lot of the information here is derived from the main documentation, the pace is slower and there are also details culled from other sources, including performance tips, comparison to other ORMs, and design philosophies. A very good effort by author Xiaonuo Gantan.

[Index](http://www.pythoncentral.io/series/python-sqlalchemy-database-tutorial/)
[Introductory Tutorial](http://www.pythoncentral.io/introductory-tutorial-python-sqlalchemy/)
[How to Install SQLAlchemy](http://www.pythoncentral.io/how-to-install-sqlalchemy/)
[Comparison to other ORMs](http://www.pythoncentral.io/sqlalchemy-vs-orms/)
[Overview of Expression Language and ORM Queries](http://www.pythoncentral.io/overview-sqlalchemys-expression-language-orm-queries/)
[Commonly Asked Questions](http://www.pythoncentral.io/sqlalchemy-faqs/)
[ORM Examples](http://www.pythoncentral.io/sqlalchemy-orm-examples/)
[Association Tables](http://www.pythoncentral.io/sqlalchemy-association-tables/)

---

### <a name="section-c"></a>3. Assignments

1. Complete the Web Scraping in Python book and all the exercises.

2. Complete all the lessons of [SQL Bolt](https://sqlbolt.com/) as well as the 2 additional topics.

3. Complete the SQLite and SQLAlchemy tutorials.

---

### <a name="section-d"></a>4. Projects

- About 6 years ago I scraped most (all?) of the reviews off of Google Play store (then called Android Market), and used to to analyze what makes people like, dislike, and uninstall apps.
