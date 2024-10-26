from django.shortcuts import render, get_object_or_404
from .models import Test, Question, TestResult
from django.core.mail import send_mail
from django.conf import settings

def send_result_email(email, name, surname, score):
    subject = 'Результаты теста'
    message = f'Привет, {name} {surname}!\nВы набрали {score} баллов в тесте.'
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

def take_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = test.questions.all()
    answers = {}
    score = 0

    if request.method == 'POST':
        for question in questions:
            user_answer = request.POST.get(f'answer_{question.id}', 'Нет ответа')
            answers[question.text] = user_answer
            if user_answer == question.correct_answer:
                score += 1

        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')

        # Сохраняем результат в базу данных
        TestResult.objects.create(
            test=test,
            name=name,
            surname=surname,
            email=email,
            score=score
        )

        # Отправляем email с результатами
        send_answers_to_admin(email, name, surname, answers)
        
        return render(request, 'quiz/thank_you.html', {'score': score})

    return render(request, 'quiz/take_test.html', {'test': test, 'questions': questions})

def send_answers_to_admin(email, name, surname, answers):
    subject = 'Ответы пользователя на тест'
    message = f'Имя: {name}\nФамилия: {surname}\nEmail: {email}\n\nОтветы:\n'
    for question_text, answer in answers.items():
        message += f'{question_text}: {answer}\n'

    # Отправка на ваш личный email
    send_mail(subject, message, settings.EMAIL_HOST_USER, ['imp17487@gmail.com'])

def home(request):
    return render(request, 'quiz/take_test.html')  # Убедитесь, что у вас есть шаблон index.html
