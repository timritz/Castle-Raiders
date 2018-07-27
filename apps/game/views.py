from django.shortcuts import render, HttpResponse, redirect
from .models import *
import Character_Attributes_OOP
import collections
import json

def index(request,name):

    context={
        # 'players': submittedPlayerList,
        'orderedPlayers': request.session['orderedPlayerDict'],
        'name': name,
        'map': request.session['map']
    }

    # print(request.session['orderedPlayerDict'])

    # print(context['map'])
    return render(request, 'game/temp_main.html', context)



def serveCards(request, player):
    player.assignCards()
    return True


def fight(request, attackerName, positionString, cardNum):
    attackingPlayer = request.session['orderedPlayerDict'][attackerName]
    tile = positionString.split('-')
    position = [int(tile[0]), int(tile[1])]

    defenderName = request.session['map'][position[0]][position[1]][1]

    if(defenderName == ""):

        return HttpResponse("No Enemy")

    defendingPlayer = request.session['orderedPlayerDict'][defenderName]

    print(defendingPlayer)

    if defendingPlayer['defense'] >= attackingPlayer['action' + str(cardNum)]:

        return HttpResponse("No Damage")

    else:

        request.session['OrderedPlayerDict'][defenderName]['health'] -= 1

        return HttpResponse(str(attackerName) + "did damage to " + str(defenderName))



    # Will take in the player who is fighting, the character who is being fought
    # Will take in their attack, defense including cards and run the initial numbers
    # Will use those numbers to calculate the results, then update orderedDict and return the result
        return HttpResponse(response)  


def runGame(request):
    request.session['playerCount'] = 0
    for player in request.session['orderedPlayerDict']:
        playerCount += 1
        serveCards(player)
    if(playerCount == 1):
        playerCount == 2
    context={
        # 'players': submittedPlayerList,
        'orderedPlayers': request.session['orderedPlayerDict'],
        'name': str(name),
        'map': request.session['map']
    }
    while(request.session['playerCount'] > 1):
        for player in request.session['orderedPlayerDict']:
            if(playerName == player.name):
                yield render(request, 'game/temp_action_main.html', context)
            else:
                yield render(request, 'game/temp_static_main.html', context)



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
            # '2': [len(map[0]) - 1, 0],
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

        print("incoming Form,", request.POST)

        # print("incoming player", request.POST['playersInfo'])
        # print(type(request.POST['playersInfo']))

        # json.loads(request.POST['playersInfo'])

        # print("incoming player", request.POST['playersInfo'])
        # print(type(request.POST['playersInfo']))


        newMap = request.POST['map'].split(',')

        i = 0
        new_list = []
        while i < len(newMap):
            new_list.append(newMap[i:i + 2])
            i += 2

        i = 0
        updated_map = []
        while i < len(new_list):
            updated_map.append(new_list[i:i + 10])
            i += 10

        request.session['orderedPlayerDict'][name]['position']['x'] = int(request.POST['playersInfoX'])
        request.session['orderedPlayerDict'][name]['position']['y'] = int(request.POST['playersInfoY'])

        print(request.session['orderedPlayerDict'][name]['position'])

        request.session['map'] = updated_map


    return redirect('/game/'+ name)

def processFight(request, name):

    if(request.method=="POST"):

        print(request.POST)
        print(name)


    attackingPlayer = request.session['orderedPlayerDict'][request.POST['attacker']]
    tile = request.POST['spotAttacked'].split('-')
    position = [int(tile[0]), int(tile[1])]

    defenderName = request.session['map'][position[0]][position[1]][1]

    if(defenderName == ""):
        print('no one to attack')
        return redirect('/game/' + name)
    defendingPlayer = request.session['orderedPlayerDict'][defenderName]

    print(defendingPlayer)

    print("defense:", defendingPlayer['cards']['card1'])
    print("attack:", attackingPlayer['cards']['card' + str(request.POST['cardUsed'])])


    if defendingPlayer['cards']['card1'] >= attackingPlayer['cards']['card' + str(request.POST['cardUsed'])]:
        print('defender won')
        return redirect('/game/' + name)
    else:
        print('attacker won')

        print(defenderName)
        print('inital health:', request.session['orderedPlayerDict'][defenderName]['health'])
        request.session['orderedPlayerDict'][defenderName]['health'] -= 1
        print('updated health:', request.session['orderedPlayerDict'][defenderName]['health'])

        request.session.modified = True

        return redirect('/game/' + name)


    # Will take in the player who is fighting, the character who is being fought
    # Will take in their attack, defense including cards and run the initial numbers
    # Will use those numbers to calculate the results, then update orderedDict and return the result
    return redirect('/game/'+name)

def processRest(request, name):

    if(request.method == "POST"):
        print(request.POST)
        request.session['orderedPlayerDict'][request.POST['player']]['health'] += 1

        request.session.modified = True


    return redirect('/game/'+name)