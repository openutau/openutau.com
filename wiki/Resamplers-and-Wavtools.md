In UTAU, resampler is the core engine that does the major works of synthesis: changing the pitch and duration of the audio sample, and applying flags to the audio. Audio rendered with different resamplers has different sound quality. Different resamplers also provide different set of flags. OpenUtau ships with a resampler, `worldline`. There are also many third-party resamplers.

Wavtool is the program that concatenates the audio slices from resampler into the final audio. OpenUtau ships with two wavtools, `simple` and `convergence`. There are also many third-party wavtools.

# Installing Resamplers
After you install resampler, please switch to "CLASSIC" renderer to use the resampler you installed.

##  Windows

Resampler must be an executable (`.exe`). Resamplers can be placed in subfolders inside the `Resamplers` folder.
1. In the OpenUtau folder, locate the resampler folder named `Resamplers`.
2. Open the resampler folder and place the resampler in the folder.

In OpenUtau version 0.1.119 or higher, resamplers can be installed by dragging and dropping the `.exe` file onto the main OpenUtau window and selecting "Install as resampler".

<img src="https://github.com/stakira/OpenUtau/assets/18076904/1a13d37d-b472-451d-b24a-e984b095bd4a" height="250">


## MacOS

Before we get into this process, I need to clarify that it is only possible on MacOS 13.7.1 (Ventura) or later, as Homebrew has discontinued its service for any older versions of MacOS. For older versions of MacOS, Macres provides a native macOS version. Put it into the resamplers folder of OpenUtau.

You can also use Windows resamplers with Wine: (tested on macOS 11.6)

### Section 1, “Installing Homebrew.”

To install Homebrew you will need to head over to the Homebrew website.

[https://brew.sh/](https://brew.sh/)

From here, you will want to copy the installation command, and open Terminal. If you are not familiar with Terminal, here is the path. <code>Applications > Utilities > Terminal.</code>

1. In the Terminal control panel, you will want to paste the installation command into the console. It will begin running the installation.
2. The installation will pause and ask for your computer’s passkey. Input the passkey and the installation will continue.
3. After it installs the, _“X code command line tools,”_ it may run into a fatal error when updating the Homebrew install. Do not worry, head over to, System Preferences > Security and Privacy, and scroll down until you see, _“allow install–sh.”_ Select OK to continue.
    Now it will run the rest of the install and you have successfully Homebrewed your Mac.

### Section 2, "Installing Wine.”

In order to install Wine, head to the WineHQ website.

[https://github.com/Gcenx/macOS_Wine_builds/releases](https://github.com/Gcenx/macOS_Wine_builds/releases)

1. Download Wine Staging from the Github releases page.
2. Drag the Wine Staging .zip to your desktop and extract.
3. After extracting the zip, run the Wine Staging application.
4. The Wine installer will run into an error since it is an external application downloaded from the internet. Head to <code>System Preferences > Security and Privacy</code>, and allow Wine access to run. After this, Wine will be installed to your computer.

After performing these two steps, we will then prepare the environment for the resamplers. Inside of Terminal we will want to begin a new session and run the installation for Wine Crossover.
```
    brew tap gcenx/wine
    brew install –cask –no-quarantine wine-crossover
```
After running these two commands your environment is set!

### Section 3, “How to run resamplers on MacOS.”

Now that you have installed both Wine and Homebrew onto your computer, we will now begin the process for installing the resamplers into MacOS. 

1. To install Windows resamplers (e.g. `resampler.exe`), drag the .exe into the OpenUtau window and choose `Install as resampler`.
2. Enable wine compatibility by setting wine path in `Tools > Preferences > Advanced > Wine Path...`. Clicking `Detect` should automatically pick wine from your `$PATH`, otherwise click `Select` to pick it yourself.
3. You can now use Windows resamplers in OpenUtau.

## Linux
[Macres](https://github.com/titinko/macres/releases) provides a native Linux version. Put it into the resamplers folder of OpenUtau.

To use Windows resamplers into Linux, follow this method:

1. Install [Wine](https://www.winehq.org/)
2. Put any Windows resampler to `Resamplers` folder (should be on `~/.local/share/OpenUtau/Resamplers`). You can also install it by using `Tools > Install Wavtool/Resampler (.exe)` in OpenUtau. Choose `Install as resampler`.
3. In OpenUtau, enable wine compatibility by setting wine path in `Tools > Preferences > Advanced > Wine Path...`. Clicking `Detect` should automatically pick wine from your `$PATH`, otherwise click `Select` to pick it yourself.
4. You can now use Windows resamplers in OpenUtau.

# Tested Resamplers and Directories
This is a list of all UTAU resamplers tested with OpenUtau.

## Windows

|  Resampler |  Author  |  Resample Manifest  |  Additional Notes |
| ------------ | ------------ | ------------ | ------------ |
|  worldline  | StAkira |    |   Built into OpenUtau. Works on all platforms. |
|  [bkh01.exe](http://z-server.game.coocan.jp/utau/utautop.html#bkh01) |  Zteer |   |
|  [doppeltler32.exe](http://utau2008.xrea.jp/2020/engine/) | Ameya  | [doppeltler32.yaml](https://github.com/Cadlaxa/Resampler-Manifests/blob/main/Resampler%20Manifests/doppeltler32.yaml)  |
|  [doppeltler64.exe](http://utau2008.xrea.jp/2020/engine/) | Ameya | [doppeltler64.yaml](https://github.com/Cadlaxa/Resampler-Manifests/blob/main/Resampler%20Manifests/doppeltler64.yaml)  |
| [EFB-GT.exe](http://custom-made.seesaa.net/article/312529786.html) | Custom.Maid | |
| EFB-PB.exe | Custom.maid ||
|  [f2resamp32.exe](http://utau2008.xrea.jp/2020/engine/f2resamp004.zip) | Ameya | [f2resamp32.yaml](https://github.com/oxygen-dioxide/openutau-manifests/blob/main/f2resamp.yaml)  |
|  [f2resamp64.exe](http://utau2008.xrea.jp/2020/engine/f2resamp004.zip) | Ameya  | [f2resamp64.yaml](https://github.com/oxygen-dioxide/openutau-manifests/blob/main/f2resamp.yaml)  |
|  [fresamp11.exe](http://utau2008.xrea.jp/downloads/fresamp011.zip) | Ameya  ||
|  fresamp12.exe | Ameya |   |
|  [fresamp14.exe](http://utau2008.xrea.jp/downloads/fresamp014.zip) | Ameya   | |
| [fresamp14omp.exe](http://utau2008.xrea.jp/downloads/fresamp014omp.zip)  | Ameya |  | Ported to OpenMP with faster rendering speed than fresamp14.exe. |
| [lessampler.exe](https://github.com/YuzukiTsuru/lessampler/releases/) | YuzukiTsuru | | [See additonal notes.](https://github.com/stakira/OpenUtau/wiki/Resamplers-and-Wavtools#compatible-with-adjustments) |
| [macres.exe](https://github.com/titinko/macres/releases)   | titinko   |  |
| model4.exe  | Ameya  |   |
| [moresampler.exe](https://bowlroll.net/file/139123) |  Kanru Hua | [moresampler.yaml](https://github.com/Cadlaxa/Resampler-Manifests/blob/main/Resampler%20Manifests/moresampler.yaml) | [See adjustments for compatibility.](https://github.com/stakira/OpenUtau/wiki/Resamplers-and-Wavtools#compatible-with-adjustments) |
| [phavoco.exe](http://utau2008.xrea.jp/downloads/phavoco010.zip) | Ameya   |  |
| [phaavoco.exe](http://utau2008.xrea.jp/2020/engine/phaavoco001.zip) | Ameya |   |
| resampler.exe  | Ameya  |  | UTAU built-in resampler.  |
| [SpaceWorld_win64.exe](https://github.com/LovelyA72/SpaceWorld/releases) | LovelyA72 |  | [See adjustments for compatibility.](https://github.com/stakira/OpenUtau/wiki/Resamplers-and-Wavtools#compatible-with-adjustments) |
|[StrayCatRunner.exe](https://github.com/Astel123457/straycat-server) | Astel123457 |  [StrayCatRunner.yaml](https://github.com/Cadlaxa/Resampler-Manifests/blob/main/Resampler%20Manifests/StrayCatRunner.yaml)|
|[straycat-rs.exe](https://github.com/UtaUtaUtau/straycat-rs/) | UtaUtaUtau | [straycat-rs.yaml](https://github.com/Cadlaxa/Resampler-Manifests/blob/main/Resampler%20Manifests/straycat-rs.yaml)  |
|[StrayCat.py](https://github.com/UtaUtaUtau/straycat) | UtaUtaUtau | [StrayCat.yaml](https://github.com/Cadlaxa/Resampler-Manifests/blob/main/Resampler%20Manifests/straycat.yaml)  | Deprecated in place of straycat-rs (above)
| [TIPS.exe](http://scientistb.web.fc2.com/program/)  | ScientistB |  |
| [tn_fnds.exe](http://z-server.game.coocan.jp/utau/utautop.html#tn_fnds) | Zteer | [tn_fnds.yaml](https://github.com/oxygen-dioxide/openutau-manifests/blob/main/tn_fnds.yaml) |
| [UDB](https://github.com/YuzukiTsuru/UDB/releases/tag/0.0.3.1) | YuzukiTsuru | | UDB means UTAU Debug Engine.|
| [vs4u.exe](http://ackiesound.ifdef.jp/download.html#vs4u) | AckieSound |  |
| [w4u.exe](http://utau2008.xrea.jp/downloads/w4u001.zip) | Zany |  [w4u.yaml](https://github.com/oxygen-dioxide/openutau-manifests/blob/main/world4utau.yaml) |
| [WARP.exe](http://custom-made.seesaa.net/article/312530509.html) | Custom.Maid |  
| [wn4u.exe](https://utaforum.net/threads/world4utau-update.20035/) | Zany | | [See adjustments for compatibility.](https://github.com/stakira/OpenUtau/wiki/Resamplers-and-Wavtools#compatible-with-adjustments) |
| [young3.exe](https://bowlroll.net/file/203018) | Zany | |

### Compatible with adjustments

- [moresampler.exe](https://bowlroll.net/file/139123)
  - Add `moresampler.exe` and the default `moreconfig.txt` to the `Resamplers` folder.
  - Add `moresampler.exe` to `Wavtools` folder without `moreconfig.txt`.
  - Moresampler should now function as either resampler only, or as both wavtool and resampler.
  - If you're using simple/convergence wavtool and encounter slow rendering times on macOS (possibly other OS too), modify `moreconfig.txt` and switch `multithread-synthesis` to `off`.
- [[SpaceWorld_win64.exe|https://github.com/LovelyA72/SpaceWorld/releases]] and [[wn4u.exe|https://utaforum.net/threads/world4utau-update.20035/]]
    - May experience issues if the voicebank is missing any frq files. SpaceWorld version 1.0.1 will not crash in the event of a missing frq file.
- [[lessampler|https://github.com/YuzukiTsuru/lessampler/releases/]]
    - In development, lack of flag support
    - Oversized Audio Model Attention

## MacOS
|  Resampler |  Author  |  Resample Manifest  |  Additional Notes |
| ------------ | ------------ | ------------ | ------------ |
|  worldline  | StAkira  |   | Built into OpenUtau. Works on all platforms. |
| [macres](https://github.com/titinko/macres/releases)   | titinko   | [macres.yaml]()  |

## Linux
|  Resampler |  Author  |  Resample Manifest  |  Additional Notes |
| ------------ | ------------ | ------------ | ------------ |
|  worldline  | StAkira  |   | Built into OpenUtau. Works on all platforms. |
| [macres](https://github.com/titinko/macres/releases)   | titinko   | [macres.yaml]()  |

# Resampler Manifest
A resampler manifest is a YAML file used to store the expressions supported by a resampler. With resampler manifests, users can add all of a resampler's supported flags at once using the `Add all expressions suggested by renderers` button in the `Expressions` editor.

<img width="453" alt="image" src="https://user-images.githubusercontent.com/54425948/227085816-4cced732-98dd-4c76-bc40-9a94f971a066.png">

Resampler manifests should have the same name as the resampler executable, stored in the same folder. The manifest must have a `.yaml` file extension. For example, the resampler manifest for `moresampler.exe` should be `moresampler.yaml` located in the same folder with `moresampler.exe`.

Below is a full example of a resampler manifest for Moresampler. To create a resampler manifest with OpenUtau, add the resampler's expressions to any `.ustx` project file. Open the project file in a text editor and copy the `expressions:` section into a blank manifest file.
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

# Installing Wavtools

## Windows
1. On your unzipped OpenUtau folder, locate the wavtool folder named `Wavtools`.
2. Open the wavtool folder and place the downloaded wavtool on the folder.

In OpenUtau version 0.1.119 or higher, wavtools can be installed by dragging and dropping the `.exe` file onto the main OpenUtau window and selecting "Install as wavtool".

<img src="https://github.com/stakira/OpenUtau/assets/18076904/1a13d37d-b472-451d-b24a-e984b095bd4a" height="250">

## macOS / Linux

In OpenUtau 0.1.560 or higher, external Windows wavtools are now supported on macOS and Linux.

1. Install Wine (follow the previous guide under macOS/Linux resamplers)
2. In OpenUtau, enable wine compatibility by setting wine path in `Tools > Preferences > Advanced > Wine Path...`. Clicking `Detect` should automatically pick wine from your `$PATH`, otherwise click `Select` to pick it yourself. (skip if you already did this)
3. Install Windows wavtools (e.g. `wavtool.exe`) by using `Tools > Install Wavtool/Resampler (.exe)`. You can drag and drop the .exe into OpenUtau window on macOS. Choose `Install as wavtool`.
4. You can now use Windows wavtools in OpenUtau

Do note that only Windows wavtools are supported, no support for external native wavtools at the moment.

# Tested Wavtools and Directories
Below is a list of all UTAU wavtools tested with OpenUtau.

| Wavtool | Author | Additonal Notes |
| --------- | -------- | ------------------ |
| simple | StAkira | Built into OpenUtau. Works on all platforms. |
| convergence | StAkira | Also built into OpenUtau. Uses phase compensation.|
| [moresampler.exe](https://bowlroll.net/file/139123) | Kanru Hua | [See adjustments for compatibility.](https://github.com/stakira/OpenUtau/wiki/Resamplers-and-Wavtools#compatible-with-adjustments) |
| [wavtool64](http://utau2008.xrea.jp/2020/engine/wavtool64.zip) | Ameya | |
| [wavtool4vcv](https://www.mediafire.com/file/1iwrak88c6xzb87/wavtool4vcv20141202.zip/file) | nmasao | |