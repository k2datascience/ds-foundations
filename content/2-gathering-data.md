# APIs, Web Scraping, SQL and Relational Databases

Learn how to acquire data from APIs and websites. Then, move on to storing and retrieving data using SQL queries and relational databases.

## Table of Contents
[1. APIs](#section-a)

[2. Web Scraping](#section-b)

[3. SQL and Databases](#section-c)

[4. Assignments](#section-d)

[5. Projects](#section-d)

---

### <a name="section-a"></a>1. API Introduction

Application Program Interface (API) is the perfect solution for gathering data from established technology companies. APIs are used to dynamically query and retrieve data quickly and effectively. Almost all companies that have a wealth of data available provide it to developers via API.

Modern APIs are built on a REST architectural style. Here is a [short overview video](https://www.youtube.com/watch?v=7YcW25PHnAA).

#### Requests
APIs are hosted on a company's web servers. For example, when you type in `www.facebook.com`, your browser sends off a request to a specific Facebook server to grab all the information needed to load `www.facebook.com`. Similarly, APIs make a request to a web server, however, instead of retrieving the HTML, CSS, and JavaScript for a webpage, an API request will retrieve data like a users information usually in JSON format. Don't worry if you don't know about JSON, we will cover that in a minute.

In Python, we will be using the Requests library to make a request to a web server to retrieve the information we need.

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
Often times when working with APIs, you will see in the documentation that you need to pass in a parameter. In programming, this is called a query parameter. A query parameter is an argument passed in as an object that we pass along with our request. In a URL you can notice a query parameter by a question mark like this `http://example.com/over/there?name=ferret`. In this example, you can see the query parameter that was passed along was {name:ferret}.

```
parameters = {"name": "ferret"}
response = requests.get("http://www.example.com/api/endpoint", parameters)
content = response.content
```


#### JSON Format
We talked a lot about sending a request, but what happens when we receive a response from the server? The most common format to receive a response is in JSON format. [JSON](http://json.org/) is way to encode data structures like lists and dictionaries to strings that ensures that they are easily readable by machines. Python uses the `json` library that allows us to convert lists and dictionaries to JSON, and convert strings to lists and dictionaries.

```
import json
response = requests.get("http://www.example.com/api/endpoint", parameters)
data = response.json()
```

#### Tutorial

Follow along with the [Requests quickstart](http://docs.python-requests.org/en/master/user/quickstart).

---

### <a name="section-b"></a>2. Web Scraping

Web scraping (web harvesting or web data extraction) is a computer software technique of extracting information from websites. This is accomplished by either directly implementing the Hypertext Transfer Protocol (on which the Web is based), or embedding a web browser.

Web scraping is closely related to web indexing, which indexes information on the web using a bot or web crawler and is a universal technique adopted by most search engines. In contrast, web scraping focuses more on the transformation of unstructured data on the web, typically in HTML format, into structured data that can be stored and analyzed in a central local database or spreadsheet. Web scraping is also related to web automation, which simulates human browsing using computer software. Uses of web scraping include online price comparison, contact scraping, weather data monitoring, website change detection, research, web mashup and web data integration.

#### Beautiful Soup Documentation

Beautiful Soup is the web scraping Python library that you will use during the bootcamp. Please go through its [official documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc).

---

### <a name="section-c"></a>3. SQL and Databases

Before diving into how to query any database, let's define what a database is. A database is a data store designed for storing, querying, and processing data. Databases store the data we want and expose an interface for interacting with that data. Most technology companies use databases to structure the data coming into the system and later query specific subsets of the data to answer questions or update existing data. Database systems also come with database management software with administrative controls, security and access controls, and a language to interface with the database.

In this module we will be learning about [SQL (Structured Query Language)](https://en.wikipedia.org/wiki/SQL), which is designed to query, update and modify data stored in a database. SQL is the most common language for working with databases and is an important tool in any data professional's toolkit. While SQL is a language, it's quite different from languages like Python or R. SQL was built specifically for querying and interacting with databases and won't have much of the functionality you can expect in traditional programming languages. Since SQL is a declarative language, the user focuses on expressing what he or she wants and the computer focuses on figuring out how to perform the computation.

A database is a collection of tables, where each table is made up of rows of data and each row has values for the same set of columns across the table. A table is very similar to a DataFrame in Pandas or how a regular CSV file is structured. Both have rows of values with a consistent set of columns.

#### Querying

SQL is the most popular database querying language on the web. A SQL query has to adhere to a defined structure and vocabulary that we use to define what we want the database to do. The SQL language has a set of general statements that you combine with specific logic to express the intent of that query. Its easy to read syntax makes it more English-like than programming languages. You can learn more about basic querying and SQL commands [here at SQLBolt](https://sqlbolt.com/). For a thorough review of all topics, Mode Analytics provides a [comprehensive tutorial](https://community.modeanalytics.com/sql/tutorial/introduction-to-sql/).

#### Databases

There are many different implementations of Relational Database Management Systems. Read a comparison of the [3 most popular systems here](https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems).

We will focus on SQLite so you can get up-and-running quickly - [tutorial of SQLite in Python](http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html).

---

### <a name="section-d"></a>4. Assignments

1. Review all the API learning resources and complete the tutorial.

2. Complete the web scraping tutorial about BeautifulSoup.

3. Complete all the lessons of [SQL Bolt](https://sqlbolt.com/) as well as the Basic, Intermediate, Advanced and Analytics training section [at Mode](https://community.modeanalytics.com/sql/tutorial/introduction-to-sql/).

4. Complete the SQLite tutorial.

---

### <a name="section-e"></a>5. Projects

Complete 2 projects. One about APIs and the other about scraping. Feel free to investigate the data similar to the Mode Analytics Training tasks and detail your findings.

#### API Projects

1. GitHub Jobs
2. (Planned) Reddit


#### Scraping Projects

1. American Federation of Labor - Scrape the [Legislative Alerts](http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts) for the most recent year. Store the title, the link URL and the date. Decide which data structure would be best and export your final data to a [pickle object](https://docs.python.org/3/library/pickle.html). *Extra challenge: Build a program that can extract all the alerts from all the years in the drop-down.*
2. National Weather Service - Scrape your [local weather](http://forecast.weather.gov/MapClick.php?lat=40.7142&lon=-74.0059) forecast. You should be able to retrieve each item in the extended forecast. Try to extract the longer weather description for each forecast. Decide which data structure would best and export your final data to a [pickle object](https://docs.python.org/3/library/pickle.html).. *Extra challenge: Build a program that can extract the extended forecast from the 3 largest cities near you.*

#### Optional API Projects

1. Sign up for the [Dark Sky API](https://darksky.net/dev/). Gather the daily weather forecasts for the city you live in during the entire year of 2015. Store the weather observation, the minimum temperature, the maximum temperature, humidity, dew point, wind speed and precipitation accumulation.
2. Sign up for the [Twitter API](https://dev.twitter.com/rest/public/search). Gather the last 100 tweets from your top 20 favorite actors, athletes, comedians, musicians, or other celebrities and public figures.
3. Sign up for the [YouTube API](https://developers.google.com/youtube/) or [SoundCloud API](https://developers.soundcloud.com/). Find the 10 most popular songs for your 5 favorite artists. Rank the songs by number of plays, listens or views.
4. If you want to design your own project, check out the following links for interesting APIs: [Reddit thread](https://www.reddit.com/r/webdev/comments/3wrswc/what_are_some_fun_apis_to_play_with/), [Computer Science Zone](http://www.computersciencezone.org/50-most-useful-apis-for-developers/) or [Mashape](https://market.mashape.com/).

#### Optional Scraping Projects

1. Scrape your alma mater for class schedule information: which classes are being taught, broken down by department and course number; by which professors; at which times on which days. *(It may be easier to start with the department of your major first)*
2. Scrape the reviews from a category of apps in the Google Play store: the review author, the date, the star rating, the bold review title, and the review text.
3. Scrape the listings of your favorite online store.
4. Do you own project.

---

#### Feedback (optional)
###### (1 - 2 minutes)

Please provide us with [feedback](https://goo.gl/forms/gkWsYCSFXw2z40v33) once you have just completed this page. It will help us improve the program both for you and for fellow students.
