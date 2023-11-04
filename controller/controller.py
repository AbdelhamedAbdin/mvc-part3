from db_config import ConnectedDB


class Controller:
    """
    Student Name:
    Student number:
    This is the main controller to handle request methods
    MVC follow the following Diagram:
    ----------------------------------

    "Request" from User ------> View -------> Controller -----> Model to Create, Update, Delete, Retrieve Data
                        <------ "Response"  <-------|
    So, the controller should have the controller to control the data to apply the above methods.

    """

    # Use the controller list to list records from MySQL DB
    def list(self):
        self.model().select_all_data()

    # Use the controller Create to create records to MySQL DB
    def create(self):
        """ Get dict of values from the request to save it in CSV file """
        model_dict = self.model().__dict__
        self.model().save(data=model_dict)

    # Use the controller Update to update records to CSV file based on its position
    def update(self, by_ref_number: str, by_disclosure_group: str):
        model_dict = self.model().__dict__
        self.model().save(filter=(by_ref_number, by_disclosure_group), data=model_dict, edit=True)

    # Use the controller delete to remove records from CSV file knowing the position number
    def delete(self, by_ref_number: str, by_disclosure_group: str):
        self.model().save(filter=(by_ref_number, by_disclosure_group), delete=True)
