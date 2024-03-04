class Playlist:
    """
    Represents a playlist with relevant information.
    """

    def __init__(self, playlist_id, name, creator, description=""):
        """
        Initialize a Playlist object with the provided information.

        :param playlist_id: The unique ID of the playlist.
        :param name: The name of the playlist.
        :param creator: The user who created the playlist.
        :param description: (Optional) A description or additional details about the playlist.
        """
        self.playlist_id = playlist_id
        self.name = name
        self.creator = creator
        self.description = description
        self.tracks = []

    def add_track(self, track):
        """
        Add a track to the playlist.

        :param track: The track to be added to the playlist.
        """
        self.tracks.append(track)

    def verify(self):
        """
        Print information about the playlist.
        """
        print(f"Playlist ID: {self.playlist_id}")
        print(f"Name: {self.name}")
        print(f"Creator: {self.creator}")
        print(f"Description: {self.description}")
        print("Tracks:")
        for index, track in enumerate(self.tracks, start=1):
            print(f"{index}. {track.name} - {track.source} ({track.length})")
