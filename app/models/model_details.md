🔹 Common Parameters Used Inside Field(...)
Let’s break down the most useful ones with real explanations:

Parameter	Purpose
default=...	Sets a static default value when field is missing
default_factory=...	Sets a callable that generates a default dynamically (e.g., uuid4)
primary_key=True	Marks this field as the primary key of the table
foreign_key="..."	Declares a foreign key constraint referencing another table
index=True	Adds a DB index on the column for faster queries
unique=True	Adds a UNIQUE constraint to the DB column
nullable=False	Prevents the column from being NULL in the database
sa_column=...	Allows attaching raw SQLAlchemy Column with advanced options



__table_name__=="name" can be mentioned inside the class  to store the table name else the class name lowercase will be saved as the table name



🔁 Relationship Type:
One-to-Many

One User → Many Alerts

Each Alert → belongs to one User

📍 Foreign Key goes into the "many" side → Alert.user_id


🔁 Relationship Type:
Many-to-Many

📍 Needs a separate link table, and no foreign key in either main model.
