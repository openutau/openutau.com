## About OpenUtau
Please see [Tutorials](Tutorials) for an overview of OpenUtau and how it differs from conventional UTAU.

## Install
For installing the OpenUtau Editor, voicebanks, and resampler, please see the [Install](Install) page.

## Projects
### Creating projects
When you start OpenUtau, you will see a blank start screen.

You can start by clicking the "New" on the Top Left and creating a blank project.

![new project](https://i.imgur.com/CO1whEG.png)

#### Tempo and Time Signature
Click on the tempo or time signature in the top left corner to edit it.

![tempo timesig](https://i.imgur.com/5ML7X13.gif)

Time signatures can have any positive whole number on top, and any power of 2 on the bottom.  
Tempos can be any number, including decimals.  

You can also add a tempo and time signature change by right-clicking the bar/measure labels.  

Unlike changing at the Top Left, which will change the tempo/time sign for the entire project,  
This method changes only the tempo/time sign from the point you have right-clicked. 

![tempo and timesig change](https://i.imgur.com/jxjnW1O.gif)

### Opening projects
Open projects using **File > Open**, or `Ctrl+O`.  
You can open the following formats.
- .ustx: OpenUtau project file
- .ust: UTAU project file
- .vsqx: VOCALOID3/4 project file
- .mid/.midi: General music score file
- [.ufdata](https://github.com/sdercolin/utaformatix-data): [UtaFormatix](https://sdercolin.github.io/utaformatix3/)'s internal data format. Compatible with most vocal synthesis project files.
- .musicxml: A universal music score file format for handling Western music staff notation as data.

### Saving projects
OpenUtau projects are saved as `.ustx` files.  
Save the current project using **File > Save**, or `Ctrl+S`.  
Save the project as a new file using **File > Save As**.

After saving the project, you can also export all tracks as separate `.ust` files using **File > Export Project > Export Ust Files**. The files will be saved in an Export folder next to the original `.ustx` file. 

#### Autosave Backups

OpenUtau automatically saves project backups every 30 seconds. It also automatically saves backups when it detects a crash.
For saved projects, backups are saved next to the file with the name “filename-autosave.ustx”.
For unsaved projects, backups are saved in the “Backups” folder within the data folder (located in places like the Singers or Resamplers folders).

If the program crashed or was force-closed previously, a project recovery dialog will appear upon the next startup, allowing you to restore the previous state.

### Exporting audio
After saving the project, use **File > Export Audio > Export wav Files** to render all tracks as separate `.wav` files.  
You can also save all of the tracks mixed to a single `.wav` file via **Mixdown To Wav File**.  

The files will be saved in an Export folder next to the original `.ustx` file. 

## Tracks
### Creating tracks
Click the **+** icon in the left panel to create a new track.

![create track](https://i.imgur.com/Fk69Epl.gif)

### Importing tracks
Imported tracks will be added to the current project under all of your existing tracks.

You can import tracks from `.ustx`, `.ust`, and `.vsqx` files using **File > Import Tracks**.  
You can import audio from `.wav`, `.mp3`, `.ogg`, and `.flac` files using **File > Import Audio**.  
You can import tracks MIDI using **File > Import MIDI**.

### Editing tracks
Select a singer from the menu in the track header.

![select singer](https://i.imgur.com/PIzAx6s.gif)

You can optionally select a phonemizer, which will automatically convert note lyrics into a form the voicebank can play. For more details, please check [Phonemizers](Phonemizers).

![phonemizer](https://i.imgur.com/wcMNzKy.gif)

The `M` in the right corner of the track header mutes the track, while the `S` solos the track. The settings cog in the lower right allows you to select a Resampler and Wavtool.

You are also able to click and drag the volume slider to adjust the volume of the track. Right click to reset this slider to +00.0.

![track volume and settings](https://i.imgur.com/MJY5vtJ.gif)

Click in the track area to create a new part. You can drag the part to move it around, drag the end to change the length, and right click to delete parts.

![edit part](https://i.imgur.com/aAFe6XU.gif)

The right click dialog also allows you to rename a part.

![rename part](https://i.imgur.com/NmStbDA.gif)

Double click on a part to open the note editor.

![open part](https://i.imgur.com/ZWOQ2Ss.gif)

### Navigation
Click on the bar/measure labels to move the playback cursor, and press space to start/stop playing.

![playback](https://i.imgur.com/jalr2JP.gif)

To scroll vertically, scroll normally.

![verti scroll](https://i.imgur.com/QegYsJX.gif)

To scroll horizontally, you can hold shift and scroll, or hover your cursor over the horizontal scroll bar and scroll.

![hori scroll](https://i.imgur.com/3UH3Kt6.gif)

To zoom horizontally, hover your cursor over the bar/measure labels and scroll.  
You can also use 'Ctrl + scroll' instead.

![hori zoom](https://i.imgur.com/yOTVNEi.gif)

To zoom vertically, hover your cursor over the vertical zoom icon and scroll.

![verti zoom](https://i.imgur.com/a8IE9W2.gif)

### Transcribe audio to notes
OpenUtau can autometically transcribe wave parts to note parts.

Before using, please download the model from [here](https://github.com/xunmengshe/OpenUtau/releases/download/0.0.0.0/some-0.0.1.oudep) and install it using "Tools → Install Dependency (.oudep)"

Right click on a wave part and click "Transcribe audio to create a note part". The transcription process takes about 1 minute.

The model is trained on clean solo vocal, so it works best on this kind of audio. It may not work well on music with instrumental or with heavy reverberation.

## Notes
Toggle tips using the question mark button or pressing `T` on the keyboard.

![tips](https://i.imgur.com/6qI2FBD.gif)

### Navigation
Scroll, zoom, and playback function the same way as the track editor.

### Basic note editing
There are two note creation modes:

`Pen Tool`
> Click to create notes, Right click to bring up an options menu. This is a good mode for tuning and intensive lyric editing due to the ease of access to batch editing tools.

`Pen Tool +`
> Click to create notes, and right click to delete notes. This is a good mode for composition and UST creation, due to its speed.

![create](https://i.imgur.com/BKKtoFA.gif)

Double click to start inputting lyric, tab to finish and switch to next note.

![lyric](https://i.imgur.com/pNeA8Ls.gif)

Drag notes to move them around. Drag the end to change the length. Hold Alt while adjusting length to resize the following note.

![resize](https://i.imgur.com/oIMv2n4.gif)

Hold Ctrl and click and drag to select multiple notes.

![select](https://i.imgur.com/arCrjjJ.gif)

Use the arrow keys to move selected notes up/down by 1 semitone, and Ctrl + arrow keys to move notes up/down by 1 octave.

![move up down](https://i.imgur.com/y5PFub7.gif)

By default, notes and lengths will snap to the nearest 16th note. To toggle snap, click on the snap icon in the top left, or press `P` on your keyboard.

![snap](https://i.imgur.com/1nIYvrt.gif)

#### Slur notes
To input slur note (a syllable that sings across multiple musical notes), input the word in the first note and input `+` in following notes.

![image](https://github.com/user-attachments/assets/609e5487-6dfc-4ff9-9c5a-b22a67d5140f)

For multisyllable languages such as English, use `+` to distribute a new syllable and use `+~` to extend the current syllable.

![image](https://github.com/user-attachments/assets/7537b521-66e6-4be7-a111-9c90e9d6bb99)

### Batch Edits, Transformers and Legacy Plugins
These can be accessed via the text options along the top of the Piano Roll view.

![transformer](https://i.imgur.com/6XI0w5z.gif)

These are applied to the selected notes (or to the whole part if none are selected) at once.  
Lyric Transformers are used for simple 1-to-1 lyric conversions.

Legacy Plugins provide limited support for UTAU plugins. To add a plugin, copy the folder into the Plugins folder of OpenUtau. Not all plugins will function normally or completely. Some popular plugins (eg. VCV conversion, CVVC conversion) are handled by track phonemizers.

![legacy](https://i.imgur.com/70eNNC9.gif)

### Edit expressions
Please see [Expressions (Flags)](Expressions-(Flags)).

### Edit pitchbends
You can show/hide pitchbends using the pitchbend icon in the top left, or by pressing `I` on your keyboard. Hidden pitchbends will still be applied to the notes.

![show hide pitchbends](https://i.imgur.com/atuJhyF.gif)

Click on the pitchbend to create new points. Drag the point to move it around.

![create pitchbend](https://i.imgur.com/pBvL2sD.gif)

Right click on the pitchbend to pick a shape.

![pitchbend shape](https://i.imgur.com/EuoimMj.gif)

Right click on a point for the option to delete it.

![delete pitchbend](https://i.imgur.com/d2gpswg.gif)
### Edit vibrato
You can show/hide vibrato using the vibrato icon in the top left, or by pressing `U` on your keyboard. Hidden vibrato will still be applied to notes.

![show hide vibrato](https://i.imgur.com/sf86vTG.gif)

Click on the vibrato icon below a note to toggle it on or off.

![toggle vibrato](https://i.imgur.com/hxwS8Wy.gif)

You can adjust the vibrato starting point, fade-in length, depth, fade-out length, frequency, and phase.

![edit vibrato](https://i.imgur.com/U1hsNem.gif)

### Edit phoneme envelopes
You can show/hide envelopes using the envelope icon in the top left, or by pressing `O` on your keyboard. Phonemization and envelope edits are applied even when hidden.

![show hide envelopes](https://i.imgur.com/4ugAXeW.gif)

Drag the pink lines to adjust the timing of phonemes within notes. Right click to reset the timing. You can right click and drag to reset multiple phonemes at once.

![envelope timing](https://i.imgur.com/0PDVaNx.gif)

Drag the bottom left corner to adjust the starting point of the envelope. Right click on the circle to reset.

![starting point](https://i.imgur.com/icQ8PUQ.gif)

Drag the top left corner to adjust the overlap amount. Right click on the circle to reset.

![overlap](https://i.imgur.com/reLOTps.gif)

## Beta version
OpenUtau provides two release channels: stable and beta. Sometimes you may want to use the beta version to try out new features, or because you encountered a bug in stable version. 

To switch to the beta version, go to "Tools → Preferences", turn on "Beta", and check for update.

If the method above doesn't work, you can also manually download the latest beta version from https://github.com/stakira/OpenUtau/releases