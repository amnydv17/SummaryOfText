const summarizeForm = document.getElementById('summarize-form');
const textInput = document.getElementById('text-input');
const summarizeButton = document.getElementById('summarize-button');
const summaryOutput = document.getElementById('summary-output');
const trainButton = document.getElementById('train-button');

summarizeButton.addEventListener('click', async (e) => {
    e.preventDefault();
    const text = textInput.value.trim();
    if (text) {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text })
        });
        const data = await response.json();
        if (data.summary) {
            summaryOutput.innerText = data.summary;
        } else {
            summaryOutput.innerText = 'Error: Unable to summarize text.';
        }
    } else {
        summaryOutput.innerText = 'Please enter some text to summarize.';
    }
});

trainButton.addEventListener('click', async (e) => {
    e.preventDefault();
    const response = await fetch('/train', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    });
    const data = await response.json();
    if (data.message) {
        alert(data.message);
    } else {
        alert('Error: Unable to train model.');
    }
});