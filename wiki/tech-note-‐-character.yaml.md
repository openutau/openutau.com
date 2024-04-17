This is a sample of the current version of `character.yaml` format. Note that it is still a work in progress and may change.

The example is based on `闇音レンリ・連続音Ver1.5`.

### About character.yaml
- `character.yaml` is the file used to store extra info that OpenUtau needs that cannot be captured by the traditional UTAU voicebank file set.
- The best way to edit `character.yaml` is from OpenUtau "Singers" dialog.
- If you manually edit it, note that this is a [YAML](https://en.wikipedia.org/wiki/YAML) file. Make sure you create a valid YAML file, especially you need exactly one space after ":". You may try to use a web YAML editor like [this one](https://codebeautify.org/yaml-editor-online).
- Every field is optional at the moment.
- The reason portrait size is scaled by its height (`portrait_height`) is because portrait images are usually longer than they are wide. Width scaling will be relative to height. Portrait images taller than 800px will be scaled down regardless of value.

### Encoding
```yml
text_file_encoding: shift_jis
```
The encoding used to read `character.txt`, `prefix.map` and `oto.ini`. The `character.yaml` itself and all the yaml dictionaries in the voicebank (such as `arpasing.yaml`), should always be `utf-8`.

### Character Info
```yml
name: 闇音レンリ・連続音Ver1.5
singer_type: utau
image: renri.bmp
author: ゆずり
voice: ゆずり
version: 1.5
web: https://renrivoice.wixsite.com/renri-voice/utau
```
These are similar basic character info in `character.txt`. If not present, info in `character.txt` will be used.

### Localized name
```yml
localized_names:
  en-US: Renri Yamine VCV Ver1.5
```
This will display localized names for the user's selected singer name display language.

available language codes: `en-US`, `de-DE`, `es-ES`, `es-MX`, `fi-FI`, `fr-FR`, `id-ID`, `it-IT`, `ja-JP`, `ko-KR`, `nl-NL`, `pl-PL`, `pt-BR`, `ru-RU`, `th-TH`, `vi-VN`, `zh-CN`, `zh-TW`
### Portrait
```yml
portrait: portrait.png
portrait_opacity: 0.67
portrait_height: 0
```
- A image file located in the voicebank folder can be used to display a portrait on Piano Roll. A relative path like "images\portrait.png" works too.
- Unless `portrait_height` is defined, the image is currently displayed in its original size unless the image is more than 800 **tall**, in which case will be resized to 800 tall. `0` means it will use the default values (this is so that smaller images don't scale up to a height of 800px by default, unless manually defined).
- If you edit the file when OpenUtau is open, go to singers dialog and click "..." -> "Refresh" to reload it.

### Sub-banks (Voice Color)
- `闇音レンリ・連続音Ver1.5` is a multi-pitch, multi-color bank.
- This voicebank has 3 voice colors: Normal, `Whisper` and `Clear`
- This voicebank has 4 tone ranges: `A3`, `D4`, `G4`, `C5`.
- The 3 voice colors and 4 tone ranges form 12 different subbanks in total, each has a different suffix.
- It also has some extras, notably `↑`, `Edge`. These are simply mapped to full tone range.
- Therefore in total 14 subbanks are specified in `character.yaml`. The suffixes visualized in table looks like:

|             | C1-C#4 | D4-F#4 | G4-B4 | C5-B7 |
| ----------- | ------ | ------ | ----- | ----- |
| **(main)**  | A3     | D4     | G4    | C5    |
| **Clear**   | CA3    | CD4    | CG4   | CC5   | 
| **Whisper** | WA3    | WD4    | WG4   | WC5   | 
| **Edge**    | '      | '      | '     | '     |
| **↑**       | ↑      | ↑      | ↑     | ↑     |

- To apply the above configuration. Go to `Tools` -> `Singers` -> `Edit Subbanks`. The final result should look like:

![subbanks](https://i.imgur.com/XznEdSu.png)

### Full Example
```yml
name: 闇音レンリ・連続音Ver1.5
localized_names:
  en-US: Renri Yamine VCV Ver1.5
singer_type: utau
text_file_encoding: shift_jis
image: renri.bmp
portrait: portrait.webp
portrait_opacity: 0.67
portrait_height: 0
author: ゆずり
voice: ゆずり
version: 1.5
web: https://renrivoice.wixsite.com/renri-voice/utau
default_phonemizer: OpenUtau.Plugin.Builtin.JapaneseVCVPhonemizer
subbanks:
- color: ''
  prefix: ''
  suffix: C5
  tone_ranges:
  - C5-B7
- color: ''
  prefix: ''
  suffix: G4
  tone_ranges:
  - G4-B4
- color: ''
  prefix: ''
  suffix: D4
  tone_ranges:
  - D4-F#4
- color: ''
  prefix: ''
  suffix: A3
  tone_ranges:
  - C1-C#4
- color: ↑
  prefix: ''
  suffix: ↑
  tone_ranges:
  - C1-B7
- color: Clear
  prefix: ''
  suffix: CC5
  tone_ranges:
  - C5-B7
- color: Clear
  prefix: ''
  suffix: CG4
  tone_ranges:
  - G4-B4
- color: Clear
  prefix: ''
  suffix: CD4
  tone_ranges:
  - D4-F#4
- color: Clear
  prefix: ''
  suffix: CA3
  tone_ranges:
  - C1-C#4
- color: Whisper
  prefix: ''
  suffix: WC5
  tone_ranges:
  - C5-B7
- color: Whisper
  prefix: ''
  suffix: WG4
  tone_ranges:
  - G4-B4
- color: Whisper
  prefix: ''
  suffix: WD4
  tone_ranges:
  - D4-F#4
- color: Whisper
  prefix: ''
  suffix: WA3
  tone_ranges:
  - C1-C#4
- color: Edge
  prefix: ''
  suffix: "'"
  tone_ranges:
  - C1-B7
```