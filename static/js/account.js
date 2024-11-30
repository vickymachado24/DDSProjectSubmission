function viewDetails(accountType) {
    const accountDetails = {
        checking: {
            balance: "$5,000.00",
            transactions: [
                { date: "2024-11-30", description: "Grocery Store", amount: "-$50.00" },
                { date: "2024-11-29", description: "Paycheck Deposit", amount: "+$1000.00" },
                { date: "2024-11-28", description: "ATM Withdrawal", amount: "-$200.00" }
            ]
        },
        savings: {
            balance: "$15,000.00",
            transactions: [
                { date: "2024-11-25", description: "Interest Credit", amount: "+$15.00" },
                { date: "2024-11-20", description: "Transfer from Checking", amount: "+$500.00" },
                { date: "2024-11-15", description: "Online Savings Deposit", amount: "+$1000.00" }
            ]
        }
    };

    const details = accountDetails[accountType];
    document.getElementById('detail-account-type').textContent = accountType.charAt(0).toUpperCase() + accountType.slice(1) + " Account";
    document.getElementById('detail-balance').textContent = "Current Balance: " + details.balance;

    const transactionList = document.getElementById('transaction-list');
    transactionList.innerHTML = '';
    details.transactions.forEach(transaction => {
        const li = document.createElement('li');
        li.textContent = `${transaction.date}   ${transaction.description} : ${transaction.amount}`;
        transactionList.appendChild(li);
    });

    document.getElementById('account-details').style.display = 'block';
}