

class db_table:
    def __init__(self):
        pass
    
    def create_table_query(self,table_name ,text_list):
        text = " , ".join(text_list)
        query = f"""create table if not exists testing_value.{table_name}(
            {text}
        )"""
        return query
    
    def create_customer(self,table_name, rows, conflict_cols):
        values = ", ".join(['%s'] *len(rows))
        rows = ",".join(rows)
        query = f"""insert into testing_value.{table_name}({rows}) values({values}) on conflict({conflict_cols}) do nothing"""
        return query
    
    def drop_table(self,table_name):
        query  = f"drop table {table_name}"
        return query
    
    def modify_cols(self, table_name, new_cols):
        query = f"""alter table {table_name} add column {new_cols};"""
        return query
    
    def select_rows(self, table_name, required, condition):
        query = f"""select {required} from {table_name} where {condition}"""
        return query
    
    