from django.shortcuts import render, HttpResponse, redirect
from .models import *
import Character_Attributes_OOP
import collections
from django.core import serializers
import json

def index(request,name):

    context={
        # 'players': submittedPlayerList,
        'orderedPlayers': request.session['orderedPlayerDict'],
        'name': name,
        'map': request.session['map']
    }
    return render(request, 'game/temp_main.html', context)



def serveCards(request, player):
    player.assignCards()
    return True


def fight(request):
    attackingPlayer = request.session['orderedPlayerDict'][request.POST['attackerName']]
    tile = request.POST['positionString'].split('-')
    position = [int(tile[0]), int(tile[1])]
    defenderName = request.session['map'][position[0]][position[1]][1]
    if(defenderName == ""):
        response = "No Enemy"
        return HttpResponse(response)
    defendingPlayer = request.session['orderedPlayerDict'][defenderName]
    if defendingPlayer['assignedCards']['defense'] >= attackingPlayer['assignedCards']['action' + str(request.POST['cardNum'])]:
        response = "No Damage Dealt"
        return HttpResponse(response)
    else:
        print(request.session['orderedPlayerDict'][defenderName]['health'])
        request.session['orderedPlayerDict'][defenderName]['health'] -= 1
        print(request.session['orderedPlayerDict'][defenderName]['health'])
        request.session.modified = True
        playerDict = collections.OrderedDict(sorted(request.session['orderedPlayerDict'].items(), key=lambda t: t[1]['priority']))
        # orderedPlayerDict = collections.OrderedDict(sorted(request.session['stats'].items(), key=lambda t: t[1]['priority']))
        return HttpResponse(json.dumps(playerDict), content_type = 'application/javascript; charset=utf8')

def game_state(request):
    gameStateDict = {}
    updatedMap = request.session['map']
    playerDict = collections.OrderedDict(sorted(request.session['orderedPlayerDict'].items(), key=lambda t: t[1]['priority']))
    gameStateDict['updatedMap'] = updatedMap
    gameStateDict['updatedPlayerDict'] = playerDict
    gameStateDict['playerTurn'] = request.session['playerTurn']
    # orderedPlayerDict = collections.OrderedDict(sorted(request.session['stats'].items(), key=lambda t: t[1]['priority']))
    return HttpResponse(json.dumps(gameStateDict), content_type = 'application/javascript; charset=utf8')

    # Will take in the player who is fighting, the character who is being fought
    # Will take in their attack, defense including cards and run the initial numbers
    # Will use those numbers to calculate the results, then update orderedDict and return the result


def activePlayer(request):
    while(request.session['playerCount'] > 1):
        for player in request.session['orderedPlayerDict']:
            yield player



def prep_game(request, name):
    if(request.method == "POST"):
        for key, value in request.POST.items():
            if((key != 'csrfmiddlewaretoken') & (key != 'start')):
                newPlayer = Player()
                newPlayer.name = key
                newPlayer.characterType = value
                newPlayer.status = "alive"

                newPlayer.save()


                print('final newPlayer', newPlayer.__dict__)

        playerList = Player.objects.all()

        characterTypeReference = {
            'Knight': Character_Attributes_OOP.Knight(),
            'Mage': Character_Attributes_OOP.Mage(),
            'Rogue': Character_Attributes_OOP.Rogue(),
            'Bard': Character_Attributes_OOP.Bard(),
        }

        request.session.clear()


        submittedPlayerList = []

        request.session['stats'] = {}

        for player in playerList:
            request.session['stats'][str(player.name)] = characterTypeReference[player.characterType].__dict__
            submittedPlayerList.append(player.name)

        for player in submittedPlayerList:
            print('player:', player)
            print('session', request.session['stats'][player])


    map = loadMap('entrance')


    first_time = True

    if(first_time):
        first_time
        positions = {}

        positions = {
            '1': [0, 0],
            '2': [1, 0],
            #'2': [len(map[0]) - 1, 0],
            '3': [0, len(map) - 1],
            '4': [len(map[0]) - 1, len(map) - 1]
        }

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

    return redirect ('/game/'+ name)


def loadMap(area):
    areaMaps = {
        'entrance':
         [
            [[11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""]],
            [[13, ""], [0, ""], [0, ""], [0, ""], [0, ""], [6, ""], [0, ""], [0, ""], [0, ""], [13, ""]],
            [[12, ""], [4, ""], [4, ""], [4, ""], [4, ""], [30, ""], [4, ""], [4, ""], [4, ""], [12, ""]],
            [[11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""]],
            [[10, ""], [10, ""], [10, ""], [10, ""], [11, ""], [11, ""], [10, ""], [10, ""], [10, ""], [10, ""]],
            [[10, ""], [10, ""], [10, ""], [10, ""], [11, ""], [11, ""], [10, ""], [10, ""], [10, ""], [10, ""]],
            [[2, ""], [2, ""], [2, ""], [2, ""], [11, ""], [11, ""], [2, ""], [2, ""], [2, ""], [2, ""]],
            [[1, ""], [1, ""], [1, ""], [1, ""], [11, ""], [11, ""], [1, ""], [1, ""], [1, ""], [1, ""]],
            [[10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""]],
            [[10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""]],
        ],
        'foyer':
         [
            [[10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""]],
            [[13, ""], [0, ""], [0, ""], [0, ""], [0, ""], [0, ""], [0, ""], [0, ""], [0, ""], [0, ""]],
            [[12, ""], [4, ""], [4, ""], [4, ""], [4, ""], [4, ""], [4, ""], [4, ""], [4, ""], [4, ""]],
            [[11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""], [11, ""]],
            [[10, ""], [10, ""], [10, ""], [10, ""], [11, ""], [11, ""], [10, ""], [10, ""], [10, ""], [10, ""]],
            [[10, ""], [10, ""], [10, ""], [10, ""], [11, ""], [11, ""], [10, ""], [10, ""], [10, ""], [10, ""]],
            [[2, ""], [2, ""], [2, ""], [2, ""], [11, ""], [11, ""], [2, ""], [2, ""], [2, ""], [2, ""]],
            [[1, ""], [1, ""], [1, ""], [1, ""], [11, ""], [11, ""], [1, ""], [1, ""], [1, ""], [1, ""]],
            [[10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""]],
            [[10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""], [10, ""]],
        ],
    }
    return areaMaps[area]


def how_to_play(request):
    return render(request, 'game/how_to_play.html')

def character_info(request):
    return render(request, 'game/character_info.html')