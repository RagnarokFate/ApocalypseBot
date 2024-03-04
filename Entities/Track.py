class Track:
    """
    Represents a music track with relevant information.
    """

    def __init__(self, track_id, name, source, length, status, user_name):
        """
        Initialize a Track object with the provided information.

        :param track_id: The unique ID of the track.
        :param name: The name of the track.
        :param source: The source of the track (e.g., album, artist).
        :param length: The duration of the track.
        :param status: The status of the track (e.g., playing, waiting).
        :param user_name: The name of the user associated with the track.
        """
        self.id = track_id
        self.name = name
        self.source = source
        self.length = length
        self.status = status
        self.user_name = user_name

    def verify(self):
        """
        Print information about the track.
        """
        print(f"The song '{self.name}' has a total duration of {self.length} via '{self.source}'.\n")
        if self.status == "playing":
            print("It's currently playing!")
        else:
            print("It's on waiting.")
