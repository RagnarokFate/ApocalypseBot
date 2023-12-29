class Course:
    """
    Represents a course with relevant information.
    """

    def __init__(self, name, id_number, tutor=None):
        """
        Initialize a Course object with the provided name and id_number.

        :param name: The name of the course.
        :param id_number: The unique ID number of the course.
        :param tutor: (Optional) The tutor or instructor of the course.
        """
        self.name = name
        self.id_number = id_number
        self.tutor = tutor

    def verify(self):
        """
        Print information about the course.
        """
        if self.tutor:
            print(f"Course: {self.name}, ID: {self.id_number}, Tutor: {self.tutor}")
        else:
            print(f"Course: {self.name}, ID: {self.id_number}")
