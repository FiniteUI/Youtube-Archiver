FROM python:3.11

COPY PlaylistArchiver.py .
COPY Playlist_Archive.env .
COPY Downloaded.dat .

#RUN mkdir /videos
RUN pip install pytube yt-dlp python-dotenv

CMD ["python", "./PlaylistArchiver.py"]