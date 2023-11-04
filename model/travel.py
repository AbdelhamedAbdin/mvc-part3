import csv, os
from pathlib import Path

from db_config import CRUDOperationsDB
from model.model import Model

BASE_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent


class Travel(Model):
    """
    Student Name:
    Student number:
    """

    file = BASE_DIR / "travelq.csv"
    column_name = "travelq"

    def __init__(self, ref_number=None, disclosure_group=None, title_en=None, title_fr=None, name=None, purpose_en=None,
                 purpose_fr=None,
                 start_date=None, end_date=None, destination_en=None, destination_fr=None, airfare=None,
                 other_transport=None,
                 lodging=None, meals=None, other_expenses=None, total=None,
                 additional_comments_en=None, additional_comments_fr=None, owner_org=None, owner_org_title=None):
        self.ref_number = ref_number
        self.disclosure_group = disclosure_group
        self.title_en = title_en
        self.title_fr = title_fr
        self.name = name
        self.purpose_en = purpose_en
        self.purpose_fr = purpose_fr
        self.start_date = start_date
        self.end_date = end_date
        self.destination_en = destination_en
        self.destination_fr = destination_fr
        self.airfare = airfare
        self.other_transport = other_transport
        self.lodging = lodging
        self.meals = meals
        self.other_expenses = other_expenses
        self.total = total
        self.additional_comments_en = additional_comments_en
        self.additional_comments_fr = additional_comments_fr
        self.owner_org = owner_org
        self.owner_org_title = owner_org_title

    def sql_data(self) -> list:
        """ Read lines from CSV file """
        db = CRUDOperationsDB()
        lines = list(db.list(self.column_name))
        return lines  # list of tuples

    def select_all_data(self) -> None:
        """Find CSV file or get an error"""
        travel_dict = list(self.__dict__)
        reader = self.sql_data()  # list
        records = []
        new_dict = {}

        for row in reader:
            for i, column in enumerate(row):
                new_dict[travel_dict[i]] = column
            records.append(new_dict)
            new_dict = {}

            if len(records) > 100:
                break

        for record in records:
            print(record)

    def get_object_list(self) -> list:
        lines = self.sql_data()
        reader = csv.DictReader(lines)
        return list(reader)

    def update(self, **kwargs):
        super().save(**kwargs)

    def delete(self, **kwargs):
        super().save(**kwargs)

    def save(self, edit=False, delete=False, **kwargs):
        if edit:
            self.update(edit=True, **kwargs)
            print("Updated successfully!")
        elif delete:
            try:
                self.delete(delete=True, **kwargs)
                print("Deleted successfully!")
            except ValueError:
                print("Invalid Filter")
        else:
            super().save(**kwargs)
            print("Saved successfully!")
