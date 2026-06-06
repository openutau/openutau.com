# Overview

This page describes the minimum set of changes required when forking OpenUtau and distributing a new editor.

Several OpenUtau-based editors have recently been released without modifying application identifiers, installer settings, update sources, or configuration storage locations. As a result, users have encountered issues such as:

* OpenUtau settings being overwritten by a forked editor
* OpenUtau becoming unable to start due to incompatible configuration files
* Installation and uninstallation information being overwritten
* File associations being unexpectedly changed
* Forked editors updating from the official OpenUtau release channel

The purpose of this document is to help developers avoid these conflicts and ensure that forked editors can coexist safely with the official OpenUtau installation.

This page focuses on identifying the locations that should be reviewed and modified before distributing a forked editor. Some items are required to prevent conflicts, while others are recommended to improve identification, branding, and user experience.

This document assumes the following coexistence model:

* Voicebanks may be shared with OpenUtau.
* External tools and dependencies may be shared with OpenUtau.
* User preferences, application settings, installer identifiers, and update channels must not be shared with OpenUtau.

Following the recommendations in this document helps prevent user environment corruption and reduces support issues caused by conflicts between OpenUtau and forked editors.

# Modification Procedures

## Modification List
Category | Target for Change | Main Files to Change | Priority | Reason
-- | -- | -- | -- | --
Settings Save Location | PrefsFilePath | OpenUtau.Core/Util/PathManager.cs | Required | To prevent corruption and startup failure caused by sharing the same settings file.
Installer Product Name | PRODUCT_NAME | OpenUtau.nsi | Required | To prevent overwriting uninstallation information.
Uninstall Key | PRODUCT_UNINST_KEY | OpenUtau.nsi | Required | To prevent Windows Registry conflicts.
Installation Path | InstallDir "$PROGRAMFILES64\OpenUtau" | OpenUtau.nsi | Required | To prevent overwriting the original version's installation directory.
Shortcut Name | OpenUtau.lnk | OpenUtau.nsi | Required | To prevent overwriting the Start Menu and Desktop shortcuts.
Executable Name | OpenUtau.exe | OpenUtau.nsi, OpenUtau/OpenUtau.csproj | Required | To prevent the installer and shortcuts from referencing the wrong executable file. To ensure users do not mistake it for the original version.
Updater | GitHub Release Repository | OpenUtau/ViewModels/UpdaterViewModel.cs | Required | To avoid the risk of users updating to the original version by referencing the original GitHub Releases.
.ustx Association | HKCR ".ustx" / OpenUtauFile | OpenUtau.nsi | Recommended | If not changed, it will take over the original version's file association. However, this is not mandatory as users can change it later.
USTX Version | kUstxVersion | OpenUtau.Core/Format/USTx.cs | Recommended (Conditional) | Targeted for change only if the USTX format is uniquely modified.
File Selection Filter | Patterns | OpenUtau/FilePicker.cs | Recommended (Conditional) | Targeted for change only if handling unique extensions or formats.
GitHub / Web Links | Wiki / Website URL | OpenUtau/Views/MainWindow.axaml.cs | Recommended | To avoid misleading users to the original version's information.
Crowdin workflow | Crowdin Project / Token | .github/workflows/crowdin.yml | Recommended | To prevent synchronization errors with the original translation and malfunction of bot settings.
Translation Sync Script | Crowdin Project Identifier | Misc/sync_strings.py | Recommended | Change if you intend to manage translation assets independently.
Splash Window | Logos and icons in SplashWindow.axaml | OpenUtau/Assets/*, OpenUtau/Views/SplashWindow.axaml | Recommended | For visual distinction from the original version
Icon | open-utau.ico | OpenUtau/Assets/* | Recommended | For visual distinction from the original version