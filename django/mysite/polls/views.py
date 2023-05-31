from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import Http404, HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import Question, Choice

# html 태그 직접 적용하기
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.question_text for q in latest_question_list])
#     output = "<h1>" + output + "</h1>" # html tag 적용 가능 (하지만 일일이 적용하는 것은 어려움)
#     return HttpResponse(output)

# 템플릿 사용하기
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

# generic view 사용하기
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


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
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})

# generic view 사용하기
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})

# generic view 사용하기
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,))) # reverse()는 http 링크를 생성해줌.