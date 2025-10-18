[Japanese / 日本語版ページ](https://w.atwiki.jp/openutau_ja/pages/14.html)
# Install OpenUtau
## Download
### Stable Version:
[![Download](https://img.shields.io/static/v1?style=for-the-badge&logo=github&label=download&message=windows-x64-installer&labelColor=FF347C&color=4ea6ea)](https://github.com/stakira/OpenUtau/releases/latest/download/OpenUtau-win-x64.exe)
[![Download](https://img.shields.io/static/v1?style=for-the-badge&logo=github&label=download&message=windows-x64-portable&labelColor=FF347C&color=4ea6ea)](https://github.com/stakira/OpenUtau/releases/latest/download/OpenUtau-win-x64.zip)
[![Download](https://img.shields.io/static/v1?style=for-the-badge&logo=github&label=download&message=windows-x86-portable&labelColor=FF347C&color=4ea6ea)](https://github.com/stakira/OpenUtau/releases/latest/download/OpenUtau-win-x86.zip)  
[![Download](https://img.shields.io/static/v1?style=for-the-badge&logo=github&label=download&message=macos-x64&labelColor=FF347C&color=4ea6ea)](https://github.com/stakira/OpenUtau/releases/latest/download/OpenUtau-osx-x64.dmg)
[![Download](https://img.shields.io/static/v1?style=for-the-badge&logo=github&label=download&message=macos-arm64&labelColor=FF347C&color=4ea6ea)](https://github.com/stakira/OpenUtau/releases/latest/download/OpenUtau-osx-arm64.dmg)  
[![Download](https://img.shields.io/static/v1?style=for-the-badge&logo=github&label=download&message=linux-x64&labelColor=FF347C&color=4ea6ea)](https://github.com/stakira/OpenUtau/releases/latest/download/OpenUtau-linux-x64.zip)

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
- Extract the tar.gz file yourself, and run `OpenUtau` from a terminal.
- Or check the community-created [installer scripts](https://hitcoder.tubs.wtf/Posts/openutau/).