document.getElementById('loan-form').addEventListener('submit', async function(e) {
    e.preventDefault();

    const loanAmount = document.getElementById('loan-amount').value;
    const loanPurpose = document.getElementById('loan-purpose').value;
    const loanTerm = document.getElementById('loan-term').value;

    const responseMessage = document.getElementById('response-message');

    // Send the form data to the backend API
    const response = await fetch('/loan_application', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        loan_amount: loanAmount,
        loan_purpose: loanPurpose,
        loan_term: loanTerm,
    })
});


    const data = await response.json();

    // Display the success or error message
    if (data.success) {
        responseMessage.innerHTML = `<p style="color: green;">${data.message}</p>`;
    } else {
        responseMessage.innerHTML = `<p style="color: red;">${data.message}</p>`;
    }
});
