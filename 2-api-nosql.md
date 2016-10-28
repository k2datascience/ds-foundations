# General Tips

## Table of Contents
[1. APIs](#section-a)

[2. NoSQL and Databases](#section-b)

[3. Assignments](#section-c)

[4. Projects](#section-d)

---

### <a name="section-a"></a>1. API Introduction

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

-GET - A GET request simply retrieves data from an endpoint.
-POST - A POST request takes some data along with it to the server. This data is usually called the payload.
-PUT - A PUT request is similar to a POST request, but is used to update the database with the payload.
-DELETE - A DELETE request is used to remove some data from the database.

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

### <a name="section-b"></a>2. NoSQL and Databases

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

### <a name="section-c"></a>3. Assignments

1. API Assignment

2. Complete the Data Wrangling with MongoDB course on Udacity

---

### <a name="section-d"></a>4. Projects

- http://knightlab.northwestern.edu/2014/03/15/a-beginners-guide-to-collecting-twitter-data-and-a-bit-of-web-scraping/
