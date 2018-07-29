from django.shortcuts import render, HttpResponse, redirect
from .models import *
import Character_Attributes_OOP
import collections
from django.core import serializers
import json

def index(request,name):
    request.session['activePlayer'] = str(next(activePlayerGen))
    context={
        # 'players': submittedPlayerList,
        'orderedPlayers': request.session['orderedPlayerDict'],
        'name': name,
        'map': request.session['map'],
        'activePlayer': request.session['activePlayer']
    }
    print(request.session['map'])
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
        worldStateDict = {}
        worldStateDict['playerDict'] = playerDict
        worldStateDict['mapArray'] = request.session['map']
        # orderedPlayerDict = collections.OrderedDict(sorted(request.session['stats'].items(), key=lambda t: t[1]['priority']))
        return HttpResponse(json.dumps(worldStateDict), content_type = 'application/javascript; charset=utf8')

def game_state(request):
    gameStateDict = {}
    updatedMap = request.session['map']
    playerDict = collections.OrderedDict(sorted(request.session['orderedPlayerDict'].items(), key=lambda t: t[1]['priority']))
    gameStateDict['updatedMap'] = updatedMap
    gameStateDict['updatedPlayerDict'] = playerDict
    gameStateDict['activePlayer'] = request.session['activePlayer']
    # orderedPlayerDict = collections.OrderedDict(sorted(request.session['stats'].items(), key=lambda t: t[1]['priority']))
    return HttpResponse(json.dumps(gameStateDict), content_type = 'application/javascript; charset=utf8')

def activePlayer(request):
    while(True):
        for player in request.session['orderedPlayerDict']:
            print(player)
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

        playerList = Player.objects.all()
        characterTypeReference = {
            'Knight': Character_Attributes_OOP.Knight(),
            'Mage': Character_Attributes_OOP.Mage(),
            'Rogue': Character_Attributes_OOP.Rogue(),
            'Bard': Character_Attributes_OOP.Bard(),
        }

        request.session.clear()

        # submittedPlayerList = []
        request.session['stats'] = {}

        for player in playerList:
            request.session['stats'][str(player.name)] = characterTypeReference[player.characterType].__dict__
            print(request.session['stats'][str(player.name)])
            # submittedPlayerList.append(player.name)

    map = loadMap('entrance')
    request.session['won'] = False
    first_time = True

    if(first_time):
        first_time
        positions = {}

        positions = {
            '1': [0, 0],
            '2': [1, 0],
            # '2': [len(map[0]) - 1, 0],
            '3': [0, len(map) - 1],
            '4': [len(map[0]) - 1, len(map) - 1]
        }

        counter = 1
        for player, value in request.session['stats'].items():
            value['position']['x'] = positions[str(counter)][0]
            value['position']['y'] = positions[str(counter)][1]

            map[value['position']['y']][value['position']['x']][1] = player
            counter += 1

        print(request.session['stats'].items())
        orderedPlayerDict = collections.OrderedDict(sorted(request.session['stats'].items(), key=lambda t: t[1]['priority']))
    request.session['orderedPlayerDict'] = orderedPlayerDict
    global activePlayerGen
    activePlayerGen = activePlayer(request)
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

def processMove(request, name):
    if(request.method=="POST"):
        newMap = json.loads(request.POST['formMap'])
        request.session['orderedPlayerDict'][name]['position']['x'] = int(request.POST['formPlayerInfoX'])
        request.session['orderedPlayerDict'][name]['position']['y'] = int(request.POST['formPlayerInfoY'])
        request.session['map'] = newMap
        response = 'Niceeee'
        return HttpResponse(response)


def processRest(request, name):

    if(request.method == "POST"):
        print(request.POST)
        request.session['orderedPlayerDict'][name]['health'] += 1
        request.session.modified = True
        return HttpResponse(json.dumps(request.session['orderedPlayerDict']), content_type = 'application/javascript; charset=utf8')

def end_turn(request):
    if(request.method == "POST"):
        print("I'm here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        request.session['activePlayer'] = str(next(activePlayerGen))
        print(request.session['activePlayer'])
        response = 'Turn Ended'
        return HttpResponse(response)
    
