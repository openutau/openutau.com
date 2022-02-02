
# Windows

This is a list of all UTAU resamplers tested with OpenUtau.

## Fully compatible
- worldline (OpenUtau builtin on all platforms)
- [[bkh01.exe|http://z-server.game.coocan.jp/utau/utautop.html#bkh01]]
- [[doppeltler32.exe|http://utau2008.xrea.jp/2020/engine/]]
- [[doppeltler64.exe|http://utau2008.xrea.jp/2020/engine/]]
- [[f2resamp32.exe|http://utau2008.xrea.jp/2020/engine/f2resamp004.zip]]
- [[f2resamp64.exe|http://utau2008.xrea.jp/2020/engine/f2resamp004.zip]]
- [[fresamp11.exe|http://utau2008.xrea.jp/downloads/fresamp011.zip]]
- fresamp12.exe
- [[fresamp14.exe|http://utau2008.xrea.jp/downloads/fresamp014.zip]]
- [[phavoco.exe|http://utau2008.xrea.jp/downloads/phavoco010.zip]]
- [[phaavoco.exe|http://utau2008.xrea.jp/2020/engine/phaavoco001.zip]]
- [[macres.exe|https://github.com/titinko/macres/releases]]
- model4.exe
- resampler.exe
- [[TIPS.exe|http://scientistb.web.fc2.com/program/]]
- [[tn_fnds.exe|http://z-server.game.coocan.jp/utau/utautop.html#tn_fnds]]
- [[w4u.exe|http://utau2008.xrea.jp/downloads/w4u001.zip]]
- [[young3.exe|https://bowlroll.net/file/203018]]
- [[vs4u.exe|http://ackiesound.ifdef.jp/download.html#vs4u]]
- [[WARP.exe|http://custom-made.seesaa.net/article/312530509.html]]
- [[EFB-GT.exe|http://custom-made.seesaa.net/article/312529786.html]]
- EFB-PB.exe
- [[SpaceWorld_win64.exe|https://github.com/LovelyA72/SpaceWorld/releases]]

## Compatible with adjustments

- moresampler.exe
  - Need to edit the following lines in moreconfig.txt:
    - Line 6 "resampler-compatibility" to on.
    - Line 16 "auto-update-llsm-mrq" to off.
  - The wavtool mode is not supported, but using it as a pure resampler works.
  - Generating llsm files with multiple processes can easily overload your computer. Please turn down threads to 1 or 2.
    - You can also set Line 15 "multithread-synthesis" to off in moreconfig.txt to avoid this problem.

# macOS

As of macOS 11.6, the below method works.

1. Install [homebrew](https://docs.brew.sh/Installation)
2. Install [wine32on64](https://github.com/Gcenx/homebrew-wine) using following commands:
```
brew tap gcenx/wine
brew install --cask --no-quarantine wine-crossover
```
3. Download "mac_additional.zip" from OpenUtau release page. Use the .sh script to wrap your exe. You will need to edit the .sh script to work with each resampler.

# Linux

For wrapping Windows resamplers into Linux, use this method:

1. Install [Wine](https://www.winehq.org/)
2. Open Resamplers folder (should be on /home/your_username/OpenUtau/Resamplers/)
3. Create a new text file with the name of your resampler (don't need to have a file extension). Open, add and edit this script:
```
#!/bin/bash
LANG="ja_JP.UTF8" wine "/absolute/path/to/your/resampler.exe" "${@,-1}"
```
4. Restart or execute OpenUtau.