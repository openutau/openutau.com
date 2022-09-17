## macOS error "This app is damaged ..."
Truth is the OpenUtau mac build is not codesigned by Apple, which is a paid service. As a result macOS treats the app as unsafe.

One way to solve it is open a terminal and run `xattr -rc /Applications/OpenUtau.app`.

## Voicebank doesn't show up in OpenUtau even if it's in the Singer folder
Make sure the voicebank includes a `character.txt` file with the line "name=(voicebank's name)".

## Why is there no sound when I hit Play?
1. Open Preferences and test the audio device.
2. Make sure the resampler selected in Preferences is compatible.
    1. Make sure your resamplers are not patched.
3. Make sure a singer is installed and selected.
4. Open up the Piano Roll window. If notes are semi-transparent, and phonemes, pitches, and expressions below don't show up, that means the lyrics do not work with the selected phonemizer and the voicebank.

## "Unable to load DLL 'worldline' or one of its dependencies" or "Dll was not found"
Install the [latest Visual C++ Redistributable](https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170)

## My CV Japanese voicebank doesn't work?
- Make sure that the OTO has aliases for every file.
- Make sure you write lyrics into notes that match the aliases. Use the built-in Hiragana/Romaji converters if necessary.
- Leave the phonemizer as "Default".
- OpenUtau will ignore filenames, because in most voicebanks each filename has multiple OTOs.

## Why doesn't VCV/CVVC/VCCV/etc. work?
- In the Utau world, the default way to use continuous sound voicebanks, like VCV or CVVC, is type the aliases as lyrics - basically hand picking samples from your voicebank and stringing them together as one note. That always works in OpenUtau by using the default CV phonemizer.
- There are specialized phonemizers to handle things like VCV/CVVC of a specific language, notably English Arpasing, Japanese VCV, and CVVC. These have a similar purpose as old Utau plugins like presamp or AutoCVVC. However, phonemizers work in a much better way: 1. They work in realtime when you are editing, and 2. They show you intuitive results in the phoneme view which you can freely adjust in the envelope area.
- However, don't expect anything work by default. OpenUtau will only implement a few phonemizers for example purposes, and even for those, some voicebanks will have non-standard quirks which will not work with the phonemizer.
- Other than the built-in phonemizers, the rest is left for the plugin developer community (see [API Doc](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/Api/README.md)).

## Singer installation / Share voicebanks with UTAU
OpenUtau aims to work on systems of all languages. Traditionally, this is very difficult - everything becomes mojibake (gibberish unicode text) on non-Japanese systems. The problem is two-fold:
1. Filename encoding in zip files.
2. Encoding of text files (oto.ini, etc).

Japanese voicebanks use 'shift_jis' encoding for both, but some languages like Chinese or Korean cannot be encoded in shift_jis.

The installer helps solve this problem by:
1. allowing you to preview and select encoding to extract filenames correctly.
2. allowing you to preview and select encoding of text files.

If your OS's system locale is set to Japanese, using the installer is not required. You can unzip yourself and share files with UTAU. You may need to change text encoding in Singers dialog.

If your OS's system locale is **not** set to Japanese, please use the installer to make sure the filenames are decoded correctly.

## Red pitch line goes everywhere.
- The UST or MIDI file may have a bad tempo set, like 50000.

## Is there a default voicebank/mascot? Can I provide a default voicebank/mascot?
- There is no default character, and no intention of creating a default character. Please do not offer one.

## Does OpenUtau require a separate wavtool or resampler?
OpenUtau comes with its own resampler and wavtools, but if you want to use ones meant for original UTAU they will work.