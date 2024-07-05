#docker build --no-cache . -t playlistarchiver-image
#docker run --name PlaylistArchiver --mount type=bind,source="D:\Youtube Archive",target=/videos --restart always playlistarchiver-image

FROM python:3.11-slim

COPY PlaylistArchiver.py .
COPY Playlist_Archive.env .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "-u", "./PlaylistArchiver.py"]