from Entities import User

class Admin(User):
    """
    Represents an admin with extended privileges.

    Inherits from the User class.
    """

    def __init__(self, admin_name, admin_id):
        """
        Initialize an Admin object with the provided admin_name and admin_id.

        :param admin_name: The name of the admin.
        :param admin_id: The unique ID number of the admin.
        """
        super().__init__(admin_name, admin_id)
        self.status = "Admin"

    def verify(self):
        """
        Verify and print admin information.
        """
        print(f"{self.name} with ID {self.id_number} is an admin of the bot (RagnarokFate).")
