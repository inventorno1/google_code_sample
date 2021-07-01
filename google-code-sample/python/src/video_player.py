"""A video player class."""

from .video_library import VideoLibrary
import random # for play random
from .video_playlist import Playlist
import re # for searching strings

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._video_playing = None
        self._is_paused = False
        self._playlists = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all available videos:")

        #Creates list of videos formatted as strings and sorts them
        video_list = []
        for video in self._video_library.get_all_videos():
            video_list.append(str(video))

        for video_info in sorted(video_list):
            print(video_info)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        # Checks if video_id exists
        if self._video_library.get_video(video_id):

            if self._video_library.get_video(video_id).is_flagged:
                print(f"Cannot play video: Video is currently flagged (reason: {self._video_library.get_video(video_id).flag_reason})")

            else:
                # Checks if video is playing
                if self._video_playing:
                    print(f"Stopping video: {self._video_playing.title}")

                # Sets 'video playing' to the respective video
                self._video_playing = self._video_library.get_video(video_id)
                self._is_paused = False
                print(f"Playing video: {self._video_library.get_video(video_id).title}")
        else:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""

        # Checks if video is playing
        if self._video_playing:
            print(f"Stopping video: {self._video_playing.title}")
            self._video_playing = None
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""

        # Iterates through videos to select non-flagged ones
        non_flagged_videos = []
        for video in self._video_library.get_all_videos():
            if not video.is_flagged:
                non_flagged_videos.append(video.video_id)

        if non_flagged_videos:
            self.play_video(random.choice(non_flagged_videos))
        else:
            print("No videos available")

    def pause_video(self):
        """Pauses the current video."""

        #Checks if video is playing
        if self._video_playing:
            #Checks if video is paused
            if self._is_paused:
                print(f"Video already paused: {self._video_playing.title}")
            else:
                self._is_paused = True
                print(f"Pausing video: {self._video_playing.title}")
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""

        if self._video_playing:
            if self._is_paused:
                self._is_paused = False
                print(f"Continuing video: {self._video_playing.title}")
            else:
                print("Cannot continue video: Video is not paused")
        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""

        if self._video_playing:
            if self._is_paused:
                print(f"Currently playing: {self._video_playing} - PAUSED")
            else:
                print(f"Currently playing: {self._video_playing}")
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        if playlist_name.lower() in self._playlists:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self._playlists[playlist_name.lower()] = Playlist(playlist_name)
            print(f"Successfully created new playlist: {self._playlists[playlist_name.lower()].title}")
            # print(self._playlists[playlist_name.lower()].videos)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        if playlist_name.lower() in self._playlists:
            if self._video_library.get_video(video_id):
                if self._video_library.get_video(video_id).is_flagged:
                    print(f"Cannot add video to {playlist_name}: Video is currently flagged (reason: {self._video_library.get_video(video_id).flag_reason})")
                else:
                    if self._video_library.get_video(video_id) in self._playlists[playlist_name.lower()].videos:
                        print(f"Cannot add video to {playlist_name}: Video already added")
                    else:
                        self._playlists[playlist_name.lower()].videos.append(self._video_library.get_video(video_id))
                        print(f"Added video to {playlist_name}: {self._video_library.get_video(video_id).title}")
            else:
                print(f"Cannot add video to {playlist_name}: Video does not exist")
        else:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")

    def show_all_playlists(self):
        """Display all playlists."""

        if self._playlists:
            print("Showing all playlists:")
            for name in sorted(self._playlists.keys()):
                print(self._playlists[name].title)
        else:
            print("No playlists exist yet")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        if playlist_name.lower() in self._playlists:
            print(f"Showing playlist: {playlist_name}")
            if self._playlists[playlist_name.lower()].videos:
                for video in self._playlists[playlist_name.lower()].videos:
                    print(video)
            else:
                print("No videos here yet")
        else:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        if playlist_name.lower() in self._playlists:
            if self._video_library.get_video(video_id):
                if self._video_library.get_video(video_id) in self._playlists[playlist_name.lower()].videos:
                    self._playlists[playlist_name.lower()].videos.remove(self._video_library.get_video(video_id))
                    print(f"Removed video from {playlist_name}: {self._video_library.get_video(video_id).title}")
                else:
                    print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
            else:
                print(f"Cannot remove video from {playlist_name}: Video does not exist")
        else:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self._playlists:
            self._playlists[playlist_name.lower()].videos.clear()
            print(f"Successfully removed all videos from {playlist_name}")
        else:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self._playlists:
            del self._playlists[playlist_name.lower()]
            print(f"Deleted playlist: {playlist_name}")
        else:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """

        video_list = []
        for video in self._video_library.get_all_videos():
            if search_term.lower() in video.title.lower():
                if not video.is_flagged:
                    video_list.append(str(video))

        if video_list:
            print(f"Here are the results for {search_term}:")
            for i in range(len(video_list)):
                print(f"{i+1}) {sorted(video_list)[i]}")
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            answer = input()
            try:
                val = int(answer) - 1
                # print(val)
                if val < len(video_list) and val >=0:
                    id = re.search(r"\(([A-Za-z0-9_]+)\)", sorted(video_list)[val])
                    # print(sorted(video_list)[val])
                    # print(id.group(1))
                    self.play_video(id.group(1))
            except ValueError:
                pass
        else:
            print(f"No search results for {search_term}")



    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """

        video_list = []
        for video in self._video_library.get_all_videos():
            if video_tag.lower() in video.tags:
                if not video.is_flagged:
                    video_list.append(str(video))

        if video_list:
            print(f"Here are the results for {video_tag}:")
            for i in range(len(video_list)):
                print(f"{i+1}) {sorted(video_list)[i]}")
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            answer = input()
            try:
                val = int(answer) - 1
                # print(val)
                if val < len(video_list) and val >=0:
                    id = re.search(r"\(([A-Za-z0-9_]+)\)", sorted(video_list)[val])
                    # print(sorted(video_list)[val])
                    # print(id.group(1))
                    self.play_video(id.group(1))
            except ValueError:
                pass
        else:
            print(f"No search results for {video_tag}")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        if self._video_library.get_video(video_id):
            if self._video_library.get_video(video_id).is_flagged:
                print("Cannot flag video: Video is already flagged")
            else:
                if self._video_playing:
                    if self._video_playing.video_id == video_id.lower():
                        self.stop_video()
                self._video_library.get_video(video_id)._is_flagged = True
                if flag_reason:
                    self._video_library.get_video(video_id)._flag_reason = flag_reason
                else:
                    self._video_library.get_video(video_id)._flag_reason = "Not supplied"
                print(f"Successfully flagged video: {self._video_library.get_video(video_id).title} (reason: {self._video_library.get_video(video_id).flag_reason})")
        else:
            print("Cannot flag video: Video does not exist")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        if self._video_library.get_video(video_id):
            video = self._video_library.get_video(video_id)
            if video.is_flagged:
                video._is_flagged = False
                video._flag_reason = None
                print(f"Successfully removed flag from video: {video.title}")
            else:
                print("Cannot remove flag from video: Video is not flagged")
        else:
            print("Cannot remove flag from video: Video does not exist")
