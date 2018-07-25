from django.shortcuts import render, HttpResponse, redirect
from .models import *
import Character_Attributes_OOP
import collections

def index(request,name):

    context={
        # 'players': submittedPlayerList,
        'orderedPlayers': request.session['orderedPlayerDict'],
        'name': name,
        'map': request.session['map']
    }


    print(context['map'])
    return render(request, 'game/temp_main.html', context)

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
<<<<<<< HEAD
            print('session', request.session['stats'][player])

        # map = [
        #     [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        #     [[0, 0], [2, 0], [1, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0]],
        #     [[0, 0], [2, 0], [1, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0]],
        #     [[0, 0], [2, 0], [1, 0], [1, 0], [1, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0]],
        #     [[0, 0], [2, 0], [1, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0]],
        #     [[0, 0], [2, 0], [1, 0], [0, 0], [1, 0], [0, 0], [1, 0], [1, 0], [1, 0], [0, 0]],
        #     [[0, 0], [2, 0], [1, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]],
        #     [[0, 0], [2, 0], [1, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]],
        #     [[0, 0], [2, 0], [1, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]],
        #     [[0, 0], [2, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]],
        # ]

        # map = [
        #     [[0, ""], [0, ""], [0, ""], [0, ""], [0, ""], [0, ""], [0, ""], [0, ""], [0, ""], [0, ""]],
        #     [[0, ""], [2, ""], [1, ""], [0, ""], [1, ""], [0, ""], [0, ""], [0, ""], [1, ""], [0, ""]],
        #     [[0, ""], [2, ""], [1, ""], [0, ""], [1, ""], [0, ""], [0, ""], [0, ""], [1, ""], [0, ""]],
        #     [[0, ""], [2, ""], [1, ""], [1, ""], [1, ""], [0, ""], [0, ""], [0, ""], [1, ""], [0, ""]],
        #     [[0, ""], [2, ""], [1, ""], [0, ""], [1, ""], [0, ""], [0, ""], [0, ""], [1, ""], [0, ""]],
        #     [[0, ""], [2, ""], [1, ""], [0, ""], [1, ""], [0, ""], [1, ""], [1, ""], [1, ""], [0, ""]],
        #     [[0, ""], [2, ""], [1, ""], [0, ""], [0, ""], [0, ""], [1, ""], [0, ""], [0, ""], [0, ""]],
        #     [[0, ""], [2, ""], [1, ""], [0, ""], [0, ""], [0, ""], [1, ""], [0, ""], [0, ""], [0, ""]],
        #     [[0, ""], [2, ""], [1, ""], [0, ""], [0, ""], [0, ""], [1, ""], [0, ""], [0, ""], [0, ""]],
        #     [[0, ""], [2, ""], [0, ""], [0, ""], [0, ""], [0, ""], [1, ""], [0, ""], [0, ""], [0, ""]],
        # ]

        map = [
            [[11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""]],
            [[13, ""], [0, ""], [0, ""], [0, ""], [0, ""], [0, ""], [0, ""], [0, ""], [0, ""], [0, ""]],
            [[12, ""], [4, ""], [4, ""], [4, ""], [4, ""], [4, ""], [4, ""], [4, ""], [4, ""], [4, ""]],
            [[11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""]],
            [[10, ""], [10, ""], [10, ""], [10, ""], [11, ""], [11, ""], [10, ""], [10, ""], [10, ""], [10, ""]],
            [[10, ""], [10, ""], [10, ""], [10, ""], [11, ""], [11, ""], [10, ""], [10, ""], [10, ""], [10, ""]],
            [[2, ""], [2, ""], [2, ""], [2, ""], [11, ""], [11, ""], [2, ""], [2, ""], [2, ""], [2, ""]],
            [[1, ""], [1, ""], [1, ""], [1, ""], [11, ""], [11, ""], [1, ""], [1, ""], [1, ""], [1, ""]],
            [[10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""]],
            [[10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""]],
        ]

        # needs to be from session
        first_time = True

        if (first_time):
            first_time
            positions = {}

            positions = {
                '1': [0, 0],
                '2': [len(map[0]) - 1, 0],
                '3': [0, len(map) - 1],
                '4': [len(map[0]) - 1, len(map) - 1]
            }
=======
print('session', request.session['stats'][player])


    map = [
        [[11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""]],
        [[13, ""], [0, ""], [0, ""], [0, ""], [0, ""], [0, ""], [0, ""], [0, ""], [0, ""], [0, ""]],
        [[12, ""], [4, ""], [4, ""], [4, ""], [4, ""], [4, ""], [4, ""], [4, ""], [4, ""], [4, ""]],
        [[11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""]],
        [[10, ""], [10, ""], [10, ""], [10, ""], [11, ""], [11, ""], [10, ""], [10, ""], [10, ""], [10, ""]],
        [[10, ""], [10, ""], [10, ""], [10, ""], [11, ""], [11, ""], [10, ""], [10, ""], [10, ""], [10, ""]],
        [[2, ""], [2, ""], [2, ""], [2, ""], [11, ""], [11, ""], [2, ""], [2, ""], [2, ""], [2, ""]],
        [[1, ""], [1, ""], [1, ""], [1, ""], [11, ""], [11, ""], [1, ""], [1, ""], [1, ""], [1, ""]],
        [[10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""]],
        [[10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""]],
    ]


first_time = True

    if (first_time):
        first_time
        positions = {}

        positions = {
            '1': [0, 0],
            '2': [len(map[0]) - 1, 0],
            '3': [0, len(map) - 1],
            '4': [len(map[0]) - 1, len(map) - 1]
        }
>>>>>>> 6d6cc53aef0bd6d1617751fbf5c21bac1bdb05cd

        print('all positions', positions)
        counter = 1
        for player, value in request.session['stats'].items():
            print('position', positions[str(counter)])
            print(player, value)

            value['position']['x'] = positions[str(counter)][0]
            value['position']['y'] = positions[str(counter)][1]

            map[value['position']['y']][value['position']['x']][1] = player

            print(counter, value['position'])
            counter += 1

        print(request.session['stats'].items())
        orderedPlayerDict = collections.OrderedDict(sorted(request.session['stats'].items(), key=lambda t: t[1]['priority']))

        # for player, value in request.session['stats'].items():
        #     print(player)
        #     print(value)
        #
        #     orderedPlayerDict[player] = value

        for player in orderedPlayerDict:
            print(player, orderedPlayerDict[player]['name'])


    request.session['map'] = map
    request.session['orderedPlayerDict'] = orderedPlayerDict
    request.session['map'] = map
    request.session['map'] = map







return redirect ('/game/'+ name)
