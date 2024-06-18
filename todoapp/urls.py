from django.urls import path
from rest_framework_nested import routers
from . import views


router=routers.DefaultRouter()

router.register('notes',views.NoteViewSet,basename='notes')
router.register('writers',views.WriterViewSet)

urlpatterns =router.urls
