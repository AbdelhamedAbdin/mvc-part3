from typing import Callable

import mysql.connector
from mysql.connector import Error


CONFIG = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'db'
}


class ConnectedDB:

    def __init__(self, command: str):
        self.command = command

    @staticmethod
    def connection():
        try:
            connection = mysql.connector.connect(**CONFIG)
        except:
            connection = None
        return connection

    def select_cursor(self) -> None:
        conn = self.connection()

        if conn:
            self.db_cursor = conn.cursor(buffered=True)
            self.db_cursor.execute(self.command)
        else:
            raise Error("Error while connecting to MySQL")

        return self.db_cursor

    def run_commit(self) -> None:
        conn = self.connection()

        if conn:
            self.db_cursor = conn.cursor(buffered=True)
            self.db_cursor.execute(self.command)
            conn.commit()
        else:
            raise Error("Error while connecting to MySQL")


class CRUDOperationsDB:

    def list(self, table_name: str) -> ConnectedDB.select_cursor:
        db = ConnectedDB(f"select * from {table_name};")
        return db.select_cursor()

    def create_data(self, table_name: str, **kwargs) -> None:
        fields = ""
        values = ""
        table_data = list(self.show_fields(table_name))
        model_dict = kwargs.get("data", {})

        for _fields in table_data:
            model_dict[_fields[0]] = self.field_validations("Create", _fields[0], _fields[1])

        for field, value in model_dict.items():
            fields += f"{field}, "
            values += f"{value}, "
        fields = fields.rstrip(", ")
        values = values.rstrip(", ")

        query = f"""INSERT INTO {table_name} ({fields}) VALUES ({values});"""
        print(query)
        # db = ConnectedDB(query)
        # db.run_commit()

    def show_fields(self, table_name: str) -> ConnectedDB.select_cursor:
        query = f"""SHOW FIELDS FROM {table_name}"""
        db = ConnectedDB(query)
        return db.select_cursor()

    def field_validations(self, operation_type: str, field: str, _type: str) -> str:
        value = ""

        if _type == "text":
            value = str(input(f"{operation_type} {field} with the string type: "))
            if value == "":
                value = None
        elif _type == "double":
            try:
                value = str("%.2f" % float(input(f"{operation_type} {field} with the float type: ")))
            except ValueError:
                print("input must be float")
                self.field_validations(operation_type, field, _type)
        else:
            raise ValueError(f"{field} is invalid field")
        return value

    def update_data(self, table_name: str, **kwargs) -> None:
        update_query = ""
        model_dict = kwargs.get("data", {})
        filter_dict = kwargs.get("filter")
        table_data = list(self.show_fields(table_name))

        for fields in table_data:
            if fields[0] not in model_dict:
                continue
            model_dict[fields[0]] = self.field_validations("Update", fields[0], fields[1])

        for field, value in model_dict.items():
            update_query += f"{field}='{value}', "
        update_query = update_query.rstrip(", ")

        query = f"""
            UPDATE {table_name}
            SET {update_query}
            WHERE ref_number={filter_dict[0]} AND disclosure_group={filter_dict[1]}
        """
        db = ConnectedDB(query)
        db.run_commit()

    def delete_record(self, table_name: str, **kwargs) -> None:
        filter_dict = kwargs.get("filter")
        query = f"""DELETE FROM {table_name} WHERE ref_number={filter_dict[0]} AND disclosure_group={filter_dict[1]}"""
        db = ConnectedDB(query)
        try:
            db.run_commit()
        except mysql.connector.errors.ProgrammingError:
            raise ValueError


print(list(CRUDOperationsDB().list("travelq"))[-3])
