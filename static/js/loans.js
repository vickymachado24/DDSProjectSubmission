function viewLoanDetails(loanType) {
    const loanDetails = {
        home: {
            amount: "$200,000",
            installments: [
                { date: "2024-12-01", amount: "$1,200.00" },
                { date: "2024-11-01", amount: "$1,200.00" },
                { date: "2024-10-01", amount: "$1,200.00" }
            ]
        },
        car: {
            amount: "$15,000",
            installments: [
                { date: "2024-12-01", amount: "$450.00" },
                { date: "2024-11-01", amount: "$450.00" },
                { date: "2024-10-01", amount: "$450.00" }
            ]
        }
    };

    const details = loanDetails[loanType];
    
    document.getElementById('detail-loan-type').textContent = loanType.charAt(0).toUpperCase() + loanType.slice(1) + " Loan";
    document.getElementById('detail-loan-amount').textContent = "Loan Amount: " + details.amount;

    const installmentList = document.getElementById('installment-list');
    installmentList.innerHTML = ''; 
    details.installments.forEach(installment => {
        const li = document.createElement('li');
        li.textContent = `${installment.date}: Installment = ${installment.amount}`;
        installmentList.appendChild(li);
    });

    document.getElementById('loan-details').style.display = 'block'; 
}