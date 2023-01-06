var words = []
const QR = document.getElementById('reader');
const GAME = document.getElementById('game');
const GAMEBOARD = document.getElementById('gameboard');
const WORDSEL = GAMEBOARD.getElementsByTagName('td');
const html5QrCode = new Html5Qrcode("reader");
const config = { fps: 10, qrbox: { width: 250, height: 250 } };

const qrCodeSuccessCallback = (word, decodedResult) => {
    if( words.some( obj => { return obj.word == word } ) ) return
    words.push({'word':word, 'team':0})
    console.log(words.length, word, words);
    WORDSEL[words.length-1].innerText = word

    if (words.length == 25) start_round()
}

function new_round(){
    words = []
    QR.classList.remove('hide');
    html5QrCode.start({ facingMode: "environment" }, config, qrCodeSuccessCallback);
    for(let i = 0; i < WORDSEL.length; i++){
        WORDSEL[i].innerText = '';
        WORDSEL[i].classList.remove('word-team-1')
        WORDSEL[i].classList.remove('word-team-2')
        WORDSEL[i].classList.remove('word-team--1')
        WORDSEL[i].classList.remove('selected')
        
    }
}

function start_round(){
    html5QrCode.stop()
    QR.classList.add('hide');
    GAME.classList.remove('hide');
    console.log(words)
    select_words_for_team(8, 1)
    select_words_for_team(8, 2)
    select_words_for_team(1, -1)
    return
}

function select_words_for_team(n, team){
    let count = 0;
    while (count < n){
        let i = Math.floor(Math.random() * 24)
        if (words[i]['team'] === 0){
            words[i]['team'] = team
            WORDSEL[i].classList.add('word-team-'+team)
            count += 1
        } 
    }
    return words
}

document.getElementById('new-round-btn').onclick = function(){ new_round(); }

for( let i = 0; i < WORDSEL.length; i++){
    WORDSEL[i].addEventListener('click', function(){
        if( this.classList.contains('selected')) this.classList.remove('selected');
        else this.classList.add('selected');
    })
}

new_round();