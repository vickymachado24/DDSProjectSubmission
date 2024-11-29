# **Electronic Banking Application**

This project is a Flask-based web application for managing user accounts, loans, and loan applications. It uses PostgreSQL for data storage and supports replication between a publisher and a subscriber database.

---

## **Features**
- User Authentication (Login/Logout)
- View Account and Loan Information
- Apply for Loans
- Publisher-Subscriber Database Replication:
  - **Read Queries**: Routed to either the publisher or subscriber database.
  - **Write Queries**: Always routed to the publisher database.

---

## **Tech Stack**
- **Backend**: Flask, Flask-SQLAlchemy  
- **Frontend**: HTML, CSS, JavaScript  
- **Database**: PostgreSQL with replication (Publisher/Subscriber)  
- **Other Libraries**: Flask-Login, Flask-WTF  

---

## **Prerequisites**
1. Install [Docker](https://docs.docker.com/get-docker/).
2. Install Python 3.9 or higher.
3. Install PostgreSQL (if not using Docker for databases).

---

## **Setup**

### **Step 1: Clone the Repository**
```bash
git clone <repository_url>
cd <repository_name>
```

### **Step 2: Set Up Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### **Step 3: Install Dependencies**

```bash
pip install -r requirements.txt
```

### **Step 4: Configure Environment Variables**
```bash
export PUBLISHER_DATABASE_URL="postgresql://postgres:postgres@localhost:5432/banking_db"
export SUBSCRIBER_DATABASE_URL="postgresql://postgres:postgres@localhost:5433/banking_subscriber_db"

export SECRET_KEY="your-secret-key"
```


### **Step 5: Run Docker Containers for Databases**
```bash
docker run --name postgres-publisher -e POSTGRES_PASSWORD=mysecretpassword -d postgres
docker run --name postgres-subscriber -e POSTGRES_PASSWORD=mysecretpassword -d postgres


```


### **Step 6: Run the Flask Application**
```bash
flask run

```
