from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages


def index(request):
    messages = ''


    if 'players' not in request.session:
        request.session['names_list'] = []
        request.session['players'] = {}
        request.session['id'] = 1



    return render(request, 'login/index.html')


def processIndex(request):

    if(request.method == "POST"):
        print(request.POST);

        if(request.POST['user_type'] == "player"):

        #         request.session['names_list'].append({
        #             'name': request.POST['inputName'],
        #             'id': request.session['id'],
        #             'character': "",
        #         })
        #
        #         print('id', request.session['id'])
        #         request.session['id'] += 1;
        #
        #     print('names_list', request.session['names_list'])
        #     print('id', request.session['id'])
        #
        #
        # return redirect('/setup/' + str(request.session['names_list'][len(request.session['names_list'])-1]['name']))

            print(request.POST['inputName'])
            request.session['players'][request.POST['inputName']] = {
                # 'name': request.POST['inputName'],
                'id':  request.session['id'],
                'character': "test"
            }

            request.session['test'] = 'successful'

        print('index players:', request.session['players'])


    return redirect('/setup/' + request.POST['inputName'])


def setup(request, name):
    print('setup players:', request.session['players'])
    print('test', request.session['test'])


    context = {
        'players': request.session['players']

    }

    print('context players: ', context['players'])
    return render(request, 'login/setup.html', context)

def reset(request):
    request.session.clear()
    return redirect('/')