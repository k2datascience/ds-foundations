# General Tips

## Table of Contents
[1. SQL and Databases](#section-a)

[2. APIs](#section-b)

[3. Assignments](#section-c)

[4. Projects](#section-d)

---

### <a name="section-a"></a>1. SQL and Databases

Before diving into how to query any database, let define what a database is. A database is a data store designed for storing, querying, and processing data. Databases store the data we want and expose an interface for interacting with that data. Most technology companies use databases to structure the data coming into the system and later query specific subsets of the data to answer questions or update existing data. Database systems also come with database management software with administrative controls, security and access controls, and a language to interface with the database.

In this module we will be learning about [SQL (Structured Query Language)](https://en.wikipedia.org/wiki/SQL), which is designed to query, update and modify data stored in a database. SQL is the most common language for working with databases and is an important tool in any data professional's toolkit. While SQL is a language, it's quite different from languages like Python or R. SQL was built specifically for querying and interacting with databases and won't have much of the functionality you can expect in traditional programming languages. Since SQL is a declarative language, the user focuses on expressing what he or she wants and the computer focuses on figuring out how to perform the computation.

A database is a collection of tables, where each table is made up of rows of data and each row has values for the same set of columns across the table. A table is very similar to a DataFrame in Pandas or how a regular CSV file is structured. Both have rows of values with a consistent set of columns.

#### Querying
SQL is the most popular database querying language on the web. A SQL query has to adhere to a defined structure and vocabulary that we use to define what we want the database to do. The SQL language has a set of general statements that you combine with specific logic to express the intent of that query. It's easy to read syntax makes it more english than programming language. You can learn more about basic querying and SQL commands [here at SQLBolt](https://sqlbolt.com/). For an thorough review of all topics, Mode Analytics provides a [comprehensive tutorial](https://community.modeanalytics.com/sql/tutorial/introduction-to-sql/).

#### Databases

There are many different implementations of Relational Database Management Systems. Read a comparison of the [3 most popular systems here](https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems).

We will focus on SQLite so you can get up-and-running quickly, and the SQLAlchemy package, which is a way to write SQL commands in a Pythonic way.

[Tutorial of SQLite in Python](http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html)

*Tutorial of SQLAlchemy*

A series of beginner-focused SQLAlchemy tutorials covering a wide range of basic topics. While a lot of the information here is derived from the main documentation, the pace is slower and there are also details culled from other sources, including performance tips, comparison to other ORMs, and design philosophies. A very good effort by author Xiaonuo Gantan.

- [Index](http://www.pythoncentral.io/series/python-sqlalchemy-database-tutorial/)
- [Introductory Tutorial](http://www.pythoncentral.io/introductory-tutorial-python-sqlalchemy/)
- [How to Install SQLAlchemy](http://www.pythoncentral.io/how-to-install-sqlalchemy/)
- [Comparison to other ORMs](http://www.pythoncentral.io/sqlalchemy-vs-orms/)
- [Overview of Expression Language and ORM Queries](http://www.pythoncentral.io/overview-sqlalchemys-expression-language-orm-queries/)
- [Commonly Asked Questions](http://www.pythoncentral.io/sqlalchemy-faqs/)
- [ORM Examples](http://www.pythoncentral.io/sqlalchemy-orm-examples/)
- [Association Tables](http://www.pythoncentral.io/sqlalchemy-association-tables/)

---

### <a name="section-b"></a>2. API Introduction

Application Program Interface (API) is the perfect solution for gathering data from established technology companies. APIs are used to dynamically query and retrieve data quickly and effectively. Almost all companies that have a wealth of data available provide it to developers via API.

Modern APIs are built on a REST architectural style. Here is a [short overview video].

#### Requests
APIs are hosted on a company's web servers. For example, when you type in `www.facebook.com`, your browser sends off a request to a specific Facebook server to grab all the information needed to load `www.facebook.com`. Similarly, API make a request to a web server, however, instead of retrieving the HTML, CSS, and JavaScript for a webpage, an API request will retrieve data like a users information usually in JSON format. Don't worry if you don't know about JSON, we will cover that in a minute.

In Python, we will be using the [request library](http://docs.python-requests.org/en/master/) to make a request to a web server to retrieve the information we need.

```
import requests
response = requests.get('http://www.example.com/api/endpoint')
```

#### Types Of Requests
There are 4 types of requests you will generally use.

- GET - A GET request simply retrieves data from an endpoint.
- POST - A POST request takes some data along with it to the server. This data is usually called the payload.
- PUT - A PUT request is similar to a POST request, but is used to update the database with the payload.
- DELETE - A DELETE request is used to remove some data from the database.

An **endpoint** is a server route that is used to retrieve specific data. For example, if the endpoint was "/api/auth", we are probably trying to authenticate a login or signup form. A **payload** is data you send along with the request to the server. For example, when you sign in to any account, there is post request made, which takes along your login credentials to the server so that it can request information from the server only for your profile information that your credentials.

#### Status Codes
After you make a request to a server, you will receive some information in return. If done correctly, you will receive the data you are expecting with a 200 status code, which means everything went well. However, you have probably seen the infamous 404 or 500 status code. Like these, there are many other status codes that represent different messages. Here are some popular ones:

- `200` - everything went well, and you received what you were expecting
- `301` - you are being redirected to another endpoint. This usually happens when a company switches domains.
- `400` - the server does not recognize your request. This is a pretty vague error and can happen for multiple reasons.
- `401` - you are not authorized to access this. You'll see this message if you aren't authenticated.
- `404` - the server cannot find the resources for the request you are making
- `500` - the server has encountered an unexpected error. You will usually see this when the server is down.

If you're curious, you can find more status codes [here](https://www.w3.org/Protocols/HTTP/HTRESP.html).

```
response = requests.get("http://www.example.com/api/endpoint")
status_code = response.status_code
```


#### Query Parameters
Often times when working with APIs, you will see in the documentation that you need to pass in a parameter. In programming, we all this a query parameter. A query parameter is an argument passed in as an object that we pass along with our request. In an url you can notice a query parameter by a question mark like this `http://example.com/over/there?name=ferret`. In this example, you can see the query parameter that was passed along was {name:ferret}.

```
parameters = {"name": "ferret"}
response = requests.get("http://www.example.com/api/endpoint". parameters)
content = response.content
```


#### JSON Format
We talked a lot about sending a request, but what happens when we receive a response from the server? The most common format to receive a response is in JSON format. [JSON](http://json.org/) is way to encode data structures like lists and dictionaries to strings that ensures that they are easily readable by machines. Python uses the `json` library that allows us to convert lists and dictionaries to JSON, and convert strings to lists and dictionaries.

```
import json
response = requests.get("http://www.example.com/api/endpoint". parameters)
data = response.json()
```

---

### <a name="section-c"></a>3. Assignments

1. Complete all the lessons of [SQL Bolt](https://sqlbolt.com/) as well as the Basic, Intermediate, Advanced and Analytics training section [at Mode](https://community.modeanalytics.com/sql/tutorial/introduction-to-sql/).

2. Complete the SQLite and SQLAlchemy tutorials.

3. API Assignment

---

### <a name="section-d"></a>4. Projects

- http://knightlab.northwestern.edu/2014/03/15/a-beginners-guide-to-collecting-twitter-data-and-a-bit-of-web-scraping/
