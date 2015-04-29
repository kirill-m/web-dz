from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
import json, datetime
from hello_django.models import Question, Answer, Tags


#def index(request):
#	context = {
#		'questions': Question.objects.popular()[:10]
#	}
#	return render(request, 'index2.html', context)	

def question(request, pk):
    try:
	q = Question.objects.get(id=pk)
    except Question.DoesNotExist:
	raise Http404
    context = {
	     'question' : Question.objects.get(id=pk),
	     'answers': Answer.objects.popular()[:10],
	     'tags': Tags.objects.all(),
    }
    
    return render_to_response('question.html', context,
        content_type="text/html")

def register(request):
	return render(request, 'register.html', ())

def login(request):
	return render(request, 'login.html', ());

def ask(request):
        return render(request, 'ask.html', ());

def add(request):
	return HttpResponse(request.POST.get('text'))


def test(request):
	try:
	    page = int(request.GET.get('page', ''))
	except ValueError:
	    page = 1;
	data = {
	     'query': request.GET.get('query'),
	     'page': page,
	}
	return HttpResponse(json.dumps(data), content_type='application/json')

@csrf_exempt
def hello_world(request):
    result = ['<h1> Hello, world! (django) </h1>']
    result.append('Post test:')
    result.append('<form method="post">')
    result.append('<input type="text" name = "test">')
    result.append('<input type="submit" value="Submit">')
    result.append('</form>')
    if request.method == 'GET':
        if request.GET.urlencode() != '':
            result.append('Get data:')
        result.append(request.GET.urlencode())
    if request.method == 'POST':
	result.append('Post data:')
        result.append(request.POST.urlencode())
    return HttpResponse('<br>'.join(result))

def index(request):
    question_list = Question.objects.popular()[:10]
    answers = Answer.objects.count()
    sort = request.GET.get('sort')
    if sort == '1':
    	question_list = Question.objects.popular()[:10]
    elif sort == '2':
	question_list = Question.objects.new()[:10]
    paginator = Paginator(question, 6) # Show 6 contacts per page
    page = request.GET.get('page')
    #try:
    #    questions = paginator.page(page)
    #except PageNotAnInteger:
    #    questions = paginator.page(1)
    #except EmptyPage:
    #    questions = paginator.page(paginator.num_pages)
    context = {
             'questions' : question_list,
             'answers': answers,
             'tags': Tags.objects.all(),
    }
    return render(request, 'index2.html', context)
