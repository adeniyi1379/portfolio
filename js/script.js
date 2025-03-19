document.getElementById('contactForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the default form submission

    const form = event.target;
    const formData = new FormData(form); // Create FormData object from the form

    // Send the form data to Formspree using fetch
    fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
            'Accept': 'application/json'
        }
    })
    .then(response => {
        if (response.ok) {
            // Show the success popup
            document.getElementById('successPopup').style.display = 'block';
            form.reset(); // Reset the form fields
        } else {
            alert('There was a problem submitting your form. Please try again.'); // Handle errors
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('There was a problem submitting your form. Please try again.'); // Handle network errors
    });
});

// Function to close the popup
function closePopup() {
    document.getElementById('successPopup').style.display = 'none';
}