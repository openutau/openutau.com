This is a sample of the current version of `character.yaml` format. Note that it is still a work in progress and may change.

The example is based on `闇音レンリ・連続音Ver1.5`.

### About character.yaml
- `character.yaml` is the file used to store extra info that OpenUtau needs that cannot be captured by the traditional UTAU voicebank file set.
- Note that this is a [YAML](https://en.wikipedia.org/wiki/YAML) file. If you manually edit it, make sure you create a valid YAML file, especially you need exactly one space after ":". You may try to use a web YAML editor like [this one](https://codebeautify.org/yaml-editor-online).
- Every field is optional at the moment.

### Character Info
```
name: 闇音レンリ・連続音Ver1.5
text_file_encoding: shift_jis
image: renri.bmp
author: ゆずり
web: https://renrivoice.wixsite.com/renri-voice/utau
```
These are similar basic character info in `character.txt`. If not present, info in `character.txt` will be used.

### Portrait
```
portrait: portrait.png
portrait_opacity: 0.67
```
- A image file located in the voicebank folder can be used to display a portrait on Piano Roll. A relative path like "images\portrait.png" works too.
- The image is currently displayed in its original size unless the image is more than 800 **tall**, in which case will be resized to 800 tall.
- If you edit the file when OpenUtau is open, go to singers dialog and click "..." -> "Refresh" to reload it.

### Sub-banks
- `闇音レンリ・連続音Ver1.5` is a multi-pitch, multi-flavor bank.
- This voicebank has 3 flavors: Normal, `Whisper` and `Clear`
- This voicebank has 4 pitches: `A3`, `D4`, `G4`, `C5`.
- The 3 flavors and 4 pitches form 12 different subbanks in total, each has a different suffix.
- It also has some extras, notably `↑`
- Therefore in total 13 subbanks are specified in `character.yaml`

### Full Example
```name: 闇音レンリ・連続音Ver1.5
text_file_encoding: shift_jis
image: renri.bmp
portrait: portrait.webp
portrait_opacity: 0.67
author: ゆずり
web: https://renrivoice.wixsite.com/renri-voice/utau
subbanks:
- prefix: ''
  suffix: CC5
  tone_ranges:
  - C5-B7
  tags:
  - Clear
- prefix: ''
  suffix: CG4
  tone_ranges:
  - G4-B4
  tags:
  - Clear
- prefix: ''
  suffix: CD4
  tone_ranges:
  - D4-F#4
  tags:
  - Clear
- prefix: ''
  suffix: CA3
  tone_ranges:
  - C1-C#4
  tags:
  - Clear
- prefix: ''
  suffix: WC5
  tone_ranges:
  - C5-B7
  tags:
  - Whisper
- prefix: ''
  suffix: WG4
  tone_ranges:
  - G4-B4
  tags:
  - Whisper
- prefix: ''
  suffix: WD4
  tone_ranges:
  - D4-F#4
  tags:
  - Whisper
- prefix: ''
  suffix: WA3
  tone_ranges:
  - C1-C#4
  tags:
  - Whisper
- prefix: ''
  suffix: C5
  tone_ranges:
  - C5-B7
- prefix: ''
  suffix: G4
  tone_ranges:
  - G4-B4
- prefix: ''
  suffix: D4
  tone_ranges:
  - D4-F#4
- prefix: ''
  suffix: A3
  tone_ranges:
  - C1-C#4
- prefix: ''
  suffix: ↑
  tone_ranges:
  - C1-B7
  tags:
  - ↑
```