This page is open to edit by anyone in the community. Feel free to add your tutorials, guides, notes, or any tip tweets in "Quick Tips" below!

# Basics
### Installation and basic usage
See our [Install](Install) page for instructions to download and install OpenUtau.  
See our [Getting Started](Getting-Started) page for basic usage and control guides.

### Introduction

OpenUtau is a free, open-source editor made for the UTAU community, by the UTAU community.  
This project is developed by a large number of volunteers, not by companies or individuals.  
You can ask questions, report bugs, and suggest new features on the [official Discord server](https://discord.gg/UfpMnqMmEM).

### Differences from original UTAU
- OpenUtau supports **multiple vocal tracks** as well as **audio tracks** for easy layouts and live previews of large projects.
- OpenUtau **pre-renders** vocal tracks in the background while editing, allowing users to preview their work quickly.  
This feature can be disabled in the Preferences menu for users who prefer to render their vocals on demand.  
- **Rendering:**  
There are two render modes in OpenUtau.  
    1. The CLASSIC renderer allows users to resample vocals with their resampler or wavtool of choice. OpenUtau is built to be compatible with most UTAU resamplers and wavtools out of the box.  
    2. WORLDLINE-R, a renderer unique to OpenUtau, combines a native resampler and wavtool into one mode. With WORLDLINE-R, users can make use of exclusive curve-based parameters similar to conventional vocal synth software, allowing for more dynamic vocal sounds.  
- **Phonemizers:**  
Phonemizers add the ability to convert lyrics to phonemes in real-time, in a fashion similar to modern vocal synth software.  
Lyrics entered into notes are automatically converted to phonemes used in a voicebank, with no effort from the user.  
Various phonemizers are available for a wide range of languages and voicebank types (VCV, CVVC, VCCV, Arpasing, and more).
- **Voice colors:**  
Voice colors allow you to switch voicebank styles (appends) on a per-note basis, as well as allowing you to assign suffixes for a voicebank's recorded vocal ranges.  
Voice colors can be defined by assigning a voicebank's appends and vocal range to a new voice color in the Singer editor. Voice colors can be selected during editing via the CLR parameter in the Piano Roll.  
OpenUtau does not support adding appends or suffixes to lyrics, as UTAU requires. Voice colors are handled automatically by OpenUtau when the vocals are rendered.
- **Expression panel:**  
Note volume, note flags, engine (resampler) switching, voice colors, etc. are easily editable in the Expressions panel found at the bottom of the Piano Roll window.  
Unlike UTAU, flags do not have to be set by being manually typed in a separate menu.  Instead, note flags are easily changed by dragging sliders in the Expressions panel. Effects of flags can be heard immediately upon playing the project.  
Custom expressions of various formats can be created.
- OpenUtau supports various languages in the user interface, and can be changed easily in the Preferences menu.
- OpenUtau is compatible with Windows, macOS, and many different flavors/distros of Linux.

### Classic singer support (conventional UTAU voice banks)
- OpenUtau attempts to follow the same format as UTAU. `character.txt`, `oto.ini`, `prefix.map`, etc. are all recognized by OpenUtau when a voicebank is installed.
- The "Singers" folder does not have to follow a rigid structure. Any folder inside the Singers folder containing a `character.txt` will be recognized by OpenUtau as a voicebank, whereas UTAU will only recognize voicebanks in the first layer of its "Singers" folder.  
- Bank settings such as voice colors, default phonemizer, and other unique settings are saved inside the voicebank in the [`character.yaml`](tech-note:-character.yaml) file. Voicebanks used in OpenUtau can be shared with other OpenUtau users without requiring a complicated setup.

## Voicebank Creation and Development
This is a vast topic to cover, and many resources and methods were established far before OpenUtau existed. Many great resources for developing UTAU voicebanks can be found across the internet! But to get started, as well as get a quick touch point for OpenUtau-specific information, visit the page below:
- https://github.com/stakira/OpenUtau/wiki/Voicebank-development

# Advanced features
### ENUNU & SimpleENUNU
ENUNU is a new technology that allows users to render vocals with the open-source AI voice synthesis software, NNSVS.  
SimpleENUNU is a different version of ENUNU intended for enthusiasts and developers, which is more up-to-date with the latest experimental versions of NNSVS.  

ENUNU models (AI voicebanks) are created and distributed by volunteers.  
OpenUtau supports ENUNU and SimpleENUNU as an experimental trial.  
  
To use an ENUNU bank in OpenUtau, simply install the appropriate version of "ENUNU for OpenUtau" (technically known as ENUNUServer), matching the ENUNU bank's version. Launch the ENUNU server and leave it running in the background. Select the ENUNU phonemizer.  
  
When an ENUNU bank is selected in OpenUtau, the ENUNU server will render the vocals and send them back to OpenUtau automatically.  
  
For more information on ENUNU support in OpenUtau, or to download the ENUNU/SimpleENUNU servers, see these pages:
- [Status of ENUNU NNSVS Support](Status-of-ENUNU-NNSVS-Support)
- [ENUNU Server for OpenUtau](https://github.com/rokujyushi/ENUNU/releases)
- [SimpleENUNU Server for OpenUtau](https://github.com/rokujyushi/SimpleEnunu/releases)

### Important note for ENUNU/SimpleENUNU users
- The voicebank must match the ENUNU server that is installed. ENUNU models can only use "ENUNU Server for OpenUtau". Likewise, SimpleENUNU models can only use "SimpleENUNU Server for OpenUtau".
- When using SimpleENUNU models, make sure the voicebank's `character.yaml` file includes the following line, if not selected during voicebank installation:
```
singer_type: Enunu
```

# Quick Tips
Got any tips for editing with OpenUtau? Feel free to share them here, or link them from social media!

### [VCCV English tutorial](https://docs.google.com/document/d/e/2PACX-1vRZ6ttcFIn56hgyYjxNwrP40KMfZbgoTlipaYKTyv6q2Sa9H4m3kc9uaQYUXe40uPTdXyDwtJQz-ATl/pub) by Anjo
This is a small VCCV English tutorial. If anything is confusing please feel free to ping @Anjo_39 in the OU Discord Server, I will try to respond as soon as I can. 