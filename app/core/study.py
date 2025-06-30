import psycopg2
import os 
from dotenv import load_dotenv
from app.service.db_queries import db_table
load_dotenv()

class database: 
    def __init__(self):
        self.host = os.getenv('DB_HOST')
        self.port = os.getenv('DB_PORT')
        self.database = os.getenv('DB_NAME')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.connection = None
        self.cursor = None
        self.db_table = db_table()
        self.connect()
    
    
    
    def connect(self):
        self.connection = psycopg2.connect(host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password)
        
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"CREATE SCHEMA IF NOT EXISTS testing_value;")

    
    def create_a_user(self):
        fields = ("id int unique PRIMARY KEY",
                  "name varchar(20) unique not null",
                  "age int ")
        create_table_query = self.db_table.create_table_query("travel_recovery",fields)
        self.cursor.execute(create_table_query)
        self.connection.commit()
    
    def insert_customer_data(self,data: dict):
        cols = [each for each in data]
        values = [str(each) for each in data.values()]
        print(values)
        insert_query = self.db_table.create_customer("travel_recovery",cols, cols[0])
        print(insert_query)
        self.cursor.execute(insert_query,values)
        self.connection.commit()
        print(f"enterd the details {values}")
    
    def drop_table(self):
        drop_table = self.db_table.drop_table("testing_value.travel_recovery")
        self.cursor.execute(drop_table)
        self.connection.commit()
        
    def modify_table(self, new_cols):
        query = self.db_table.modify_cols("testing_value.travel_recovery",new_cols)
        self.cursor.execute(query)
        self.connection.commit()
        
    def select_query(self, required, condtion):
        query = self.db_table.select_rows("testing_value.travel_recovery",required,condtion)
        print(query)
        self.cursor.execute(query)
        value = self.cursor.fetchone()
        print(value)
        
        
obj = database()

print("creating a connection")

# obj.connect()
data = {"id": 1,"name": "aju","age": 13}
obj.create_a_user()
obj.insert_customer_data(data)
# obj.modify_table('"password" VARCHAR(200)')  
obj.select_query("name","id = 1")
print("droping the table")
obj.drop_table()
