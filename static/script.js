document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    // Get form values
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Simple validation (you can add more complex validation here)
    if (username === 'user' && password === 'pass') {
        // Redirect to landing page if validation is successful
        window.location.href = 'index.html';
    } else {
        // Show error message if validation fails
        document.getElementById('error-message').textContent = 'Invalid username or password';
    }
});
