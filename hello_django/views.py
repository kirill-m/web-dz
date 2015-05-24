from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
import json, datetime
from hello_django.models import Question, Answer, Tags, User, Profile, QLike, ALike
from django.contrib import auth

def question(request, pk):
    try:
	q = Question.objects.get(id=pk)
    except Question.DoesNotExist:
	raise Http404
    id = request.GET.get('id')
    vote = request.GET.get('vote')
    user = request.GET.get('user')
    if vote == 'up1':
        q = Question.objects.get(id=id)
        u = User.objects.get(id=user)
        try:
                QLike.objects.get(question_id=q.id, user_id=u.id)
        except QLike.DoesNotExist:
                ql = QLike(question_id=q.id, user_id=u.id, voted=1)
                ql.save()
                q.rating = q.rating + 1
                q.save()
        else:
                ql = QLike.objects.get(question_id=q.id, user_id=u.id)
                if ql.voted == 0:
                        q.rating = q.rating + 1
                        q.save()
                        ql.voted = None
                        ql.save()
                elif ql.voted == None:
                        q.rating = q.rating + 1
                        q.save()
                        ql.voted = 1
                        ql.save()
    elif vote == 'down1':
        q = Question.objects.get(id=id)
        u = User.objects.get(id=user)
        try:
                QLike.objects.get(question_id=q.id, user_id=u.id)
        except QLike.DoesNotExist:
                ql = QLike(question_id=q.id, user_id=u.id, voted=0)
                ql.save()
                q.rating = q.rating-1
                q.save()
        else:
                ql = QLike.objects.get(question_id=q.id, user_id=u.id)
                if ql.voted == 1:
                        q.rating = q.rating - 1
                        q.save()
                        ql.voted = None
                        ql.save()
                elif ql.voted == None:
                        q.rating = q.rating - 1
                        q.save()
                        ql.voted = 0
                        ql.save()
    if vote == 'up2':
        a = Answer.objects.get(id=id)
        u = User.objects.get(id=user)
        try:
                ALike.objects.get(answer_id=a.id, user_id=u.id)
        except ALike.DoesNotExist:
                al = ALike(answer_id=a.id, user_id=u.id, voted=1)
                al.save()
                a.rating = a.rating + 1
                a.save()
        else:
                al = ALike.objects.get(answer_id=a.id, user_id=u.id)
                if al.voted == 0:
                        a.rating = a.rating + 1
                        a.save()
                        al.voted = None
                        al.save()
                elif al.voted == None:
                        a.rating = a.rating + 1
                        a.save()
                        al.voted = 1
                        al.save()
    elif vote == 'down2':
        a = Answer.objects.get(id=id)
        u = User.objects.get(id=user)
        try:
                ALike.objects.get(answer_id=a.id, user_id=u.id)
        except ALike.DoesNotExist:
                al = ALike(answer_id=a.id, user_id=u.id, voted=0)
                al.save()
                a.rating = a.rating-1
                a.save()
        else:
                al = ALike.objects.get(answer_id=a.id, user_id=u.id)
                if al.voted == 1:
                        a.rating = a.rating - 1
                        a.save()
                        al.voted = None
                        al.save()
                elif al.voted == None:
                        a.rating = a.rating - 1
                        a.save()
                        al.voted = 0
                        al.save()	
    context = {
	     'question' : Question.objects.get(id=pk),
	     'answers': Answer.objects.popular()[:10],
	     'tags': Tags.objects.all(),
	     'pk': pk,
    }
    
    return render(request, 'question.html', context)

def register(request):
	return render(request, 'register.html', ())

def voted(request, tag):
	rate = request.GET.get('tag')
	if rate == 'up':
		return redirect('/ask')
	elif rate == 'down':
		return redirect('/login')

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
             'usr' : u,
             'rating': u.profile.rating,
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
    id = request.GET.get('id') 
    vote = request.GET.get('vote')
    user = request.GET.get('user')
    if vote == 'up':
	q = Question.objects.get(id=id)
	u = User.objects.get(id=user)
	try:
		QLike.objects.get(question_id=q.id, user_id=u.id)
	except QLike.DoesNotExist:
		ql = QLike(question_id=q.id, user_id=u.id, voted=1)
		ql.save()
		q.rating = q.rating + 1
		q.save()
	else:
		ql = QLike.objects.get(question_id=q.id, user_id=u.id)
		if ql.voted == 0:
			q.rating = q.rating + 1
			q.save()
			ql.voted = None
			ql.save()
		elif ql.voted == None:
			q.rating = q.rating + 1
                        q.save()
                        ql.voted = 1
                        ql.save()
    elif vote == 'down':
	q = Question.objects.get(id=id)
	u = User.objects.get(id=user)
	try:
		QLike.objects.get(question_id=q.id, user_id=u.id)
	except QLike.DoesNotExist:
		ql = QLike(question_id=q.id, user_id=u.id, voted=0)
                ql.save()
		q.rating = q.rating-1
		q.save()
	else:
		ql = QLike.objects.get(question_id=q.id, user_id=u.id)
                if ql.voted == 1:
                        q.rating = q.rating - 1
                        q.save()
			ql.voted = None
    			ql.save()
		elif ql.voted == None:
			q.rating = q.rating - 1
                        q.save()
                        ql.voted = 0
                        ql.save()
    paginator = Paginator(question_list, 4) # Show 4 contacts per page
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    context = {
             #'questions' : question_list,
             'answers': answers,
             'tags': Tags.objects.all(),
	     'likes': QLike.objects.all(),
	     'questions': questions,
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

