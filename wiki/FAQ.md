## Why is there no sound when I hit Play?
- Open Preferences and test the audio device.
- Make sure the resampler selected in Preferences is compatible. If your resamplers were patched, try unpatched ones.
- Make sure a singer is installed and selected.
- Open up the midi window. If notes are semi-transparent, and phonemes, pitches, and expressions below don't show up, the lyrics do not work with the selected phonemizer and the voicebank.

## Why extra voicebank installation step?
- Utau has a long history, carrying debts. Encoding is one of them. Remember all the gibberish?
- OpenUtau needs to convert encoding of voicebank files, and also the file paths, installing within the software is the easiest way.
- It also creates a opportunity for you to configure the voicebank, so that OpenUtau can understand it better and automate things.

## Why doesn't VCV/CVVC/VCCV/etc. work?
- In the Utau world, the default way to use continuous sound voicebanks, like VCV or CVVC, is type the aliases as lyrics. Basically hand picking samples. That always works in OpenUtau by using the default CV phonemizer.
- There are specialized phonemizers to handle things like VCV/CVVC of a specific language. Notably English Arpasing, Japanese VCV, and CVVC. These have a similar purpose as old Utau plugins like presamp or AutoCVVC. However, phonemizers work in a much better way than them: 1. It works in realtime when you are editing. 2. It shows you intuitive results in the phoneme view.
- However, don't expect anything work by default. OpenUtau will only implement a few phonemizers for example purposes, and even for those, some voicebanks will have non-standard quirks and don't work.
- Except the built-in phonemizers, the rest is left for the plugin developer community (see [API Doc](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/Api/README.md)).

## Red pitch line goes everywhere.
- The ust or midi file may have a bad tempo set, like 50000.

## Is there a default voicebank/mascot? Can I provide a default voicebank/mascot?
- There is no default character, and no intention of creating a default character. Please do not offer one.

## Does OpenUtau require a separate wavtool?
- OpenUtau uses its own internal wavtool. This helps it with handling resampler pre-rendering and multiple resampler threads.