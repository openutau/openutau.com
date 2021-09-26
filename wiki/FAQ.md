## Why no sound?
- Open Preferences and test the audio device.
- Make sure resampler selected in Preferences is compatible. If your resamplers were patched, try unpatched ones.
- Make sure a singer is installed and selected.
- Open up midi window. If notes are semi transparent, and phonemes pitches, and expressions below don't show up, the lyrics does not work with the selected phonemizer and the voicebank.

## Why the voicebank doesn't show up?
- OpenUtau relies on character.txt to detect voicebanks.
- Create a character.txt in the voicebank folder and put a line "name=<name>" in it.

## Why extra step for voicebank install?
- Utau has a long history, carrying debts. Encoding is one of them. Remember all the gibberish?
- OpenUtau need to convert encoding of voicebank file, install is the easiest way.
- It also creates a opportunity for you to config the voicebank, so that OpenUtau can understand better and automate things.

## Why VCV/CVVC/VCCV/etc does not work?
- In Utau world, the default way to use continuous sound voicebanks, like VCV or CVVC, is type the aliases as lyric. Basically hand picking samples. That always work in OpenUtau using the default CV phonemizer.
- There are specialized phonemizers to handle things like VCV/CVVC of a specific language. Currently notably English Arpasing, Japanese VCV and CVVC. These has similar purpose as old Utau plugins like presamp or AutoCVVC. However, phonemizers works in a much better way than them: 1. it works at realtime when you are editing. 2. it shouls you intuitive results in the phoneme view.
- However, don't expect anything work by default. OpenUtau will only implement a few phonemizers for example purpose, and even for those, some voicebanks will have non-standard quirks and don't work.
- Except the builtin phonemizers, the rest is left for the plugin developer community (see [API Doc](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/Api/README.md)).

## Red pitch line goes everywhere.
- The ust or midi file may have a bad tempo set, like 50000.
