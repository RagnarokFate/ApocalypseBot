class Event:
    """
    Represents an event, such as a study session or gaming session, for students.
    """

    def __init__(self, event_id, subject, date, time, caption, pingable):
        """
        Initialize an Event object with the provided information.

        :param event_id: The unique ID of the event.
        :param subject: The subject or type of event (e.g., study session, gaming session).
        :param date: The date of the event.
        :param time: The time of the event.
        :param caption: A caption or additional details about the event.
        :param pingable: Whether the event will send a notification in time.
        """
        self.id = event_id
        self.subject = subject
        self.date = date
        self.time = time
        self.caption = caption
        self.pingable = pingable

    def verify(self):
        """
        Print information about the event.
        """
        print(f"The {self.subject} event is occurring at {self.time} on {self.date}.")
        print(f"It is necessary to follow: {self.caption}\n")

        if self.pingable:
            print("This event will ping you in time.")
        else:
            print("This event will **not** ping you in time.")
