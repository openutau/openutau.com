# Installing Resamplers
##  Windows

File must be in `.exe` and be can placed in subfolders.
1. On your unzipped OpenUtau folder, locate the resampler folder named `Resamplers`.
2. Open the resampler folder and place the resampler on the folder.

## macOS

As of macOS 11.6, the below method works.

1. Install [homebrew](https://brew.sh/)
2. Install [wine32on64](https://github.com/Gcenx/homebrew-wine) using following commands:
```
brew tap gcenx/wine
brew install --cask --no-quarantine wine-crossover
```
3. Download "mac_additional.zip" from [OpenUtau release page](https://github.com/stakira/OpenUtau/releases). Use the .sh script to wrap your exe. You will need to edit the .sh script to work with each resampler.

## Linux

For wrapping Windows resamplers into Linux, use this method:

1. Install [Wine](https://www.winehq.org/)
2. Open Resamplers folder (should be on /home/your_username/OpenUtau/Resamplers/)
3. Create a new text file with the name of your resampler (don't need to have a file extension). Open, add and edit this script:
```
#!/bin/bash
LANG="ja_JP.UTF8" wine "/absolute/path/to/your/resampler.exe" "${@,-1}"
```
4. Restart or execute OpenUtau.

# Tested Resamplers and Directories
This is a list of all UTAU resamplers tested with OpenUtau.

|  Resampler |  Author  |  Additional Notes |
| ------------ | ------------ | ------------ |
|  worldline  | StAkira  |   OpenUtau built-in on all platforms. |
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
| [TIPS.exe](http://scientistb.web.fc2.com/program/)  | ScientistB |   |
| [tn_fnds.exe](http://z-server.game.coocan.jp/utau/utautop.html#tn_fnds) | Zteer |  |
| [UDB](https://github.com/YuzukiTsuru/UDB/releases/tag/0.0.3.1) | YuzukiTsuru | UDB means UTAU Debug Engine.|
| [vs4u.exe](http://ackiesound.ifdef.jp/download.html#vs4u) | Akky |  |
| [w4u.exe](http://utau2008.xrea.jp/downloads/w4u001.zip) | Zany |   |
| [WARP.exe](http://custom-made.seesaa.net/article/312530509.html) | Custom.Maid | |
| [wn4u.exe](https://utaforum.net/threads/world4utau-update.20035/) | Zany | [See adjustments for compatibility.](https://github.com/stakira/OpenUtau/wiki/Resamplers-and-Wavtools#compatible-with-adjustments) |
| [young3.exe](https://bowlroll.net/file/203018) | Zany |   |

## Compatible with adjustments

- [moresampler.exe](https://bowlroll.net/file/139123)
  - Add `moresampler.exe` without `moreconfig.txt` in `Resamplers` folder
  - Add `moresampler.exe` with unmodified `moreconfig.txt` in `Wavtools` folder
  - Now you should able to use it either as resampler only, or as both wavtool and resampler.
- [[SpaceWorld_win64.exe|https://github.com/LovelyA72/SpaceWorld/releases]] and [[wn4u.exe|https://utaforum.net/threads/world4utau-update.20035/]]
    - May experience issues if the voicebank doesn't have frq files generated beforehand. SpaceWorld version 1.0.1 prevents the software from crashing in case of a missing frq file.
- [[lessampler|https://github.com/YuzukiTsuru/lessampler/releases/]]
    - In development, lack of flag support
    - Oversized Audio Model Attention

# Installing Wavtools
## Windows
1. On your unzipped OpenUtau folder, locate the wavtool folder named `Wavtools`.
2. Open the wavtool folder and place the downloaded wavtool on the folder.

## macOS

## Linux

# Tested Wavtools and Directories
This is a list of all UTAU wavtools tested with OpenUtau.

| Wavtool | Author | Additonal Notes |
| --------- | -------- | ------------------ |
| simple | StAkira | OpenUtau built-in on all platforms. |
| convergence | StAkira | OpenUtau built-in on all platforms. Phase compensation implemented.|
| [moresampler.exe](https://bowlroll.net/file/139123) | Kanru Hua | [See adjustments for compatibility.](https://github.com/stakira/OpenUtau/wiki/Resamplers-and-Wavtools#compatible-with-adjustments) |
| [wavtool64](http://utau2008.xrea.jp/2020/engine/wavtool64.zip) | Ameya | |
| [wavtool4vcv](https://www.mediafire.com/file/1iwrak88c6xzb87/wavtool4vcv20141202.zip/file) | nmasao | |