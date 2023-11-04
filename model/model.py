import csv

from db_config import CRUDOperationsDB


class Model:
    """
        Student Name:
        Student number:
        This is the important section where it can be applied to any model such as in our task
        (Travel() model) to validate the data and change the data if there's a change has
        happened by control methods if there's a request came to control.
    """
    table_name = "travelq"

    def save(self, **kwargs):
        """Save method to save the data in CSV file when Create or Update operations run"""

        edit = False
        delete = False

        if kwargs.get("edit"):
            edit = kwargs.pop("edit")

        if kwargs.get("delete"):
            delete = kwargs.pop("delete")

        if not edit and not delete:  # create
            operation = CRUDOperationsDB()
            operation.create_data(self.table_name, **kwargs)
        elif edit:  # update
            operation = CRUDOperationsDB()
            operation.update_data(self.table_name, **kwargs)
        elif delete:  # delete
            operation = CRUDOperationsDB()
            operation.delete_record(self.table_name, **kwargs)
