from django.urls import path
from .views import AnswerUpdateAPIView, QuestionUpdateAPIView, QuizListCreate, AddQuestionAPIView, AddAnswerAPIView, QuizUpdateAPIView
from .views import (
    QuizRetrieveUpdateDestroy,
    QuestionListCreate, QuestionRetrieveUpdateDestroy,
    AnswerListCreate, AnswerRetrieveUpdateDestroy,
    submit_quiz,
)

urlpatterns = [
    path('quizzes/', QuizListCreate.as_view(), name='quiz-list-create'),
    path('add_question/', AddQuestionAPIView.as_view(), name='add-question-api'),
    path('add_answer/', AddAnswerAPIView.as_view(), name='add-answer-api'),
    path('quizzes/<int:pk>/', QuizRetrieveUpdateDestroy.as_view(), name='quiz-retrieve-update-destroy'),
    path('quizzes/<int:pk>/edit/', QuizUpdateAPIView.as_view(), name='quiz_update'),

    path('questions/', QuestionListCreate.as_view(), name='question-list-create'),
    path('questions/<int:pk>/', QuestionRetrieveUpdateDestroy.as_view(), name='question-retrieve-update-destroy'),
    path('questions/<int:pk>/edit/', QuestionUpdateAPIView.as_view(), name='question_update'),
    path('answers/', AnswerListCreate.as_view(), name='answer-list-create'),
    path('answers/<int:pk>/', AnswerRetrieveUpdateDestroy.as_view(), name='answer-retrieve-update-destroy'),
    path('answers/<int:pk>/edit/', AnswerUpdateAPIView.as_view(), name='answer_update'),
    path('quizzes/<int:quiz_id>/submit/', submit_quiz, name='submit-quiz'),
]
