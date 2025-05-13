from django.urls import path
from . import views

urlpatterns = [
	path('genders/list', views.gender_list),
	path('genders/add', views.add_gender),
	path('genders/edit/<int:genderId>', views.edit_gender),
	path('genders/delete/<int:genderId>', views.delete_gender),

]
