import os, subprocess, zipfile

import librosa

from filedifficulty import writeDifficulty
from fileinfo import writeInfo

songfile = "/home/jnewnham/Downloads/Smash Mouth - All Star.mp3"
samples, samplerate = librosa.load(songfile)

tempo, beat_times = librosa.beat.beat_track(
    samples, sr=samplerate, start_bpm=120, units="time"
)

# delete any beats earlier than the first three seconds
beat_times = [b for b in beat_times if b > 3]

# convert beat times to notes
def make_note(time: float):
    return {
        "_time": time,
        "_lineIndex": 0,
        "_lineLayer": 0,
        "_type": 0,
        "_cutDirection": 8,
    }


notes = [make_note(time) for time in beat_times]

# write out song
songfilename = os.path.splitext(os.path.basename(songfile))[0]
if not os.path.exists("songs"):
    os.mkdir("songs")
if not os.path.exists("zips"):
    os.mkdir("zips")
os.chdir("songs")
if not os.path.exists(songfilename):
    os.mkdir(songfilename)
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-i",
            songfile,
            "-c:a",
            "libvorbis",
            "-q:a",
            "4",
            songfilename + "/song.ogg",
        ]
    )
os.chdir(songfilename)
writeDifficulty(notes)
writeInfo(songfilename)

with zipfile.ZipFile(
    os.path.join("..", "..", "zips", songfilename + ".zip"), "w", zipfile.ZIP_DEFLATED
) as zipf:
    for root, dirs, files in os.walk("."):
        for fname in files:
            zipf.write(os.path.join(root, fname))
