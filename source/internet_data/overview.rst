.. index:: API, HTTP, requests, JSON, internet data, web services

.. _Internet-Data:

Internet Data
=============

.. note::
   *Source:* Contributed by PhD students in COMP 501 at Loyola University Chicago.

Every day you interact with online services powered by data: weather apps, maps,
movie databases, sports scores, and more. Much of this data is accessible to
programmers through **APIs** (Application Programming Interfaces). An API provides
a structured way to request information from a web service without needing to scrape
raw HTML.

.. index:: API; definition, web service; API, HTTP; API communication

What Is an API?
---------------

An API defines a predictable way for applications to communicate with each other.
Many websites expose public APIs that let you request data directly. Examples include:

- Weather services
- News headlines
- Public transportation schedules
- Currency exchange rates
- Sports statistics
- GitHub repository information

Most APIs communicate over HTTP and return data in JSON format.

.. index:: HTTP; GET request, HTTP; POST request, query parameters; URL, URL; query string

HTTP Basics
-----------

The most common HTTP request types are:

- **GET** — retrieve data (this is what we use in this chapter)
- **POST** — send new data
- **PUT/PATCH** — update existing data
- **DELETE** — remove data

A URL can include **query parameters** to filter or customize the response:

.. code-block:: none

   https://api.example.com/weather?city=Chicago&units=metric

Everything after ``?`` is a query string: ``city=Chicago`` and ``units=metric`` are
two parameters separated by ``&``.

.. index:: requests module, requests.get(), HTTP; status codes, response.status_code

The ``requests`` Module
------------------------

Install it if needed:

.. code-block:: none

   pip install requests

Basic usage:

.. code-block:: python

   import requests

   url = "https://api.github.com"
   response = requests.get(url)

   print(response.status_code)
   print(response.text)

Common status codes:

- ``200`` — OK (success)
- ``404`` — Not Found
- ``401`` — Unauthorized
- ``500`` — Server Error

Always check the status code before using the response data.

.. index:: JSON; parsing with requests, response.json(), API response; dict conversion

Parsing JSON
------------

Most APIs return JSON, which Python's ``requests`` library can convert directly to
a dictionary:

.. code-block:: python

   import requests

   url = "https://api.github.com/repos/python/cpython"
   response = requests.get(url)

   if response.status_code == 200:
       data = response.json()
       print(data["full_name"])
       print(data["stargazers_count"])

``response.json()`` parses the JSON body and returns the equivalent Python object —
usually a dictionary or a list of dictionaries.

.. index:: query parameters; requests, requests.get(); params dict

Using Query Parameters
-----------------------

Instead of building query strings manually, pass parameters as a dictionary:

.. code-block:: python

   import requests

   url = "https://api.example.com/search"
   params = {"q": "python", "limit": 5}

   response = requests.get(url, params=params)
   print(response.url)        # shows the full URL with parameters appended
   print(response.json())

.. index:: requests.exceptions.ConnectionError, requests.exceptions.Timeout, HTTP; error handling

Handling Errors
---------------

Defensive code checks the status code and handles network failures:

.. code-block:: python

   import requests

   url = "https://api.example.com/data"
   try:
       response = requests.get(url, timeout=5)
       if response.status_code != 200:
           print("Error:", response.status_code)
       else:
           print(response.json())
   except requests.exceptions.ConnectionError:
       print("Network error: could not connect.")
   except requests.exceptions.Timeout:
       print("Request timed out.")

.. index:: json.dump(); file output, API response; saving to file

Saving API Results to a File
-----------------------------

After retrieving data you can persist it locally for later analysis:

.. code-block:: python

   import requests
   import json

   url = "https://api.github.com/users/octocat"
   response = requests.get(url)

   if response.status_code == 200:
       data = response.json()
       with open("octocat.json", "w") as f:
           json.dump(data, f, indent=2)

``json.dump`` writes a Python object to a file as JSON. ``indent=2`` makes the
output human-readable.

.. index:: GitHub API; example, requests; complete example

Putting It Together
-------------------

Here is a complete program that looks up a GitHub user:

.. literalinclude:: ../../examples/introcs-python/internet_data/github_user_lookup.py
   :language: python

Exercises
---------

1. Request data from ``https://api.github.com/users/octocat`` and print the
   ``login``, ``public_repos``, and ``followers`` fields.
2. Use the Open-Meteo API to fetch the first five hourly temperature values
   for Chicago (latitude 41.88, longitude -87.62):

   .. code-block:: none

      https://api.open-meteo.com/v1/forecast?latitude=41.88&longitude=-87.62&hourly=temperature_2m

3. Request country information from:

   .. code-block:: none

      https://restcountries.com/v3.1/name/canada

   Print the population, region, and capital.

4. Write a program that accepts a city name from the user, fetches its coordinates
   from:

   .. code-block:: none

      https://geocoding-api.open-meteo.com/v1/search?name=<city>

   and saves the JSON response to ``city_data.json``. Handle the case where the
   city is not found and the case where there is no internet connection.

5. Some APIs paginate large datasets. Write a loop that fetches up to five pages
   of results from an API of your choice, merges them into a single list, and
   prints the total number of items retrieved.
