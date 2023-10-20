OpenUtau supports [DiffSinger (maintained by OpenVPI)](https://github.com/openvpi/diffsinger), a machine learning based singing synthesizer.

## Setup
Before using DiffSinger on OpenUtau, please download [nsf_hifigan vocoder](https://github.com/xunmengshe/OpenUtau/releases/download/0.0.0.0/nsf_hifigan.oudep) . Drag and drop to import it into OpenUtau.

## Preferences
- Diffsinger Rendering speedup is 50 times by default. A smaller speedup may improve the quality of audio, but slow down the rendering.
- OpenUtau uses CPU to render by default. If you use Windows and have a discrete graphics card, you can use DirectML to make rendering faster. Please set "Machine Learning Runner" to "directml", choose your discrete graphics card in "GPU" menu, and **restart your OpenUtau**.
<img src="https://user-images.githubusercontent.com/54425948/212444421-ad399723-d2ba-4e0e-9341-3aa40f502304.png" width="400"/>

## Expressions
Here are the expressions supported by DiffSinger:
  - PITD (pitch curve)
  - DYN (volume curve)
  - GENC (gender curve, need voicebank's support. See [here](https://github.com/openvpi/DiffSinger/releases/tag/v1.6.0#Overview) for details. The default range -100\~+100 equals to shifting the formant by +12\~-12 semitones.)
  - VELC (velocity curve, need voicebank's support. See [here](https://github.com/openvpi/DiffSinger/releases/tag/v1.6.0#Overview) for details. This expression will affect the speed of the head and tail of the vowels. Every increase of 100 in this expression will multiply the speed by 2.)

VELC is a custom expression defined by DiffSinger and isn't included in new projects. To add this expression into your project, click “Expreeions → Add all expressions suggested by renderers”

You can also adjust the range of each expression in this menu.

<img width="453" alt="image" src="https://user-images.githubusercontent.com/54425948/221748809-ae6553d7-4a6b-4ec6-8c62-ea6fefb21f10.png">