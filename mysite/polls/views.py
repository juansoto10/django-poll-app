from django.shortcuts import get_object_or_404, render
# from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
from django.urls import reverse

from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html') -> Loading template with django.template.loader.get_template()
    context = {'latest_question_list': latest_question_list}
    # output = ', '.join([q.question_text for q in latest_question_list]) -> Hardcoded way to show questions
    # return HttpResponse(template.render(context, request)) -> Another way to render template
    return render(request, 'polls/index.html', context)

# Note that once we’ve done this in all these views, we no longer need to import loader and HttpResponse.
# The render() function takes the request object as its first argument, a template name as its second argument and a
# dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with the
# given context.


def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)

    # First way -->
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist.')
    #
    # return render(request, 'polls/detail.html', {'question': question})

    # Second way: shortcut -->
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

# The get_object_or_404() function takes a Django model as its first argument and an arbitrary number of
# keyword arguments, which it passes to the get() function of the model’s manager. It raises Http404 if the object
# doesn’t exist.

# There’s also a get_list_or_404() function, which works just as get_object_or_404() – except using filter() instead of
# get(). It raises Http404 if the list is empty.


def results(request, question_id):
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after succesfully dealing with POST data.
        # This prevents data from being posted twice if a user hits the back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
