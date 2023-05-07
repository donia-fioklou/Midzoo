from django.urls import include, path
from rest_framework import routers
from api.views.Engine_view import EngineViewSet

from api.views.customize_user_view import  GetUserByEmail, Registration
from api.views.message_view import MessageViewSet
from api.views.path_view import PathViewSet
from api.views.reservation_view import ReservationViewSet
from api.views.school_view import SchoolViewSet

app_name = 'api'
router=routers.SimpleRouter()
router.register('register',Registration,basename='register')
router.register('engine',EngineViewSet,basename='engine')
router.register('message',MessageViewSet,basename='message')
router.register('path',PathViewSet,basename='path')
router.register('reservation',ReservationViewSet,basename='reservation')
router.register('school',SchoolViewSet,basename='school')



urlpatterns = [
    path('api/',include(router.urls)),
    path('api/GetUserByEmail/',GetUserByEmail.as_view(),name='GetUserByEmail'),

]
