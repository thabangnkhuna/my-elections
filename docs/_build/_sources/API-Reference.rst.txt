API Reference
=============

MyParty provides a RESTful API to interact with party and guest data programmatically. The API allows you to perform CRUD operations on parties, guests, and expenses.

Base URL: /api/v1/

Endpoints
---------

GET /parties/
- Returns a list of all parties.

GET /parties/{party_id}/
- Returns details of a specific party.

POST /parties/
- Creates a new party.

PUT /parties/{party_id}/
- Updates details of an existing party.

DELETE /parties/{party_id}/
- Deletes a party.

And more endpoints for guests and expenses...

Authentication
--------------
The API requires authentication using an API token. To obtain a token, create a superuser and generate a token from the admin dashboard.

For more details and examples, please refer to the API documentation.
