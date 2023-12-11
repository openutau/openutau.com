## Troubleshooting
### My voicebank doesn't show up in OpenUtau, even though it's in the Singers folder!
Make sure the voicebank folder includes a `character.txt` file. Inside the file, write `name=(voicebank's name)`.

### Why is there no sound when I play a project?
1. Open the Preferences menu from Tools > Preferences. Press the "Test" button below the "Playback Device" dropdown list.  
If you hear a tone, your audio device is working correctly.  
If you don't hear a tone, choose a different device in the "Playback Device" list and press "Test" again.
2. Make sure you have selected a singer for the track on the left side of the editor window.  
If your track has no singer selected, it will not make sound.
3. Make sure the resampler is compatible with OpenUtau.  
If the track is set to the "Classic" renderer, check the selected resampler of the track in the Engine menu (gray gear icon).  
Select a compatible resampler in the "Resampler" dropdown list. Select a compatible wavtool in the "Wavtool" dropdown list.  
The "worldline" resampler and the "convergence" and "simple" wavtools are built into OpenUtau, and should work on all platforms.
4. Double click on a track part to open the Piano Roll window. None of the notes should be semi-transparent. Phonemes, pitches, and expressions should appear below the notes.  
If your notes do not appear this way, this means that the lyrics in the notes do not work with the selected singer or the selected phonemizer.  
Try selecting a compatible singer or phonemizer.  
5. Make sure at least one track is not muted.  
If the "M" button is highlighted on a track, it is muted. Press the "M" button to unmute the track.

### My CV Japanese voicebank doesn't work!
1. Make sure that the `oto.ini` file has an alias for every sound file in the bank.
2. Make sure all lyrics match an alias in the `oto.ini` file. If necessary, use the built-in Hiragana/Romaji converters to correct the lyrics.
3. Make sure the phonemizer is set to "Default".
4. If an alias exists for a sound file in the voicebank, OpenUtau will only use the alias.
OpenUtau will fall back to reading filenames if an alias is missing, but by default, it will only select the aliases in the `oto.ini`.  

### How do I select an external resampler? [Moresampler, macres, TIPS, etc.] is not in the renderer list.
Resamplers are selected in the Engine menu of the track. WORLDLINE-R is a special renderer, and it cannot use external resamplers.  
Select the "Classic" renderer for the track, then click on the gray gear icon to select the resampler and the wavtool for that track.

### The pitch line is acting strange in my project!
If the project was imported from a UST or MIDI file, the tempo of the imported file may be set incorrectly. Commonly, files will be erroneously set to high BPM values, such as 50000.  
Set the project BPM to the correct value in the main editor window.

### OpenUtau crashes when I try to open the Preferences menu!
In the folder where OpenUtau is installed, find the `prefs.json` file.  
Open the file in a text editor. Find and remove the line `"language": "axaml"`. Save the file.  

This is a known bug when updating OpenUtau from version 0.1.90. See the [Release Notes](https://github.com/stakira/OpenUtau/wiki/Release-Notes#0191-05-15-2023) page for more details.

### On Windows, it says "Unable to load DLL 'worldline' or one of its dependencies" or "DLL was not found".
Install the [latest Visual C++ Redistributable](https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170).

### I get the worldline.dll error "There is no application set to open the document [...]" when trying to switch to the worldline resampler mid-project.
The worldline resampler only works when either "convergence or "simple" are selected as the wavtool. This is also the case when switching resamplers mid-project. Change the wavtool to either of these options and the error should go away.

### On macOS, when I try to run OpenUtau, it says "This app is damaged".
Apple requires developers to "sign" their apps in order to be trusted software. Having Apple sign an app costs money, and is not necessary for this project. As a result, Apple and macOS treats OpenUtau as "unsafe".  
To run OpenUtau on macOS, the app must be "trusted" to run on your Mac.  
Open a terminal and run `xattr -rc /Applications/OpenUtau.app`. Try opening OpenUtau again.

### I still can't solve my problem
You can send a feedback through [Discord](https://discord.gg/UfpMnqMmEM) or [GitHub Issue](https://github.com/stakira/OpenUtau/issues/new/choose). When sending feedbacks, please explain how to reproduce your bug, and provide your `.ustx` project, OpenUtau log file and full screenshots of your OpenUtau window.

Use `Win+Shift+S` to take a screenshot on Windows. Use `Shift+Command+3` to take a screenshot on MacOS

Use "Help > Open Logs Location" to find your OpenUtau log file.
![image](https://github.com/stakira/OpenUtau/assets/54425948/c4c19dc1-aed4-4fa3-a047-5d82fd3dbf20)

## Design and history
### How does VCV/CVVC/VCCV/etc. work?
- VCV and CVVC voicebanks, also known as "continuous sound" or 連続音 (*renzokuon*), use natural transitions between notes to smoothly blend sounds together during rendering. The standard method to organize these sounds is to directly type sound aliases from the `oto.ini` file into notes. Effectively, this is like hand-picking samples from the voicebank and connecting them together manually.  
If this style is preferred, it can be utilized via the "Default" phonemizer in OpenUtau.
- OpenUtau offers special phonemizers for many languages to handle aliases from VCV or CVVC banks automatically. Phonemizers emulate old UTAU plugins, such as presamp or AutoCVVC, with different advantages:  
    1. Phonemizers operate in realtime while editing lyrics.
    2. Results from phonemizers are displayed intuitively in the envelope editor below the notes.  
    3. In the envelope editor, the timing of the sound can be easily adjusted.  
- Not all voicebanks will play nicely with OpenUtau. Some banks have specific quirks that the phonemizer cannot use, and OpenUtau does not support every type of voicebank in every language.
- OpenUtau relies on the plugin developer community to create phonemizers for unsupported voicebanks.  
If you wish to help make a new phonemizer, take a look at the [OpenUtau plugin API documentation](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/Api/README.md).

### Singer installation / Sharing voicebanks with UTAU
OpenUtau aims to work on systems of all languages. Traditionally, this is very difficult. Japanese text can become unreadable mojibake (gibberish Unicode) on non-Japanese systems.  
We face two main problems:
1. Filename encoding in zip files.
2. Encoding of text inside files (`oto.ini`, etc).

Japanese voicebanks traditionally use `shift_jis` encoding for filenames and text, but some languages like Chinese or Korean cannot be encoded in `shift_jis`.

The voicebank installer in OpenUtau helps to solve this problem: filenames and text files can be previewed during installation to ensure that the correct encoding is selected.

If your computer's system locale is set to Japanese, using the installer is not required. The zip archive can be unzipped, and OpenUtau can share files with UTAU. The text encoding may need to be changed in the Singers dialog.

If your computer's system locale is **not** set to Japanese, please use the installer to make sure the filenames and text files are decoded correctly.

### Does OpenUtau require a separate wavtool or resampler?
OpenUtau includes a default resampler and two wavtools by default. The included resampler and wavtools should work on any platform.  
In addition, the WORLDLINE-R renderer acts as its own resampler and wavtool, and allows for use of exclusive, special features that do not work with classic resamplers.  
OpenUtau intends to maintain compatibility with standard UTAU resamplers and wavtools. However, compatibility cannot be guaranteed.

## Future plans
### Is there a default voicebank/mascot? Can I provide one?
OpenUtau does not offer a default voicebank or mascot, and we do not have any intention of creating a voicebank or mascot for our project.  
Fans may feel free to make voicebanks or mascots inspired by OpenUtau, but we will not accept any offers for a default voicebank/mascot.

## NNSVS / ENUNU related FAQ
See the [Status of ENUNU NNSVS Support](https://github.com/stakira/OpenUtau/wiki/Status-of-ENUNU-NNSVS-Support#faq) page for more info on using NNSVS/ENUNU in OpenUtau.
