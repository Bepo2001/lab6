from django.urls import path
from . import views

app_name="sql"
urlpatterns=[
    path("Students",views.students,name="students"),
    path("Courses",views.courses,name="courses"),
    path("Details/<int:student_id>/",views.details,name="details")

]