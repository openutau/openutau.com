resamplerは音声合成の主要な作業を行う合成エンジンで、音声サンプルのピッチと長さを変更しフラグの音質の変更を適用します。
OpenUtauには`worldline`というresamplerが同梱されています。また、外部のresamplerも多数存在します。
resamplerを変更すると、合成された音声の音質が変わります。また、resamplerによって使えるフラグも異なります。

wavtoolは、resamplerから渡された音声を繋ぎ合わせて一つの音声にするプログラムです。OpenUtauには`simple`と`convergence`という2つのwavtoolが同梱されています。また、外部のwavtoolも多数存在します。
wavtoolを変更すると、音声の繋ぎ合わせかたが変わります。

# resamplerのインストール
resamplerをインストールして、使えるようにするために"CLASSIC"レンダラーに切り替えてください。

##  Windows

resamplerは実行ファイル(`.exe`)である必要があります。resamplerは`Resamplers`フォルダーの子フォルダー内に置くこともできます。
1. OpenUtauがインストールされているフォルダーの中で`Resamplers`というフォルダーを探します。
2. `Resamplers`フォルダーを開き、その中にresamplerを入れます。

OpenUtauのバージョン0.1.119以降では、`.exe`ファイルをOpenUtauのメインウィンドウにドラッグ＆ドロップして、「Install as resampler」を選択すると、resamplerをインストールできます。

<img src="https://github.com/stakira/OpenUtau/assets/18076904/1a13d37d-b472-451d-b24a-e984b095bd4a" height="250">


## MacOS
[Macres](https://github.com/titinko/macres/releases)がmacOS版を提供しています。これをOpenUTAUのResamplersフォルダーに入れます。

Wineを使用してWindows用のresamplerを使うこともできます。(macOS 11.6でテスト済み)

1. [homebrew](https://brew.sh/ja/)をインストールします。
2. 以下のコマンドを使って[wine](https://github.com/Gcenx/homebrew-wine)をインストールします。
```
brew tap gcenx/wine
brew install --cask --no-quarantine wine-crossover
```
3. [release page](https://github.com/stakira/OpenUtau/releases/tag/OpenUtau-Latest)から"mac_additional.zip"をダウンロードします。
4. `mac_additional.zip`内の`moresampler.sh`スクリプトを使用して、resamplerを使えるようにします。これによってresamplerのファイル名が`moresampler-0.8.4/moresampler.exe`に置き換わります。

このスクリプトは`Resamplers`フォルダーに追加する必要があり、`.exe`形式のresamplerを追加するたびに編集する必要があります。

## Linux
[Macres](https://github.com/titinko/macres/releases)がLinux版を提供しています。これをOpenUTAUのResamplersフォルダーに入れます。

WindowsのresamplerをLinuxで使えるようにするには、以下の方法を使用します。

1. [Wine](https://www.winehq.org/)をインストールします。
2. `Resamplers`フォルダーを開きます。(`/home/your_username/OpenUtau/Resamplers/`にあるはずです)
3. 導入するresamplerの名前で新しいテキストファイルを作成します（拡張子は要りません）。
4. テキストファイルを開き、次のスクリプトを追加します。
```
#!/bin/bash
LANG="ja_JP.UTF8" wine "/[resamplerのあるフォルダーまでの絶対パス]/resampler.exe" "${@,-1}"
```
5. `"[resamplerのあるフォルダーまでの絶対パス]/resampler.exe"`をresamplerのファイル名に変更してください。
6. OpenUtauを再起動します。

# テスト済みresamplerとその情報
OpenUtauでテストしたすべてのresamplerのリストです。

## Windows

|  Resampler |  作者  |  備考 |
| ------------ | ------------ | ------------ |
|  worldline  | StAkira  |   OpenUtauに同梱。すべてのプラットフォームで動作します。|
|  [bkh01.exe](http://z-server.game.coocan.jp/utau/utautop.html#bkh01) |  Zteer |   |
|  [doppeltler32.exe](http://utau2008.xrea.jp/2020/engine/) | 飴屋/菖蒲  |   |
|  [doppeltler64.exe](http://utau2008.xrea.jp/2020/engine/) | 飴屋/菖蒲 |   |
| [EFB-GT.exe](http://custom-made.seesaa.net/article/312529786.html) | Custom.Maid | |
| EFB-PB.exe | Custom.maid | |
|  [f2resamp32.exe](http://utau2008.xrea.jp/2020/engine/f2resamp004.zip) | 飴屋/菖蒲 |   |
|  [f2resamp64.exe](http://utau2008.xrea.jp/2020/engine/f2resamp004.zip) | 飴屋/菖蒲  |   |
|  [fresamp11.exe](http://utau2008.xrea.jp/downloads/fresamp011.zip) | 飴屋/菖蒲  |   |
|  fresamp12.exe | 飴屋/菖蒲 |   |
|  [fresamp14.exe](http://utau2008.xrea.jp/downloads/fresamp014.zip) | 飴屋/菖蒲   |   |
| [fresamp14omp.exe](http://utau2008.xrea.jp/downloads/fresamp014omp.zip)  | 飴屋/菖蒲 | fresamp14.exeより描画速度が速いOpenMPに移植|
| [lessampler.exe](https://github.com/YuzukiTsuru/lessampler/releases/) | YuzukiTsuru | [互換性のための調整を参照](https://github.com/stakira/OpenUtau/wiki/ResamplerとWavtool(日本語)#互換性のための調整) |
| [macres.exe](https://github.com/titinko/macres/releases)   | titinko   |   |
| model4.exe  | 飴屋/菖蒲  |   |
| [moresampler.exe](https://bowlroll.net/file/139123) |  Kanru Hua |  [互換性のための調整を参照](https://github.com/stakira/OpenUtau/wiki/ResamplerとWavtool(日本語)#互換性のための調整) |
| [phavoco.exe](http://utau2008.xrea.jp/downloads/phavoco010.zip) | 飴屋/菖蒲   |   |
| [phaavoco.exe](http://utau2008.xrea.jp/2020/engine/phaavoco001.zip) | 飴屋/菖蒲 |   |
| resampler.exe  | 飴屋/菖蒲  | UTAU同梱のresampler|
| [SpaceWorld_win64.exe](https://github.com/LovelyA72/SpaceWorld/releases) | LovelyA72 | [互換性のための調整を参照](https://github.com/stakira/OpenUtau/wiki/ResamplerとWavtool(日本語)#互換性のための調整) |
|[StrayCatRunner.exe](https://github.com/Astel123457/straycat-server) | Astel123457 |   |
|[StrayCat.py](https://github.com/UtaUtaUtau/straycat) | UtaUtaUtau |   |
| [TIPS.exe](http://scientistb.web.fc2.com/program/)  | ScientistB |   |
| [tn_fnds.exe](http://z-server.game.coocan.jp/utau/utautop.html#tn_fnds) | Zteer |  |
| [UDB](https://github.com/YuzukiTsuru/UDB/releases/tag/0.0.3.1) | YuzukiTsuru | UDBはUTAU Debug Engineという意味|
| [vs4u.exe](http://ackiesound.ifdef.jp/download.html#vs4u) | あっきー |  |
| [w4u.exe](http://utau2008.xrea.jp/downloads/w4u001.zip) | Zany |   |
| [WARP.exe](http://custom-made.seesaa.net/article/312530509.html) | Custom.Maid | |
| [wn4u.exe](https://utaforum.net/threads/world4utau-update.20035/) | Zany | [互換性のための調整を参照](https://github.com/stakira/OpenUtau/wiki/ResamplerとWavtool(日本語)#互換性のための調整) |
| [young3.exe](https://bowlroll.net/file/203018) | Zany |   |

### 互換性のための調整

- [moresampler.exe](https://bowlroll.net/file/139123)
  - `moresampler.exe`とデフォルト状態の`moreconfig.txt`を`Resamplers`フォルダーに追加します。
  - `moresampler.exe`のみを`wavtools`フォルダーに追加します（`moreconfig.txt`は必要なし）。
  - moresamplerがresamplerとして、またはwavtoolとresamplerの両方として動作するようになります。
- [[SpaceWorld_win64.exe|https://github.com/LovelyA72/SpaceWorld/releases]] and [[wn4u.exe|https://utaforum.net/threads/world4utau-update.20035/]]
    - 音源にfrqファイルがない場合、問題が発生する可能性があります。SpaceWorldバージョン1.0.1では、frqファイルが見つからない場合でもクラッシュしません。
- [[lessampler|https://github.com/YuzukiTsuru/lessampler/releases/]]
    - 開発中でフラグが不足しています
    - 過大な音声モデルに注意

## MacOS
|  Resampler |  作者  |  備考 |
| ------------ | ------------ | ------------ |
|  worldline  | StAkira  |   OpenUtauに同梱。すべてのプラットフォームで動作します。|
| [macres](https://github.com/titinko/macres/releases)   | titinko   |   |

## Linux
|  Resampler |  作者  |  備考 |
| ------------ | ------------ | ------------ |
|  worldline  | StAkira  |   OpenUTAUに同梱。すべてのプラットフォームで動作します。|
| [macres](https://github.com/titinko/macres/releases)   | titinko   |   |

# resamplerマニフェスト
resamplerマニフェストとは、resamplerが対応している機能を保存するYAMLファイルです。resamplerマニフェストがあると、表情エディターの「使用可能な表情をまとめて追加する」ボタンを使ってresamplerが対応しているすべてのフラグをまとめて追加できます。

<img width="453" alt="image" src="https://user-images.githubusercontent.com/54425948/227085816-4cced732-98dd-4c76-bc40-9a94f971a066.png">

resamplerマニフェストは、resamplerの実行ファイルと同じ名前で、同じフォルダーに置く必要があります。resamplerマニフェストのファイル拡張子は`.yaml`である必要があります。例えば、`moresampler.exe`のresamplerマニフェストは`moresampler.yaml`ファイルで、`moresampler.exe`と同じフォルダーに置く必要があります。

以下はMoresamplerのすべての機能を入れたresamplerマニフェストの例です。OpenUtauでリサンプラーマニフェストを作成するには、任意の`.ustx`プロジェクトファイルにresamplerの表情を追加します。テキストエディターでプロジェクトファイルを開き、`expressions:`セクションを空のマニフェストファイルにコピーします。
```yaml
expressions:
  gen:
    name: Gender Factor
    abbr: gen
    type: Numerical
    min: -100
    max: 100
    default_value: 0
    is_flag: true
    flag: g
  mbre:
    name: Breathiness (Moresampler)
    abbr: mbre
    type: Numerical
    min: -100
    max: 100
    default_value: 0
    is_flag: true
    flag: Mb
  tens:
    name: Tension
    abbr: tens
    type: Numerical
    min: -100
    max: 100
    default_value: 0
    is_flag: true
    flag: Mt
  pit:
    name: Pitch deviation (flag)
    abbr: pit
    type: Numerical
    min: -1200
    max: 1200
    default_value: 0
    is_flag: true
    flag: t
  pkcp:
    name: Peak Compressor
    abbr: pkcp
    type: Numerical
    min: 0
    max: 100
    default_value: 86
    is_flag: true
    flag: P
  amp:
    name: Amplitude Modulation
    abbr: amp
    type: Numerical
    min: -100
    max: 100
    default_value: 0
    is_flag: true
    flag: A
  cons:
    name: Unvoiced Consonant Gain
    abbr: cons
    type: Numerical
    min: -20
    max: 100
    default_value: 0
    is_flag: true
    flag: b
  fstr:
    name: Force Stretch
    abbr: fstr
    type: Options
    min: 0
    max: 1
    default_value: 0
    is_flag: true
    options:
    - ''
    - e
    - Me
  opn:
    name: Openness
    abbr: opn
    type: Numerical
    min: -100
    max: 100
    default_value: 0
    is_flag: true
    flag: Mo
  res:
    name: Resonance
    abbr: res
    type: Numerical
    min: -100
    max: 100
    default_value: 0
    is_flag: true
    flag: Mr
  dry:
    name: Dryness
    abbr: dry
    type: Numerical
    min: -100
    max: 100
    default_value: 0
    is_flag: true
    flag: Md
  cors:
    name: Coarseness
    abbr: cors
    type: Numerical
    min: 0
    max: 100
    default_value: 0
    is_flag: true
    flag: MC
  grwl:
    name: Growl
    abbr: grwl
    type: Numerical
    min: 0
    max: 100
    default_value: 0
    is_flag: true
    flag: MG
  dist:
    name: Distortion
    abbr: dist
    type: Numerical
    min: 0
    max: 100
    default_value: 0
    is_flag: true
    flag: MD
  stbl:
    name: Stabilization
    abbr: stbl
    type: Numerical
    min: 0
    max: 10
    default_value: 0
    is_flag: true
    flag: Ms
  mint:
    name: Model Interpolation
    abbr: mint
    type: Numerical
    min: 0
    max: 100
    default_value: 100
    is_flag: true
    flag: Mm
```

# Wavtoolのインストール

## Windows
1. 展開したOpenUtauフォルダーで、`Wavtools`というフォルダーを探します。
2. `Wavtools`フォルダを開き、ダウンロードしたwavtoolをそのフォルダーに置きます。

OpenUtau バージョン 0.1.119以降でwavtoolをインストールするには、`.exe`ファイルをOpenUtauのメインウィンドウにドラッグ＆ドロップして、「Install as wavtool」を選択します。

<img src="https://github.com/stakira/OpenUtau/assets/18076904/1a13d37d-b472-451d-b24a-e984b095bd4a" height="250">

## macOS / Linux

外部のwavtoolは、現在のところmacOSやLinuxでサポートされていません。  

# テストされたwavtoolとその情報
以下はOpenUtauでテストしたすべてのwavtoolのリストです。

| Wavtool | Author | Additonal Notes |
| --------- | -------- | ------------------ |
| simple | StAkira | OpenUtauに同梱。すべてのプラットフォームで動作します。|
| convergence | StAkira | OpenUtauに同梱。位相補正を使用|
| [moresampler.exe](https://bowlroll.net/file/139123) | Kanru Hua | [互換性のための調整を参照](https://github.com/stakira/OpenUtau/wiki/ResamplerとWavtool(日本語)#互換性のための調整) |
| [wavtool64](http://utau2008.xrea.jp/2020/engine/wavtool64.zip) | 飴屋/菖蒲 | |
| [wavtool4vcv](https://www.mediafire.com/file/1iwrak88c6xzb87/wavtool4vcv20141202.zip/file) | nmasao | |