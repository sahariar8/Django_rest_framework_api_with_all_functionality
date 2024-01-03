
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from employee import views

router = DefaultRouter()
router.register('student',views.EmployeeApi)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
    
]
