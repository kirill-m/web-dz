from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
import json, datetime
from hello_django.models import Question, Answer, Tags, User
from django.contrib import auth

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
    
    return render(request, 'question.html', context)

def register(request):
	return render(request, 'register.html', ())

def login(request):
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
	else:
		return render(request, 'login.html', {'login_error': True})
	return render(request, 'login.html', ());

def logout(request):
	auth.logout(request)
	return redirect('/')

def ask(request):
        return render(request, 'ask.html', ());

def add(request):
	return HttpResponse(request.POST.get('text'))

def tags(request, tag ):
	tag_get = request.GET.get('tag')
	context = {
	'questions' : Question.objects.popular()[:10],
        'tags': Tags.objects.all(),
	'tag_get' : Tags.objects.get(name=tag_get),
	}
	return render(request, 'tags.html', context)

def user (request, pk):
	try:
        	u = User.objects.get(id=pk)
    	except User.DoesNotExist:
        	raise Http404
    	context = {
             'user' : u,
             'rating': 99,
             'email': u.email,
	     'first_name': u.first_name,
	     'last_name': u.last_name,
	     'questions': u.question_set.all(),
    }
	return render(request, 'user.html', context);


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

