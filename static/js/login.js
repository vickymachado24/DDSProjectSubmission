document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    
    if (loginForm) {
        loginForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            
            // Here you would typically send this data to your backend for authentication
            console.log(`Login attempted for user: ${username}`);
            alert('Login functionality not implemented in this demo.');
        });
    }
});