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

## Red pitch line goes everywhere.
- The ust or midi file may have a bad tempo set, like 50000.
