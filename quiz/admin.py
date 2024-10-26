# Register your models here.
from django.contrib import admin
from .models import Test, Question, TestResult

admin.site.register(Test)
admin.site.register(Question)
admin.site.register(TestResult)
