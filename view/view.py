from controller.controller import Controller
from model.travel import Travel


class View(Controller):
    """
        Student Name:
        Student number:
        This View is responsible for getting requests and show results for user
        According to the user request that had been handled by the controller methods
    """
    model = Travel

    def __init__(self):
        self.operations()
        self.request()

    # Read the steps that must be taken
    @staticmethod
    def operations():
        print("------------------------------")
        print("Developer Name: Abdallah")
        print("Enter one of the following operation: ")
        print("1: ALL DATA")
        print("2: CREATE")
        print("3: UPDATE")
        print("4: DELETE\r")

    # Get the expected output or raise an error
    def request_handler(self) -> int:
        try:
            request_output = int(input("Type Operation Number: "))
        except ValueError:
            print("Invalid input, the input must be an integer")
            self.request()
        else:
            return request_output

    # Get the target request from controller
    def request(self) -> None:
        request_output = self.request_handler()
        if request_output == 1:
            self.list()
        elif request_output == 2:
            self.create()
        elif request_output == 3:
            by_ref_number = str(input("Type the valid ref_number to Update it: "))
            by_disclouser_group = str(input("Type the valid disclouser_group to Update it: "))
            self.update(by_ref_number, by_disclouser_group)
        elif request_output == 4:
            by_ref_number = str(input("Type the valid ref_number to Remove it: "))
            by_disclouser_group = str(input("Type the valid disclouser_group to Remove it: "))
            self.delete(by_ref_number, by_disclouser_group)
        else:
            print("Invalid input, please take a look at the menu right above and pick the correct choice from it")
            self.request()
