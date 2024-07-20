let startTime;
let updatedTime;
let difference;
let tInterval;
let running = false;

const startButton = document.getElementById('startButton');
const stopButton = document.getElementById('stopButton');
const resetButton = document.getElementById('resetButton');
const timeDisplay = document.getElementById('timeDisplay');

startButton.addEventListener('click', startTimer);
stopButton.addEventListener('click', stopTimer);
resetButton.addEventListener('click', resetTimer);

function startTimer() {
    if (!running) {
        startTime = new Date().getTime() - (difference || 0);
        tInterval = setInterval(getShowTime, 1);
        running = true;
        startButton.textContent = 'Pause';
    } else {
        clearInterval(tInterval);
        running = false;
        startButton.textContent = 'Start';
    }
}

function stopTimer() {
    clearInterval(tInterval);
    running = false;
    startButton.textContent = 'Start';
}

function resetTimer() {
    clearInterval(tInterval);
    running = false;
    difference = 0;
    startButton.textContent = 'Start';
    timeDisplay.textContent = '00:00:00';
}

function getShowTime() {
    updatedTime = new Date().getTime();
    difference = updatedTime - startTime;

    let hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    let minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
    let seconds = Math.floor((difference % (1000 * 60)) / 1000);

    hours = (hours < 10) ? "0" + hours : hours;
    minutes = (minutes < 10) ? "0" + minutes : minutes;
    seconds = (seconds < 10) ? "0" + seconds : seconds;

    timeDisplay.textContent = hours + ':' + minutes + ':' + seconds;
}
