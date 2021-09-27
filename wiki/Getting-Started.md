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

## Create and edit tracks
(to do)
## Create and edit notes
(to do)