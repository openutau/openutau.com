## Install OpenUtau
[![Download](https://img.shields.io/static/v1?style=for-the-badge&logo=github&label=download&message=latest&labelColor=FF347C&color=4ea6ea)](https://github.com/stakira/OpenUtau/releases/download/OpenUtau-Latest/OpenUtau.zip)

Download the latest release from here. OpenUtau is currently Windows-only.  
After unzipping to a new folder, you can start the application by double clicking `OpenUtau.exe`. Every time you start OU, it will check for any updates.

## Install a resampler
Put a resampler exe or dll into the Resamplers folder. If you already use UTAU, you can copy + paste resamplers that you already have. Check [Resamplers](../Resamplers) for a list of compatible resamplers.

In OpenUtau, go to Tools > Preferences to select a resampler for preview and export. You can also adjust the number of pre-render threads to improve resampler performance.

![select resampler](https://imgur.com/eMcoHxp.gif)

There is no need to provide a wavtool, as OpenUtau uses its own internal wavtool.

## Install a voicebank
Voicebanks can be installed through Tools > Install Singer, or through Tools > Install Singer (Advanced).

![install voicebank](https://i.imgur.com/hLBaWWl.png)

Voicebanks must be compressed into a ZIP, RAR, 7z, or UAR file. When voicebanks are installed, the text will be converted to Unicode. If you have already unzipped voicebanks for use in UTAU, you cannot copy + paste them, because the files will still be encoded in Shift-JIS. You will need to compress the voicebank again and reinstall it for use in OpenUtau.

"Install Singer" assumes that the voicebank is originally in ASCII or Shift-JIS. For most voicebanks, this option will be enough.

"Install Singer (Advanced)" allows you to manually select the encoding for the filenames and the configurations. Use this option if you're not sure about how the voicebank is encoded (for example, a Japanese voicebank created by a Chinese user).  

![select file encoding](https://i.imgur.com/jCgde1s.png)  
![select text encoding](https://i.imgur.com/xuGkJht.png)

## Projects
### Creating projects
When you start OpenUtau you have a new, blank project.  
You can also start a new project from File > New.

![new project](https://i.imgur.com/td8Imgw.png)

#### Tempo and Time Signature
Click on the tempo or time signature in the top left corner to edit it.

![tempo timesig](https://i.imgur.com/5ML7X13.gif)

Time signatures can have any positive whole number on top, and any power of 2 on the bottom.  
Tempos can be any number, including decimals.  
Changing the tempo or time signature mid-project is not supported yet.

#### Expressions
Expressions allow you to change parameters note-by-note, similar to flags in UTAU. Expressions are saved per-project. To edit expression settings, go to Tools > Expressions.

![expressions](https://i.imgur.com/XxXvpLj.gif)

##### Default expressions
| Name     | Abbreviation | Purpose                                           | Range      | Default |
| -------- | ------------ | ------------------------------------------------- | ---------- | ------- |
| Velocity | VEL          | Consonant velocity (stretch/shorten preutterance) | 0 - 200    | 100     |
| Volume   | VOL          | Note volume                                       | 0 - 200    | 100     |
| Accent   | ACC          | Envelope starting volume                          | 0 - 200    | 100     |
| Decay    | DEC          | Envelope ending volume                            | 0 - 100    | 0       |
| Gender   | GEN          | g flag (formant shift)                            | -100 - 100 | 0       |
| Breath   | BRE          | B flag (breathiness)                              | 0 - 100    | 0       |
| Lowpass  | LPF          | H flag (low pass filter)                          | 0 - 100    | 0       |

##### Adding expressions
Use the + and - buttons in the lower left corner to add and remove expressions. Some expressions cannot be removed.  
Fill out the name, abbreviation, resampler flag, minimum, maximum, and default value. The resampler flag must be a single flag by itself without any numbers. If you want the whole project to have a certain value (eg. Mt+20) please put the number in the Default box.

![add expression](https://i.imgur.com/vUMtfK6.gif)

### Opening projects
Open projects using File > Open, or Ctrl+O.  
You can open `.ustx`, `.ust`, or `.vsqx` files.

### Saving projects
OpenUtau projects are saved as `.ustx` files.  
Save the current project using File > Save, or Ctrl+S.  
Save the project as a new file using File > Save As.

After saving the project, you can also export all tracks as separate `.ust` files using File > Save As Ust Files. The files will be saved in the same folder as the original `.ustx` file.

## Tracks
### Creating tracks
### Importing tracks
### Editing tracks
## Create and edit notes
(to do)