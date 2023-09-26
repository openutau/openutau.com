Feel free to add your tutorials, guides, notes, or any tip tweets to this page!

# Basics
### From installation to basic usage
[Getting Started](Getting-Started)

### Introduction; About OpenUtau

OpenUtau is a free, open-source editor made for the UTAU community. 
OpenUtau is developed by a large number of volunteers, not by companies or individuals.  
You can ask questions, report bugs, and suggest new features on the [official Discord server](https://discord.gg/UfpMnqMmEM).

### Difference from original UTAU
- Support for **multiple vocal tracks**, as well as **audio tracks**
- **Pre-rendering**, for faster results as you edit.
- **Renderer:**  
There are two render modes: Classic, which edits each note one by one, and WORLDLINE-R, which allows you to set parameters across notes.  
WORLDLINE-R does not allow conventional engine selection, while Classic allows use of conventional engines (Resamplers and Wavtools).
- **Phonemizer:**  
Phonemizers add the ability to convert phonemes in real time. Leave the VCV and CVVC conversion to Phonemizer, and enter lyrics more intuitively in a fashion similar to more modern vocal synth editors.  
In addition, there are Phonemizers available for many languages and voice bank methods.
- **Voice Color:**  
Voice Colors allow you to switch appends on a per-note basis, as well as allowing you to adjust pitch-based suffix settings. You are able to define a Voice Color by setting the sub-banks and range in the singer window, and you use them in the expressions panel by selecting the CLR parameter.
Conventional use via entering expression names in lyrics is not supported.
- **Expression panel:**  
Volume, flags, engine (resampler) switching, Voice Color, and so on, are able to be set in an expression panel found at the bottom of the piano roll.  
Flags can be entered by dragging numbers instead of manually typing character sets.
Custom expressions of various formats can be created.
- Multilingual support for UI
- Compatible with Windows, Mac, and Linux

### Classic Singers (conventional UTAU voice banks)
- Basically the same format as UTAU. Character.txt, oto.ini, prefix.map, etc. can be used.
- All folders with character.txt in the voice folder are recognized as voice banks (the original UTAU recognizes only surface-level folders).
- OpenUtau's unique voicebank settings (VoiceColor, default Phonemizer, etc.) are recorded in the [character.yaml](tech-note:-character.yaml)

# Advanced
### ENUNU & SimpleENUNU
What is ENUNU: A technology that allows you to use the AI ​​singing voice synthesis system NNSVS on UTAU  
What is SimpleENUNU: Another version of ENUNU for enthusiasts and developers, that is more compatible with the latest NNSVS  

ENUNU models (AI voicebanks) are distributed by volunteers.  
OpenUtau also supports it on a trial basis. It can be used by installing the appropriate version of "ENUNU for OpenUtau" (aka ENUNUServer), launching it separately behind OU, and selecting ENUNU phonemizer.

- [Status of ENUNU NNSVS Support](Status-of-ENUNU-NNSVS-Support)
- [ENUNU Server for OpenUtau](https://github.com/rokujyushi/ENUNU/releases)
- [SimpleENUNU Server for OpenUtau](https://github.com/rokujyushi/SimpleEnunu/releases)

- **Attention**
    - Use "ENUNU for OpenUtau" and "ENUNUServer" for ENUNU models and "SimpleENUNUServer" for SimpleENUNU models.
    - When using SimpleENUNU models, add the following to character.yaml if not selected during installation:  
    ```
    singer_type: Enunu
    ```

# Quick Tips
