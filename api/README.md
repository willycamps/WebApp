REST-API Documentation
=========


Installation
------------

After cloning, create a virtual environment and install the requirements

    $ virtualenv flaskapi
    $ source flaskapi/bin/activate
    (flaskapi) $ pip3 install -r requirements.txt


Running
-------

To run the server use the following command:

    (flaskapi) $ python api.py
     * Running on http://127.0.0.1:5000/ (Press Ctrl C)
     * Restarting stat

Then from a different terminal window you can send requests.

API Documentation
-----------------

- POST **/api/register**

    Register a new user.<br>
    The body must contain a JSON object that defines `username` and `password` fields.<br>
    On success a status code 201 is returned. The body of the response contains a JSON object with the newly added user. A `Location` header contains the URI of the new user.<br>
    On failure status code 400 (bad request) is returned.<br>
    Notes:
    - The password is hashed before it is stored in the database. Once hashed, the original password is discarded.
    - In a production deployment secure HTTP must be used to protect the password in transit.

- GET **/api/users/&lt;int:id&gt;**

    Return a user.<br>
    On success a status code 200 is returned. The body of the response contains a JSON object with the requested user.<br>
    On failure status code 400 (bad request) is returned.

- GET **/api/users/**

    Return all the users.
    On success a status code 200 is returned. The body of the response contains a JSON object with the all users.
    On failure status code 400 (bad request) is returned.

- GET **/api/login**

    Return a protected resource.
    This request must be authenticated using a HTTP Basic Authentication header. Instead of username and password, the client can provide a valid authentication token in the username field. If using an authentication token the password field is not used and can be set to any value.
    On success a JSON object with data for the authenticated user is returned.
    On failure status code 401 (unauthorized) is returned.

- GET **/api/token**

    Return an authentication token.<br>
    This request must be authenticated using a HTTP Basic Authentication header.<br>
    On success a JSON object is returned with a field `token` set to the authentication token for the user and a field `duration` set to the (approximate) number of seconds the token is valid.<br>
    On failure status code 401 (unauthorized) is returned.

- GET **/api/resource**

    Return a protected resource.<br>
    This request must be authenticated using a HTTP Basic Authentication header. Instead of username and password, the client can provide a valid authentication token in the username field. If using an authentication token the password field is not used and can be set to any value.<br>
    On success a JSON object with data for the authenticated user is returned.<br>
    On failure status code 401 (unauthorized) is returned.

Example
-------

The following `curl` command registers a new user with username `willy` and password `python`:

    $curl -i -X POST -H "Content-Type: application/json" -d '{"name":"willy","password":"python"}' http://127.0.0.1:5000/register 
    
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 43
    Server: Werkzeug/0.16.0 Python/3.8.5
    Date: Sun, 06 Jun 2021 22:44:53 GMT

    {
        "message": "registered successfully"
    }

    curl -i -X GET -H "Content-Type: application/json" http://127.0.0.1:5000/api/users/1
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 26
    Server: Werkzeug/0.16.0 Python/3.8.5
    Date: Sun, 06 Jun 2021 22:52:55 GMT

    {
    "username": "willy"
    }


    curl -i -X GET -H "Content-Type: application/json" http://127.0.0.1:5000/api/users
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 463
    Server: Werkzeug/0.16.0 Python/3.8.5
    Date: Sun, 06 Jun 2021 23:02:13 GMT

    {
    "users": [
        {
        "admin": false, 
        "name": "willy", 
        "password": "sha256$Hve7h6Pl$83a5f94a5685aa4158e31701c1281c6587e01f9ff6df7ee8c7a1936bede42d99", 
        "public_id": "4c99115b-43ab-4dfa-89c2-d202d7360054"
        }, 
        {
        "admin": false, 
        "name": "willy", 
        "password": "sha256$9jgLl6Vk$bbafad4b82518ba8a7ea48d5a0679bb66f95ee61a16b4da154b125271eb106e0", 
        "public_id": "b016d441-24cc-4a36-96ed-c228b2275216"
        }
    ]
    }

    curl -u willy:python -i -X GET http://127.0.0.1:5000/api/login
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 191
    Server: Werkzeug/0.16.0 Python/3.8.5
    Date: Sun, 06 Jun 2021 23:07:58 GMT

    {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiI0Yzk5MTE1Yi00M2FiLTRkZmEtODljMi1kMjAyZDczNjAwNTQiLCJleHAiOjE2MjMwMjI2Nzh9.iM5gRhU2q05rk3KYOgXjEz1r7KsyjeulT_Wo_aktVjk"
    }


    These credentials can now be used to access protected resources:

    $ curl -u willy:python -i -X GET http://127.0.0.1:5000/api/resource
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 30
    Server: Werkzeug/0.9.4 Python/2.7.3
    Date: Thu, 28 Nov 2013 20:02:25 GMT
    
    {
      "data": "Hello, Willy!"
    }

Using the wrong credentials the request is refused:

    $ curl -u Willy:Ruby -i -X GET http://127.0.0.1:5000/api/resource
    HTTP/1.0 401 UNAUTHORIZED
    Content-Type: text/html; charset=utf-8
    Content-Length: 19
    WWW-Authenticate: Basic realm="Authentication Required"
    Server: Werkzeug/0.9.4 Python/2.7.3
    Date: Thu, 28 Nov 2013 20:03:18 GMT
    
    Unauthorized Access


$ curl -u willy:python -i -X GET http://127.0.0.1:5000/api/token
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 139
    Server: Werkzeug/0.9.4 Python/2.7.3
    Date: Thu, 28 Nov 2013 20:04:15 GMT
    
    {
      "duration": 600,
      "token": "eyJhbGciOiJIUzI1NiIsImV4cCI6MTM4NTY2OTY1NSwiaWF0IjoxMzg1NjY5MDU1fQ.eyJpZCI6MX0.XbOEFJkhjHJ5uRINh2JA1BPzXjSohKYDRT472wGOvjc"
    }

And now during the token validity period there is no need to send username and password to authenticate anymore:

    $ curl -u eyJhbGciOiJIUzI1NiIsImV4cCI6MTM4NTY2OTY1NSwiaWF0IjoxMzg1NjY5MDU1fQ.eyJpZCI6MX0.XbOEFJkhjHJ5uRINh2JA1BPzXjSohKYDRT472wGOvjc:x -i -X GET http://127.0.0.1:5000/api/resource
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 30
    Server: Werkzeug/0.9.4 Python/2.7.3
    Date: Thu, 28 Nov 2013 20:05:08 GMT
    
    {
      "data": "Hello, Willy!"
    }

Once the token expires it cannot be used anymore and the client needs to request a new one. Note that in this last example the password is arbitrarily set to `x`, since the password isn't used for token authentication.

An interesting side effect of this implementation is that it is possible to use an unexpired token as authentication to request a new token that extends the expiration time. 
This effectively allows the client to change from one token to the next and never need to send username and password after the initial token was obtaine

## TODO
* Object Relational Mapper (ORM) 

Change Log
----------

**v0.2** - First Endpoints created.

**v0.1** - Initial release.

