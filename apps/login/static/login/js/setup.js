$(document).ready(function(){
    $('label.form-check-label.knightRadio').hover(function(){
        console.log('hovered')
        $('img.knightPic').addClass('bordered');
        },function(){
            $('img.knightPic').removeClass('bordered');
        }
    );

    $('label.form-check-label.mageRadio').hover(function(){
        console.log('hovered')
        $('img.magePic').addClass('bordered');
        },function(){
            $('img.magePic').removeClass('bordered');
        }
    );

    $('label.form-check-label.rogueRadio').hover(function(){
        console.log('hovered')
        $('img.roguePic').addClass('bordered');
        },function(){
            $('img.roguePic').removeClass('bordered');
        }
    );

    $('label.form-check-label.bardRadio').hover(function(){
        console.log('hovered')
        $('img.bardPic').addClass('bordered');
        },function(){
            $('img.bardPic').removeClass('bordered');
        }
    );


    $('label.form-check-label.knightRadio').click(function(){
        console.log('clicked')
        $('img').removeClass('selected')
        $('img.knightPic').addClass('selected')
        $('#{{name}}Character').attr('value', 'Knight')

    });

    $('label.form-check-label.mageRadio').click(function(){
        console.log('clicked')
        $('img').removeClass('selected')
        $('img.magePic').addClass('selected')
        $('#{{name}}Character').attr('value', 'Mage')
    });

    $('label.form-check-label.rogueRadio').click(function(){
        console.log('clicked')
        $('img').removeClass('selected')
        $('img.roguePic').addClass('selected')
        $('#{{name}}Character').attr('value', 'Rogue')
    });

    $('label.form-check-label.bardRadio').click(function(){
        console.log('clicked')
        $('img').removeClass('selected')
        $('img.bardPic').addClass('selected')
        $('#{{name}}Character').attr('value', 'Bard')
    });
});