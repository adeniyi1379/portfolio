document.getElementById("contactForm").addEventListener("submit", function(event) {
    event.preventDefault();

    emailjs.init({
        publickey:"IsBy3j5UW6dM9LSq4"
    });

    const formData = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        message: document.getElementById("message").value
    };

    emailjs.send("service_mxwvlqz", "template_3tcwosk", this)
        .then(response => {
            alert("Email sent successfully!");
        })
        .catch(error => {
            alert("Failed to send email.");
        });
});
