from django.contrib import admin
from .models import StudentMarks
from .models import StudentFees
from .models import StudentAttendance

admin.site.register(StudentMarks)
admin.site.register(StudentFees)
admin.site.register(StudentAttendance)
