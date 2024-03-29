from django.db import models



class Courses(models.Model):
    courseID=models.CharField(max_length=7,primary_key=True)

    def __str__(self):
        return self.courseID

class Student(models.Model):
    studentName=models.CharField(max_length=64)
    studentID=models.IntegerField(primary_key=True)
    studentGPA=models.FloatField(max_length=1)
    studentYear=models.IntegerField(max_length=4)
    courses=models.ManyToManyField(Courses,related_name="courses_for_student")
    

    def __str__(self):
        return self.studentName