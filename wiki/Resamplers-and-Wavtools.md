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

###Section 3, “How to run resamplers on MacOS.”

Now that you have installed both Wine and Homebrew onto your computer, we will now begin the process for installing the resamplers into MacOS. Before we get started, I will like to clarify that for this step we will be converting the executables (<code>.exe</code>) into <code>.sh</code> files. That will be the result we want in order to run resamplers. Here is how.

1. From the OpenUTAU github release page, download the <code>“Mac_Additional.zip.”</code> This will be the package we use to convert the resamplers into <code>.sh</code> files.

2. Before we get started, let’s find the version of wine that you have installed.

_For Intel MacOS …_

Perform CMND+SHIFT+G, to locate the directory. Now input the following path, /usr/local/bin/. What you will be looking for is either Wine32 or Wine64. Depending on what you have will be important information for a future step. Remember this!

_For Silicon MacOS …_

Open Terminal and run the following command.
```
    which wine
```
After running this prompt you will receive the location of your Wine installation. *( eg. <code>/opt/homebrew/bin/wine</code> )
Please copy this location as it is very important for the following steps.

3. Download the resampler of your choice, for this tutorial, I will be installing TIPS. Extract the resampler, and run OpenUTAU.

4. Drag the <code>resampler.exe</code> into the OpenUTAU window. It will then ask you if you want to install as a resampler or wavtool, select the resampler option since that is what we are working with today.

![MacOS_Install_Samp1](https://64.media.tumblr.com/7752e2e8853648a467c91fd0c00fd269/a1e3bf701d537d70-ee/s1280x1920/9625a363c1306cb11fc72361c5a7da62349104d9.png)

5. Extract the <code>Mac_Additional.zip</code>, by extracting it, it will generate a, <code>moresampler.sh</code> file. Rename the file after the resampler you will be working with, *(eg. <code>TIPS.sh</code> ).

6. Open this file with textedit by double-clicking, or right-clicking. Select, _“Open with textedit.”_
Now we will edit the <code>.sh</code> file with resampler’s information. 

![MacOS_Install_Samp2](https://64.media.tumblr.com/a2b2428b58b151a9e3355813e32b4c89/a1e3bf701d537d70-0d/s1280x1920/a5224effb8c5ad3a834283748a483b1f5fce8804.png)

7. Locate the, <code>moresampler-0.8.4/moresampler.exe</code> delete it, and replace with only the resampler name, eg. <code>“TIPS.exe.</code>

![MacOS_Install_Samp3](https://64.media.tumblr.com/5195fff9a3b0f008664e378db43ab682/a1e3bf701d537d70-6d/s1280x1920/518c570fd9110c803080c80b8f788e4400917d5c.png)

_For MacOS Intel …_

In the field for, <code>exec /usr/local/bin/wine32on64</code> replace the Wine extension with your version of Wine. This will look like, <code>exec /usr/local/bin/wine64</code> since my computer is running Wine64.

![MacOS_Install_Samp4](https://64.media.tumblr.com/d7d8b0a032bb3ffd70758a8e74a8d03f/a1e3bf701d537d70-ec/s1280x1920/3c28e6700e06aea3535898a7075c8dbd3cd0900b.png)

_For MacOS Silicon …_

In the field for, <code>exec /usr/local/bin/wine32on64</code> replace this field with the location of your wine installation. This will may like, <code>/opt/homebrew/bin/wine.</code>

It should look like this!

![MacOS_Install_Samp5](https://64.media.tumblr.com/9e44935d17ce7ff785cfe0bde561a134/a1e3bf701d537d70-6c/s1280x1920/726ad7f83ad54b2b65983cb75618ed352d5733c7.png)

9. In OpenUTAU, to quickly access to resampler folder, select the, “help,” tag, and, "Open Logs Location.” We will not be working with the logs, from here you will open the resampler folder.

10. OpenUTAU will have already generated a <code>.sh</code> file for <code>TIPS.exe</code> in this scenario. With the edited <code>TIPS.sh</code> on your desktop, drag and drop it in the resampler folder, and replace.

11. Return to OpenUTAU, and select, “CLASSIC,” in the resampler field, and to the right there will be a cog icon. From here you will be able to select your downloaded resamplers.

![MacOS_Install_Samp6](https://64.media.tumblr.com/188ae1248d9dc27fbc1c1c2dd471c566/a1e3bf701d537d70-7e/s1280x1920/0ad2b8566b8ddb2d357abd97619d7496a9c91e61.png)

The first render may take awhile if this is your first time running the instance.

You can repeat this process and download as many resamplers as you like. 


## Linux
[Macres](https://github.com/titinko/macres/releases) provides a native Linux version. Put it into the resamplers folder of OpenUtau.

For wrapping Windows resamplers into Linux, use this method:

1. Install [Wine](https://www.winehq.org/)
2. Open the `Resamplers` folder (should be on `~/.local/share/OpenUtau/Resamplers`)
3. Create a new text file with the name of your resampler (no file extension required). 
4. Open the text file and add this script.
```
#!/bin/bash
LANG="ja_JP.UTF8" wine "/absolute/path/to/your/resampler.exe" "${@,-1}"
```
5. Change `"/absolute/path/to/your/resampler.exe"` to the path of the resampler.
6. Restart OpenUtau.

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

External wavtools are not supported on macOS or Linux at this time.  

# Tested Wavtools and Directories
Below is a list of all UTAU wavtools tested with OpenUtau.

| Wavtool | Author | Additonal Notes |
| --------- | -------- | ------------------ |
| simple | StAkira | Built into OpenUtau. Works on all platforms. |
| convergence | StAkira | Also built into OpenUtau. Uses phase compensation.|
| [moresampler.exe](https://bowlroll.net/file/139123) | Kanru Hua | [See adjustments for compatibility.](https://github.com/stakira/OpenUtau/wiki/Resamplers-and-Wavtools#compatible-with-adjustments) |
| [wavtool64](http://utau2008.xrea.jp/2020/engine/wavtool64.zip) | Ameya | |
| [wavtool4vcv](https://www.mediafire.com/file/1iwrak88c6xzb87/wavtool4vcv20141202.zip/file) | nmasao | |