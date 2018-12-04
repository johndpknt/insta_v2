from users.viewsets import UsersViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', SnippetViewSet, base_name='users')

# for url in router.urls:
#     print(url, '\n')
