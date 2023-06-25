# ~[0.1.158](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.158) (06-11-2023)

## Major Changes
- [d60f403](https://github.com/stakira/OpenUtau/commit/d60f403) - Upgrade to avalonia 11 ([@stakira](https://github.com/stakira))
    - Version upgrade + series of fixes to breaking changes. See `Misc` for further relevant commits.
    - Keep an eye out for bugs!
- [08d7693](https://github.com/stakira/OpenUtau/commit/08d7693) - Installer version available (nsis installer) ([@stakira](https://github.com/stakira))

## Phonemizer Changes
- [#736](https://github.com/stakira/OpenUtau/pull/736) - `VOGEN` Fix consonant timing ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#731](https://github.com/stakira/OpenUtau/pull/731) - `ES SYL` Starting CCV + VV transition fix ([@lottev1991](https://github.com/lottev1991))
- [#732](https://github.com/stakira/OpenUtau/pull/732) - `ES VCCV` Code and function optimization ([@lottev1991](https://github.com/lottev1991))
- [#734](https://github.com/stakira/OpenUtau/pull/734) - `JA CVVC` Read CV append voice color ([@lottev1991](https://github.com/lottev1991))
- [#737](https://github.com/stakira/OpenUtau/pull/737) - `VIE VCV` Phonemizer Update ([@lottev1991](https://github.com/lottev1991))

## Misc
- [704b54c](https://github.com/stakira/OpenUtau/commit/704b54c) - Clean up views ([@stakira](https://github.com/stakira))
- [723109f](https://github.com/stakira/OpenUtau/commit/723109f) - Fix pianoroll interactions ([@stakira](https://github.com/stakira))
- [395a182](https://github.com/stakira/OpenUtau/commit/395a182) - Fix locales and themes ([@stakira](https://github.com/stakira))
- [1e1a052](https://github.com/stakira/OpenUtau/commit/1e1a052) - Rewrite oto view ([@stakira](https://github.com/stakira))
- [d33a440](https://github.com/stakira/OpenUtau/commit/d33a440) - Better waveform drawing  ([@stakira](https://github.com/stakira))
- [5a47b79](https://github.com/stakira/OpenUtau/commit/5a47b79) + [bf0c8be](https://github.com/stakira/OpenUtau/commit/bf0c8be) + [22a674f](https://github.com/stakira/OpenUtau/commit/22a674f)- UI fixes ([@stakira](https://github.com/stakira))
- [839ac40](https://github.com/stakira/OpenUtau/commit/839ac40) - Fix dropping file  ([@stakira](https://github.com/stakira))
- [8227dee](https://github.com/stakira/OpenUtau/commit/8227dee) - Update packages, refactor file picker and nullness ([@stakira](https://github.com/stakira))
- [ee91432](https://github.com/stakira/OpenUtau/commit/ee91432) - Fix nullness in release configuration ([@stakira](https://github.com/stakira))
- [78fc333](https://github.com/stakira/OpenUtau/commit/78fc333) - Fix tab key for lyric box ([@stakira](https://github.com/stakira))
- [91bc579](https://github.com/stakira/OpenUtau/commit/91bc579) - Fix Mac build ([@stakira](https://github.com/stakira))
- [a52c64d](https://github.com/stakira/OpenUtau/commit/a52c64d) - Add select singer type step to install ([@stakira](https://github.com/stakira))
- [a227d56](https://github.com/stakira/OpenUtau/commit/a227d56) - tweak singer setup view ([@stakira](https://github.com/stakira))

***

# ~[0.1.129](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.129) (06-03-2023)

## Features
- [#718](https://github.com/stakira/OpenUtau/pull/718) - SimpleENUNU Support ([@rokujyushi](https://github.com/rokujyushi))
    - You can now load SimpleENUNU models in OpenUtau! Note: currently, there is no support for SingingStyle.
    - To use SimpleENUNU within OpenUtau, please download SimpleENUNUServer: https://github.com/rokujyushi/SimpleEnunu/releases/tag/SimpleEnunu-OpenUtau-0.1.0 <br>
        ![image showing Ritsu CrissCross and other SimpleENUNU models in the singer selection window](https://user-images.githubusercontent.com/93469977/241399775-a0af7ef2-acb9-4a83-abf2-f26bc7a967da.png)
- [#723](https://github.com/stakira/OpenUtau/pull/723) - Add Track Name ([@maiko3tattun](https://github.com/maiko3tattun))
    - Allows users to name tracks as a whole!
    - In addition, a track is now set at start up, track names are now referenced by default in wav exports, and part names are referenced in legacy UST exports.  
![image showing new track names feature](https://i.imgur.com/g4q6i3W.png)

## Bug Fixes
- [bda13a6](https://github.com/stakira/OpenUtau/commit/bda13a6) - Fix updater dialog crash  ([@stakira](https://github.com/stakira))

## Translations
- [#725](https://github.com/stakira/OpenUtau/pull/725) - Fix Japanese translations (improved) ([@maiko3tattun](https://github.com/maiko3tattun))

## Misc
- [7b53731](https://github.com/stakira/OpenUtau/commit/7b53731) - Fix PluginRunnerTest  ([@stakira](https://github.com/stakira))
- [#727](https://github.com/stakira/OpenUtau/pull/727) - Fix expression selection changes when reloading part ([@maiko3tattun](https://github.com/maiko3tattun))
- [07ec981](https://github.com/stakira/OpenUtau/commit/07ec981) - Save piano roll toggles in prefs ([@stakira](https://github.com/stakira))
    - The "show waveform/pitch/phoneme/vibrato/etc" toggles on the piano roll should be persistent now.
- [1c6e760](https://github.com/stakira/OpenUtau/commit/1c6e760) - Tweak track header ([@stakira](https://github.com/stakira))
- [e21b836](https://github.com/stakira/OpenUtau/commit/e21b836) - Silence pan logging ([@stakira](https://github.com/stakira))

***

# ~[0.1.119](https://github.com/stakira/OpenUtau/releases/tag/build%2F0.1.119) (05-28-2023)

## Features
- [#691](https://github.com/stakira/OpenUtau/pull/691) - Singer Window Improvements, etc ([@maiko3tattun](https://github.com/maiko3tattun))
    - General improvements to the singer window have been made! Primary additions are alias search, as well as pre-selecting the singer based on active part. <br>
    ![example of alias search function](https://imgur.com/1rTdCKL.gif)
- [#711](https://github.com/stakira/OpenUtau/pull/711) - General Lyrics Replacement tool ([@maiko3tattun](https://github.com/maiko3tattun))
    - This new macro uses regular expressions to convert lyrics. It is highly scalable and simplifies replacement of any language. Adding and sharing new presets is encouraged!
    <br>![example animation of 'General lyrics replacement' in action](https://imgur.com/BFib5mt.gif)
- [#712](https://github.com/stakira/OpenUtau/pull/712) - Drag and drop to install .dll phonemizers, .exe resamplers and wavtools ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
    - Externally provided phonemizers, resamplers and wavtools should no longer require manual folder management. Just drag and drop to install! 
    ```Diff
    OS-specific feedback required: Mac and Linux
    ```
    ![example of .exe install via drag and drop](https://user-images.githubusercontent.com/54425948/239664701-1fffee4f-3626-43ab-b4db-d7c7b3b32f47.png)
- [#713](https://github.com/stakira/OpenUtau/pull/713) - Add support for Classic Ust Flags ([@arkfinn](https://github.com/arkfinn))
    - [94b00a5](https://github.com/stakira/OpenUtau/commit/94b00a5) fixes some issues with the original implementation.

## Bug Fixes

- [#708](https://github.com/stakira/OpenUtau/pull/708) - `Pitch Baking` Fix PITD erasing region misplaced, process the whole part by default ([@oxygen-dioxide](https://github.com/oxygen-dioxide))

## Phonemizer Changes
- [#693](https://github.com/stakira/OpenUtau/pull/693) - `ES VCCV` VCC/CC fix + ValidateAlias for "E" semivowel ([@lottev1991](https://github.com/lottev1991))
- [#707](https://github.com/stakira/OpenUtau/pull/707) - `ZH CVV` Use new mapping style + voice color support + "yan" vowel fix + "_un" ending alternative
- [#709](https://github.com/stakira/OpenUtau/pull/709) - `KO CVC` "ch" VC fix (romaja/mixed VC) ([@lottev1991](https://github.com/lottev1991))
- [#710](https://github.com/stakira/OpenUtau/pull/710) - `Various JA phoemizers` PhoneticHint support and Unicode countermeasures ([@maiko3tattun](https://github.com/maiko3tattun))
- [#716](https://github.com/stakira/OpenUtau/pull/716) - `EN VCCV` phonemizer refactor ([@mmemmim](https://github.com/mmemim) & [@cubialpha](https://github.com/cubialpha))
- [#720](https://github.com/stakira/OpenUtau/pull/720) - `ES VCCV` Add different consonant lengths support ([@lottev1991](https://github.com/lottev1991))

## Misc
- [11fa8cc](https://github.com/stakira/OpenUtau/commit/11fa8cc) - nicer version compare  ([@stakira](https://github.com/stakira))

***

# ~[0.1.96](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.96) (05-21-2023)
```Diff
@@ Major Change @@
```
From this point on, OpenUtau has a [Stable](https://github.com/stakira/OpenUtau/tree/stable) and [Beta](https://github.com/stakira/OpenUtau/tree/master) branch. You may opt into the Beta in-program by going to `Tools`>`Preferences`>`Advanced`, and toggling `Beta` to On. Doing so may open you up to experiencing bugs, so exercise caution!

## Misc
- [dd2d0f2](https://github.com/stakira/OpenUtau/commit/dd2d0f2) - adds stale workflow and increases releases kept ([@stakira](https://github.com/stakira))
- [bd5641c](https://github.com/stakira/OpenUtau/commit/bd5641c) - Setup beta and stable release channels ([@stakira](https://github.com/stakira))
    - [225b97d](https://github.com/stakira/OpenUtau/commit/225b97d) corrects beta releases link, title and description.

***

# ~[0.1.92](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.92) (05-16-2023)

## Misc
- [#af16021](https://github.com/stakira/OpenUtau/commit/af16021) - Refactor locale initialization ([@stakira](https://github.com/stakira))
    - Preventative measures for situations similar to the 0.1.90 bug, general refactoring.
    - This commit also changes the `mid` on the `stereo panning slider` to **`C`** (for Center).
***

# ~[0.1.91](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.91) (05-15-2023)

## Bug Fixes
- [#689](https://github.com/stakira/OpenUtau/pull/689) - fix en-US language saving and loading ([@lennyservant](https://github.com/lennyservant))
    - This should resolve the critical errors (preferences crash, singers not loading) from 0.1.90. Sorry for the inconvenience!
    - If still encountering issues, navigate to the `prefs.json` file in your OpenUtau folder structure, and remove the line `"language": "axaml",` and save.

***
# ~[0.1.90](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.90) (05-15-2023)
```Diff
! Caution !
This build has known bugs !
```
- Selecting `preferences` currently causes OpenUtau to crash. Fix incoming at [#689](https://github.com/stakira/OpenUtau/pull/689). 

Fix note: If you at any point updated to this version and ran it, and have been experiencing persistent issues even after updating to new versions -- you may need to remove the "languages" line from your prefs.JSON, or simply delete the prefs.JSON wholly (warning: this will reset any customization OpenUtau stores in preferences to the default).

## Features
- [#668](https://github.com/stakira/OpenUtau/pull/668) - Stereo Panning Slider ([@nfrid](https://github.com/nfrid))
    - Stereo panning now available in the `track header`, under the `volume slider`. It works similarly to volume; left click and hold to drag, and right click will set the slider to mid. <br>
    ![example animation of 'Stereo Panning Slider' set to mid](https://user-images.githubusercontent.com/13046595/234082612-b803c922-7328-476c-9ff7-55113ed9fcca.png) <br>
    ![example animation of 'Stereo Panning Slider' set to left](https://user-images.githubusercontent.com/13046595/234082697-c123fdcd-12dd-4f17-8b09-7a24bd954bbc.png) <br>
    ![example animation of 'Stereo Panning Slider' set to right](https://user-images.githubusercontent.com/13046595/234082665-3ef4ec83-6d42-4d59-b025-99a934effca7.png)

- [#676](https://github.com/stakira/OpenUtau/pull/676) - Move Suffix to Voice Color ([@maiko3tattun](https://github.com/maiko3tattun))
    - A macro to remove suffixes from lyrics and move them to the voice color panel if a matching suffix is found in the voice color settings. If not found, the suffix will remain in the lyric.
    ![example animation of 'Move Suffix to Voice Color' in action](https://i.imgur.com/p108qe0.gif)

## Phonemizer Changes
- [#667](https://github.com/stakira/OpenUtau/pull/667) - **Removed Phonemizer: `EN Teto`** ([@adlez27](https://github.com/adlez27))
    - Depreciated. It is recommended to use `EN Delta` Phonemizer when using Kasane Teto's English voicebank. The seperately compiled version of `EN Teto` can be found here if necessary: https://github.com/adlez27/OpenUtau/releases/tag/Teto-0.1.0
- [#681](https://github.com/stakira/OpenUtau/pull/681) - **Merged Phonemizers: `EN Delta V1` and `EN Delta V2`** ([@lottev1991](https://github.com/lottev1991))
    - `EN Delta V1` and `EN Delta V2` are now merged into one Phonemizer: **`EN Delta`**. 
        - Split strings are now handled automatically rather than having to manually select which version you require.
- [#674](https://github.com/stakira/OpenUtau/pull/674) + [#677](https://github.com/stakira/OpenUtau/pull/677)- **Add Spanish and Italian G2P** ([@lottev1991](https://github.com/lottev1991))
    - G2P allows you to write words that may not appear in the dictionary. It will use the data it was trained on to take a guess at the phonemes for the word written, rather than just resulting in a `word not found` error. Support for this has been added to *all* current Spanish Phonemizers, and `IT SYL`!
- [#680](https://github.com/stakira/OpenUtau/pull/680) - `JA VCV & CVVC` Add presamp.ini `VCPAD` support, fix a bug when single pitch voicebank ([@maiko3tattun](https://github.com/maiko3tattun))
- [#675](https://github.com/stakira/OpenUtau/pull/675) - `ES VCCV`  Starting CCV bug fix ([@lottev1991](https://github.com/lottev1991))
- [#684](https://github.com/stakira/OpenUtau/pull/684) - `ES VCCV` Add stop consonant/affricate CC ValidateAlias ([@lottev1991](https://github.com/lottev1991))
- [#688](https://github.com/stakira/OpenUtau/pull/688) - `Vietnamese Phonemizers` Updated to fix Voice Color support ([@janikyou](https://github.com/janikyou))


## Translation
- [#676](https://github.com/stakira/OpenUtau/pull/676) - Add and improve Japanese translations ([@maiko3tattun](https://github.com/maiko3tattun))
- [#679](https://github.com/stakira/OpenUtau/pull/679) - Fix around language ([@maiko3tattun](https://github.com/maiko3tattun))
    - Fixed a bug that caused the language to run in the same language as InstalledUICulture the first time it was launched, but reset to en-US when the preference window was opened

## Misc
- [#4dca53d](https://github.com/stakira/OpenUtau/commit/4dca53d78ddfd9569a01c975e0e961c948ee53bf) - Adds g2p training code ([@stakira](https://github.com/stakira))
- [#669](https://github.com/stakira/OpenUtau/pull/669) - Refactor PluginRunner to OpenUtau.Core and make testable ([@arkfinn](https://github.com/arkfinn))
- [#676](https://github.com/stakira/OpenUtau/pull/676) - Add and fix LyricBatchEdits ([@maiko3tattun](https://github.com/maiko3tattun))
    - _Fix RemoveToneSuffix_
    - _Add ChangeVoiceColorCommand in NoteCommand_
- [#680](https://github.com/stakira/OpenUtau/pull/680) - Add PresampSamplePhonemizer and fixes ([@maiko3tattun](https://github.com/maiko3tattun))
    - _Sample for developers. Not included in release build_
- [#682](https://github.com/stakira/OpenUtau/pull/682) - Defaults to paging instead of scrolling ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#686](https://github.com/stakira/OpenUtau/pull/686) - Flag filter based on resampler manifests ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
    - Support for an `expression-filter` feature in resampler manifests. To quote: 
    > Many resamplers are unable to parse flags correctly when there are moresampler-specific flags, because most resamplers only use single-character flags, but moresampler uses multi-character flags, such as "Mt", "Me", "Mb". To solve this issue, we can pass only the supported flags (specified in resampler manifest) into the resampler."
    - This is one part of a broader feature implementation. See also `Let renderers provide expression suggestions` - [#599](https://github.com/stakira/OpenUtau/pull/599). 

***

# [0.1.57](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.57)~[0.1.73](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.73) (04-23-2023)

**Past release notes:** This is the first! If you need to know about previous releases, please see the github commit history. Efforts will be made to make sure that features up until this point are documented on the wiki. See [Getting Started](https://github.com/stakira/OpenUtau/wiki/Getting-Started).

## Features
- [#661](https://github.com/stakira/OpenUtau/pull/661) - Pitch Baking ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
    - A macro has been added under the `notes` topline menu item in the piano roll: `convert PITD to pitch control points`:
        
        ![example animation of 'convert PITD to pitch control points' in action](https://i.imgur.com/JcbJlRs.gif)
- [#662](https://github.com/stakira/OpenUtau/pull/662) - Support for importing and exporting time signatures in MIDI files ([@liuycsd](https://github.com/liuycsd))


## Bug Fixes
- [#89550fe](https://github.com/stakira/OpenUtau/commit/89550fe94cbdf5e6f808904626154cf5ebf5ce62) - revert macos dylib hack from #6fc7b35 ([@stakira](https://github.com/stakira))
    - **This should address the mac builds from 0.1.53 though 0.1.57 giving a Failed to render error on MacOS.** 
- [#657](https://github.com/stakira/OpenUtau/pull/657) - Fix disappearing notes on plugin execution ([@arkfinn](https://github.com/arkfinn))

## Phonemizer Changes
- [#644](https://github.com/stakira/OpenUtau/pull/644) - `EN Delta V1` VCC ending fix ([@lottev1991](https://github.com/lottev1991))
- [#646](https://github.com/stakira/OpenUtau/pull/646) - `JA CVVC` Add crossfade CV support for non-vowels ([@lottev1991](https://github.com/lottev1991))
- [#655](https://github.com/stakira/OpenUtau/pull/655) - **New Phonemizer: `JA VCV & CVVC`** ([@maiko3tattun](https://github.com/maiko3tattun))
    - `JA VCV & CVVC` allows support of multiple voicebank formats in one phonemiser. It supports CV, VCV and CVVC Japanese voicebanks (including pitches or colors of differing formats within the same hierarchy). With the settings one can adjust within a presamp.ini file, this is a powerful addition to the Phonemizer roster. Please give it a try if it suits your needs. 
        - Introduces a new base class for phonemizers that work with the existing presamp.ini file type.
- [#656](https://github.com/stakira/OpenUtau/pull/656) - Improved loading of Append.maps for multi-prefix maps ([@maiko3tattun](https://github.com/maiko3tattun))
    - Within this PR, full implementation of the presamp.ini parsing for `JA VCV & CVVC` is included. Relevant tests have also been added at [#06c8475](https://github.com/stakira/OpenUtau/pull/656/commits/06c8475fbae109beabe925c7169916e2185406bf).
- [#659](https://github.com/stakira/OpenUtau/pull/659) - Adjustments to Phonemizer and SyllableBasedPhonemizer to allow automated testing ([@adlez27](https://github.com/adlez27))
    - Some example tests have been provided. It is encouraged to write tests for SBP phonemizers both existing and in development. [#666](https://github.com/stakira/OpenUtau/pull/666) - Read dictionary sync when testing is related.
- [#663](https://github.com/stakira/OpenUtau/pull/663), [#664](https://github.com/stakira/OpenUtau/pull/664), [#665](https://github.com/stakira/OpenUtau/pull/665) - `EN Delta V1` Add additional X-SAMPA vowels + misc fixes ([@lottev1991](https://github.com/lottev1991))
    - The dictionary template has also been updated to support these.


## Misc
- [#647](https://github.com/stakira/OpenUtau/pull/647) - Add .vscode folder into gitignore ([@oxygen-dioxide](https://github.com/oxygen-dioxide))

***

>_OpenUtau's version numbers increase per accepted PR request. As such, these changelogs are grouped with the date of acceptance treated as a "release"._