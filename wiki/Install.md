[Japanese / 日本語版ページ](https://w.atwiki.jp/openutau_ja/pages/14.html)
# Install OpenUtau
## Download
### Stable Version:
[![Download OpenUtau-win-x64.exe](https://img.shields.io/static/v1?style=for-the-badge&logo=github&label=download&message=windows-x64-installer&labelColor=FF347C&color=4ea6ea)](https://github.com/stakira/OpenUtau/releases/latest/download/OpenUtau-win-x64.exe)
[![Download OpenUtau-win-x64.zip](https://img.shields.io/static/v1?style=for-the-badge&logo=github&label=download&message=windows-x64-portable&labelColor=FF347C&color=4ea6ea)](https://github.com/stakira/OpenUtau/releases/latest/download/OpenUtau-win-x64.zip)
[![Download OpenUtau-win-x86.zip](https://img.shields.io/static/v1?style=for-the-badge&logo=github&label=download&message=windows-x86-portable&labelColor=FF347C&color=4ea6ea)](https://github.com/stakira/OpenUtau/releases/latest/download/OpenUtau-win-x86.zip)  
[![Download OpenUtau-osx-x64.dmg](https://img.shields.io/static/v1?style=for-the-badge&logo=github&label=download&message=macos-x64&labelColor=FF347C&color=4ea6ea)](https://github.com/stakira/OpenUtau/releases/latest/download/OpenUtau-osx-x64.dmg)
[![Download OpenUtau-osx-arm64.dmg](https://img.shields.io/static/v1?style=for-the-badge&logo=github&label=download&message=macos-arm64&labelColor=FF347C&color=4ea6ea)](https://github.com/stakira/OpenUtau/releases/latest/download/OpenUtau-osx-arm64.dmg)  
[![Download OpenUtau-linux-x64.zip](https://img.shields.io/static/v1?style=for-the-badge&logo=github&label=download&message=linux-x64&labelColor=FF347C&color=4ea6ea)](https://github.com/stakira/OpenUtau/releases/latest/download/OpenUtau-linux-x64.zip)

> [!CAUTION]
> From version 0.1.549 onwards, the application will not start if the [.NET 8 runtime](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) is not installed.

### Beta Version:
The beta version can be downloaded from the GitHub [Release Page](https://github.com/stakira/OpenUtau/releases).  

If you install the beta version from the start, you may be prompted to install the stable version during the initial launch update notification (because the default setting in Preferences is to use the stable version).  
First, enable “Beta” in Preferences.

#### How to Download from GitHub's [Release Page](https://github.com/stakira/OpenUtau/releases)
The latest stable version is marked with green text `Latest` next to the version number. The beta version is marked with brown text `Pre-release`.

First, click “Show all assets” to display all versions.
- On Windows, use “OpenUtau-win-x64” by default. The difference between .exe and .zip is explained below.
- For certain specialized Windows environments (Arm devices) like Surface, use “OpenUtau-win-arm64”.
- If you are using a 32-bit OS on Windows, use “OpenUtau-win-x86”.
- On macOS, if your CPU is an Intel chip, use “OpenUtau-osx-x64.dmg”.
- On macOS, if your CPU is Apple Silicon (such as an M1 chip), use “OpenUtau-osx-arm64.dmg”.
- On Linux, use “OpenUtau-linux-x64.zip” or “OpenUtau-linux-arm64.zip”.
- Files ending in “.xml” are administrative files for developers and are not used for installation.

## Windows
OpenUtau supports Windows 8.1 and above (Windows 10 is required for DiffSinger).

#### Installer (OpenUtau-win-x64.exe)
Double-click the downloaded .exe and follow the installation instructions.  
- Please install to the default location (Program Files).  
(Currently, there is an issue where the location of the previous installation is not remembered during updates.)
- When using the installer version, the location for voicebanks, engines, plugins, etc., is fixed to the user's Documents folder.  
Since this requires a significant amount of storage space, if your C drive lacks sufficient capacity or you use OneDrive backup, please use the portable version instead of the installer version.

#### Portable version (OpenUtau-win-x64.zip)
After unzipping to a new folder, you can start the application by double-clicking `OpenUtau.exe`.
- For the portable version, you will place voicebanks, engines, plugins, etc., in the folder containing OpenUtau.exe.  
Installation on a separate partition or external HDD is also possible (note that operation may be slower on external devices).
- Never place it in locations requiring administrator privileges, such as "Program Files".
- If placing it in folders like Downloads or Documents, be sure to disable OneDrive backup.
- If storage space is insufficient, consider placing it on a different drive.

## macOS
OpenUtau supports macOS 10.14 Mojave and above (macOS 11 Big Sur is required for DiffSinger).
1. Double-click the downloaded .dmg file.
2. Drag the app icon to the folder icon.
3. Open Terminal, type `xattr -rc /Applications/OpenUtau.app`, and press Enter.
4. Open OpenUtau from the Applications folder or LaunchPad.

## Linux
#### Arch or similar (Eg. Manjaro)
- Install [openutau-bin](https://aur.archlinux.org/packages/openutau-bin) from AUR (Eg. using [yay](https://github.com/Jguer/yay) `yay -S openutau-bin`).
#### Gentoo
- Install `app-eselect/eselect-repository` in order to enable the guru overlay.
- Run `eselect repository enable guru` and `emaint sync -r guru` to enable and sync the overlay (`dev-vcs/git` may be needed to be installed).
- Run `emerge openutau` to install OpenUtau.
#### Other
- Extract the .zip file yourself, and run `OpenUtau` from a terminal using `./OpenUtau` on the same folder OpenUtau was extracted.
- Or check the community-created [installer scripts](https://hitcoder.tubs.wtf/Posts/openutau/).

## Select UI language
By default, OpenUtau will use the same language as your computer, or English if a translation is unavailable. To manually change the language, go to **Tools > Preferences**.

![language](https://i.imgur.com/WDgg4Z6.gif)

# Install a resampler
OpenUtau provides an internal wavtool along with a resampler, **Worldline**.   
To install an external resampler, place a resampler .exe or .dll into the "Resamplers" folder where OpenUtau is installed. 

> [!TIP]
> On linux, the `Resamplers` folder is located at `~/.local/share/OpenUtau/Resamplers`.

If you already use UTAU, you can copy + paste resamplers that you already have. Check [Resamplers](Resamplers-and-Wavtools) for a list of compatible resamplers.

After adding a track, you can select the resampler and wavtool by pressing the settings cog on the lower right of the track header. Please note that only wavtools that are compatible with the currently selected resampler will be shown; for instance only "simple" and "convergence" will be available to choose when Worldline is selected.

# Install a voicebank
Voicebanks can be installed through **Tools > Install Singer...**

![install voicebank](https://i.imgur.com/FpIZ21J.png)

On non-Japanese systems, unzipping a zip file created on a Japanese system often leads to mojibake file names. The **Install Singer** tool helps convert file names correctly. You could also **unzip yourself** if the file names can be correctly unzipped.

When installing a voicebank, a window will pop up with a file encoding option. Use this option if you're not sure about how the voicebank is encoded (for example, a Japanese voicebank created by a Chinese user). You will know when the encoding is right.

![select file encoding](https://i.imgur.com/sSpDhPc.png)  

Another way to install singers is to set the **Additional Singer Path** to an existing folder with singers, such as the UTAU voice folder.

You can then see your installed voicebanks in the **Tools > Singers...** menu.

If you're using MacOS, before you download a voicebank, navigate to `Settings > General` and uncheck `Open "safe" files after downloading`.

![image](https://github.com/user-attachments/assets/662debe9-8c67-459f-916a-8f9b05f81bae)