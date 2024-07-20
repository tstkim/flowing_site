const gameBoard = document.getElementById('gameBoard');
const cells = Array.from(document.querySelectorAll('.cell'));
let currentPlayer = 'x';
let gameActive = true;
const winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
];

function handleCellClick(event) {
    const cell = event.target;
    const cellIndex = cell.dataset.index;

    if (cell.textContent !== '' || !gameActive) {
        return;
    }

    cell.textContent = currentPlayer;
    cell.classList.add(currentPlayer);

    if (checkWin()) {
        alert(`${currentPlayer.toUpperCase()} wins!`);
        gameActive = false;
        return;
    }

    if (cells.every(cell => cell.textContent !== '')) {
        alert('Draw!');
        gameActive = false;
        return;
    }

    currentPlayer = currentPlayer === 'x' ? 'o' : 'x';
}

function checkWin() {
    return winningConditions.some(condition => {
        return condition.every(index => {
            return cells[index].classList.contains(currentPlayer);
        });
    });
}

cells.forEach(cell => cell.addEventListener('click', handleCellClick));
