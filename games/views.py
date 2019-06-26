# from django.http import HttpResponse
# from django.template import loader
# from django.shortcuts import render
#
#
# def index(request):
#     # template = loader.get_template('games/index.html')
#     return render(request, 'games/index.html')
#
# # class IndexView(generic.ListView):
# #     template_name = 'polls/index.html'
# #     context_object_name = 'latest_question_list'

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm, MainForm


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('games/index.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'games/index.html', {'form': form})


def main(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MainForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('games/result')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MainForm()

    return render(request, 'games/main.html', {'form': form})


def result(request):
    return render(request, 'games/result.html')