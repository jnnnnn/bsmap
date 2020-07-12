import json

contents = {
    "_version": "1.0.0",
    "_BPMChanges": [],
    "_events": [],
    "_notes": [],
    "_obstacles": [],
    "_bookmarks": [],
}


def writeDifficulty(notes):
    with open("Expert.dat", "w") as f:
        json.dump({**contents, "_notes": notes}, f)

