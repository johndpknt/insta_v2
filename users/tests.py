from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .views import UserViewSet
# Create your tests here.


from .models import Users


class UsersTestCase(TestCase):


    def setUp(self):
        Users.objects.create(first_name = "Test_FirstName", last_name = "TestLastName", email = "test@test.com", phone_number = "+919980522044", role = "admin")


    def test_user_get(self):
        factory = APIRequestFactory()
        request = factory.get("/api/users/")
        view = UserViewSet.as_view({'get': 'list'})
        response = view(request)
        assert response.status_code == 200

    def test_user_creation(self):
        factory = APIRequestFactory()
        request = factory.post("/api/users/",{"first_name": "Test", "last_name": "LastName", "email": "john@gmail.com", "phone_number": "+919980522044", "role": "REGULAR"} ,format='json')
        view = UserViewSet.as_view({'post': 'create'})
        response = view(request)
        assert response.status_code == 201

    def test_user_updation(self):
        print("Hello Testing the updation ")
        factory = APIRequestFactory()
        request = factory.put("/api/users/",{"role": "REGULAR"} ,format='json')
        view = UserViewSet.as_view({'put': 'update'})
        import pdb;pdb.set_trace()
        response = view(request, pk=1)
        assert response.status_code == 201


    def test_user_deletion(self):
        print("testing user deleting")

        
