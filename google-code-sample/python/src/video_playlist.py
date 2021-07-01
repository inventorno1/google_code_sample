"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, playlist_title):
        """Playlist constructor"""
        self._title = playlist_title
        self._videos = []

    @property
    def title(self) -> str:
        """Returns the title of a playlist."""
        return self._title

    @property
    def videos(self) -> list:
        """Returns the list of videos of a playlist."""
        return self._videos

    def __str__(self):
        return playlist_title
