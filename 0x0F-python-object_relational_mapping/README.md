# Python - Object-relational mapping
* (ORM) is a technique that allows you to work with relational databases using Python objects and classes instead of writing raw SQL queries.

![ORM](https://miro.medium.com/v2/resize:fit:700/0*CB27ux4zU5yoJROO)

## Description
(ORM) is a technique that allows you to work with relational databases using Python objects and classes instead of writing raw SQL queries. ORM libraries, such as SQLAlchemy, Django ORM, and Peewee, provide a way to map database tables to Python classes and perform database operations using Python code.  In practice, you would work with more complex data models and perform various database operations. ORM simplifies database interactions and makes your code more readable and maintainable.

## Features
 * **Database Connection:** You start by establishing a connection to the database you want to work with. This connection is typically defined in your application's configuration.
 * **Mapping Classes to Tables:** You define Python classes that represent tables in the database. Each class attribute corresponds to a column in the table, and the class itself represents a row in the table. These classes are often referred to as "models."
 * **Session Management:** ORM libraries typically provide a session or context in which database operations can be performed. A session is a unit of work that allows you to query the database, insert, update, or delete records.
 * **CRUD Operations:** You can use Python methods to perform Create, Read, Update, and Delete (CRUD) operations on the database. For example:
	* **Create:** You create new records by instantiating model objects and adding them to the session.
	* **Read:** You query the database using Python methods and filters to retrieve data.
	* **Update:** You modify existing records by changing the attributes of model objects and committing the changes to the session.
	* **Delete:** You delete records by removing model objects from the session and committing the changes.
 * **Transaction Management:** ORM libraries often provide transaction management to ensure that multiple database operations are executed atomically. Transactions allow you to commit or roll back a series of operations as a single unit.
 * **Query Building:** ORM libraries offer query builders or query languages that allow you to create complex SQL queries using Python code. This helps in constructing queries dynamically.
 * **Migration and Schema Management:** ORM libraries often provide tools for managing database schema changes, such as creating tables, altering columns, and adding indexes.
 * **Database Agnostic:** ORM libraries aim to be database agnostic, meaning you can switch between different database systems (e.g., MySQL, PostgreSQL, SQLite) without changing your Python code.

## Usage
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the database connection
engine = create_engine('mysql:///mydatabase.db')

# Define the base class for models
Base = declarative_base()

# Define a model (Python class) that maps to a database table
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(100))

# Create the database tables based on the defined models
Base.metadata.create_all(engine)

# Create a session to work with the database
Session = sessionmaker(bind=engine)
session = Session()

# Create a new user and add it to the session
new_user = User(username='john_doe', email='john@example.com')
session.add(new_user)

# Commit the changes to the database
session.commit()

# Query the database to retrieve user data
user = session.query(User).filter_by(username='john_doe').first()
print(f"User ID: {user.id}, Username: {user.username}, Email: {user.email}")

# Close the session
session.close()
```

## Credits
 * [10 common stumbling blocks for SQLAlchemy newbies](https://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html)
 * [SQLAlchemy](https://www.sqlalchemy.org/)
 * [SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
 * [Introduction to MySQL in Python](https://www.mikusa.com/python-mysql-docs/introduction.html)
 * [Introduction to SQLAlchemy](https://www.youtube.com/watch?v=woKYyhLCcnU)
 * [SQLAlchemy Turns Python Objets Inot Database Entries](https://youtu.be/AKQ3XEDI9Mw?si=QVq6UPMEqBmqBF-8)

## Contact
 * [Sakhile Ndlazi](https://www.twitter.com/sakhilelindah)
