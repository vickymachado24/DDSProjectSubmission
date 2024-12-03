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
4. initdb (postgresql) is already added to path. (if docker approach doesn't work)

---

## **Setup**

## **DB Setup Docker Approach **
Ensure Docker is running on your system before proceeding.
### **Step 1: Pull Required Docker Images**
```bash
docker pull jishnat/postgres-publisher:latest
docker pull jishnat/postgres-subscriber:latest
docker pull jishnat/custom-sub-postgres
docker pull jishnat/custom-postgres

```
### **Step 2: Create Docker Network**
```bash
docker network create pg_network

```
### **Step 3: Run Publisher Database**
Open a new terminal for the publisher:
```bash
docker stop postgres-publisher
docker rm postgres-publisher
docker run --name postgres-publisher --network pg_network -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=banking_db -p 5432:5432 -d jishnat/custom-postgres
docker start postgres-publisher

```
### **Step 4: Verify Publisher Database**
Access the publisher container:
```bash
docker exec -it postgres-publisher psql -U postgres
```
Confirm the database exists:
```bash
\c banking_db
```
### **Step 5: Run Subscriber Database**
Open a new terminal for the subscriber:
```bash
docker stop postgres-subscriber
docker rm postgres-subscriber
docker run --name postgres-subscriber --network pg_network -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=banking_subscriber_db -p 5433:5432 -d jishnat/custom-sub-postgres
docker start postgres-subscriber
```

### **Step 6: Verify Subscriber Database**
Access the subscriber container:
```bash
docker exec -it postgres-subscriber psql -U postgres
```
Confirm the database exists:
```bash
\c banking_subscriber_db
```
## **DB Setup Postgresql initdb server Approach **

### Publisher Setup

1. **Add PostgreSQL `bin` folder to Environment Variables**  
   Add the `bin` folder of your PostgreSQL installation (e.g., `C:\Program Files\PostgreSQL\15\bin`) to your system's PATH environment variable.

2. **Initialize the Publisher Database**  
```bash
   initdb /path/to/somefolder/pub
```This creates a data configuration folder for the publisher.

3. **Edit the PostgreSQL Configuration**
Navigate to the sub folder and open postgresql.conf in a text editor. 
Modify the following parameters:
```plaintext 
listen_addresses = '*'
wal_level = logical
max_wal_senders = 10
max_replication_slots = 10
port = 5432  # Change port to avoid conflicts with the default 5432
```
Save and exit.
4. **Update pg_hba.conf for Authentication**
In the sub folder, edit the pg_hba.conf file.
Add these lines at the end of the file:
```plaintext
host    all             all             127.0.0.1/32            md5
host    all             all             ::1/128                 md5
```

5. **Start the Publisher Server**
```bash
  pg_ctl -D /path/to/somefolder/pub start
```

6. **Connect to the Publisher Server**
Open a new terminal and connect using psql:
```bash
psql -U postgres -h localhost -p 5432
```
7. **Set Up the Publisher Database and Table **
Run the queries inside the below links step by step:

8. **Verify Publications **
```sql
\dRp
SELECT * FROM pg_publication;
```

### Publisher Setup

9. **Initialize the Subscriber Database**
```bash
initdb /path/to/somefolder/sub
```
This creates a data configuration folder for the subscriber.
10. **Edit the PostgreSQL Configuration**
Navigate to the sub folder and open postgresql.conf in a text editor.
Modify the following parameters
```plaintext
listen_addresses = '*'
port = 5434  # Use a different port from the publisher
```
Save and exit.
11. **Update pg_hba.conf for Authentication**
In the sub folder, edit the pg_hba.conf file.
Add these lines at the end of the file
```plaintext
host    all             all             127.0.0.1/32            md5
host    all             all             ::1/128                 md5
```
12. **Start the Subscriber Server**
```bash
pg_ctl -D /path/to/somefolder/sub start

```
13. **Connect to the Subscriber Server**
Open a new terminal and connect using psql:
```bash
psql -h localhost -p 5433 -d postgres
```
14. **Set Up the Subscriber Database and Subscription**
Run the scripts one by one mentioned in the link, in steps:

15. **Verify Subscription**
Ensure the subscription is working by checking the transactions table in the subscriber database:
```sql
SELECT * FROM transactions;
```
16. **Note for Multiple Subscribers**

If setting up additional subscribers, use a different subscription name for each (e.g., transactions_sub2 for the next subscriber), but keep all other parameters the same

### **Step 1: Clone the Repository**
```bash
docker pull jishnat/postgres-publisher:latest
docker pull jishnat/postgres-subscriber:latest
docker pull jishnat/custom-postgres

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

### **Step 4: Run the Flask Application**
```bash
flask run
```
or 
if you are using an IDE like Pycharm
run the __init__.py
