# ~0.1.90 (05-15-2023)

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
- [#680](https://github.com/stakira/OpenUtau/pull/680) - `JA VCV & CVVC` Add presamp.ini `VCPAD` support ([@maiko3tattun](https://github.com/maiko3tattun))
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

# 0.1.57~0.1.73 (04-23-2023)

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