# UTAU Plugin
UTAU plugins are software distributed by the user community to extend the functionality of the original UTAU.

OpenUtau partially supports legacy plugins. Not all plugins are usable.  
For some plugins, OpenUtau's unique parameters applied to a note may be lost. (This occurs because plugins that delete existing values require deleting and re-adding the note.)

As a unique feature of OpenUtau, you can select non-adjacent notes to apply plugins (the original UTAU only allows selecting contiguous notes).

## Batch Processing
OpenUtau is developed with the policy of implementing as many useful features as possible directly into the OpenUtau ifself, minimizing reliance on external plugins.  
Using the “Batch Edits” in the piano roll allows you to perform most basic batch edits.

## Regarding VCV/CVVC Conversion
In OpenUtau, please do not use plugins to convert lyrics into VCV/CVCV.  
If lyrics contain “unnecessary caracters other than lyrics,” features like multi-pitch mapping and Voice Color may not function properly.

OpenUtau includes automatic lyric conversion features.  
Using "Phonemizer" converts most voicebanks to appropriate aliases, which are displayed in the alias field below.

# Installing UTAU Plugins
Please note that most plugins are designed for Windows and do not support macOS/Linux.  
- Create part as needed and open the PianoRoll window.
- Open the plugin folder via the menu bar: “Batch Edit > Legacy Plugin > Open Folder”.
- Unzip the downloaded plugin and copy it into the plugin folder.

# Compatibility
This is a list of all plugins for UTAU that have been tested in OpenUtau. Many popular plugins haven't been tested yet, so please update the list if you try plugins that aren't shown.

Note that some plugins themselves may have problem running on non-Japanese systems or other situations. OpenUtau being compatible does not guarantee your setup is compatible. Also note that OU's compatibility with specific plugins may change over time as it updates, so this list may be out of date.

## Fully compatible
* [AutoPitchWriter](https://www.youtube.com/watch?v=pdxMg2ViASU)
* [AutoVibrato](https://ameblo.jp/maiko3utau/entry-12617377622.html)
* [frqeditor](https://www.mediafire.com/file/f92l5gnk3512aaf/frqeditor20160417.zip/file) (May need to manually specify a resampler in the options beforehand)
* [Humanizer](https://bowlroll.net/file/54423)
* [iroiro2](https://ux.getuploader.com/bizz_v/) (Doesn't open for some people?)
* [Lyric Parser 2.1](https://snowphones.weebly.com/lyric-parser-20.html)
* [omakase2020](https://ameblo.jp/maiko3utau/entry-12615869960.html)
* [RandomVibrato](https://ameblo.jp/maiko3utau/entry-12095627508.html)
* [UNotePad](https://github.com/oxygen-dioxide/UNotePad)
* [UTAU Plugin Launcher](https://ameblo.jp/maiko3utau/entry-12648640444.html)
* [VibratoStocker](https://ameblo.jp/maiko3utau/entry-12544042092.html)
* [Extended Pitch Editor/拡張ピッチエディタ](http://z-server.game.coocan.jp/utau/utautop.html#pitedit) (Works with a few bugs, except for mode 1 editing) 
## Compatible with adjustments
* [Freq Tracer](http://z-server.game.coocan.jp/utau/utautop.html) (A note placed on the piano roll is needed to get FreqTracer to run. You also need to adjust pitches some after the plugin has run, and only works in "Mode 2" mode.)
* [Lab2UST](https://github.com/UtaUtaUtau/nnsvslabeling#lab2ust) - A note placed on the piano roll is needed, and offsets the results. If you try to load a frq at the time of writing, you will not get any result
## Incompatible
* [envedit/拡張エンベロープエディタ](http://z-server.game.coocan.jp/utau/utautop.html) - Works, but OU can't keep complex envelope changes intact (anything beyond what attack/decay can emulate), so basically useless
* [flagedit/拡張フラグエディタ](http://z-server.game.coocan.jp/utau/utautop.html) - Opens, but changes don't go through
* [HANASHITAI](https://www.nicovideo.jp/watch/sm20488427) - Doesn't open in OU, but works as a standalone tool
* [PrintMOV Style Tuning](https://utaforum.net/resources/printmov-tuning-helper-plugin.497/) - Opens, but doesn't change any pitchbends
