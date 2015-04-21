from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json, datetime

questions = [
	{'id': 1, 'title': 'How to build a lunapark?', 'content': u'Read here',
	'tags': ['moon','howto'], 'created': datetime.datetime.now()},
	{'id': 2, 'title': 'How to build a lunapark?', 'content': u'Read here', 
        'tags': ['moon','howto','lunapark'], 'created': datetime.datetime.now()},
	{'id': 3, 'title': 'how to build a lunapark?', 'content': u'Read here', 
        'tags': ['moon','howto','lunapark'], 'created': datetime.datetime.now()},
	{'id': 4, 'title': 'how to build a lunapark?', 'content': u'Read here', 
        'tags': ['moon','howto','lunapark'], 'created': datetime.datetime.now()},
	{'id': 5, 'title': 'how to build a lunapark?', 'content': u'Read here',
        'tags': ['moon','howto','lunapark'], 'created': datetime.datetime.now()},
]

def index(request):
	context = {
		'questions':questions
	}
	return render(request, 'index2.html', context)	

#def question(request, pk):
#	data = {
#	    'pk': int(pk)
#	}
#	return HttpResponse(json.dumps(data), content_type='application/json')

def question(request, pk):
    # View code here...
    return render_to_response('question.html',
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

