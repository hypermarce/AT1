document.addEventListener("DOMContentLoaded", function() {
    var createForm = document.getElementById('createQuestion');
    var questionText = document.getElementById('questionText');
    var questionAnswerForm = document.getElementById('questionAnswer')
    var questionDataDecoded = questionData == '  ' ? null : JSON.parse(decodeHtmlEntity(questionData));
    var correctIncorrectText = document.getElementById('correctIncorrectText')
    var nextQuestion = false

    function updateQuestionText() {
        questionText.innerHTML = questionDataDecoded.question
    }

    if(questionData === "  ") {
        questionAnswerForm.style.display = 'none'
    } else {
        updateQuestionText()
    }

    createForm.onsubmit = function(e) {
        e.preventDefault(); // Prevent the default form submission behavior

        var selectedType = document.getElementById('type').value;

        let url = new URL(window.location.origin)
        url.searchParams.append('type', selectedType)

        window.location.href = url.href
    };

    questionAnswerForm.onsubmit = (e) => {
        e.preventDefault();

        if(!nextQuestion) {
            if(e.target[0].value == "") return

            document.getElementById('answerInput').disabled = true
            nextQuestion = true
            document.getElementById('submitButton').innerHTML = "Next Question"

            if(parseInt(e.target[0].value) == parseInt(questionDataDecoded.answer)) {
                correctIncorrectText.innerHTML = '✅'
            } else correctIncorrectText.innerHTML = '❌'

        } else window.location.reload();

    }

    document.addEventListener('keypress', function(event) {
        if(event.key == "Enter" && nextQuestion) window.location.reload();
    });

});

function decodeHtmlEntity(encodedJson) {
    const decodedJson = encodedJson.replace(/&quot;/g, '"');
    return decodedJson;
}
