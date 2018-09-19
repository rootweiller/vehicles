# Vehicles Module

for install run <code>docker-compose up</code>

It is necessary to have installed and configured docker and docker-compose

In the environment variables define:
* DB_NAME
* DB_USER
* DB_PASS
* DB_SERVICE
* DB_PORT


# Endpoints

* Method GET:
Search for DNI: <url>http://127.0.0.1:8000/users/vehicles/search/?dni=12345678</url>
Search for Name of user: <url>http://127.0.0.1:8000/users/vehicles/search/?name=Juan</url>
Search for license plate: <url>http://127.0.0.1:8000/users/vehicles/search/?license_plate=ABC-123</url>

* Method POST:
Add Vehicles to DB: <url>http://127.0.0.1:8000/users/vehicles/</url>
Add Users: <url>http://127.0.0.1:8000/users/</url>

# Test 

<code>python manage.py test users</code>