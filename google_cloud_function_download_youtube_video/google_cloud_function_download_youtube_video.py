from pytube import YouTube
import os
from urllib.parse import urlparse, parse_qs
from google.cloud import storage
from moviepy.editor import VideoFileClip


# Rename this with the google cloud bucket name you have created
gcloud_bucket_name = "original_audio_video"
storage_client = storage.Client()
bucket = storage_client.get_bucket(gcloud_bucket_name)

def file_exists(filepath):
  fname = filepath.split('/')[-1]
  val = bucket.get_blob(fname)
  if val is not None:
      return True
  else:
      return False

def get_id(url):
    u_pars = urlparse(url)
    quer_v = parse_qs(u_pars.query).get('v')
    if quer_v:
        return quer_v[0]
    pth = u_pars.path.split('/')
    if pth:
        return pth[-1]



def upload_blob( source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))


def download_url(youtube_url, id):
    yt = YouTube(youtube_url)
    path = '/tmp/'
    yt.streams.first().download(output_path=path, filename=id)
    return path + id + '.mp4'


def download_video(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """

    print("request_args ", request.args)
    print("request_data ", request.data)
    print("request_form ", request.form)
    values = request.form
    url = values['url']
    print("url: ", url)
    id = get_id(url)
    print("id ", id)
    video_filename = '/tmp/' + id + '.mp4'
    audio_file_name = video_filename.replace(".mp4", ".wav")

    if file_exists(video_filename) and file_exists(audio_file_name):
        print ("Audio and Video files exist")
        return
    else:
        print("Audio and Video files donot exist")
        video_filename = download_url(url, id)

        if os.path.isfile(video_filename):
            print(video_filename, " exists")
        else:
            print(video_filename, " doesn't exists")

        videoclip = VideoFileClip(video_filename)
        videoclip.audio.write_audiofile(audio_file_name, ffmpeg_params=['-ac', '1'])

        upload_blob( video_filename, video_filename.split('/')[-1])
        upload_blob( audio_file_name, audio_file_name.split('/')[-1])
        return
