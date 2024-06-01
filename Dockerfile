#docker build . -t playlistarchiver
#docker run --name PlaylistArchiver --mount type=bind,source="D:\Youtube Archive",target=/videos --restart always playlistarchiver

FROM python:3.11

COPY PlaylistArchiver.py .
COPY Playlist_Archive.env .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "-u", "./PlaylistArchiver.py"]