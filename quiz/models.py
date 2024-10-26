from django.db import models

# Create your models here.

class Test(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Question(models.Model):
    test = models.ForeignKey(Test, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    correct_answer = models.CharField(max_length=100)
    options = models.JSONField()  # Список вариантов ответов

    def __str__(self):
        return f"Question in {self.test.title}"

class TestResult(models.Model):
    test = models.ForeignKey('Test', on_delete=models.CASCADE, related_name='results')
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.surname} - {self.score} баллов"
