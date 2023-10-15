from django.db import models
from django.contrib.auth.models import User  


class StudentMarks(models.Model):
    subject_code = models.CharField(max_length=50)
    subject_name = models.CharField(max_length=100)
    letter_grade = models.CharField(max_length=2)
    points = models.FloatField()
    credit = models.FloatField()
    credit_points = models.FloatField()

class StudentFees(models.Model):
    SEMESTER_CHOICES = (
        ('Semester 1', 'Semester 1'),
        ('Semester 2', 'Semester 2'),
        ('Semester 3', 'Semester 3'),
        ('Semester 4', 'Semester 4'),
        ('Semester 5', 'Semester 6'),
        ('Semester 6', 'Semester 6'),
        ('Semester 7', 'Semester 7'),
    )

    semester = models.CharField(max_length=20, choices=SEMESTER_CHOICES)
    semester_fees = models.DecimalField(max_digits=10, decimal_places=2)
    bus_fare = models.DecimalField(max_digits=10, decimal_places=2)
    hostel_charge = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    fine = models.DecimalField(max_digits=10, decimal_places=2)
    examination_fees = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.semester


class StudentAttendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Optional link to a specific user
    date = models.DateField()
    is_present = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user} - {self.date}: {'Present' if self.is_present else 'Absent'}"
