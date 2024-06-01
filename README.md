# Youtube Archiver
This project is a simple python script to download all videos from a youtube playlist.

I have this project running on a local server continually, and an Archive playlist on youtube. Whenever I add a new video to the playlist, the program will download it the next time it runs. 

## Set Up
The requirements for running the script can be found in [Requirements.txt](Requirements.txt). The script relies on a Playlist_Archive.env file for the playlist URL and destination folder to store the videos in. An example for the .env file is included in the repository: [Playlist_Archive.env.example](Playlist_Archive.env.example).

The program can be run locally, or in a virtual python environment, but I have it running on docker. Included is a [Dockerfile](Dockerfile) for creating the docker container. With the docker file, the container can be created and started with the following commands:
```dockerfile
docker build . -t playlistarchiver
docker run --name PlaylistArchiver --mount type=bind,source="D:\Youtube Archive",target=/videos --restart always playlistarchiver
```
A bind mount is created to store the video files.
Keep in mind the paths in the commands above are for my personal set up, and would need to be changed.
