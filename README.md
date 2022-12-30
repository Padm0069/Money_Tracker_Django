# Money_Tracker_Django
Part of Cohesive Intern hiring (Backend)
Money Tracker is a Django based web application for splitting expenses with your friends 
##Features
- ### **Backend (Django)**

- REST API for
    - List of known users (friends)
    - Creating, updating, and deleting transactions.  the list of transactions.
- The transaction is associated with a set of users to split it across. Users can/cannot be a member. It should also have a spending category
- Uses Django's built-in authentication system to authenticate users
- Uses Django's built-in ORM to store the data in an SQLite database

##Frontend
- Uses Bootstrap and js for frontend.
- Displays the list of transactions and allow the user to filter the transactions by date and category.

### Steps for running project
```bash
git clone 
cd Money_Tracker_Django
cp .env.example .env
```
##### Fill the .env file with the correct database,

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
source .env
python manage.py migrate
python manage.py runserver
```
