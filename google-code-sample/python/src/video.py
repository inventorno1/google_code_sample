"""A video class."""

from typing import Sequence


class Video:
    """A class used to represent a Video."""

    def __init__(self, video_title: str, video_id: str, video_tags: Sequence[str]):
        """Video constructor."""
        self._title = video_title
        self._video_id = video_id

        # Turn the tags into a tuple here so it's unmodifiable,
        # in case the caller changes the 'video_tags' they passed to us
        self._tags = tuple(video_tags)
        self._is_flagged = False
        self._flag_reason = None

    @property
    def title(self) -> str:
        """Returns the title of a video."""
        return self._title

    @property
    def video_id(self) -> str:
        """Returns the video id of a video."""
        return self._video_id

    @property
    def tags(self) -> Sequence[str]:
        """Returns the list of tags of a video."""
        return self._tags

    @property
    def is_flagged(self) -> bool:
        """Returns the flagged state of a video."""
        return self._is_flagged

    @property
    def flag_reason(self) -> str:
        """Returns the flag reason of a video."""
        return self._flag_reason

    def __str__(self):
        # Re format tags into desired string format
        taglist = " ".join([str(item) for item in self.tags])

        temp = f"{self.title} ({self.video_id}) [{taglist}]"
        if self.is_flagged:
            temp += f" - FLAGGED (reason: {self.flag_reason})"
        return temp
