from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'game/mainBoard.html')

def changeMap(request, newMapName):
    newMap = Map.objects.get(name=newMapName).first()
    return render(request, 'mapScreen.html', { 'loadMap':newMap })

def updatePosition(request):
    response = 'Will send position updates of characters to player screen'
    ## Takes in - 
    ## Outputs -
    return HttpResponse(response)

def updatePosition(request):
    response = 'Will send position updates of characters to player screen'
    ## Takes in -
    ## Outputs -
    return HttpResponse(response)