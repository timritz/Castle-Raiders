from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages


def index(request):
    messages = ''


    if 'players' not in request.session:
        request.session['players'] = {}
        request.session['id'] = 1

        request.session.modified = True

    return render(request, 'login/index.html')


def processIndex(request):

    if(request.method == "POST"):
        print(request.POST);

        if(request.POST['user_type'] == "player"):

            print(request.POST['inputName'])
            newPlayer = request.POST['inputName']
            request.session['players'][newPlayer] = {
                # 'name': request.POST['inputName'],
                'id':  request.session['id'],
                'character': "test"
            }

            request.session['test'] = 'successful'

            request.session.modified = True


        print('index players:', request.session['players'])

    return redirect('/setup/' + request.POST['inputName'])


def setup(request, name):
    print('setup players:', request.session['players'])
    print('test', request.session['test'])

    context = {
        'players': request.session['players'],
        'name': name
    }

    return render(request, 'login/setup.html', context)

def reset(request):
    request.session.clear()
    return redirect('/')

def updateGroup(request, name):

    if(request.method=='POST'):

        print("form", request.POST)
        print('unupdate players: ', request.session['players'])
        print("player", request.session['players'][name])
        print("stat", request.session['players'][name]['character'])

        request.session['players'][name]['character'] = request.POST['characterChoice']

        print("stat", request.session['players'][name]['character'])

        request.session.modified = True


        context = {
            'players': request.session['players']
        }

    return redirect('/setup/' + name)