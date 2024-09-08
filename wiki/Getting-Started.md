## About OpenUtau
Please see [Tutorials](Tutorials) for an overview of OpenUtau and how it differs from conventional UTAU.

## Install OpenUtau
[![Download](https://img.shields.io/static/v1?style=for-the-badge&logo=github&label=download&message=windows-x64&labelColor=FF347C&color=4ea6ea)](https://github.com/stakira/OpenUtau/releases/latest/download/OpenUtau-win-x64.zip)</br>
[![Download](https://img.shields.io/static/v1?style=for-the-badge&logo=github&label=download&message=windows-x86&labelColor=FF347C&color=4ea6ea)](https://github.com/stakira/OpenUtau/releases/latest/download/OpenUtau-win-x86.zip)</br>
[![Download](https://img.shields.io/static/v1?style=for-the-badge&logo=github&label=download&message=macos-x64&labelColor=FF347C&color=4ea6ea)](https://github.com/stakira/OpenUtau/releases/latest/download/OpenUtau-osx-x64.dmg)</br>
[![Download](https://img.shields.io/static/v1?style=for-the-badge&logo=github&label=download&message=linux-x64&labelColor=FF347C&color=4ea6ea)](https://github.com/stakira/OpenUtau/releases/latest/download/OpenUtau-linux-x64.tar.gz)

### Windows
- OpenUtau only supports Windows 10 and above.
- After unzipping to a new folder, you can start the application by double-clicking `OpenUtau.exe`. Every time you start OU, it will check for updates first.
### macOS
- Double click the dmg file downloaded. Drag the app icon to the folder icon.
- See [FAQ](https://github.com/stakira/OpenUtau/wiki/FAQ#macos-error-this-app-is-damaged-) if macOS reports "app is damaged".
### Linux
#### Arch or similar (Eg. Manjaro)
- Install [openutau-bin](https://aur.archlinux.org/packages/openutau-bin) from AUR (Eg. using [yay](https://github.com/Jguer/yay) `yay -S openutau-bin`).
#### Gentoo
- Install `app-eselect/eselect-repository` in order to enable the guru overlay.
- Run `eselect repository enable guru` and `emaint sync -r guru` to enable and sync the overlay (`dev-vcs/git` may be needed to be installed).
- Run `emerge openutau` to install OpenUtau.
#### Other
- Extract the tar.gz file yourself, and run `OpenUtau` from a terminal.
- Or check the community-created [installer scripts](https://hitcoder.tubs.wtf/Posts/openutau/).

## Select UI language
By default, OpenUtau will use the same language as your computer, or English if a translation is unavailable. To manually change the language, go to **Tools > Preferences**.

![language](https://i.imgur.com/WDgg4Z6.gif)

## Install a resampler
OpenUtau provides an internal wavtool along with a resampler, **Worldline**. 


To install an external resampler, place a resampler .exe or .dll into the "Resamplers" folder where OpenUtau is installed. 

> [!TIP]
> On linux, the `Resamplers` folder is located at `~/.local/share/OpenUtau/Resamplers`.

If you already use UTAU, you can copy + paste resamplers that you already have. Check [Resamplers](Resamplers-and-Wavtools) for a list of compatible resamplers.

After adding a track, you can select the resampler and wavtool by pressing the settings cog on the lower right of the track header. Please note that only wavtools that are compatible with the currently selected resampler will be shown; for instance only "simple" and "convergence" will be available to choose when Worldline is selected.

## Install a voicebank
Voicebanks can be installed through **Tools > Install Singer...**

![install voicebank](https://i.imgur.com/FpIZ21J.png)

On non-Japanese systems, unzipping a zip file created on a Japanese system often leads to mojibake file names. The **Install Singer** tool helps convert file names correctly. You could also **unzip yourself** if the file names can be correctly unzipped.

When installing a voicebank, a window will pop up with a file encoding option. Use this option if you're not sure about how the voicebank is encoded (for example, a Japanese voicebank created by a Chinese user). You will know when the encoding is right.

![select file encoding](https://i.imgur.com/sSpDhPc.png)  

Another way to install singers is to set the **Additional Singer Path** to an existing folder with singers, such as the UTAU voice folder.

You can then see your installed voicebanks in the **Tools > Singers...** menu.

## Projects
### Creating projects
When you start OpenUtau, you have a new, blank project.  
You can also start a new project from **File > New**.

![new project](https://i.imgur.com/td8Imgw.png)

#### Tempo and Time Signature
Click on the tempo or time signature in the top left corner to edit it.

![tempo timesig](https://i.imgur.com/5ML7X13.gif)

Time signatures can have any positive whole number on top, and any power of 2 on the bottom.  
Tempos can be any number, including decimals.  

You can also change the tempo and time signature by right-clicking the bar/measure labels.

![tempo and timesig change](https://i.imgur.com/jxjnW1O.gif)

#### Expressions
Expressions allow you to change parameters note-by-note, similar to flags in UTAU. Expressions are saved per-project. To edit expression settings, go to **Tools > Expressions**.

![expressions](https://i.imgur.com/XxXvpLj.gif)

##### Default expressions
| Name     | Abbreviation | Purpose                                           | Range      | Default |
| -------- | ------------ | ------------------------------------------------- | ---------- | ------- |
| Velocity | VEL          | Consonant velocity (stretch/shorten preutterance) | 0 - 200    | 100     |
| Volume   | VOL          | Note volume                                       | 0 - 200    | 100     |
| Attack   | ATK          | Envelope starting volume                          | 0 - 200    | 100     |
| Decay    | DEC          | Envelope ending volume                            | 0 - 100    | 0       |
| Voice color    | CLR          | Utilizes voicebank appends/colors           | No range, options    | Blank       |
| Resampler engine    | ENG          | Change resamplers on the fly           | No range, options    | , worldline64.exe |
| Gender   | GEN          | g flag (formant shift)                            | -100 - 100 | 0       |
| Breath   | BRE          | B flag (breathiness)                              | 0 - 100    | 0       |
| Lowpass  | LPF          | H flag (low pass filter)                          | 0 - 100    | 0       |
| Modulation | MOD        | Note modulation from original pitch               | 0 - 100    | 0       |
| Alternate | ALT         | Alternate aliasing for duplicates in oto.ini      | 0 - 16     | 0       |
| Tone shift | SHFT       | Allows for selecting pitch alias                  | -36 - 36   | 0       |

##### Adding expressions
Use the + and - buttons in the lower left corner to add and remove expressions. Some expressions cannot be removed. There are two types of expressions, numerical expressions and fixed options.

For numerical expressions fill out the name, abbreviation, resampler flag, minimum, maximum, and default value. The resampler flag must be a single flag by itself without any numbers. If you want the whole project to have a certain value (eg. Mt+20) please put the number in the Default box.

![add expression](https://i.imgur.com/kzKnSgf.gif)

For options, fill out the name, abbreviation, checkbox, and option values. This is for flags that don't take any numbers, like for toggling between stretching and looping.

![add options](https://i.imgur.com/FyQ6XMd.gif)

### Opening projects
Open projects using **File > Open**, or `Ctrl+O`.  
You can open `.ustx`, `.ust`, or `.vsqx` files.

### Saving projects
OpenUtau projects are saved as `.ustx` files.  
Save the current project using **File > Save**, or `Ctrl+S`.  
Save the project as a new file using **File > Save As**.

After saving the project, you can also export all tracks as separate `.ust` files using **File > Export Project > Export Ust Files**. The files will be saved in an Export folder next to the original `.ustx` file. 

### Exporting audio
After saving the project, use **File > Export Audio > Export wav Files** to render all tracks as separate `.wav` files. The files will be saved in an Export folder next to the original `.ustx` file. 

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

### Batch Edits, Transformers and Legacy Plugins
These can be accessed via the text options along the top of the Piano Roll view.

![transformer](https://i.imgur.com/6XI0w5z.gif)

These are applied to the selected notes (or to the whole part if none are selected) at once.  
Lyric Transformers are used for simple 1-to-1 lyric conversions.

Legacy Plugins provide limited support for UTAU plugins. To add a plugin, copy the folder into the Plugins folder of OpenUtau. Not all plugins will function normally or completely. Some popular plugins (eg. VCV conversion, CVVC conversion) are handled by track phonemizers.

![legacy](https://i.imgur.com/70eNNC9.gif)

### Edit expressions
Use the arrow by the expressions to select which one you want to edit. 

![select expression](https://i.imgur.com/5gzG0ch.gif)

The gear icon will allow you to view the expression settings for the whole project.

![project expressions](https://i.imgur.com/ACjYqcS.gif)

Click to set a value, and right click to reset it to the project default.

![edit expression](https://i.imgur.com/2PKCb2p.gif)
#### VEL (velocity)
This corresponds to UTAU's Consonant Velocity. This affects the length of the fixed region of the OTO, which is the beginning of the note/phoneme.

![vel](https://i.imgur.com/ls2ECcq.gif)
#### VOL (volume)
This raises or lowers the overall volume of the note/phoneme.

![vol](https://i.imgur.com/11QKExP.gif)
#### ATK (attack)
This raises or lowers the volume of the beginning of the note/phoneme.

![atk](https://i.imgur.com/lw5wg26.gif)
#### DEC (decay)
This lowers the volume of the rest of the note/phoneme.

![dec](https://i.imgur.com/MNU1Bws.gif)

#### ENG (Resampler Engine)
Selects resampler engine used to render this phoneme. If value is "", the engine selected in Preferences is used.

![eng-setting](https://i.imgur.com/Fm2fZZ2.png)
![eng](https://i.imgur.com/BtgIg3u.gif)

#### MOD (modulation)
This determines how much the pitch is flattened from the original recording. By default this is 0, or completely flat.

#### Options Flags (Non-Numerical Flags)
Add a flag. Change its type to "Options" and set "Option Values" to ",e".
You will be able to use an expression to add nothing or "e" to resampler flags.

![flage-setting](https://i.imgur.com/7DEflzM.png)
![flage](https://i.imgur.com/Q6NUw93.gif)

#### Other expressions
All other expressions are like flags in UTAU.
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