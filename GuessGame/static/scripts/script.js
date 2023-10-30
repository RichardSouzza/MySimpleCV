import confetti from 'https://cdn.skypack.dev/canvas-confetti';


const question = document.getElementById('question');
const input = document.getElementById('input');
const tip = document.getElementById('tip');
const replay = document.getElementById('replay');
let targetNumber = generateRandomNumber();


input.addEventListener('keyup', (event) => {
    if (event.key === 'Enter') {
        resetReplayState();
        verifyGuess(input.value);
    }
});


function verifyGuess(guess) {
    if (guess == targetNumber) {
        win();
    }
    else if (guess < targetNumber && guess >= targetNumber - 10) {
        changeTip('O número que estou pensando é um pouco maior.');
    }
    else if (guess < targetNumber) {
        changeTip('O número que estou pensando é maior.');
    }
    else if (guess > targetNumber && guess <= targetNumber + 10) {
        changeTip('O número que estou pensando é um pouco menor.');
    }
    else if (guess > targetNumber) {
        changeTip('O número que estou pensando é menor.');
    }
}


function win() {
    changeTip('');
    replay.innerText = 'Vamos jogar de novo?';
    question.innerText = 'Você acertou! 😃';
    confetti({
        particleCount: 120,
        decay: 0.905,
        origin: {x: 0.1, y: 1}
    });
    confetti({
        particleCount: 120,
        decay: 0.905,
        origin: {x: 0.9, y: 1}
    });
}


function changeTip(text) {
    tip.innerText = text;
}


function resetReplayState() {
    replay.innerText = '';
}


function generateRandomNumber() {
    const randomNumber = Math.floor(Math.random() * 100) + 1;
    return randomNumber;
}
