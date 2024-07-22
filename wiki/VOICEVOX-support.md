OpenUtau supports VOICEVOX (humming function).  
It is provided by the following [License](https://github.com/VOICEVOX/voicevox_engine/blob/master/LGPL_LICENSE)

## What is VOICEVOX?
[VOICEVOX](https://voicevox.hiroshiba.jp/) is a free, medium-quality text-to-speech and singing voice synthesis software.  
Click here for [Github](https://github.com/VOICEVOX/voicevox/tree/main)

## VOICEVOX Software Terms of Use  
### LICENSE AGREEMENT  
1. You may use the software for commercial and non-commercial purposes.  
2. Use of the created audio is subject to the terms and conditions of the respective audio library.  
3. When you grant a license to others to use the audio you have created, you must require them to comply with the provisions of 2 and 3 of this license agreement.  

### Prohibitions  
* Redistribution of this software, in whole or in part, without permission  
* Decompiling, reverse engineering, or disclosing these methods to the public.  
* Causing disadvantage to the creator or any third party.  
* Acts that offend public order and morals.  

### Disclaimer  
The producer is not responsible for any damage or disadvantage caused by this software.  

### Other  
Credit must be given to VOICEVOX when using this software.  


Taken from the terms of use on the [VOICEVOX website.](https://voicevox.hiroshiba.jp/term/)  
Please enjoy using VOICEVOX and abide by the Terms of Use!  
Please refer to the README.txt file for each character for credit information!

## How to install
Upgrade OpenUtau by turning on "Beta" in the preferences.  
DL [VOICEVOX](https://voicevox.hiroshiba.jp/) with the whole editor.  
DL the [VOICEVOX_Singer.zip](https://github.com/rokujyushi/OpenUtau/releases/tag/0.0.0.0) and 
D&D it into the main window of OpemUtau.  
Start OpemUtau while running VOICEVOX.

An engine-only dependency package will be created in the future. (This is just a plan)

## Phonemizers
The following are currently supported.  
* S-VOICEVOX JA(Simple Voicevox Japanese Phonemizer)  

To be supported in the future (This is just a plan)
* S-VOICEVOX EN to JA
* VOICEVOX JA
* VOICEVOX EN to JA

## Phonemes
Available phonemes are currently only in hiragana.  

![image](https://github.com/stakira/OpenUtau/assets/93469977/230dbd33-e7c8-4494-95f6-418d644f3257)


## Expressions
The following are currently supported.
* DYN (Dynamics)
 Allows volume adjustment after speech synthesis
* SHFT (tone shift)
 For adjusting the input pitch of speech synthesis (in phrases).
 It changes the way you sing.
* CLR(Voice Color)
 Changes the voice quality of each singer (per phrase).
* VOL (Volume)
 Adjustment of voice synthesizer input volume (per phrase)
* PITD (pitch curve)
  Adjusts the text-to-speech input pitch (in frames).

To be supported in the future
* SHFC (tone shift curve)
* VOLC(volume curve)
* BSNG (bass singer)