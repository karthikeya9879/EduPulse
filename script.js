// This script runs after the HTML page has fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Find all the elements we need to interact with
    const summarizeBtn = document.getElementById('summarize-btn');
    const summaryContainer = document.getElementById('summary-container');

    // If the button doesn't exist on the page, do nothing
    if (!summarizeBtn) {
        return;
    }

    // Add a click event listener to the button
    summarizeBtn.addEventListener('click', () => {
        // Get the professor ID from the button's data attribute
        const professorId = summarizeBtn.dataset.professorId;

        // Show a loading state inside the summary container
        summaryContainer.innerHTML = '<p class="text-indigo-600">Generating AI coaching summary, please wait...</p>';
        summarizeBtn.disabled = true;
        summarizeBtn.textContent = 'Generating...';

        // Use the Fetch API to call our backend route
        fetch(`/summarize/${professorId}`)
            .then(response => response.json()) // Parse the JSON response from the server
            .then(data => {
                // Update the container with the summary from the AI
                summaryContainer.innerHTML = `<div class="prose max-w-none">${data.summary}</div>`;
                
                // Hide the button after generating the summary for a cleaner look
                summarizeBtn.style.display = 'none';
            })
            .catch(error => {
                // Show an error message if something goes wrong
                console.error('Error fetching AI summary:', error);
                summaryContainer.innerHTML = '<p class="text-red-500">An error occurred. Please try again.</p>';
                summarizeBtn.disabled = false;
                summarizeBtn.textContent = 'Generate Summary';
            });
    });
});
