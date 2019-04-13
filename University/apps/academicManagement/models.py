from django.db import models

# Create your models here.
class Student(models.Model):
    lastName = models. CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    Dni = models.CharField(max_length=8)
    birthDate = models.DateField()
    GNRES = (('F','Female'),('M','Male'))
    Gnre = models.CharField(max_length=1, choices=GNRES, default='M')

    def FullName(self):
        string = "{0} {1}"
        return string.format(self.firstName, self.lastName)

    def __str__(self):
        return self.FullName()

class Course(models.Model):
    Name = models.CharField(max_length=50)
    Credits = models.PositiveSmallIntegerField()
    State = models.BooleanField(default=True)

    def __str__(self):
        string = "{0} ({1})"
        return string.format(self.Name, self.Credits)

class Enrollment(models.Model):
    Student = models.ForeignKey(Student, null=False, blank= False, on_delete=models.CASCADE)
    Course = models.ForeignKey(Course, null=False, blank=False, on_delete=models.CASCADE)
    EnrollmentDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        string = "{0} => {1}"
        return string.format(self.Student, self.Course.Name)
