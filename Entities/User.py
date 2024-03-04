class User:
    """
    Represents a Discord user with additional attributes.
    """

    def __init__(self, name, id_number):
        """
        Initialize a User object with the provided name and id_number.

        :param name: The name of the user.
        :param id_number: The unique ID number of the user.
        """
        self.name = name
        self.id_number = id_number
        self.status = "default"
        self.is_premium = False

    def verify(self):
        """
        Verify and print user information.

        This method will be overridden by subclasses.
        """
        print(f"{self.name} with ID {self.id_number} is a default Discord user.")
        pass  # This method will be overridden by subclasses
