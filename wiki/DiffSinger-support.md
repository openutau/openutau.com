OpenUtau supports [DiffSinger (maintained by OpenVPI)](https://github.com/openvpi/diffsinger), a machine learning based singing synthesizer.

## Setup
Before using DiffSinger on OpenUtau, please download [nsf_hifigan vocoder](https://github.com/xunmengshe/OpenUtau/releases/download/0.0.0.0/nsf_hifigan.oudep) . Drag and drop to import it into OpenUtau.

Turn on "beta" in preferences and upgrade your OpenUtau, because some new voicebanks might use features not yet supported by the current stable build.

macOS 11 Big Sur or higher is required to use Diffsinger on macOS.

## Preferences
- Diffsinger Rendering speedup is 50 times by default. A smaller speedup may improve the quality of audio, but slow down the rendering.
- OpenUtau uses CPU to render by default. If you use Windows and have a discrete graphics card, you can use DirectML to make rendering faster. Please set "Machine Learning Runner" to "DirectML" (or "CoreML" on macOS), choose your discrete graphics card in "GPU" menu, and **restart your OpenUtau**.
<img src="https://user-images.githubusercontent.com/54425948/212444421-ad399723-d2ba-4e0e-9341-3aa40f502304.png" width="400"/>

## Expressions
Here are the expressions supported by DiffSinger:
  - PITD (pitch curve)
  - DYN (volume curve)
  - GENC (gender curve, need voicebank's support. See [here](https://github.com/openvpi/DiffSinger/releases/tag/v1.6.0#Overview) for details. The default range -100\~+100 equals to shifting the formant by +12\~-12 semitones.)
  - VELC (velocity curve, need voicebank's support. See [here](https://github.com/openvpi/DiffSinger/releases/tag/v1.6.0#Overview) for details. This expression will affect the speed of the head and tail of the vowels. Every increase of 100 in this expression will multiply the speed by 2.)
  - ENE (energy curve, need voicebank's support. See [here](https://github.com/openvpi/DiffSinger/releases/tag/v2.0.0) for details. This expression will manipulate the voice's energy, including manipulating the voicing amount.)
  - BREC (breathiness curve, need voicebank's support. See [here](https://github.com/openvpi/DiffSinger/releases/tag/v2.0.0) for details. This expression will manipulate the voice's breathiness; a higher curve increases it, while a lower curve decreases it.)
  - TENC (tension curve, need voicebank's support. See [here](https://github.com/openvpi/DiffSinger/releases/tag/v2.3.0) for details. This expression will affect the tenseness of the voice, e.g. manipulates power and nasality.)
  - VOIC (voicing curve, need voicebank's support. See [here](https://github.com/openvpi/DiffSinger/releases/tag/v2.3.0) for details. This expression will affect the amount of voicing, e.g. manipulates how much voicing is present on the voice. Similar to energy curve and is considered a "successor".)
  - PEXP (pitch expressiveness curve, voicebank needs to have a pitch model for this to work. See [here](https://github.com/openvpi/DiffSinger/releases/tag/v2.1.0) for details. This expression manipulates how expressive the rendered pitch will be. The default value is 100 (max).)
  - SHFC (tone shift curve, need vocoder's support See [here](https://github.com/openvpi/vocoders/releases/tag/pc-nsf-hifigan-44.1k-hop512-128bin-2025.02) for more details. This parameter can assign tones of voice from other vocal ranges to a different vocal range (e.g. whistle register to a lower note) to manipulate how the voice will sound. It can also be used to manually increase the vocal range of the voice.)
  - Voice color curves (no abbreviation; voicebank needs to contain vocal modes (voice colors). This allows for gradual transitions between different voice colors, akin to vocal modes in Synthesizer V or XSY in VOCALOID4.)

VELC, ENE, PEXP and voice color curves are custom expressions defined by DiffSinger and aren't included in new projects. To add these expressions into your project, click “Expressions → Add all expressions suggested by renderer”

You can also adjust the range of each expression in this menu.

<img width="453" alt="image" src="https://user-images.githubusercontent.com/54425948/221748809-ae6553d7-4a6b-4ec6-8c62-ea6fefb21f10.png">