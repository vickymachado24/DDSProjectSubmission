document.addEventListener('DOMContentLoaded', () => {
    const loanForm = document.getElementById('loan-form');
    
    if (loanForm) {
        loanForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const amount = document.getElementById('loan-amount').value;
            const purpose = document.getElementById('loan-purpose').value;
            const term = document.getElementById('loan-term').value;
            
            // Here you would typically send this data to your backend
            console.log(`Loan application submitted: $${amount} for ${purpose} over ${term} years`);
            alert('Loan application submitted successfully!');
        });
    }
});