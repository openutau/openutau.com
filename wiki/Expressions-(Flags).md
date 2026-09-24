# About expressions
In OpenUtau, parameters such as volume, velocity, Voice Color (append subbanks), modulation, and UTAU flags are collectively referred to as “expressions.”  
Additionally, there are expression types that allow drawing curves rather than applying them to individual notes.  
The available expressions vary depending on the renderer.

# Edit expressions
Use the arrow by the expressions to select which one you want to edit. 

![select expression](https://i.imgur.com/5gzG0ch.gif)

The gear icon will allow you to view the expression settings for the whole project.

![project expressions](https://i.imgur.com/ACjYqcS.gif)

Click to set a value, and right click to reset it to the project default.

![edit expression](https://i.imgur.com/2PKCb2p.gif)

# Default expressions
| Name     | Abbreviation | Purpose                                           | Range      | Default | Note |
| -------- | ------------ | ------------------------------------------------- | ---------- | ------- | ----- |
| Velocity | VEL          | Consonant velocity (stretch/shorten preutterance) | 0 - 200    | 100     | |
| Volume   | VOL          | Note volume                                       | 0 - 200    | 100     | |
| Attack   | ATK          | Envelope starting volume                          | 0 - 200    | 100     | |
| Decay    | DEC          | Envelope ending volume                            | 0 - 100    | 0       | |
| Voice color    | CLR          | Utilizes voicebank appends/colors           | No range, options    | Blank       | |
| Resampler engine    | ENG          | Change resamplers on the fly           | No range, options    | , worldline64.exe | |
| Gender   | GEN          | g flag (formant shift)                            | -100 - 100 | 0       | Currently unsupported in the default OpenUTAU renderers; You can use **GENC** instead |
| Gender(Curve)   | GENC          | g flag (formant shift) - Same with GEN, but uses curve                            | -100 - 100 | 0       | |
| Breath   | BRE          | B flag (breathiness)                              | 0 - 100    | 0       | Currently unsupported in the default OpenUTAU renderers; You can use **BREC** instead |
| Breath(Curve)   | BREC          | B flag (breathiness) - Same with BRE, but  uses curve                             | 0 - 100    | 0       | |
| Lowpass  | LPF          | H flag (low pass filter)                          | 0 - 100    | 0       | |
| Modulation | MOD        | Note modulation from original pitch               | 0 - 100    | 0       | |
| Alternate | ALT         | Alternate aliasing for duplicates in oto.ini      | 0 - 16     | 0       | |
| Tone shift | SHFT       | Allows for selecting pitch alias                  | -36 - 36   | 0       | |

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
Selects the resampler engine used to render a phoneme. When set to "", it falls back to the choice set in the project's default settings, unless individual track preferences are used.  
![eng-setting](https://i.imgur.com/Fm2fZZ2.png)  
You can have multiple resamplers loaded into your project properties as shown, selectable by a toggle menu.

![resampler-select](https://github.com/user-attachments/assets/7b6a345e-be5d-400c-85d3-e1e8509a4efe)  

To add more resamplers, write the filename into the options field after the first comma.  
Use the filename exactly as written: typing `moresampler, resampler` etc. will not work.

The example above is written like this:  
`,moresampler.exe,doppeltler64.exe,resampler.exe,straycat-rs.exe,TIPS.exe,tn_fnds.exe`  
If a resampler is in a subfolder, it needs to be called with the subfolder path:  
`,subfolder\resampler.exe`

#### MOD (modulation)
This determines how much the pitch is flattened from the original recording. By default this is 0, or completely flat.  
This is an obsolete feature and is not recommended for use.

#### MOD+ (modulation plus)
Reflect the original pitch of the voicebanks on the gray pitch line in the piano roll.  
Unlike MOD, it can also be used with VCV/CVCV.

#### Options Flags (Non-Numerical Flags)
Add a flag. Change its type to "Options" and set "Option Values" to ",e".
You will be able to use an expression to add nothing or "e" to resampler flags.

![flage-setting](https://i.imgur.com/7DEflzM.png)
![flage](https://i.imgur.com/Q6NUw93.gif)

#### Other expressions
All other expressions are like flags in UTAU.  
For the expressions and flags not described here, you can check the [[(English) UTAU Wiki's page|https://utau.fandom.com/wiki/Help:UTAU_User_Manual_-_7]], or [[(Japanese) UTAU Users' Mutual Aid Wiki's Page|https://w.atwiki.jp/utaou/pages/41.html]].

# Edit expressions lineup
Expressions are saved per-project. To edit expression settings, go to **Tools > Expressions**.

![expressions](https://i.imgur.com/XxXvpLj.gif)

### Adding expressions
Use the + and - buttons in the lower left corner to add and remove expressions. Some expressions cannot be removed. There are two types of expressions, numerical expressions and fixed options.

For numerical expressions fill out the name, abbreviation, resampler flag, minimum, maximum, and default value. The resampler flag must be a single flag by itself without any numbers. If you want the whole project to have a certain value (eg. Mt+20) please put the number in the Default box.

![add expression](https://i.imgur.com/kzKnSgf.gif)

For options, fill out the name, abbreviation, checkbox, and option values. This is for flags that don't take any numbers, like for toggling between stretching and looping.

![add options](https://i.imgur.com/FyQ6XMd.gif)
