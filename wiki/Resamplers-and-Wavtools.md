# Installing Resamplers
##  Windows

Resampler must be an executable (`.exe`). Resamplers can be placed in subfolders inside the `Resamplers` folder.
1. In the OpenUtau folder, locate the resampler folder named `Resamplers`.
2. Open the resampler folder and place the resampler in the folder.

In OpenUtau version 0.1.119 or higher, resamplers can be installed by dragging and dropping the `.exe` file onto the main OpenUtau window and selecting "Install as resampler".

<img src="https://github.com/stakira/OpenUtau/assets/18076904/1a13d37d-b472-451d-b24a-e984b095bd4a" height="250">


## macOS

As of macOS 11.6, the below method works.

1. Install [homebrew](https://brew.sh/)
2. Install [wine32on64](https://github.com/Gcenx/homebrew-wine) using following commands:
```
brew tap gcenx/wine
brew install --cask --no-quarantine wine-crossover
```
3. Download "mac_additional.zip" from the [release page](https://github.com/stakira/OpenUtau/releases/tag/OpenUtau-Latest).
4. Use the `moresampler.sh` script inside the `mac_additional.zip` to wrap the resampler: Replace `moresampler-0.8.4/moresampler.exe` with the filename of the resampler.

This script will need to be added to the `Resamplers` folder and edited for every `.exe` resampler that is added.

## Linux

For wrapping Windows resamplers into Linux, use this method:

1. Install [Wine](https://www.winehq.org/)
2. Open the `Resamplers` folder (should be on /home/your_username/OpenUtau/Resamplers/)
3. Create a new text file with the name of your resampler (no file extension required). 
4. Open the text file and add this script.
```
#!/bin/bash
LANG="ja_JP.UTF8" wine "/absolute/path/to/your/resampler.exe" "${@,-1}"
```
5. Change `"/absolute/path/to/your/resampler.exe"` to the filename of the resampler.
6. Restart OpenUtau.

# Tested Resamplers and Directories
This is a list of all UTAU resamplers tested with OpenUtau.

|  Resampler |  Author  |  Additional Notes |
| ------------ | ------------ | ------------ |
|  worldline  | StAkira  |   Built into OpenUtau. Works on all platforms. |
|  [bkh01.exe](http://z-server.game.coocan.jp/utau/utautop.html#bkh01) |  Zteer |   |
|  [doppeltler32.exe](http://utau2008.xrea.jp/2020/engine/) | Ameya  |   |
|  [doppeltler64.exe](http://utau2008.xrea.jp/2020/engine/) | Ameya |   |
| [EFB-GT.exe](http://custom-made.seesaa.net/article/312529786.html) | Custom.Maid | |
| EFB-PB.exe | Custom.maid | |
|  [f2resamp32.exe](http://utau2008.xrea.jp/2020/engine/f2resamp004.zip) | Ameya |   |
|  [f2resamp64.exe](http://utau2008.xrea.jp/2020/engine/f2resamp004.zip) | Ameya  |   |
|  [fresamp11.exe](http://utau2008.xrea.jp/downloads/fresamp011.zip) | Ameya  |   |
|  fresamp12.exe | Ameya |   |
|  [fresamp14.exe](http://utau2008.xrea.jp/downloads/fresamp014.zip) | Ameya   |   |
| [fresamp14omp.exe](http://utau2008.xrea.jp/downloads/fresamp014omp.zip)  | Ameya | Ported to OpenMP with faster rendering speed than fresamp14.exe. |
| [lessampler.exe](https://github.com/YuzukiTsuru/lessampler/releases/) | YuzukiTsuru | [See additonal notes.](https://github.com/stakira/OpenUtau/wiki/Resamplers-and-Wavtools#compatible-with-adjustments) |
| [macres.exe](https://github.com/titinko/macres/releases)   | titinko   |   |
| model4.exe  | Ameya  |   |
| [moresampler.exe](https://bowlroll.net/file/139123) |  Kanru Hua |  [See adjustments for compatibility.](https://github.com/stakira/OpenUtau/wiki/Resamplers-and-Wavtools#compatible-with-adjustments) |
| [phavoco.exe](http://utau2008.xrea.jp/downloads/phavoco010.zip) | Ameya   |   |
| [phaavoco.exe](http://utau2008.xrea.jp/2020/engine/phaavoco001.zip) | Ameya |   |
| resampler.exe  | Ameya  | UTAU built-in resampler.  |
| [SpaceWorld_win64.exe](https://github.com/LovelyA72/SpaceWorld/releases) | LovelyA72 | [See adjustments for compatibility.](https://github.com/stakira/OpenUtau/wiki/Resamplers-and-Wavtools#compatible-with-adjustments) |
|[StrayCatRunner.exe](https://github.com/Astel123457/straycat-server) | Astel123457 |   |
|[StrayCat.py](https://github.com/UtaUtaUtau/straycat) | UtaUtaUtau |   |
| [TIPS.exe](http://scientistb.web.fc2.com/program/)  | ScientistB |   |
| [tn_fnds.exe](http://z-server.game.coocan.jp/utau/utautop.html#tn_fnds) | Zteer |  |
| [UDB](https://github.com/YuzukiTsuru/UDB/releases/tag/0.0.3.1) | YuzukiTsuru | UDB means UTAU Debug Engine.|
| [vs4u.exe](http://ackiesound.ifdef.jp/download.html#vs4u) | AckieSound |  |
| [w4u.exe](http://utau2008.xrea.jp/downloads/w4u001.zip) | Zany |   |
| [WARP.exe](http://custom-made.seesaa.net/article/312530509.html) | Custom.Maid | |
| [wn4u.exe](https://utaforum.net/threads/world4utau-update.20035/) | Zany | [See adjustments for compatibility.](https://github.com/stakira/OpenUtau/wiki/Resamplers-and-Wavtools#compatible-with-adjustments) |
| [young3.exe](https://bowlroll.net/file/203018) | Zany |   |

## Compatible with adjustments

- [moresampler.exe](https://bowlroll.net/file/139123)
  - Add `moresampler.exe` and the default `moreconfig.txt` to the `Resamplers` folder.
  - Add `moresampler.exe` to `Wavtools` folder without `moreconfig.txt`.
  - Moresampler should now function as either resampler only, or as both wavtool and resampler.
- [[SpaceWorld_win64.exe|https://github.com/LovelyA72/SpaceWorld/releases]] and [[wn4u.exe|https://utaforum.net/threads/world4utau-update.20035/]]
    - May experience issues if the voicebank is missing any frq files. SpaceWorld version 1.0.1 will not crash in the event of a missing frq file.
- [[lessampler|https://github.com/YuzukiTsuru/lessampler/releases/]]
    - In development, lack of flag support
    - Oversized Audio Model Attention

# Resampler Manifest
A resampler manifest is a YAML file used to store the expressions supported by a resampler. With resampler manifests, users can add all of a resampler's supported flags at once using the `Add all expressions suggested by renderers` button in the `Expressions` editor.

<img width="453" alt="image" src="https://user-images.githubusercontent.com/54425948/227085816-4cced732-98dd-4c76-bc40-9a94f971a066.png">

Resampler manifests should have the same name as the resampler executable, stored in the same folder. The manifest must have a `.yaml` file extension. For example, the resampler manifest for `moresampler.exe` should be `moresampler.yaml` located in the same folder with `moresampler.exe`.

Below is a full example of a resampler manifest for Moresampler. To create a resampler manifest with OpenUtau, add the resampler's expressions to any `.ustx` project file. Open the project file in a text editor and copy the `expressions:` section into a blank manifest file.
```yaml
expressions:
  gen:
    name: Gender Factor
    abbr: gen
    type: Numerical
    min: -100
    max: 100
    default_value: 0
    is_flag: true
    flag: g
  mbre:
    name: Breathiness (Moresampler)
    abbr: mbre
    type: Numerical
    min: -100
    max: 100
    default_value: 0
    is_flag: true
    flag: Mb
  tens:
    name: Tension
    abbr: tens
    type: Numerical
    min: -100
    max: 100
    default_value: 0
    is_flag: true
    flag: Mt
  pit:
    name: Pitch deviation (flag)
    abbr: pit
    type: Numerical
    min: -1200
    max: 1200
    default_value: 0
    is_flag: true
    flag: t
  pkcp:
    name: Peak Compressor
    abbr: pkcp
    type: Numerical
    min: 0
    max: 100
    default_value: 86
    is_flag: true
    flag: P
  amp:
    name: Amplitude Modulation
    abbr: amp
    type: Numerical
    min: -100
    max: 100
    default_value: 0
    is_flag: true
    flag: A
  cons:
    name: Unvoiced Consonant Gain
    abbr: cons
    type: Numerical
    min: -20
    max: 100
    default_value: 0
    is_flag: true
    flag: b
  fstr:
    name: Force Stretch
    abbr: fstr
    type: Options
    min: 0
    max: 1
    default_value: 0
    is_flag: true
    options:
    - ''
    - e
    - Me
  opn:
    name: Openness
    abbr: opn
    type: Numerical
    min: -100
    max: 100
    default_value: 0
    is_flag: true
    flag: Mo
  res:
    name: Resonance
    abbr: res
    type: Numerical
    min: -100
    max: 100
    default_value: 0
    is_flag: true
    flag: Mr
  dry:
    name: Dryness
    abbr: dry
    type: Numerical
    min: -100
    max: 100
    default_value: 0
    is_flag: true
    flag: Md
  cors:
    name: Coarseness
    abbr: cors
    type: Numerical
    min: 0
    max: 100
    default_value: 0
    is_flag: true
    flag: MC
  grwl:
    name: Growl
    abbr: grwl
    type: Numerical
    min: 0
    max: 100
    default_value: 0
    is_flag: true
    flag: MG
  dist:
    name: Distortion
    abbr: dist
    type: Numerical
    min: 0
    max: 100
    default_value: 0
    is_flag: true
    flag: MD
  stbl:
    name: Stabilization
    abbr: stbl
    type: Numerical
    min: 0
    max: 10
    default_value: 0
    is_flag: true
    flag: Ms
  mint:
    name: Model Interpolation
    abbr: mint
    type: Numerical
    min: 0
    max: 100
    default_value: 100
    is_flag: true
    flag: Mm
```

# Installing Wavtools

## Windows
1. On your unzipped OpenUtau folder, locate the wavtool folder named `Wavtools`.
2. Open the wavtool folder and place the downloaded wavtool on the folder.

In OpenUtau version 0.1.119 or higher, wavtools can be installed by dragging and dropping the `.exe` file onto the main OpenUtau window and selecting "Install as wavtool".

<img src="https://github.com/stakira/OpenUtau/assets/18076904/1a13d37d-b472-451d-b24a-e984b095bd4a" height="250">

## macOS / Linux

External wavtools are not supported on macOS or Linux at this time.  

# Tested Wavtools and Directories
Below is a list of all UTAU wavtools tested with OpenUtau.

| Wavtool | Author | Additonal Notes |
| --------- | -------- | ------------------ |
| simple | StAkira | Built into OpenUtau. Works on all platforms. |
| convergence | StAkira | Also built into OpenUtau. Uses phase compensation.|
| [moresampler.exe](https://bowlroll.net/file/139123) | Kanru Hua | [See adjustments for compatibility.](https://github.com/stakira/OpenUtau/wiki/Resamplers-and-Wavtools#compatible-with-adjustments) |
| [wavtool64](http://utau2008.xrea.jp/2020/engine/wavtool64.zip) | Ameya | |
| [wavtool4vcv](https://www.mediafire.com/file/1iwrak88c6xzb87/wavtool4vcv20141202.zip/file) | nmasao | |