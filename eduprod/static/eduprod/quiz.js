document.addEventListener("DOMContentLoaded", function() {
    // Get references to HTML elements
    var createForm = document.getElementById('createQuestion');
    var questionText = document.getElementById('questionText');
    var questionAnswerForm = document.getElementById('questionAnswer')
    var questionDataDecoded = questionData == '  ' ? null : JSON.parse(decodeHtmlEntity(questionData));
    var correctIncorrectText = document.getElementById('correctIncorrectText')
    var nextQuestion = false

    // Function to update the question text
    function updateQuestionText() {
        questionText.innerHTML = questionDataDecoded.question
    }
    
    // If no question data, hide the answer form; otherwise, update question text
    if (questionData === "  ") {
        questionAnswerForm.style.display = 'none'
    } else {
        updateQuestionText()
    }

    // Handle form submission for creating a new question
    createForm.onsubmit = function(e) {
        e.preventDefault(); // Prevent the default form submission behavior

        // Get selected question type
        var selectedType = document.getElementById('type').value;

        // Construct URL with selected question type
        let url = new URL(window.location.origin);
        url.searchParams.append('type', selectedType);

        // Redirect to the new URL
        window.location.href = url.href;
    };

    // Handle form submission for answering a question
    questionAnswerForm.onsubmit = (e) => {
        e.preventDefault();

        // If not on next question, check answer
        if (!nextQuestion) {
            if (e.target[0].value == "") return;

            // Disable input and show correct/incorrect
            document.getElementById('answerInput').disabled = true;
            nextQuestion = true;
            document.getElementById('submitButton').innerHTML = "Next Question";

            // Show correct or incorrect message
            if (parseInt(e.target[0].value) == parseInt(questionDataDecoded.answer)) {
                correctIncorrectText.innerHTML = '✅';
            } else correctIncorrectText.innerHTML = '❌';
        } else window.location.reload(); // Reload page for next question
    }

    // Reload page on pressing Enter key after answering a question
    document.addEventListener('keypress', function(event) {
        if (event.key == "Enter" && nextQuestion) window.location.reload();
    });

});

// Function to decode HTML entities
function decodeHtmlEntity(encodedJson) {
    const decodedJson = encodedJson.replace(/&quot;/g, '"');
    return decodedJson;
}
