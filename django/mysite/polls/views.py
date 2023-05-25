from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from .models import Question

# html 태그 직접 적용하기
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.question_text for q in latest_question_list])
#     output = "<h1>" + output + "</h1>" # html tag 적용 가능 (하지만 일일이 적용하는 것은 어려움)
#     return HttpResponse(output)

# 템플릿 사용하기
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

# Leave the rest of the views (detail, results, vote) unchanged
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

# 404 에러 출력하기
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Holy shit! Question does not exist")
#     return render(request, "polls/detail.html", {"question": question})

# 한 번에 404 출력하기
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)