import json

info = {
    "_version": "1.0.0",
    "_songName": "",
    "_songSubName": "",
    "_songAuthorName": "",
    "_levelAuthorName": "jnnnnn's generator 1.0",
    "_beatsPerMinute": 120,
    "_songTimeOffset": 0,
    "_shuffle": 0,
    "_shufflePeriod": 0.5,
    "_previewStartTime": 30,
    "_previewDuration": 10,
    "_songFilename": "song.ogg",
    "_coverImageFilename": "",
    "_environmentName": "NiceEnvironment",
    "_difficultyBeatmapSets": [
        {
            "_beatmapCharacteristicName": "Standard",
            "_difficultyBeatmaps": [
                {
                    "_difficulty": "Expert",
                    "_difficultyRank": 9,
                    "_beatmapFilename": "Expert.dat",
                    "_noteJumpMovementSpeed": 10,
                    "_noteJumpStartBeatOffset": 0,
                }
            ],
        }
    ],
}


def writeInfo(songauthortitle):
    author, name = songauthortitle.split(" - ")
    with open("info.dat", "w") as f:
        json.dump({**info, "_songName": name, "_songAuthorName": author}, f)
