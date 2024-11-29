from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserLogin(db.Model):
    __tablename__ = 'USERLOGIN'
    LoginID = db.Column(db.Integer, primary_key=True)
    CustomerID = db.Column(db.Integer, nullable=False)
    Username = db.Column(db.String(255), nullable=False)
    Password = db.Column(db.String(255), nullable=False)
    LastLoginTime = db.Column(db.Date)  # Date type
    Salt = db.Column(db.String(255), nullable=False)
    Customer_CustomerID = db.Column(db.Integer, db.ForeignKey('CUSTOMER.CustomerID'), nullable=False)

    customer = db.relationship('Customer', backref='user_logins')

class Person(db.Model):
    __tablename__ = 'PERSON'
    PersonID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(255))
    LastName = db.Column(db.String(255))
    DOB = db.Column(db.Date)
    Email = db.Column(db.String(255))
    PhoneNumber = db.Column(db.String(255))
    TaxIdentifier = db.Column(db.String(255))
    Address_1 = db.Column(db.String(255))
    Address_2 = db.Column(db.String(255))
    ApartmentNumber = db.Column(db.Integer)
    State = db.Column(db.String(255))
    County = db.Column(db.String(255))
    PostalCode = db.Column(db.Integer)
    Country = db.Column(db.String(255))
    OnboardingApplication_ApplicationID = db.Column(db.Integer, db.ForeignKey('ONBOARDINGAPPLICATION.ApplicationID'))

    onboarding_application = db.relationship('OnboardingApplication', backref='person')

class OnboardingApplication(db.Model):
    __tablename__ = 'ONBOARDINGAPPLICATION'
    ApplicationID = db.Column(db.Integer, primary_key=True)
    PersonID = db.Column(db.Integer, db.ForeignKey('PERSON.PersonID'))
    ApplicationStatus = db.Column(db.String(255))
    SubmissionDate = db.Column(db.Date)
    ApprovalDate = db.Column(db.Date)

class Customer(db.Model):
    __tablename__ = 'CUSTOMER'
    CustomerID = db.Column(db.Integer, primary_key=True)
    CustomerType = db.Column(db.String(255))
    Person_PersonID = db.Column(db.Integer, db.ForeignKey('PERSON.PersonID'))

    person = db.relationship('Person', backref='customer')

class Branch(db.Model):
    __tablename__ = 'BRANCH'
    BranchID = db.Column(db.Integer, primary_key=True)
    BranchName = db.Column(db.String(255))
    Address_1 = db.Column(db.String(255))
    Address_2 = db.Column(db.String(255))
    ApartmentNumber = db.Column(db.Integer)
    State = db.Column(db.String(255))
    County = db.Column(db.String(255))
    PostalCode = db.Column(db.Integer)
    Country = db.Column(db.String(255))
    PhoneNumber = db.Column(db.String(255))

class UserRoles(db.Model):
    __tablename__ = 'USER_ROLES'
    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(255))
    permissions = db.Column(db.JSON)

class Employee(db.Model):
    __tablename__ = 'EMPLOYEE'
    EmployeeID = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('USER_ROLES.role_id'))
    Position = db.Column(db.String(255))
    Person_PersonID = db.Column(db.Integer, db.ForeignKey('PERSON.PersonID'))
    Branch_BranchID = db.Column(db.Integer, db.ForeignKey('BRANCH.BranchID'))

    role = db.relationship('UserRoles', backref='employees')
    person = db.relationship('Person', backref='employees')
    branch = db.relationship('Branch', backref='employees')

class Account(db.Model):
    __tablename__ = 'ACCOUNT'
    AccountID = db.Column(db.Integer, primary_key=True)
    AccountType = db.Column(db.String(255))
    AccountNumber = db.Column(db.String(255))
    CurrentBalance = db.Column(db.Numeric(18, 2))
    DateOpened = db.Column(db.Date)
    DateClosed = db.Column(db.Date)
    AccountStatus = db.Column(db.String(255))
    Branch_BranchID = db.Column(db.Integer, db.ForeignKey('BRANCH.BranchID'))

    branch = db.relationship('Branch', backref='accounts')

class CustomerAccount(db.Model):
    __tablename__ = 'CUSTOMER_ACCOUNT'
    Customer_CustomerID = db.Column(db.Integer, db.ForeignKey('CUSTOMER.CustomerID'), primary_key=True)
    Account_AccountID = db.Column(db.Integer, db.ForeignKey('ACCOUNT.AccountID'), primary_key=True)

    customer = db.relationship('Customer', backref='customer_accounts')
    account = db.relationship('Account', backref='customer_accounts')

class Transaction(db.Model):
    __tablename__ = 'TRANSACTION'
    TransactionID = db.Column(db.Integer, primary_key=True)
    Account_AccountID = db.Column(db.Integer, db.ForeignKey('ACCOUNT.AccountID'))
    Amount = db.Column(db.Numeric(18, 2))
    TransactionType = db.Column(db.String(255))
    TransactionDate = db.Column(db.Date)

    account = db.relationship('Account', backref='transactions')

class TransactionLogs(db.Model):
    __tablename__ = 'TRANSACTION_LOGS'
    LogID = db.Column(db.Integer, primary_key=True)
    TransactionID = db.Column(db.Integer, db.ForeignKey('TRANSACTION.TransactionID'))
    LogDetails = db.Column(db.String(255))
    CreatedAt = db.Column(db.DateTime)

    transaction = db.relationship('Transaction', backref='transaction_logs')

class PaymentGatewayLogs(db.Model):
    __tablename__ = 'PAYMENT_GATEWAY_LOGS'
    GatewayLogID = db.Column(db.Integer, primary_key=True)
    TransactionLogID = db.Column(db.Integer, db.ForeignKey('TRANSACTION_LOGS.LogID'))
    GatewayName = db.Column(db.String(255))
    Status = db.Column(db.String(255))
    GatewayTimestamp = db.Column(db.DateTime)

    transaction_log = db.relationship('TransactionLogs', backref='gateway_logs')

class LoanApplications(db.Model):
    __tablename__ = 'LOANAPPLICATIONS'
    ApplicationID = db.Column(db.Integer, primary_key=True)
    PersonID = db.Column(db.Integer, db.ForeignKey('PERSON.PersonID'))
    LoanType = db.Column(db.String(255))
    RequestedAmount = db.Column(db.Numeric(18, 2))
    Status = db.Column(db.String(255))
    ApplicationDate = db.Column(db.Date)

    person = db.relationship('Person', backref='loan_applications')

class Loan(db.Model):
    __tablename__ = 'LOAN'
    LoanID = db.Column(db.Integer, primary_key=True)
    LoanType = db.Column(db.String(255))
    LoanAmount = db.Column(db.Integer)
    InterestRate = db.Column(db.Numeric(5, 2))
    Term = db.Column(db.Integer)
    StartDate = db.Column(db.Date)
    EndDate = db.Column(db.Date)
    Status = db.Column(db.String(255))
    Customer_CustomerID = db.Column(db.Integer, db.ForeignKey('CUSTOMER.CustomerID'))
    LoanApplications_ApplicationID = db.Column(db.Integer, db.ForeignKey('LOANAPPLICATIONS.ApplicationID'))

    customer = db.relationship('Customer', backref='loans')
    loan_application = db.relationship('LoanApplications', backref='loans')



class LoanPayment(db.Model):
    __tablename__ = 'LOAN_PAYMENT'
    LoanPaymentID = db.Column(db.Integer, primary_key=True)
    ScheduledPaymentDate = db.Column(db.Date)
    PaymentAmount = db.Column(db.Numeric(18, 2))
    PrincipalAmount = db.Column(db.Numeric(18, 2))
    InterestAmount = db.Column(db.Numeric(18, 2))
    PaidAmount = db.Column(db.Numeric(18, 2))
    PaidDate = db.Column(db.Date)
    Loan_LoanID = db.Column(db.Integer, db.ForeignKey('LOAN.LoanID'))


class KYC(db.Model):
    __tablename__ = 'KYC'
    KYCID = db.Column(db.Integer, primary_key=True)
    PersonID = db.Column(db.Integer, db.ForeignKey('PERSON.PersonID'))
    VerificationType = db.Column(db.String(255))
    Status = db.Column(db.String(255))
    DocumentID = db.Column(db.Integer)


class Notification(db.Model):
    __tablename__ = 'NOTIFICATIONS'
    NotificationID = db.Column(db.Integer, primary_key=True)
    CustomerID = db.Column(db.Integer, db.ForeignKey('CUSTOMER.CustomerID'))
    Message = db.Column(db.String(255))
    NotificationType = db.Column(db.String(255))
    Status = db.Column(db.String(255))
    StartDate = db.Column(db.Date)
    EndDate = db.Column(db.Date)


class ServiceRequest(db.Model):
    __tablename__ = 'SERVICE_REQUESTS'
    RequestID = db.Column(db.Integer, primary_key=True)
    CustomerID = db.Column(db.Integer, db.ForeignKey('CUSTOMER.CustomerID'))
    Details = db.Column(db.String(255))
    Status = db.Column(db.String(255))


class SupportTicket(db.Model):
    __tablename__ = 'SUPPORT_TICKETS'
    TicketID = db.Column(db.Integer, primary_key=True)
    RequestID = db.Column(db.Integer, db.ForeignKey('SERVICE_REQUESTS.RequestID'))
    IssueDescription = db.Column(db.String(255))
    Status = db.Column(db.String(255))


class SecurityQuestion(db.Model):
    __tablename__ = 'SECURITYQUESTIONS'
    QuestionID = db.Column(db.Integer, primary_key=True)
    QuestionText = db.Column(db.String(255))


class CustomerSecurityAnswer(db.Model):
    __tablename__ = 'CUSTOMERSECURITYANSWERS'
    answer_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('CUSTOMER.CustomerID'))
    question_id = db.Column(db.Integer, db.ForeignKey('SECURITYQUESTIONS.QuestionID'))
    answer = db.Column(db.String(255))


class FraudAlert(db.Model):
    __tablename__ = 'FRAUD_ALERTS'
    AlertID = db.Column(db.Integer, primary_key=True)
    CustomerID = db.Column(db.Integer, db.ForeignKey('CUSTOMER.CustomerID'))
    Description = db.Column(db.String(255))
    Timestamp = db.Column(db.TIMESTAMP)


class FraudCase(db.Model):
    __tablename__ = 'FRAUD_CASES'
    CaseID = db.Column(db.Integer, primary_key=True)
    CustomerID = db.Column(db.Integer, db.ForeignKey('CUSTOMER.CustomerID'))
    CaseDescription = db.Column(db.String(255))
    CaseStatus = db.Column(db.String(255))
    ResolutionDate = db.Column(db.Date)
