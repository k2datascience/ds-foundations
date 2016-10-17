##API Introduction
So far you have worked with some small data sets, however, in the real world you will be working with large amounts of data that is always changing. It doesn't make much sense to download a file each time you want to use that set of data. So what do we use?

Application Program Interface (API) is the perfect solution. APIs are used to dynamically query and retrieve data quickly and effectively. Almost all companies that have a wealth of data available provide it to developers via API.

##Requests
APIs are hosted on a company's web servers. For example, when you type in `www.facebook.com`, your browser sends off a request to a specific Facebook server to grab all the information needed to load `www.facebook.com`. Similarly, API make a request to a web server, however, instead of retrieving the HTML, CSS, and JavaScript for a webpage, an API request will retrieve data like a users information usually in JSON format. Don't worry if you don't know about JSON, we will cover that in a minute.

In Python, we will be using the [request library](http://docs.python-requests.org/en/master/) to make a request to a web server to retrieve the information we need.

```
import requests
response = requests.get('http://www.example.com/api/endpoint')
```

##Types Of Requests
There are 4 types of requests you will generally use.

-GET - A GET request simply retrieves data from an endpoint.
-POST - A POST request takes some data along with it to the server. This data is usually called the payload.
-UPDATE - An UPDATE request is similar to a post request, but is used to update the database with the payload.
-DELETE - A DELETE request is used to remove some data from the database.

An **endpoint** is a server route that is used to retrieve specific data. For example, if the endpoint was "/api/auth", we are probably trying to authenticate a login or signup form. A **payload** is data you send along with the request to the server. For example, when you sign in to any account, there is post request made, which takes along your login credentials to the server so that it can request information from the server only for your profile information that your credentials.

##Status Codes
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


##Query Parameters
Often times when working with APIs, you will see in the documentation that you need to pass in a parameter. In programming, we all this a query parameter. A query parameter is an argument passed in as an object that we pass along with our request. In an url you can notice a query parameter by a question mark like this `http://example.com/over/there?name=ferret`. In this example, you can see the query parameter that was passed along was {name:ferret}.

```
parameters = {"name": "ferret"}
response = requests.get("http://www.example.com/api/endpoint". parameters)
content = response.content
```


##JSON Format
We talked a lot about sending a request, but what happens when we receive a response from the server? The most common format to receive a response is in JSON format. [JSON](http://json.org/) is way to encode data structures like lists and dictionaries to strings that ensures that they are easily readable by machines. Python uses the `json` library that allows us to convert lists and dictionaries to JSON, and convert strings to lists and dictionaries.

```
import json
response = requests.get("http://www.example.com/api/endpoint". parameters)
data = response.json()
```

**Assignments:**
Complete the [Codecademy Python APIs Tutorial](https://www.codecademy.com/courses/python-intermediate-en-6zbLp/0/1)

Complete the web scraping tutorial on [AnalyticsVidhya](https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/)

Read [API Integration in Python - Part 1](https://realpython.com/blog/python/api-integration-in-python/)
