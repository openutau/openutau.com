Feel free to add your tutorials, guides, notes, or any tip tweets to this page!

# Basics
### From installation to basic usage
[Getting Started](Getting-Started)

### Introduction; About OpenUtau
Open source software that allows you to use UTAU voice banks.  
OpenUtau is developed by a large number of volunteers, not by companies or individuals.  
You can ask questions, report bugs, and suggest new features on the [official Discord server](https://discord.gg/UfpMnqMmEM).

### Difference from original UTAU
- Multitrack and audio (accompaniment) can be use
- Pre rendering
- Renderer:  
There are two synthesis methods: Classic, which edits each note one by one, and WORLDLINE-R, which allows you to set parameters across notes.  
WORLDLINE-R does not allow conventional engine selection
- Phonemizer:  
Ability to convert phonemes in real time. Leave the VCV and CVVC conversion to Phonemizer, and basically enter only words or hiragana for lyrics.  
In addition, there are many phonemizers for each language voice banks.
- VoiceColor:  
Ability that supports the selection of append voice banks. Can be used by setting the sub-banks and range in the singer window.  
Conventional use of entering expression names in lyrics is not supported.
- Expression panel:  
Volume, flags, VoiceColor, engine(resampler) switching, etc. are all set in the expression panel at the bottom of the piano roll.  
Flags can be entered by dragging numbers instead of entering characters.
- Multilingual support for UI
- Compatible with Windows, Mac and Linux

### Classic Singers (conventional UTAU voice banks)
- Basically the same format as UTAU, character.txt, oto.ini, prefix.map, etc. can be used.
- All folders with character.txt in the voice folder are recognized as voice banks (the original UTAU recognizes only surface folders).
- OpenUtau's unique voicebank settings (VoiceColor, default Phonemizer, etc.) are recorded in [character.yaml](tech-note:-character.yaml)

# Advanced
### ENUNU & SimpleENUNU
What is ENUNU: A technology that allows you to use the AI ​​singing voice synthesis system NNSVS on UTAU  
What is SimpleENUNU: Another ENUNU for enthusiasts and developers with easy to update NNSVS  

ENUNU models (AI voicebank) are distributed by volunteers.  
OpenUtau also supports it on a trial basis. It can be used by installing "ENUNU for OpenUtau", launching it separately behind the OU, and selecting ENUNU phonemizer.

- [Status of ENUNU NNSVS Support](Status-of-ENUNU-NNSVS-Support)
- [ENUNU Server for OpenUtau](https://github.com/rokujyushi/ENUNU/releases)
- [SimpleENUNU Server for OpenUtau](https://github.com/rokujyushi/SimpleEnunu/releases)

- **Attention**
    - Use "ENUNU for OpenUtau" and "ENUNUServer" for ENUNU models and "SimpleENUNUServer" for SimpleENUNU models.
    - When using the SimpleENUNU model, add the following to character.yaml.  
    ```
    singer_type: Enunu
    ```

# Quick Tips
