## Why is there no sound when I hit Play?
1. Open Preferences and test the audio device.
2. Make sure the resampler selected in Preferences is compatible.
    1. Make sure your resamplers are not patched.
3. Make sure a singer is installed and selected.
4. Open up the midi window. If notes are semi-transparent, and phonemes, pitches, and expressions below don't show up, the lyrics do not work with the selected phonemizer and the voicebank.

## It's so laggy!
This typically happens when you set render thread high with already multithreaded resamplers, like moresampler. In that case 8 moresamplers easily overloads your computer and push CPU usage to 100%. Please lower the thread count setting in OpenUtau.

## Singer installation / Share voicebanks with UTAU
OpenUtau aims to work on systems of all languages. Traditionally this is very difficult. Everything becomes mojibake on non-Japanese systems. The problem is two-fold:
1. Filename encoding in zip files.
2. Encoding of text files (oto.ini, etc).

Japanese voicebanks use shift_jis for both, but some languages like Chinese or Korean cannot be encoded in shift_jis.

The installer helps by:
1. allowing you to preview and select encoding to extract filenames correctly.
2. allowing you to preview and select encoding of text files.

If your Windows is set to Japanese, using the installer is not required. You can unzip yourself and share files with UTAU. You may need to change text encoding in Singers dialog.

If your Windows is not set to Japanese, please use the installer to make sure filenames are decoded correctly.

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