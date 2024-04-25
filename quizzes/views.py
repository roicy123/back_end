from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Quiz, Question, Answer
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer

class QuizListCreate(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class AddQuestionAPIView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

class AddAnswerAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Quiz, Question, Answer
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer

class QuizListCreate(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]

    # Override delete method to handle DELETE request
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class QuestionListCreate(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

class AnswerListCreate(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class AnswerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]


class QuizUpdateAPIView(generics.UpdateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]

class QuestionUpdateAPIView(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

class AnswerUpdateAPIView(generics.UpdateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Quiz, Question, Answer
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer

@api_view(['POST'])
def submit_quiz(request, quiz_id):
    serializer = QuizSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    quiz = serializer.save()

    answers = request.data.get('answers')
    if not answers:
        return Response({'error': 'No answers provided'}, status=status.HTTP_400_BAD_REQUEST)

    correct_answers = 0
    incorrect_answers = []
    for answer in answers:
        question_id = answer.get('question')
        if not question_id:
            return Response({'error': 'No question provided'}, status=status.HTTP_400_BAD_REQUEST)

        question = Question.objects.get(id=question_id)
        answer_id = answer.get('answer')
        if not answer_id:
            return Response({'error': 'No answer provided'}, status=status.HTTP_400_BAD_REQUEST)

        answer_obj = Answer.objects.get(id=answer_id)
        if answer_obj.is_correct:
            correct_answers += 1
        else:
            incorrect_answers.append(question.answers.get(is_correct=True).content)

    score = (correct_answers / len(quiz.questions)) * 100
    return Response({
        'score': score,
        'correct_answers': [question.content for question in quiz.questions if question.answers.filter(is_correct=True).first().id == answers[question.id]],
        'incorrect_answers': incorrect_answers,
    })