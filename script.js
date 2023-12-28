document.addEventListener('DOMContentLoaded', () => {
    const gameBoard = document.getElementById('game-board');
    let cardValues = [];
    let cardElements = [];
    let matchesFound = 0;

    function checkForMatch() {
        if (cardElements[0].textContent === cardElements[1].textContent) {
            cardElements.forEach(card => card.classList.add('matched'));
            matchesFound += 2;
            if (matchesFound === cardValues.length) {
                alert('You won!');
            }
        } else {
            cardElements.forEach(card => card.textContent = '');
        }
        cardElements = [];
    }

    function onCardClicked(e) {
        if (cardElements.length < 2 && e.target.textContent === '') {
            e.target.textContent = cardValues[e.target.dataset.index];
            cardElements.push(e.target);
            if (cardElements.length === 2) {
                setTimeout(checkForMatch, 500);
            }
        }
    }

    fetch('http://localhost:5000/shuffle')
        .then(response => response.json())
        .then(cards => {
            cardValues = cards;
            cards.forEach((_, index) => {
                const cardElement = document.createElement('div');
                cardElement.classList.add('card');
                cardElement.dataset.index = index;
                cardElement.addEventListener('click', onCardClicked);
                gameBoard.appendChild(cardElement);
            });
        });
});

