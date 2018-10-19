window.addEventListener("keydown", function(e) {
    // space and arrow keys
    if([32, 37, 38, 39, 40].indexOf(e.keyCode) > -1) {
        e.preventDefault();
    }
}, false);

// var map = {{map | safe}}

// var characters = {{orderedPlayers | safe}}
// var totalCharacters = 0;

// var name = "{{name}}"
var myVar = setInterval(loadMap, 3000);

function loadMap() {
    var d = new Date();
    // document.getElementById("demo").innerHTML = d.toLocaleTimeString();
}

console.log(map)

function displayWorld(){
    var output = '';
    var tileDict = {
        0: 'wall',
        1: 'water',
        2: 'grassWater_front',
        3: 'wall',
        4: 'wall_bottom',
        5: 'lamppost',
        10: 'grass',
        11: 'stone_floor',
        12: 'ladder_bottom',
        13: 'ladder',
        14: 'ladder_top',
        30: 'door'
    }
    // console.log("~")
    // console.log("I'm here 1")
    // print("I'm here!!")

    var output = ""
    for(var i=0; i<map.length; i++){
        output = output += "<div class='row'>";
        for(var j=0; j<map[i].length; j++){
            if(map[i][j][1]==""){
                output = output += "<div class='tile' style=\"background-image: url('/static/game/img/" + tileDict[map[i][j][0]] + ".png')\"></div>";
                // console.log('player not found')
            }else{
                output = output += "<div class='playerTile' style=\"background-image:url('/static/game/img/" + characters[map[i][j][1]]['name'] + "-guard-f.png'), url('/static/game/img/" + tileDict[map[i][j][0]] +".png')\"></div>";
            }
        }
        output += "</div>";
    }
    // console.log('output')
    // console.log(output);
    document.getElementById('playerMap').innerHTML = output;
}

displayWorld()

function displayHighlightedWorld(name){
    var centerX = characters[name]['position']['x']
    var centerY = characters[name]['position']['y']

    console.log(centerX)
    console.log(centerY)
    

    var output = '';
    var tileDict = {
        0: 'wall',
        1: 'water',
        2: 'grassWater_front',
        3: 'wall',
        4: 'wall_bottom',
        5: 'lamppost',
        10: 'grass',
        11: 'stone_floor',
        12: 'ladder_bottom',
        13: 'ladder',
        14: 'ladder_top',
        30: 'door'
    }
    // print("I'm here!!")

    var output = ""
    for(var i=0; i<map.length; i++){
        output = output += "<div class='row'>";
        for(var j=0; j<map[i].length; j++){


            if((j-centerX <= 1) & (i-centerY <= 1) & (j-centerX >= -1) & (i-centerY >= -1) &!((j-centerX ==0)& (i-centerY == 0))){
                console.log('highlighted')
                console.log("X diff: ", (j-centerX))
                console.log("Y diff: ", (i-centerY))

                if(map[i][j][1]==""){
                    output = output += "<div class='tile highlighted' data-position='" + i + "-" + j + "' " + "style=\"background-image: url('/static/game/img/" + tileDict[map[i][j][0]] + ".png')\"></div>";
                }else{
                    output = output += "<div class='playerTile highlighted' data-position='" + i + "-" + j + "' " + "style=\"background-image:url('/static/game/img/" + characters[map[i][j][1]]['name'] + "-guard-f.png'), url('/static/game/img/" + tileDict[map[i][j][0]] +".png')\"></div>";
                }
            }else{
                if(map[i][j][1]==""){
                    output = output += "<div class='tile' data-position='" + i + "-" + j + "' " + "style=\"background-image: url('/static/game/img/" + tileDict[map[i][j][0]] + ".png')\"></div>";
                    // console.log('player found')
                }else{
                    output = output += "<div class='playerTile' data-position='" + i + "-" + j + "' " + "style=\"background-image:url('/static/game/img/" + characters[map[i][j][1]]['name'] + "-guard-f.png'), url('/static/game/img/" + tileDict[map[i][j][0]] +".png')\"></div>";
                }
            }
        }
        output += "</div>";
    }
    // console.log('output')
    // console.log(output);
    document.getElementById('playerMap').innerHTML = output;
}

// displayHighlightedWorld()

function movePlayer(currentPlayer){
    var moved = 0

    console.log('current player in movePlayer', currentPlayer)
    player = characters[currentPlayer]
    
    console.log(player)
    console.log('start moving')
    $(document).keydown(function(e) {
        // console.log(player)
        // console.log(map)

        if(moved <player.movementSpeed){
            console.log(moved)
            console.log(player.movementSpeed)
            

            if(e.keyCode == 37) { // LEFT
                // console.log('starting left')
                if(player['position']['x']-1 >=0){
                    if((map[player['position']['y']][player['position']['x']-1][1] == "") & (map[player['position']['y']][player['position']['x']-1][0] > 9)){
                        // console.log(map[player['position']['y']][player['position']['x']])
                        map[player['position']['y']][player['position']['x']][1] = ""
                        player['position']['x'] --;
                        map[player['position']['y']][player['position']['x']][1] = currentPlayer
                        console.log("triggered left")
                        // console.log(player['position']['x'])

                        moved++

                    }
                }

            }
            else if(e.keyCode == 38){ // UP
                if(player['position']['y']-1 >=0){
                    if((map[player['position']['y']-1][player['position']['x']][1] == "")  & (map[player['position']['y']-1][player['position']['x']][0] > 9)){
                        map[player['position']['y']][player['position']['x']][1] = ""
                        player['position']['y'] --;
                        map[player['position']['y']][player['position']['x']][1] = currentPlayer

                        console.log("triggered up")
                        // console.log(player['position']['y'])
                        
                        moved++

                    }
                }

            }
            else if (e.keyCode == 39) { // RIGHT
                if(player['position']['x']+1 <=map[0].length-1){
                    // console.log(map[0].length-1)
                    if((map[player['position']['y']][player['position']['x']+1][1] == "")  & (map[player['position']['y']][player['position']['x']+1][0] > 9)){
                        map[player['position']['y']][player['position']['x']][1] = ""
                        player['position']['x'] ++;
                        map[player['position']['y']][player['position']['x']][1] = currentPlayer	

                        console.log("triggered right")
                        // console.log(player['position']['x'])
                        
                        moved++

                    }
                }

            }
            else if (e.keyCode == 40) { // DOWN
                if(player['position']['y']+1 <= map.length-1){
                    // console.log(map.length-1)

                    if((map[player['position']['y']+1][player['position']['x']][1] == "")  & (map[player['position']['y']+1][player['position']['x']][0] > 9)){
                        map[player['position']['y']][player['position']['x']][1] = ""
                        player['position']['y'] ++;
                        map[player['position']['y']][player['position']['x']][1] = currentPlayer

                        console.log("triggered down")
                        // console.log(player['position']['y'])

                        // console.log("new change")
                        
                        moved++

                    }
                }

            }
        }
        if(moved <player.movementSpeed){
            console.log('performed step')
        } else{
            console.log('performed step')
            console.log('movements completed')
            map = map

            console.log(player['position']['x'])
            console.log(player['position']['y'])
            $('#formMap').attr('value', map)
            $('#formPlayerInfoX').attr('value', player['position']['x'])
            $('#formPlayerInfoY').attr('value', player['position']['y'])

            // $.ajax({
            //     type: "POST",
            //     url: "/game/update/{{name}}",
            //     // data: $('#ajaxForm').serialize(),
            //     data: $('#formMove').serialize(),
            //     success: function(resp){
            //         // console.log(resp)
            //         console.log('successful ajax return')
            //     },
            //     error: function(){
            //         console.log('errors')
            //     }
            // })
        }
        displayWorld()
    });


}




$(document).ready(function(){
    $('button.action1').click(function(){
        console.log('clicked')
        $('#choices1').toggle();
        $('#choices2').hide();
    });

    $('button.action2').click(function(){
        console.log('clicked')
        $('#choices2').toggle();
        $('#choices1').hide();
    });

    $('button.attack1').click(function(){
        console.log('clicked')
        $('button.action1').hide();
        $('#choices1').hide();
        displayHighlightedWorld(name)
        $('div.highlighted').click(function(){
            displayWorld()
            console.log('clicked')
            console.log($(this).attr('data-position'))
            var position = $(this).attr('data-position')
            // name = name
            var card = "2"

            $('#formAttacker').attr('value', name)
            $('#formSpotAttacked').attr('value', position)
            $('#formCardUsed').attr('value', card)

        });
    });

    $('button.move1').click(function(){
        console.log('clicked')
        $('button.action1').hide();
        $('#choices1').hide();
        console.log('name before movePlayer', name)
        movePlayer(name)
        // $('#formMap').attr('value', map)
        console.log(map)
        
       
        // $.ajax({
        //     type: "POST",
        //     url: "/game/update/ajaxTest/1",
        //     // data: $('#ajaxForm').serialize(),
        //     data: $('#formMove').serialize(),
        //     success: function(resp){
        //         console.log(resp)
        //         console.log('successful ajax return')
        //     },
        //     error: function(){
        //         console.log('errors')
        //     }
        // })


        // $.post(url('/game/processMove'),{'map': map}, )

    });

    $('button.rest1').click(function(){
        console.log('clicked')
        $('button.action1').hide();
        $('#choices1').hide();

        $('#formPlayer').attr('value', name)

    });

    $('button.attack2').click(function(){
        console.log('clicked')
        $('button.action2').hide();
        $('#choices2').hide();
        displayHighlightedWorld(name)
        $('div.highlighted').click(function(){
            displayWorld()
            console.log('clicked')
            console.log($(this).attr('data-position'))
            var position = $(this).attr('data-position')
            // name = name
            var card = "3"

            $('#formAttacker').attr('value', name)
            $('#formSpotAttacked').attr('value', position)
            $('#formCardUsed').attr('value', card)

            // <input id ="formAttacker" type='hidden' name='attacker' value="">
            // <input id ="formSpotAttacked" type='hidden' name='spotAttacked' value="">
            // <input id ="formCardUsed" type='hidden' name='cardUsed' value="">
        });
    });

    $('button.move2').click(function(){
        console.log('clicked')
        $('button.action2').hide();
        $('#choices2').hide();
        movePlayer(name)
    });

    $('button.rest2').click(function(){
        console.log('clicked')
        $('button.action2').hide();
        $('#choices2').hide();

        $('#formPlayer').attr('value', name)

    });

    $('#ajaxForm').click(function(){
        console.log('clicked')
        console.log($(this).serialize())
        $.ajax({
            type: "POST",
            url: "/game/update/ajaxTest/1",
            data: $(this).serialize(),
            success: function(resp){
                console.log(resp)
                console.log('successful ajax return')
            },
            error: function(){
                console.log('errors')
            }
            

        })

    });

});


function gameLoop(){
    console.log("gameLoop is running!");
    displayWorld();





    setTimeout(gameLoop, 2000)
}

// gameLoop();