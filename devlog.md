## 2020-07-12

Start project. Initial vision is a python gui app that shows a spectrum. Use librosa beat detection to automatically position notes (or at least the places where notes may appear). Use time-followed bsplines to create tracks for controllers and make sure levels are pitched correctly by measuring required bspline acceleration.

Considered writing as a blender plugin as that would give a lot of things for free:

- 3d environment
- python environment
- UI toolkit

Try without blender to start with.

First version will just do librosa beats and simple positioning of notes.

Future feature: prevent notes from blocking player's view by occlusion detection and deleting occluded notes (stretch -- recalculating splines)

Future feature: detect duplicate parts of songs and repeat the pattern for them.

Future feature: have high-energy and low-energy parts, where the player gets a rest in a lower-energy part of the song.

Future feature: detect short-term duplicates and repeat the previous pattern but horizontally (or vertically?) inverted.

Future feature: instead of splitting notes evenly between hands, swing focus left and right.

OK, start on first version. Following https://musicinformationretrieval.com/beat_tracking.html

Future feature: hpss to split percussion and melody between hands ?

Version 1 done. Writes out a map, librosa detected beats. Only goes for the first two minutes?