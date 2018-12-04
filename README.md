# insta_v2
This is the updated Repo


# 1. How to Install ?
A. Using Docker Image

-> clone the codebase

-> docker-compose up

B. Using venv

-> create and activate a virtual env

-> clone the codebase inside virtual env

-> install the dependencies: pip install requirements.txt

-> change the database credentials in settings.py

-> make migrations : python manage.py migrate users

-> run the server : python manage.py runserver

# 2. How to Test ?

A. Create A user

curl -X POST \
  http://localhost:8000/api/users/ \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 953e47d9-3d16-4c0e-b291-782f90fec901' \
  -H 'cache-control: no-cache' \
  -d '{
      "first_name" : "Luee",
      "email" : "abcdr@gmail.com",
      "phone_number" : "+919980522044",
      "last_name" : "Garnaik",
      "role" : "REGULAR"
   }
'

B. Get A Single  user by ID

curl -X GET \
  http://localhost:8000/api/users/2/ \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 90911d99-c6ad-44c1-923e-ed4f17ee6a42' \
  -H 'cache-control: no-cache' \
  -d '{
      "first_name" : "Maxi"

   }
'

C. Get all user

curl -X GET \
  http://localhost:8000/api/users/ \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 1ef93583-fb9c-46ff-88de-a1758357ae5a' \
  -H 'cache-control: no-cache' \
  -d '{
      "first_name" : "Maxi"

   }
'

C. Update a User

curl -X PUT \
  http://localhost:8000/api/users/1/ \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 4eeee875-c35b-448d-9622-90d2d40c1f6f' \
  -H 'cache-control: no-cache' \
  -d '{
      "first_name" : "Maxi"

   }
'

D. Delete A User

curl -X DELETE \
  http://localhost:8000/api/users/1/ \
  -H 'Content-Type: application/json' \
'



