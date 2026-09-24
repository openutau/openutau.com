これは現バージョンでの`character.yaml`のサンプルです。開発中のため変更する可能性があります。

例として`闇音レンリ・連続音Ver1.5`を使用します。

### character.yamlについて
- `character.yaml`は従来のUTAU音源内のファイルからは取得できない、OpenUTAUで必要な追加情報を保存するためのファイルです。
- `character.yaml`を編集するには、OpenUTAUの「シンガー」ダイアログを使うのがベストです。
- 手動で編集する場合、このファイルが[YAML](https://en.wikipedia.org/wiki/YAML)形式であることに注意してください。YAMLファイルが正しく作れているか確認しましょう。特に、「:」の後に半角スペースを一つ入れるのを忘れないでください。[このような](https://codebeautify.org/yaml-editor-online)Web YAMLエディタを使うのもいいでしょう。
- 現時点では、すべての項目はオプションです。
- 立ち絵が高さ（`portrait_height`）基準で拡大縮小されるのは、通常立ち絵は横よりも縦が長いからです。幅は高さに比例して拡大縮小します。高さが800pxを超える立ち絵は、値に関係なく縮小されます。

### エンコード
```yml
text_file_encoding: shift_jis
```
エンコードは`character.txt`・`prefix.map`・`oto.ini`を読み込むときに使われます。`character.yaml`と音源に同梱するyaml形式の辞書ファイル（`arpasing.yaml`など）は、`utf-8`である必要があります。

### キャラクター情報
```yml
name: 闇音レンリ・連続音Ver1.5
singer_type: utau
image: renri.bmp
author: ゆずり
voice: ゆずり
version: 1.5
web: https://renrivoice.wixsite.com/renri-voice/utau
```
この部分はUTAUの`character.txt`に似ています。この項目が存在しない場合は`character.txt`の情報が使用されます。

### ローカライズ名
```yml
localized_names:
  en-US: Renri Yamine VCV Ver1.5
```
シンガー名が表示言語に合わせてローカライズされるとき、ここにある名前が使われます。

使用可能な言語コード: `en-US`, `de-DE`, `es-ES`, `es-MX`, `fi-FI`, `fr-FR`, `id-ID`, `it-IT`, `ja-JP`, `ko-KR`, `nl-NL`, `pl-PL`, `pt-BR`, `ru-RU`, `th-TH`, `vi-VN`, `zh-CN`, `zh-TW`
### 立ち絵
```yml
portrait: portrait.png
portrait_opacity: 0.67
portrait_height: 0
```
- 音源フォルダー内にある画像ファイルを使って、立ち絵をピアノロールに表示することができます。「images\portrait.png」のような相対パスも使用できます。
- `portrait_height`が定義されていなければ、画像は今のところ元のサイズで表示されます。ただし、画像の**高さ**が800を超える場合は、高さが800にリサイズされます。`0`の場合はデフォルト値を使用します（手動で定義されていないときに、小さい画像が高さ800pxまで拡大されないようにするため）。
- OpenUTAUの起動中にファイルを編集した場合は、シンガーダイアログで"..." -> "更新"をクリックして再読み込みしてください。

### サブバンク (Voice Color)
- `闇音レンリ・連続音Ver1.5`は多音階で、表情が複数ある音源です。
- 表情は`Normal`, `Whisper` `Clear`の3個です。
- 音階は`A3`, `D4`, `G4`, `C5`の4個です。
- 3つの表情が4音階でサブバンクは合計12種類となり、それぞれサフィックスが異なります。
- また、`↑`、`Edge`などの表情もあります。これらは単純に全音域に割り当てられます。
- したがって、`character.yaml`で指定するサブバンクは合計14個です。サフィックスを表にすると次のようになります。

|             | C1-C#4 | D4-F#4 | G4-B4 | C5-B7 |
| ----------- | ------ | ------ | ----- | ----- |
| **(main)**  | A3     | D4     | G4    | C5    |
| **Clear**   | CA3    | CD4    | CG4   | CC5   | 
| **Whisper** | WA3    | WD4    | WG4   | WC5   | 
| **Edge**    | '      | '      | '     | '     |
| **↑**       | ↑      | ↑      | ↑     | ↑     |

- 上記の構成を適用するには「ツール」->「シンガー」->「サブバンクの編集」からサブバンクを編集してください。最終的にはこのようになります。

![subbanks](https://i.imgur.com/XznEdSu.png)

### 全て記述した例
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