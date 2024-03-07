document.addEventListener('DOMContentLoaded', function () {
    var typingText = document.getElementById('typing-text');
    if (typingText) {
        var text = typingText.getAttribute('data-text').trim();
        typingText.setAttribute('data-text', ''); // Clear data-text attribute
        typingText.textContent = text; // Set text content directly
    }
});