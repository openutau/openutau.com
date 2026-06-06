# Overview

This page describes the minimum set of changes required when forking OpenUtau and distributing a new editor.

Several OpenUtau-based editors have recently been released without modifying application identifiers, installer settings, update sources, or configuration storage locations. As a result, users have encountered issues such as:

OpenUtau settings being overwritten by a forked editor
OpenUtau becoming unable to start due to incompatible configuration files
Installation and uninstallation information being overwritten
File associations being unexpectedly changed
Forked editors updating from the official OpenUtau release channel

The purpose of this document is to help developers avoid these conflicts and ensure that forked editors can coexist safely with the official OpenUtau installation.

This page focuses on identifying the locations that should be reviewed and modified before distributing a forked editor. Some items are required to prevent conflicts, while others are recommended to improve identification, branding, and user experience.

This document assumes the following coexistence model:

Voicebanks may be shared with OpenUtau.
External tools and dependencies may be shared with OpenUtau.
User preferences, application settings, installer identifiers, and update channels must not be shared with OpenUtau.

Following the recommendations in this document helps prevent user environment corruption and reduces support issues caused by conflicts between OpenUtau and forked editors.

# Modification Procedures

## Modification List
Category | Modification Target | Priority | Reason
-- | -- | -- | --
Settings Storage | PrefsFilePath in PathManager.cs | Mandatory | To prevent corruption and startup failure caused by sharing configuration files
Installer Product Name | PRODUCT_NAME in OpenUtau.nsi | Mandatory | To prevent overwriting uninstallation information
Uninstall Key | PRODUCT_UNINST_KEY | Mandatory | To prevent Windows Registry conflicts
Installation Directory | InstallDir "$PROGRAMFILES64\OpenUtau" | Mandatory | To prevent overwriting the original application's installation directory
Shortcut Name | OpenUtau.lnk | Mandatory | To prevent overwriting Start Menu / Desktop shortcuts
Executable Reference | OpenUtau.exe | Mandatory | To prevent launching the wrong application
Updater | UpdaterViewModel.cs | Mandatory | To prevent risks of updating to the original version by referencing original GitHub Releases
.ustx Association | HKCR ".ustx" / OpenUtauFile | Recommended | If not changed, it will hijack the original's file association. Not mandatory as users can change it later
USTX Version | kUstxVersion in USTx.cs | Conditionally Recommended | Only needs modification if the USTX format itself is customized
File Picker Filter | Patterns in FilePicker.cs | Conditionally Recommended | Only needs modification if handling unique extensions or formats
GitHub / Web Links | Wiki / WebSite URL | Recommended | To avoid misleading users to the original project's information
Crowdin workflow | .github/workflows/crowdin.yml | Recommended | To prevent malfunctions in translation synchronization and bot settings
Translation Sync Script | Misc/sync_strings.py | Recommended | Change if managing translation assets independently
Splash Window | Logos and icons in SplashWindow.axaml | Recommended | For visual distinction from the original version
Icon | open-utau.ico | Recommended | For visual distinction from the original version
App Display Name | Assembly Name in OpenUtau.csproj etc. | Recommended | To ensure users do not mistake it for the original version