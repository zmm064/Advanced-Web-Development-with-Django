from django.views import generic
from django.shortcuts import redirect
from django.views.generic.base import TemplateResponseMixin

from .models import Question
from .models import Choice
from .mixins import RequireLoginMixin


"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
"""


class IndexView(RequireLoginMixin, generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

"""
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
"""


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class DeleteView(generic.DeleteView):
    model = Question
    success_url = "/polls/"


class VoteView(generic.View):

    def get_queryset(self, question_id, choice_id):
        return Choice.objects.get(pk=choice_id)

    def post(self, request, pk):
        question_id = pk
        choice_id = request.POST.get('choice', None)
        try:
            queryset = self.get_queryset(question_id, choice_id)
        except (KeyError, Choice.DoesNotExist):
            return redirect('polls:detail', pk=question_id)
        else:
            queryset.votes += 1
            queryset.save()
            return redirect('polls:results', pk=question_id)


class ResultsView(TemplateResponseMixin, generic.View):
    template_name = 'polls/results.html'

    def get_queryset(self, question_id):
        return Question.objects.get(pk=question_id)

    def get(self, request, pk):
        queryset = self.get_queryset(pk)
        context = {'question': queryset}
        return self.render_to_response(context)
