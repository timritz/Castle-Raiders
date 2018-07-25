from django.shortcuts import render, HttpResponse, redirect
from .models import *
import Character_Attributes_OOP

def index(request,name):

    # print()
    playerList = Player.objects.all()
    # print('playerList', playerList)
    # print()

    characterTypeReference = {
        'Knight': Character_Attributes_OOP.Knight(),
        'Mage': Character_Attributes_OOP.Mage(),
        'Rogue': Character_Attributes_OOP.Rogue(),
        'Bard': Character_Attributes_OOP.Bard(),
    }



    request.session.clear()

    print()
    print('session', request.session.values())
    print()

    submittedPlayerList = []

    request.session['stats'] = {}

    for player in playerList:
        # print(player.characterType)
        # print(characterTypeReference[player.characterType].__dict__)
        request.session['stats'][str(player.name)] = characterTypeReference[player.characterType].__dict__

        print()
        print("Player name:", player.name)
        print('Session of player:', request.session['stats'][player.name])
        print()

        submittedPlayerList.append(player.name)

    print()
    print('players', submittedPlayerList)
    print('session', request.session['stats'])
    print()

    for player in submittedPlayerList:
        print('player:', player)
        print('session', request.session['stats'][player])



    map = [
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [2, 0], [1, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0]],
        [[0, 0], [2, 0], [1, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0]],
        [[0, 0], [2, 0], [1, 0], [1, 0], [1, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0]],
        [[0, 0], [2, 0], [1, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0]],
        [[0, 0], [2, 0], [1, 0], [0, 0], [1, 0], [0, 0], [1, 0], [1, 0], [1, 0], [0, 0]],
        [[0, 0], [2, 0], [1, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [2, 0], [1, 0], [0, 1], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [2, 0], [1, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [2, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]],
    ]



    # needs to be from session
    first_time = True

    if(first_time):
        first_time
        positions = {}

        positions = {
            '1': [0,0],
            '2': [len(map[0])-1, 0],
            '3': [0,len(map)-1],
            '4': [len(map[0])-1,len(map)-1]
        }

        print('all positions', positions)
        counter = 1
        for player, value in request.session['stats'].items():

            print('position', positions[str(counter)])
            print(player, value)

            value['position']['x'] = positions[str(counter)][0]
            value['position']['y'] = positions[str(counter)][1]

            map[value['position']['y']][value['position']['x']][1] = 1

            print(counter, value['position'])
            counter += 1


        playerOrder = []


        for player, value in request.session['stats'].items():



            value['position']['x'] = positions[str(counter)][0]
            value['position']['y'] = positions[str(counter)][1]

            map[value['position']['y']][value['position']['x']][1] = 1

            print(counter, value['position'])
            counter += 1








    context={
        'players': submittedPlayerList,
        'name': name,
        'map': map

    }








    print()
    print("going to game")
    print()

    return render(request, 'game/mainBoard.html', context)

def prep_game(request, name):
    if(request.method == "POST"):
        print(request.POST)

        for key, value in request.POST.items():
            # print(key)
            # print(value)
            if((key != 'csrfmiddlewaretoken') & (key != 'start')):
                newPlayer = Player()
                newPlayer.name = key
                newPlayer.characterType = value
                newPlayer.status = "alive"

                newPlayer.save()


                print('final newPlayer', newPlayer.__dict__)






    return redirect ('/game/'+ name)
