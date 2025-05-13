#routinely download videos from a specific playlist
from pytube import Playlist
import os
import dotenv
import yt_dlp
import time

while True:
    print("Starting process...")

    #load data from env
    print("Loading environment variables...")
    dotenv.load_dotenv("Playlist_Archive.env")
    PLAYLIST = os.getenv('PLAYLIST')
    DESTINATION = os.getenv('DESTINATION')

    if not os.path.isdir(DESTINATION):
        os.makedirs(DESTINATION)

    download_file = os.path.join(DESTINATION, 'Downloaded.dat')

    #build file dict
    videos = []
    if os.path.isfile(download_file):
        with open(download_file, "r") as f:
            for i in f:
                videos.append(i.strip())
    else:
        open(download_file, "x")

    #load yt_dlp
    options = {
        "forcetitle": True,
        "forceid": True,
        "forcefilename": True,
        "format": "mp4",
        "outtmpl": f"{DESTINATION}/%(uploader)s - %(title)s.mp4"
    }
    downloader = yt_dlp.YoutubeDL(options)

    print(f"Loading playlist {PLAYLIST}...")
    playlist = Playlist(PLAYLIST)

    #for some reason accessing playlist.videos randomly throws an error
    #but then the next time it will process fine
    #just adding this to stop the program from crashing
    try:
        print(f"{len(playlist.videos)} videos currently in playlist...")
    
        for i in playlist.videos:
            if i.video_id not in videos:
                print(f"Processing video {i.video_id}...")
                downloader.download(i.watch_url)

                print(f"Processing for video {i.video_id} complete.")
                
                #write download to download file
                with open(download_file, "a+") as f:
                    f.write(i.video_id)
                    f.write('\n')
            #else:
                #print(f"Video {i.video_id} already downloaded. Skipping...")

    except KeyError as e:
        print(f'Error on key {e}')

    print(f"Processing for playlist {PLAYLIST} complete.")
    print("Process complete.")
    print("Sleeping for 300 seconds...")
    time.sleep(300)






