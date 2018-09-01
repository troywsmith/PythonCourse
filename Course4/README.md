# Using Databases with Python

Some skills learned:
- SQL
- SQLite3
- D3.js

### Chapter 14: Object Oriented Python

attribute: A variable that is part of a class.

class: A template that can be used to construct an object. Defines the attributes and methods that will make up the object.

child class: A new class created when a parent class is extended. The child class inherits all of the attributes and methods of the parent class.

constructor: An optional specially named method (__init__) that is called at the moment when a class is being used to construct an object. Usually this is used to set up initial values for the object.

destructor: An optional specially named method (__del__) that is called at the moment just before an object is destroyed. Destructors are rarely used.

inheritance: When we create a new class (child) by extending an existing class (parent). The child class has all the attributes and methods of the parent class plus additional attributes and methods defined by the child class.

method: A function that is contained within a class and the objects that are constructed from the class. Some object-oriented patterns use ‘message’ instead of ‘method’ to describe this concept.

object: A constructed instance of a class. An object contains all of the attributes and methods that were defined by the class. Some object-oriented documentation uses the term ‘instance’ interchangeably with ‘object’.

parent class: The class which is being extended to create a new child class. The parent class contributes all of its methods and attributes to the new child class


### Chapter 15: Using Databases and SQL

attribute: One of the values within a tuple. More commonly called a “column” or “field”.

constraint: When we tell the database to enforce a rule on a field or a row in a table. A common constraint is to insist that there can be no duplicate values in a particular field (i.e., all the values must be unique).

cursor: A cursor allows you to execute SQL commands in a database and retrieve data from the database. A cursor is similar to a socket or file handle for network connections and files, respectively.

database browser: A piece of software that allows you to directly connect to a database and manipulate the database directly without writing a program.

foreign key: A numeric key that points to the primary key of a row in another table. Foreign keys establish relationships between rows stored in different tables.

index: Additional data that the database software maintains as rows and inserts into a table to make lookups very fast.

logical key: A key that the “outside world” uses to look up a particular row. For example in a table of user accounts, a person’s email address might be a good candidate as the logical key for the user’s data.

normalization: Designing a data model so that no data is replicated. We store each item of data at one place in the database and reference it elsewhere using a foreign key.

primary key: A numeric key assigned to each row that is used to refer to one row in a table from another table. Often the database is configured to automatically assign primary keys as rows are inserted.

relation: An area within a database that contains tuples and attributes. More typically called a “table”.

tuple: A single entry in a database table that is a set of attributes. More typically called “row”.

SQL injection: 

### Chapter 16: Visualizing Data

