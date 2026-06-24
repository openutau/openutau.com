> The latest stable version is [0.1.565](#01565-09-14-2025).  
> See also [Known Bugs](https://github.com/stakira/OpenUtau/wiki/Known-Bugs).

<!-- Use the following GitHub CLI command to get a list of pull requests:
gh pr list --state merged --repo stakira/OpenUtau --limit 1000 --json number,title,author,url,mergedAt --jq ".[] | select(.mergedAt >= \"2025-07-22T00:00:00Z\") | \"- [#\(.number)](\(.url)) - \(.title) - ([@\(.author.login)](https://github.com/\(.author.login)))\""

## Features
## Bug Fixes
## Phonemizer Changes
## Misc
-->

# ~[0.1.568 Beta](https://github.com/stakira/OpenUtau/releases/tag/0.1.568) (03-16-2026)

> [!WARNING]
> **The .ustx version has been updated to 0.9. It cannot be opened with previous versions of OpenUtau.**

## Features
- [#1870](https://github.com/stakira/OpenUtau/pull/1870) - Add feature to split vocal part at playhead cursor - ([@arx-ein](https://github.com/arx-ein))

  https://private-user-images.githubusercontent.com/29670169/523278795-73b5ffc8-40ea-4393-b16a-279cd997dd44.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzQ2ODc2NzEsIm5iZiI6MTc3NDY4NzM3MSwicGF0aCI6Ii8yOTY3MDE2OS81MjMyNzg3OTUtNzNiNWZmYzgtNDBlYS00MzkzLWIxNmEtMjc5Y2Q5OTdkZDQ0Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjAzMjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwMzI4VDA4NDI1MVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWZiMWUwYmZmOGQ3ODNhYjVhNzhhMzRiY2IyY2NjN2NlOGY1NDg4MGYzNWM4NTU0YTg3ZTEyODgzZmU4N2YwZTgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.LaCDOQYqfqbrDn8qWXFsdfgPzwFQFRi8tT6LWcerd08

- [#1888](https://github.com/stakira/OpenUtau/pull/1888) - Add Theme Editor - ([@atouu](https://github.com/atouu))

  https://private-user-images.githubusercontent.com/67765922/529491503-ad67c9e5-43c7-446e-b9b6-2ed3f305fef2.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzQ2ODc3MTksIm5iZiI6MTc3NDY4NzQxOSwicGF0aCI6Ii82Nzc2NTkyMi81Mjk0OTE1MDMtYWQ2N2M5ZTUtNDNjNy00NDZlLWI5YjYtMmVkM2YzMDVmZWYyLm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjAzMjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwMzI4VDA4NDMzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWE1M2MzYzY2MGIxMzM4Yjg5ODhjNjY0NmIyNmJhNjJhMmQ3YTlhZjRlYWUyNDVkOGU0NTJhZDA4MWI5MWM1ODUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.Op3qGo50ZXW7loaXMNAQ9_egvI1v9BxdU5RltQOpyWs

- [#1905](https://github.com/stakira/OpenUtau/pull/1905) - Add Curve Tools and Curve Selection/Copy/Paste - ([@maiko3tattun](https://github.com/maiko3tattun))  
  <img width="584" height="162" alt="image" src="https://github.com/user-attachments/assets/9ff2f94e-f68d-4a87-864b-9478c2fd5c3d" />

- [#1910](https://github.com/stakira/OpenUtau/pull/1910) - Make Piano Roll Attachable to MainWindow - ([@atouu](https://github.com/atouu))
  - [#1941](https://github.com/stakira/OpenUtau/pull/1941) - PianoRoll Enhancements - ([@atouu](https://github.com/atouu))

  https://private-user-images.githubusercontent.com/67765922/532454721-72e31930-841d-4420-a327-665f1ef2e73d.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzQ2ODc3MjAsIm5iZiI6MTc3NDY4NzQyMCwicGF0aCI6Ii82Nzc2NTkyMi81MzI0NTQ3MjEtNzJlMzE5MzAtODQxZC00NDIwLWEzMjctNjY1ZjFlZjJlNzNkLm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjAzMjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwMzI4VDA4NDM0MFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTI0YWNjNTI0MjViYmM5OWIxMzU4MDAxMmNiNWFhMTNkYTI5MzJjYzdjMWY4NGFiNjdiNDQ2ZjAzMGUwMmI0OGMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.A1AwGR4I9zk2omtpBhYr3p4q-Go_lcjE4AERrWxGw6c

- [#1968](https://github.com/stakira/OpenUtau/pull/1968) - Trim and fade for the wave part - ([@maiko3tattun](https://github.com/maiko3tattun))  
  <img width="854" height="314" alt="image" src="https://github.com/user-attachments/assets/c269d234-6bdd-47cf-b198-282c037e7a32" />

- [#1987](https://github.com/stakira/OpenUtau/pull/1987) - Smooth Pitch Shape - ([@maiko3tattun](https://github.com/maiko3tattun))

  https://private-user-images.githubusercontent.com/130257355/556271138-f4d08a88-f3f8-42b2-a97f-8a32fbc41fca.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzQ2ODc3MjEsIm5iZiI6MTc3NDY4NzQyMSwicGF0aCI6Ii8xMzAyNTczNTUvNTU2MjcxMTM4LWY0ZDA4YTg4LWYzZjgtNDJiMi1hOTdmLThhMzJmYmM0MWZjYS5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMzI4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDMyOFQwODQzNDFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jMzdmZDA3NDJjMzY5OGU2NjI4ZjkyODMyMjFiYTY5Y2UyN2VkMzZlMjA2OWM4NzE3NTg0OGFlYzQ3MzEyNGMwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.fyw6jOYIBM-iAb78wEfJ5Wr1R66z810u3i-wENxGC5Y

### Feature Enhancements
- [#1902](https://github.com/stakira/OpenUtau/pull/1902) - Responsive Track Header - ([@atouu](https://github.com/atouu))
- [#1940](https://github.com/stakira/OpenUtau/pull/1940) - Disable the menu when undo is not possible / Display the command name (take2) - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1944](https://github.com/stakira/OpenUtau/pull/1944) - Loading external batch edits - ([@AnAndroNerd](https://github.com/AnAndroNerd))
- [#1993](https://github.com/stakira/OpenUtau/pull/1993) - Enhanced Pitch Line Drawing Tool (Supports Sine Waves/S-Curves) - ([@rokujyushi](https://github.com/rokujyushi))
- [#2000](https://github.com/stakira/OpenUtau/pull/2000) - [Transcribe] Refactor and unify APIs, add GAME algorithm and long chunk detection - ([@yqzhishen](https://github.com/yqzhishen))
- [#2004](https://github.com/stakira/OpenUtau/pull/2004) - [Transcribe] RMVPE support - ([@emeraldsingers](https://github.com/emeraldsingers))
- [#1947](https://github.com/stakira/OpenUtau/pull/1947) - simple package manager - ([@stakira](https://github.com/stakira))

## Bug Fixes
- [#1855](https://github.com/stakira/OpenUtau/pull/1855) - Fix: load consonants from YAML file - ([@Cadlaxa](https://github.com/Cadlaxa))
- [#1864](https://github.com/stakira/OpenUtau/pull/1864) - Ust Import Enhancement - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1914](https://github.com/stakira/OpenUtau/pull/1914) - Replace backslash with slash in archive entry keys when installing singer. - ([@atouu](https://github.com/atouu))
- [#1919](https://github.com/stakira/OpenUtau/pull/1919) - Fix error phoneme pitch - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1920](https://github.com/stakira/OpenUtau/pull/1920) - Fix key event issues - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1929](https://github.com/stakira/OpenUtau/pull/1929) - Make plugin async and fix plugin when shell is use - ([@atouu](https://github.com/atouu))
- [#1930](https://github.com/stakira/OpenUtau/pull/1930) - Fix Worldline crashes for some Windows machines - ([@atouu](https://github.com/atouu))
- [#1935](https://github.com/stakira/OpenUtau/pull/1935) - Fix track expsressions duplicate bug - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1872](https://github.com/stakira/OpenUtau/pull/1872) - fix(coreml): w/a fallback to EnableOnSubgraphs=0 on exception - ([@fumiama](https://github.com/fumiama))
- [#2009](https://github.com/stakira/OpenUtau/pull/2009) - CoreML fixes - ([@AnAndroNerd](https://github.com/AnAndroNerd))

## Misc
- [#1861](https://github.com/stakira/OpenUtau/pull/1861) - feat(onnx): only show gpu selection on dml runner - ([@fumiama](https://github.com/fumiama))
- [#1876](https://github.com/stakira/OpenUtau/pull/1876) - Update macOS x64 runner version in github actions workflow - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1928](https://github.com/stakira/OpenUtau/pull/1928) - Set InvokeAsync priority to background in ProgressBarNotification - ([@atouu](https://github.com/atouu))
- [#1937](https://github.com/stakira/OpenUtau/pull/1937) - Add Worldline Build Workflow - ([@atouu](https://github.com/atouu))
- [#1938](https://github.com/stakira/OpenUtau/pull/1938) - Rebuild Worldline - ([@app/github-actions](https://github.com/app/github-actions))
- [#1942](https://github.com/stakira/OpenUtau/pull/1942) - Exempt Feature Requests - ([@BagelHero](https://github.com/BagelHero))


# ~[0.1.567 Beta](https://github.com/stakira/OpenUtau/releases/tag/0.1.567) (11-29-2025)

> [!WARNING]
> **The .ustx version has been updated. It cannot be opened with previous versions of OpenUtau.**

## Features
- [#1396](https://github.com/stakira/OpenUtau/pull/1396) - Add RandomizeTiming function to batch edit - ([@maiko3tattun](https://github.com/maiko3tattun))
  - By combining it with tuning randomization, you can create doubling.
- [#1805](https://github.com/stakira/OpenUtau/pull/1805) - Supprt Track Expressions, Import entire flags and Skip flag output when the value is default - ([@maiko3tattun](https://github.com/maiko3tattun))

https://github.com/user-attachments/assets/b34de0f8-b4c4-4ff3-98d8-79409bbb7903
- [#1815](https://github.com/stakira/OpenUtau/pull/1815) - Support dropping multiple files at once - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1821](https://github.com/stakira/OpenUtau/pull/1821) - Custom Theme Support - ([@AnAndroNerd](https://github.com/AnAndroNerd)) <img width="967" height="677" alt="image" src="https://github.com/user-attachments/assets/490c33f0-faa6-4fc5-aafb-3609fb17893d" />

- [#1839](https://github.com/stakira/OpenUtau/pull/1839) - Support for ignoring auto-VCV during ust import - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#c71fdb6](https://github.com/stakira/OpenUtau/commit/c71fdb65a1d25521fcbdfbb108e51fb276c9159e) - Removes worldline-r2 for now ([@stakira](https://github.com/stakira))

## Bug Fixes
- [#1745](https://github.com/stakira/OpenUtau/pull/1745) - Translate the message displayed when SOME is not installed - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1834](https://github.com/stakira/OpenUtau/pull/1834) - Fix Rider errors - ([@AnAndroNerd](https://github.com/AnAndroNerd))
- [#1845](https://github.com/stakira/OpenUtau/pull/1845) - Fix yaml timing entry overrides with new instance of the phonemizer - ([@Cadlaxa](https://github.com/Cadlaxa))
- [#1846](https://github.com/stakira/OpenUtau/pull/1846) - Set PlayingMaster to false on PlayTestSound - ([@atouu](https://github.com/atouu))
- [#1848](https://github.com/stakira/OpenUtau/pull/1848) - Fix Voice Color Remapping Bug - ([@maiko3tattun](https://github.com/maiko3tattun))


# ~[0.1.566 Beta](https://github.com/stakira/OpenUtau/releases/tag/0.1.566) (11-28-2025)

> [!WARNING]
> **The .ustx version has been updated. It cannot be opened with previous versions of OpenUtau.**

## Features
### New Features
- [#fb9e157](https://github.com/stakira/OpenUtau/commit/fb9e157d57327fe801eff7a044032379940ee895) - Worldline-R2 renderer test version 1. Select it from the renderer dropdown menu in header tracker. ([@stakira](https://github.com/stakira))
- [#1428](https://github.com/stakira/OpenUtau/pull/1428) - Microtonal tuning function and batch editing of randomization - ([@maiko3tattun](https://github.com/maiko3tattun))

https://github.com/user-attachments/assets/c21c6356-2350-4f74-8760-67cac776e728
- [#1645](https://github.com/stakira/OpenUtau/pull/1645) - Add feature to merge vocal parts - ([@arx-ein](https://github.com/arx-ein))
- [#1674](https://github.com/stakira/OpenUtau/pull/1674) - Add Commonnote Batch Edits - ([@AnAndroNerd](https://github.com/AnAndroNerd))
- [#1678](https://github.com/stakira/OpenUtau/pull/1678) - Add new batch edit "Replace '-' with '+~'". - ([@AnAndroNerd](https://github.com/AnAndroNerd))
- [#1778](https://github.com/stakira/OpenUtau/pull/1778) - Add OverwriteLinePitchTool  - ([@rokujyushi](https://github.com/rokujyushi))
- [#1804](https://github.com/stakira/OpenUtau/pull/1804) - Ctrl+Shift+V to paste as plain notes - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
<img alt="image" src="https://github.com/user-attachments/assets/9e9225bc-c7d1-4ae6-8541-c6549920fa7a" />

### Feature Enhancements
- [#1468](https://github.com/stakira/OpenUtau/pull/1468) - Allow assignment of an oto set to multiple colors - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1540](https://github.com/stakira/OpenUtau/pull/1540) - Fix "Lyrics Replacement" and Improved "Edit Lyrics" - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1635](https://github.com/stakira/OpenUtau/pull/1635) - Togglable expressions view - ([@atouu](https://github.com/atouu))
- [#1638](https://github.com/stakira/OpenUtau/pull/1638) - Auto focus to the text field in dialogs - ([@arx-ein](https://github.com/arx-ein))
  - [#1748](https://github.com/stakira/OpenUtau/pull/1748) - Fix auto focused text field in dialogs not accepting keyboard inputs - ([@arx-ein](https://github.com/arx-ein))
- [#1654](https://github.com/stakira/OpenUtau/pull/1654) - Improve and translate the error report - ([@maiko3tattun](https://github.com/maiko3tattun))
  - [#1744](https://github.com/stakira/OpenUtau/pull/1744) - Fix bug in voicebank error checker - ([@maiko3tattun](https://github.com/maiko3tattun))
  - [#1807](https://github.com/stakira/OpenUtau/pull/1807) - Fix VoicebankErrorChecker could not correctly detect bit depth - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1668](https://github.com/stakira/OpenUtau/pull/1668) - Add Legacy Plugins and Reset Batch Edits to right click menu on Piano Roll - ([@AnAndroNerd](https://github.com/AnAndroNerd))
- [#1685](https://github.com/stakira/OpenUtau/pull/1685) - Always uses CPU for vogen rendering - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1730](https://github.com/stakira/OpenUtau/pull/1730) - convert `-` to `+~` instead of `+` when importing other formats - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1742](https://github.com/stakira/OpenUtau/pull/1742) - Support import multiple audios at once; remove 'import midi' menu item - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1753](https://github.com/stakira/OpenUtau/pull/1753) - Musicxml import: support `<backup>` and `<chord>`, support slurs, ties and multisyllabic words - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1797](https://github.com/stakira/OpenUtau/pull/1797) - Allow wavtool/resampler picker to open native UNIX executables - ([@atayeem](https://github.com/atayeem))
- [#1802](https://github.com/stakira/OpenUtau/pull/1802) - Support .mrq file when .frq isn't present [MOD+] - ([@Astel123457](https://github.com/Astel123457))
- [#1829](https://github.com/stakira/OpenUtau/pull/1829) - Store MainWindow and PianorollWindow Size - ([@maiko3tattun](https://github.com/maiko3tattun))

## Bug Fixes
- [#1613](https://github.com/stakira/OpenUtau/pull/1613) - Reload when singer's avatar is changed - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1625](https://github.com/stakira/OpenUtau/pull/1625) - Fix playhead resets to its initial position when using 'Do nothing' on pause. - ([@atouu](https://github.com/atouu))
  - [#1806](https://github.com/stakira/OpenUtau/pull/1806) - Check if miniaudio is not paused before resetting currentTimeMs. - ([@atouu](https://github.com/atouu))
- [#1626](https://github.com/stakira/OpenUtau/pull/1626) - Fix playhead moving when playing samples - ([@atouu](https://github.com/atouu))
- [#1627](https://github.com/stakira/OpenUtau/pull/1627) - Fixes related to VOICEVOXRenderer. - ([@rokujyushi](https://github.com/rokujyushi))
- [#1641](https://github.com/stakira/OpenUtau/pull/1641) - Fix tone generator crackling - ([@Kabinet0](https://github.com/Kabinet0))
- [#1646](https://github.com/stakira/OpenUtau/pull/1646) - Fix note editing tool toggle button behavior - ([@arx-ein](https://github.com/arx-ein))
- [#1667](https://github.com/stakira/OpenUtau/pull/1667) - escape dollar sign in default gitignore used in publishing singer - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1690](https://github.com/stakira/OpenUtau/pull/1690) - Fix VoiceColorRemapping Crash - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1702](https://github.com/stakira/OpenUtau/pull/1702) - Add save dialog when opening file with Open Recent menu - ([@arx-ein](https://github.com/arx-ein))
- [#1724](https://github.com/stakira/OpenUtau/pull/1724) - Fix Windows legacy plugins on macOS and Linux - ([@atouu](https://github.com/atouu))
- [#1743](https://github.com/stakira/OpenUtau/pull/1743) - [SBP update] Instance-based Dictionary - ([@Cadlaxa](https://github.com/Cadlaxa))
- [#1766](https://github.com/stakira/OpenUtau/pull/1766) - Fixed issue where parts didn't extend when adding notes - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1771](https://github.com/stakira/OpenUtau/pull/1771) - Fix DIR was displayed as unsupported expression in the Classic Renderer - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1774](https://github.com/stakira/OpenUtau/pull/1774) - feat(onnx): drop Vortice.DXGI & update dml to 1.23.0 - ([@fumiama](https://github.com/fumiama))
- [#1798](https://github.com/stakira/OpenUtau/pull/1798) - worldline memory leak fix - ([@AnAndroNerd](https://github.com/AnAndroNerd))
- [#1809](https://github.com/stakira/OpenUtau/pull/1809) - Fix the pianoroll progress bar - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1810](https://github.com/stakira/OpenUtau/pull/1810) - Fix the left-aligned track number - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1819](https://github.com/stakira/OpenUtau/pull/1819) - Fix voicebank merger error message - ([@maiko3tattun](https://github.com/maiko3tattun))

## Phonemizer Changes
- [#1719](https://github.com/stakira/OpenUtau/pull/1719) - `New!` Add Diffsinger Filipino Phonemizer (DIFFS FIL) - ([@julieraptor](https://github.com/julieraptor))
- [#1671](https://github.com/stakira/OpenUtau/pull/1671) - `New!` Add Millefeuille and Marzipan Phonemizers - Take 2 - ([@imsupposedto](https://github.com/imsupposedto))
- [#1534](https://github.com/stakira/OpenUtau/pull/1534) - `Syllable Based Phonemizers` Replacement update - ([@Cadlaxa](https://github.com/Cadlaxa))
- [#1619](https://github.com/stakira/OpenUtau/pull/1619) - `FIL VCV & CVVC` Add ConsException to CC transitions - ([@Cadlaxa](https://github.com/Cadlaxa))
- [#1651](https://github.com/stakira/OpenUtau/pull/1651) - `JA VCV & CVVC` Adds Normalization to [- C]s in Japanese Presamp Phonemizer based on CFLAGS - ([@AnAndroNerd](https://github.com/AnAndroNerd))
- [#1666](https://github.com/stakira/OpenUtau/pull/1666) - `KO CV` Improved behavior, Changed setting file to yaml - ([@EX3exp](https://github.com/EX3exp))
- [#1712](https://github.com/stakira/OpenUtau/pull/1712) - `ZH CVV+` Bugfix Chinese CVV Plus Phonemizer - ([@AnAndroNerd](https://github.com/AnAndroNerd))
- [#1738](https://github.com/stakira/OpenUtau/pull/1738) - `IT G2P + Phonemizers` Replace Italian G2p with improved version + adjust phonemizers - ([@lottev1991](https://github.com/lottev1991))
- [#1796](https://github.com/stakira/OpenUtau/pull/1796) - `ZH CVVC` Add [REPLACE] support for Chinese CVVC Phonemizer - ([@Slidingwall](https://github.com/Slidingwall))

## Misc
- [#1472](https://github.com/stakira/OpenUtau/pull/1472) - Improvements preferences and related to singers folder - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1551](https://github.com/stakira/OpenUtau/pull/1551) - Improve loading popup consistency and visuals - ([@Kabinet0](https://github.com/Kabinet0))
  - [#1808](https://github.com/stakira/OpenUtau/pull/1808) - Fix bugs in loading screen changes - ([@Kabinet0](https://github.com/Kabinet0))
- [#1592](https://github.com/stakira/OpenUtau/pull/1592) - Beta won't ask for downgrading to stable - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1628](https://github.com/stakira/OpenUtau/pull/1628) - Add Linux Appimage package - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1630](https://github.com/stakira/OpenUtau/pull/1630) - Make a tar.gz Linux artifact instead of zip - ([@atouu](https://github.com/atouu))
- [#1683](https://github.com/stakira/OpenUtau/pull/1683) - Move recovery project notification to welcome page - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1689](https://github.com/stakira/OpenUtau/pull/1689) - Add text to the Singer Setup Dialog - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1726](https://github.com/stakira/OpenUtau/pull/1726) - Update error message for encrypted singer - ([@adlez27](https://github.com/adlez27))
- [#1755](https://github.com/stakira/OpenUtau/pull/1755) - Stop rendering on project load - ([@atouu](https://github.com/atouu))
- [#1782](https://github.com/stakira/OpenUtau/pull/1782) - Enlarge the “Waiting Rendering” - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1843](https://github.com/stakira/OpenUtau/pull/1843) - Update DML to 1.15.4 - ([@KakaruHayate](https://github.com/KakaruHayate))
- [#1673](https://github.com/stakira/OpenUtau/pull/1673) - Fix broken link to ENUNU wiki page in README.md - ([@cedkim](https://github.com/cedkim))
- [#1684](https://github.com/stakira/OpenUtau/pull/1684) - Install NSIS in github acitons - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1705](https://github.com/stakira/OpenUtau/pull/1705) - Add a mention of .NET 8 to bug-report.yml - ([@AnAndroNerd](https://github.com/AnAndroNerd))
- [#1812](https://github.com/stakira/OpenUtau/pull/1812) - support NNAPI for downstream(mobile) - ([@KakaruHayate](https://github.com/KakaruHayate))

***
# ~[0.1.565](https://github.com/stakira/OpenUtau/releases/tag/0.1.565) (09-14-2025)
## Bug Fixes
- [#1692](https://github.com/stakira/OpenUtau/pull/1692) - Revert "fix legacy plugin output" - ([@stakira](https://github.com/stakira))

### Summary of new features since the last stable release!
#### Main Windows
- Splash window
- Welcome page
#### Piano roll
- Search notes by alias
- Clear caches for each phrase
- Add DrawLine Pitch Tool and improvement Tools
- Support displaying real curves from DiffSinger variance predictor
- 'reset all' editing macro
- Move to the next track part with PageUp/PageDown keys
#### Render
- Classic renderer: support direct
- Support SimpleENUNUServer0.5.0
- Support Diffsinger multi-dictionary
#### Misc
- Refactor preferences page to using a navigation sidebar, rearrange preference items
- Voicebank Merger
- Recovery project function
- MusicXML Import

***
# ~[0.1.564 Beta](https://github.com/stakira/OpenUtau/releases/tag/0.1.564) (08-31-2025)
## Bug Fixes
- [#1623](https://github.com/stakira/OpenUtau/pull/1623) - Added font settings for macOS - ([@rokujyushi](https://github.com/rokujyushi))
- [#1a6924a](https://github.com/stakira/OpenUtau/commit/1a6924a0932eaf48c73dd52717b7e2eae386e807) - voicebank error checker nullness fixes ([@stakira](https://github.com/stakira))
## Misc
- [#1622](https://github.com/stakira/OpenUtau/pull/1622) - Sync translated strings from crowdin to official repo - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))

***
# ~[0.1.562 Beta](https://github.com/stakira/OpenUtau/releases/tag/0.1.562) (07-21-2025)
## Bug Fixes
- [#1610](https://github.com/stakira/OpenUtau/pull/1610) - (Re) MOD+ related bug fixes - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1614](https://github.com/stakira/OpenUtau/pull/1614) - Fix crash when playing test sound on an unavailable audio device - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1616](https://github.com/stakira/OpenUtau/pull/1616) - Fix list items could not be controlled by keyboard - ([@maiko3tattun](https://github.com/maiko3tattun))

## Phonemizer Changes
- [#1609](https://github.com/stakira/OpenUtau/pull/1609) - `FILtoJA` Fixes to `ng` note.lyric bug - ([@Cadlaxa](https://github.com/Cadlaxa))
- [#1612](https://github.com/stakira/OpenUtau/pull/1612) - `S-VOICEVOX JA` Fixed a processing branch for phrases containing slur - ([@rokujyushi](https://github.com/rokujyushi))

***
# ~[0.1.560 Beta](https://github.com/stakira/OpenUtau/releases/tag/0.1.560) (07-19-2025)

> [!CAUTION]
> There is a bug that prevents the use of MOD+.

## Features
### New Features
- [#1509](https://github.com/stakira/OpenUtau/pull/1509) - Add welcome page - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
  - [#1550](https://github.com/stakira/OpenUtau/pull/1550) - Fixed unexpected behavior of welcome page - ([@maiko3tattun](https://github.com/maiko3tattun))  
  <img width="700" alt="image" src="https://github.com/user-attachments/assets/bbb5bcba-ce56-4312-b122-1f49351cd8dc" />
- [#1488](https://github.com/stakira/OpenUtau/pull/1488) - [DiffSinger]Ctrl+R for Load rendered pitch - ([@lunaiproject](https://github.com/lunaiproject))
- [#1506](https://github.com/stakira/OpenUtau/pull/1506) - Enunu style support - ([@rokujyushi](https://github.com/rokujyushi))
- [#1531](https://github.com/stakira/OpenUtau/pull/1531) - Search notes by alias - ([@maiko3tattun](https://github.com/maiko3tattun))  
  <img alt="image" src="https://github.com/user-attachments/assets/78579056-ad46-4118-81c4-3079f9794a55" />
- [#1539](https://github.com/stakira/OpenUtau/pull/1539) - Support displaying real curves from DiffSinger variance predictor - ([@yqzhishen](https://github.com/yqzhishen))  
  <img width="700" alt="image" src="https://github.com/user-attachments/assets/09eb6a91-0cba-4a2e-ba6b-02a21bc6ac06" />
- [#1596](https://github.com/stakira/OpenUtau/pull/1596) - Voicebank Merger - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))  
  <img width="700" alt="image" src="https://github.com/user-attachments/assets/cb6139c5-6d34-437a-af80-422e66c1b676" />
### Feature Enhancements
- [#1447](https://github.com/stakira/OpenUtau/pull/1447) - Removed 0.9f limit of Preutter delta - ([@Cadlaxa](https://github.com/Cadlaxa))
- [#1456](https://github.com/stakira/OpenUtau/pull/1456) - Resize the beginning of part - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1485](https://github.com/stakira/OpenUtau/pull/1485) - Improved mouse cursor - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1521](https://github.com/stakira/OpenUtau/pull/1521) - Hide DiffSinger Language Code in Phoneme Canvas - ([@mrtigermeat](https://github.com/mrtigermeat))
- [#1527](https://github.com/stakira/OpenUtau/pull/1527) - Voicevox refactoring and additional functionality. - ([@rokujyushi](https://github.com/rokujyushi))
- [#1533](https://github.com/stakira/OpenUtau/pull/1533) - Lyric box: add back "enter to apply" feature - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1548](https://github.com/stakira/OpenUtau/pull/1548) - Allow scrolling main view when hovering over Singer List - ([@Kabinet0](https://github.com/Kabinet0))
- [#1554](https://github.com/stakira/OpenUtau/pull/1554) - Improved pitch hit test for overlapping pitches - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1560](https://github.com/stakira/OpenUtau/pull/1560) - Add "Install Wavtool/Resampler (.exe)" in menu - ([@atouu](https://github.com/atouu))
  - [#1599](https://github.com/stakira/OpenUtau/pull/1599) - Translate Exe Setup Dialog - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1567](https://github.com/stakira/OpenUtau/pull/1567) - Added play file button to singers dialog - ([@Kabinet0](https://github.com/Kabinet0))
- [#1568](https://github.com/stakira/OpenUtau/pull/1568) - Simplifies tempo importing - ([@stakira](https://github.com/stakira))
- [#1571](https://github.com/stakira/OpenUtau/pull/1571) - Use Wine directly instead of wrappers on Mac and Linux - ([@atouu](https://github.com/atouu))

## Bug Fixes
### Major Changes
- [#1558](https://github.com/stakira/OpenUtau/pull/1558) - Fix Up/Down keys not working - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1604](https://github.com/stakira/OpenUtau/pull/1604) - Oto validation before worldline rendering - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
  - Many crashes at worldline can now be prevented!
- [#1480](https://github.com/stakira/OpenUtau/pull/1480) - Fixed issue with voice bank loading due to differences in spec between OS - ([@maiko3tattun](https://github.com/maiko3tattun))
### Others
- [#1401](https://github.com/stakira/OpenUtau/pull/1401) - Fixed a bug in Singer's error report - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1460](https://github.com/stakira/OpenUtau/pull/1460) - Fix OpenUtau's data folders appearing in the wrong place on macOS - ([@Nyaacinth](https://github.com/Nyaacinth))
- [#1503](https://github.com/stakira/OpenUtau/pull/1503) - Fixed Vibrato VolLink was not copied - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1541](https://github.com/stakira/OpenUtau/pull/1541) - Fix "#Charset:" - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1555](https://github.com/stakira/OpenUtau/pull/1555) - Fixes OpenUtau's data folders appearing in the wrong place on Linux - ([@Seele-Vollerei32](https://github.com/Seele-Vollerei32))
- [#1562](https://github.com/stakira/OpenUtau/pull/1562) - Fixed OpenUtau getting stuck in the background when closing on Linux (and maybe Mac). - ([@atouu](https://github.com/atouu))
- [#1576](https://github.com/stakira/OpenUtau/pull/1576) - Fix manifest loading - ([@rokujyushi](https://github.com/rokujyushi))
- [#1577](https://github.com/stakira/OpenUtau/pull/1577) - fix legacy plugin output - ([@takunnma5286](https://github.com/takunnma5286))
- [#1586](https://github.com/stakira/OpenUtau/pull/1586) - Check if plugin is exe or bat before using wine - ([@atouu](https://github.com/atouu))
- [#1594](https://github.com/stakira/OpenUtau/pull/1594) - Fix unable to load empty ust - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1603](https://github.com/stakira/OpenUtau/pull/1603) - Fix OpenUtau crashing when oto.ini contains two `#Charset:` lines - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))

## Phonemizer Changes
- [#1530](https://github.com/stakira/OpenUtau/pull/1530) - `New!` Add Turkish CVVC Phonemizer  - ([@IsE333](https://github.com/IsE333))
- [#1597](https://github.com/stakira/OpenUtau/pull/1597) - `New!` Add [FIL VCV & CVVC] and [FIL to JA] phonemizers - ([@Cadlaxa](https://github.com/Cadlaxa))

## Misc
- [#1360](https://github.com/stakira/OpenUtau/pull/1360) - Capitalize machine learning runner names in UI - ([@RedBlackAka](https://github.com/RedBlackAka))
- [#1362](https://github.com/stakira/OpenUtau/pull/1362) - Update all macOS build targets to conform .NET 8 - ([@RedBlackAka](https://github.com/RedBlackAka))
- [#1439](https://github.com/stakira/OpenUtau/pull/1439) - Log on Singer and Phonemizer change - ([@Astel123457](https://github.com/Astel123457))
- [#1479](https://github.com/stakira/OpenUtau/pull/1479) - Updated operating instructions. - ([@rokujyushi](https://github.com/rokujyushi))
  - [#1547](https://github.com/stakira/OpenUtau/pull/1547) - Corrected description - ([@rokujyushi](https://github.com/rokujyushi))
- [#1524](https://github.com/stakira/OpenUtau/pull/1524) - More flexible translation of error messages - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1528](https://github.com/stakira/OpenUtau/pull/1528) - Add GitHub action tests on arm devices for windows, mac and linux - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1529](https://github.com/stakira/OpenUtau/pull/1529) - update csharp-kana to 1.0.2 - ([@wolfgitpr](https://github.com/wolfgitpr))
- [#1536](https://github.com/stakira/OpenUtau/pull/1536) - Sync translations from crowdin to official repo - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1564](https://github.com/stakira/OpenUtau/pull/1564) - Fix drag and drop area in main window - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1565](https://github.com/stakira/OpenUtau/pull/1565) - Fixed translated error messages being overwritten by upper level abstract messages - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1572](https://github.com/stakira/OpenUtau/pull/1572) - [DiffSinger] Fix weired error message - ([@yqzhishen](https://github.com/yqzhishen))
- [#1575](https://github.com/stakira/OpenUtau/pull/1575) - fix typo - ([@shuntia](https://github.com/shuntia))
- [#1591](https://github.com/stakira/OpenUtau/pull/1591) - fix osx upload-artifact action - ([@odeinjul](https://github.com/odeinjul))
- [#1593](https://github.com/stakira/OpenUtau/pull/1593) - Log system encoding - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1598](https://github.com/stakira/OpenUtau/pull/1598) - Fix batch edit order - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1606](https://github.com/stakira/OpenUtau/pull/1606) - Update Resampler Metafiles - ([@Cadlaxa](https://github.com/Cadlaxa))
- [#1607](https://github.com/stakira/OpenUtau/pull/1607) - Installer: High DPI support, MUI2, desktop shortcut, cleanups - ([@RedBlackAka](https://github.com/RedBlackAka))

***
# ~[0.1.550 Beta](https://github.com/stakira/OpenUtau/releases/tag/0.1.550) (05-07-2025)

> [!WARNING]
> **The .ustx version has been updated. It cannot be opened with previous versions of OpenUtau.**

## Features
- [#1432](https://github.com/stakira/OpenUtau/pull/1432) - Classic renderer: support direct - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1483](https://github.com/stakira/OpenUtau/pull/1483) - Clear caches for each phrase - ([@maiko3tattun](https://github.com/maiko3tattun))  
![image](https://github.com/user-attachments/assets/45734db5-c205-4c25-a165-6c2eb2b83509)
- [#1499](https://github.com/stakira/OpenUtau/pull/1499) - Added ability to draw a dash line for the default value of the curve. - ([@rokujyushi](https://github.com/rokujyushi))  
![image](https://github.com/user-attachments/assets/bdd9f2e2-4a86-4c27-a87a-fdeae3dab4ae)
- [#1400](https://github.com/stakira/OpenUtau/pull/1400) - Improvement of Knife Tool and bug fixes for Tool+Ctrl key - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1496](https://github.com/stakira/OpenUtau/pull/1496) - Reduced load wait times for VOICEVOX. - ([@rokujyushi](https://github.com/rokujyushi))
- [#1487](https://github.com/stakira/OpenUtau/pull/1487) - Seperated steps for DiffSinger - ([@lunaiproject](https://github.com/lunaiproject))
- [#1166](https://github.com/stakira/OpenUtau/pull/1166) - Add recovery project function - ([@maiko3tattun](https://github.com/maiko3tattun))  
![image](https://github.com/stakira/OpenUtau/assets/130257355/f9573d9a-b145-446b-86a3-97aa741e8f5a)
- [#1409](https://github.com/stakira/OpenUtau/pull/1409) - More ExpSelector. - ([@rokujyushi](https://github.com/rokujyushi))
![image](https://github.com/user-attachments/assets/e56a4078-60ab-4ce7-ba19-00a6f058e3e5)

## Bug Fixes
- [#1462](https://github.com/stakira/OpenUtau/pull/1462) - Fixed many expression issues and improved the properties panel - ([@maiko3tattun](https://github.com/maiko3tattun))
  - Remove expression when right-clicking combo box in properties panel
  - Changed to remove instead of set the value when the same value as the default value of track expression is selected in the properties panel
  - Fixed Phonemizer not running immediately after selecting voice color in properties panel
  - Fixed a case where the expression of the first phoneme of the selected note should be displayed, but the one of the second or later phonemes was displayed
  - When right-clicking on the UI to delete an expression, modified to delete unwanted expressions with the same abbr in the same note
- [#1449](https://github.com/stakira/OpenUtau/pull/1449) - Fix part always snapping to measure line if the starting position of a part isn't in the current view - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1433](https://github.com/stakira/OpenUtau/pull/1433) - Fix Command Injection Vulnerability in Classic Renderer - ([@Cadlaxa](https://github.com/Cadlaxa))
- [#1526](https://github.com/stakira/OpenUtau/pull/1526) - Fix textbox caret behavior - ([@IsE333](https://github.com/IsE333))
- [#1515](https://github.com/stakira/OpenUtau/pull/1515) - Fix unable to paste multiline lyrics into lyrics dialog - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1514](https://github.com/stakira/OpenUtau/pull/1514) - Use available screen if no primary screen is set - ([@atouu](https://github.com/atouu))
- [#1512](https://github.com/stakira/OpenUtau/pull/1512) - Don't use `/usr/bin`, just use `fc-match` - ([@Lord-Valen](https://github.com/Lord-Valen))
- [#1498](https://github.com/stakira/OpenUtau/pull/1498) - Zip file produced by voicebank publisher should use slash, not backslash - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1478](https://github.com/stakira/OpenUtau/pull/1478) - TrackHeader changes. - ([@rokujyushi](https://github.com/rokujyushi))

## Phonemizer Changes
- [#1436](https://github.com/stakira/OpenUtau/pull/1436) - `EN C+V` Code fixes and Dictionary updates - ([@Cadlaxa](https://github.com/Cadlaxa))
- [#1445](https://github.com/stakira/OpenUtau/pull/1445) - `JA VCV & CVVC` Enhanced test code and Bug fixes - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1426](https://github.com/stakira/OpenUtau/pull/1426) - `EN ARPA+` Fixes vanila Arpabet phonemes conflicts to Romaji VV - ([@Cadlaxa](https://github.com/Cadlaxa))
- [#1501](https://github.com/stakira/OpenUtau/pull/1501) - `EN VCCV` Update Starlight fix - ([@AnAndroNerd](https://github.com/AnAndroNerd))
- [#1505](https://github.com/stakira/OpenUtau/pull/1505) - `EN` Update ARPA+, EN C+V, and EN-XSAMPA Phonemizers - ([@Cadlaxa](https://github.com/Cadlaxa))

## Misc
- [#1457](https://github.com/stakira/OpenUtau/pull/1457) - Show window title in macOS - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1523](https://github.com/stakira/OpenUtau/pull/1523) - More friendly error message for renderer that doesn't support autopitch - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1492](https://github.com/stakira/OpenUtau/pull/1492) - When saving oto.ini, always include alias in oto lines even if the filename and alias are same - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1403](https://github.com/stakira/OpenUtau/pull/1403) - Show Note Properties Panel by default - ([@maiko3tattun](https://github.com/maiko3tattun))

***
# ~[0.1.549 Beta](https://github.com/stakira/OpenUtau/releases/tag/0.1.549) (02-24-2025)
> **This version is upgraded from .NET 6 to .NET 8, where in theory 10.14 support is dropped.**
## Features
- [#1424](https://github.com/stakira/OpenUtau/pull/1424) - DiffSinger: support SHFC (pitch shift curve) - ([@yqzhishen](https://github.com/yqzhishen))
- [#1408](https://github.com/stakira/OpenUtau/pull/1408) - Move to the next track part with PageUp/PageDown keys - ([@maiko3tattun](https://github.com/maiko3tattun))

https://private-user-images.githubusercontent.com/130257355/411304902-d9c39628-ada3-40e7-b7d1-cc0115a8c361.mp4
- [#1419](https://github.com/stakira/OpenUtau/pull/1419) - Change batch edit quantize to grid size - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1204](https://github.com/stakira/OpenUtau/pull/1204) - Add hover tooltip to music key menu and snap div menu - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1386](https://github.com/stakira/OpenUtau/pull/1386) - show singer default phonemizer in track phonemizer menu - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
![image](https://github.com/user-attachments/assets/6fabe7a6-4023-490d-8a23-2119ec82c27f)

## Bug Fixes
- [#1375](https://github.com/stakira/OpenUtau/pull/1375) - Musicxml: fix crash after importing a musicxml without tempo - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1376](https://github.com/stakira/OpenUtau/pull/1376) - Remove conditions on phoneme definition checks of dspitch - ([@yqzhishen](https://github.com/yqzhishen))
- [#1389](https://github.com/stakira/OpenUtau/pull/1389) - fix slice tool extending the part too much - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1394](https://github.com/stakira/OpenUtau/pull/1394) - Centering the Splash Window - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1395](https://github.com/stakira/OpenUtau/pull/1395) - Fix Note Properties Panel not working after auto reloading oto - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1406](https://github.com/stakira/OpenUtau/pull/1406) - Faster expression commands - ([@maiko3tattun](https://github.com/maiko3tattun))

## Phonemizer Changes
- [#1329](https://github.com/stakira/OpenUtau/pull/1329) - `New!` Add Arpabet C+V Phonemizer - ([@Cadlaxa](https://github.com/Cadlaxa))
- [#1425](https://github.com/stakira/OpenUtau/pull/1425) - `ZH CVVC` length of VC should be based on the whole length of the syllable, including slur notes - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1275](https://github.com/stakira/OpenUtau/pull/1275) - `DIFFS EN+` fixes to phoneme replacements with LangCode - ([@Cadlaxa](https://github.com/Cadlaxa))
- [#1371](https://github.com/stakira/OpenUtau/pull/1371) - `EN ARPA+` Add dynamic variations for 'dynMid_vv' - ([@Cadlaxa](https://github.com/Cadlaxa))
- [#1399](https://github.com/stakira/OpenUtau/pull/1399) - `KO` [KO Classic Phonemizers + BaseKoreanPhonemizer] Improve KO romanization + phonetic hint fix + typo fix - ([@lottev1991](https://github.com/lottev1991))
- [#1380](https://github.com/stakira/OpenUtau/pull/1380) - `JA` Add "legacy" to the names of JA VCV and JA CVVC phonemizers - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))

## Misc
- [#1388](https://github.com/stakira/OpenUtau/pull/1388) - Fix github actions not working on linux - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1374](https://github.com/stakira/OpenUtau/pull/1374) - Add links to FAQ, and instructions for solving 'This app is damaged' on macOS into release page - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1390](https://github.com/stakira/OpenUtau/pull/1390) - Add GitHub issue template for feature requests - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))

***
# ~[0.1.547 Beta](https://github.com/stakira/OpenUtau/releases/tag/0.1.547) (12-20-2024)
## Features
- [#1327](https://github.com/stakira/OpenUtau/pull/1327) - Adds a splash window - ([@stakira](https://github.com/stakira))
- [#1152](https://github.com/stakira/OpenUtau/pull/1152) - Add MusicXML Import - ([@porime42](https://github.com/porime42))
- [#1342](https://github.com/stakira/OpenUtau/pull/1342) - Refactor preferences page to using a navigation sidebar, rearrange preference items - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1336](https://github.com/stakira/OpenUtau/pull/1336) - Add Full Screen option - ([@RedBlackAka](https://github.com/RedBlackAka))
- [#1334](https://github.com/stakira/OpenUtau/pull/1334) - Multi-selection support for ExpressionsDialog. - ([@rokujyushi](https://github.com/rokujyushi))

## Bug Fixes
- [#1325](https://github.com/stakira/OpenUtau/pull/1325) - Key scale change function modified. - ([@rokujyushi](https://github.com/rokujyushi))

## Phonemizer Changes
- [#1281](https://github.com/stakira/OpenUtau/pull/1281) - `DIFFS JA` Diffsinger Ja phonemizer: support kana - ([@wolfgitpr](https://github.com/wolfgitpr))

## Translation
- [#1332](https://github.com/stakira/OpenUtau/pull/1332) - Update German translation - ([@RedBlackAka](https://github.com/RedBlackAka))

## Misc
- [#1356](https://github.com/stakira/OpenUtau/pull/1356) - When inputting invalid number, textbox won't show yellow error message - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1353](https://github.com/stakira/OpenUtau/pull/1353) - Upgrade OnnxRuntime and DirectML, fixing DiffSinger on mac arm64 - ([@RedBlackAka](https://github.com/RedBlackAka))
- [#1337](https://github.com/stakira/OpenUtau/pull/1337) - Resolve a warning - ([@RedBlackAka](https://github.com/RedBlackAka))
- [#1358](https://github.com/stakira/OpenUtau/pull/1358) - sync strings - ([@stakira](https://github.com/stakira))
- [#1328](https://github.com/stakira/OpenUtau/pull/1328) - When "saving as", or exporting wav, use the filename of the current file by default - ([@Cadlaxa](https://github.com/Cadlaxa))

***
# ~[0.1.546 Beta](https://github.com/stakira/OpenUtau/releases/tag/0.1.546) (11-13-2024)
## Features
- [#1268](https://github.com/stakira/OpenUtau/pull/1268) - Add DrawLine Pitch Tool - ([@rokujyushi](https://github.com/rokujyushi))  
![image](https://github.com/user-attachments/assets/a3fa6073-0990-45a1-ac38-b41bb86e2d0d)
  - This corresponds to the Line tool only in the Piano Roll and to the Line tool (Shift+Left click) and Horizontal Line tool (Shift+Ctrl+Left click) in the Expression panel.
- [#1295](https://github.com/stakira/OpenUtau/pull/1295) - Support SimpleENUNUServer0.5.0 - ([@rokujyushi](https://github.com/rokujyushi))
- [#1287](https://github.com/stakira/OpenUtau/pull/1287) - VOICEVOXRenderer Tempo change support - ([@rokujyushi](https://github.com/rokujyushi))
- [#1285](https://github.com/stakira/OpenUtau/pull/1285) - When resetting expressions, only reset curve expressions where the note is selected; Remove duplicate editing macros - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))

## Bug Fixes
- [#1179](https://github.com/stakira/OpenUtau/pull/1179) - [KoreanPhonemizerUtil] Fixed crashing when reading ini from non-utf-8 singers - ([@EX3exp](https://github.com/EX3exp))
- [#1290](https://github.com/stakira/OpenUtau/pull/1290) - Fix openutau failing to import midi if it contains two lyric events at the same time - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1319](https://github.com/stakira/OpenUtau/pull/1319) - fix diffsinger pitch: pre&tail SP pitch - ([@wolfgitpr](https://github.com/wolfgitpr))
- [#1311](https://github.com/stakira/OpenUtau/pull/1311) - Fix openutau crashing when trying to edit the preutterence of an invalid phoneme - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1284](https://github.com/stakira/OpenUtau/pull/1284) - Fix openutau crashing after pressing Ctrl+Z in lyric box twice and enter - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1286](https://github.com/stakira/OpenUtau/pull/1286) - Fix LyricBox UI - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1324](https://github.com/stakira/OpenUtau/pull/1324) - Fix LyricBox - ([@rokujyushi](https://github.com/rokujyushi))
- [#1323](https://github.com/stakira/OpenUtau/pull/1323) - Fix ExpEdit - ([@rokujyushi](https://github.com/rokujyushi))

## Phonemizer Changes
- [#1303](https://github.com/stakira/OpenUtau/pull/1303) - `New!` Add "Chinese CVV Plus Phonemizer" - ([@2xxbin](https://github.com/2xxbin))
- [#1276](https://github.com/stakira/OpenUtau/pull/1276) - `ZH` update chinese g2p - ([@wolfgitpr](https://github.com/wolfgitpr))
- [#1321](https://github.com/stakira/OpenUtau/pull/1321) - `EN VCCV` Missed exception for "skt" - ([@BagelHero](https://github.com/BagelHero))
- [#1320](https://github.com/stakira/OpenUtau/pull/1320) - `EN VCCV` Starlight Fix - ([@AnAndroNerd](https://github.com/AnAndroNerd))
- [#1280](https://github.com/stakira/OpenUtau/pull/1280) - `DIFFS` Diffsinger phonemizers: G2p results add langcode by default; Check if phoneme is supported by duration model - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1278](https://github.com/stakira/OpenUtau/pull/1278) - `DIFFS` diffsinger phonemizers: error in one sentence won't affect the following sentences - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1289](https://github.com/stakira/OpenUtau/pull/1289) - `EN ARPA+` Fix [CCV] lastC and removed some redundant CCV splitter - ([@Cadlaxa](https://github.com/Cadlaxa))
- [#1316](https://github.com/stakira/OpenUtau/pull/1316) - `Based` Update SyllableBasedPhonemizer.cs - ([@lonelyapple011](https://github.com/lonelyapple011))
- [#1314](https://github.com/stakira/OpenUtau/pull/1314) - `KO CV` Modify KoreanCVPhonemizer.cs - ([@2xxbin](https://github.com/2xxbin))
- [#1297](https://github.com/stakira/OpenUtau/pull/1297) - `TH VCCV` Fix phoneme parser for Thai VCCV - ([@printto](https://github.com/printto))
- [#1305](https://github.com/stakira/OpenUtau/pull/1305) - `KO` Add Romanized lyrics support to all Korean phonemizers - ([@2xxbin](https://github.com/2xxbin))

## Misc
- [#1308](https://github.com/stakira/OpenUtau/pull/1308) - [High priority] Bump JSON package version version to 8.0.5 - ([@lottev1991](https://github.com/lottev1991))
- [#1317](https://github.com/stakira/OpenUtau/pull/1317) - Rename 'OpenUtau Wiki' in the 'help' section on the toolbar to 'OpenUtau Documentation' - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1262](https://github.com/stakira/OpenUtau/pull/1262) - Remove restart notes from preferences where it doesn't apply and installer improvements - ([@RedBlackAka](https://github.com/RedBlackAka))

***
# ~[0.1.543 Beta](https://github.com/stakira/OpenUtau/releases/tag/0.1.543) (09-02-2024)
## Features
- [#1241](https://github.com/stakira/OpenUtau/pull/1241) - VOICEVOX Volume operation F0 read support - ([@rokujyushi](https://github.com/rokujyushi))
- [#1248](https://github.com/stakira/OpenUtau/pull/1248) - Support Diffsinger multi-dictionary - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1256](https://github.com/stakira/OpenUtau/pull/1256) - Add checks for phoneme definitions in dsdict.yaml - ([@yqzhishen](https://github.com/yqzhishen))

## Bug Fixes
- [#1260](https://github.com/stakira/OpenUtau/pull/1260) - Fix openutau crash when exporting midi file with a note above 127 - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1234](https://github.com/stakira/OpenUtau/pull/1234) - Message box maximum height and scroll bars in place - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1255](https://github.com/stakira/OpenUtau/pull/1255) - Avoid repeated dictionary and model loading in DiffSingerBasePhonemizer - ([@yqzhishen](https://github.com/yqzhishen))
- [#1257](https://github.com/stakira/OpenUtau/pull/1257) - Improve error message when parameter is missing for DiffSinger acoustic models - ([@yqzhishen](https://github.com/yqzhishen))
- [#1232](https://github.com/stakira/OpenUtau/pull/1232) - use the first available audio device - ([@krn1pnc](https://github.com/krn1pnc))

## Phonemizer Changes
- [#1242](https://github.com/stakira/OpenUtau/pull/1242) - `New!` Add SimpleVOICEVOX ENtoJA Phonemizer - ([@rokujyushi](https://github.com/rokujyushi))
- [#1189](https://github.com/stakira/OpenUtau/pull/1189) - `EN ARPA+` Update ARPA+ G2p Dictionary (preparing for model retrain) - ([@Cadlaxa](https://github.com/Cadlaxa))
- [#1243](https://github.com/stakira/OpenUtau/pull/1243) - `EN ARPA+` [ARPA+ Phonemizer] Re-adjusted consonant lengths - ([@Cadlaxa](https://github.com/Cadlaxa))
- [#1235](https://github.com/stakira/OpenUtau/pull/1235) - `ZH` fix g2p input bug - ([@wolfgitpr](https://github.com/wolfgitpr))

## Translation
- [#1249](https://github.com/stakira/OpenUtau/pull/1249) - Update Strings.ru-RU.axaml - ([@KagamineP](https://github.com/KagamineP))
- [#1253](https://github.com/stakira/OpenUtau/pull/1253) - Update translations in Strings.de-DE.axaml - ([@RedBlackAka](https://github.com/RedBlackAka))
- [#1254](https://github.com/stakira/OpenUtau/pull/1254) - Updated Vietnamese translation - ([@Huangphoux](https://github.com/Huangphoux))

## Misc
- [#1263](https://github.com/stakira/OpenUtau/pull/1263) - Update README.md - ([@stakira](https://github.com/stakira))

***
# ~[0.1.542 Beta](https://github.com/stakira/OpenUtau/releases/tag/0.1.542) (08-04-2024)
## Features
- [#1223](https://github.com/stakira/OpenUtau/pull/1223) - Add a 'reset all' editing macro - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))

## Phonemizer Changes
- [#1202](https://github.com/stakira/OpenUtau/pull/1202) - `New!` Thai VCCV Phonemizer - ([@printto](https://github.com/printto))
- [#1207](https://github.com/stakira/OpenUtau/pull/1207) - `ZH` `ZH-YUE` update chinese/cantonese g2p - ([@wolfgitpr](https://github.com/wolfgitpr))
- [#1212](https://github.com/stakira/OpenUtau/pull/1212) - `KO` Apply Korean sandhi rules to Classic phonemizers - ([@lottev1991](https://github.com/lottev1991))
- [#1208](https://github.com/stakira/OpenUtau/pull/1208) - `DIFFS JA` [Bug fix; important] [JA Monophone G2P] Small phoneme fix - ([@lottev1991](https://github.com/lottev1991))
- [#1196](https://github.com/stakira/OpenUtau/pull/1196) - `EN X-SAMPA` [Bug fix] [EN X-SAMPA Phonemizer] Fix several bugs + Add dark L vowels - ([@lottev1991](https://github.com/lottev1991))
- [#1191](https://github.com/stakira/OpenUtau/pull/1191) - `EN ARPA+` Fix [CV] validation on ARPA+ Phonemizer - ([@Cadlaxa](https://github.com/Cadlaxa))
- [#1190](https://github.com/stakira/OpenUtau/pull/1190) - `JA VCV & CVVC` [Bug fix; important] [JA Presamp Phonemizer] Bugfix for empty [PRIORITY] and [REPLACE] newlines + update MsToTickAt() code - ([@lottev1991](https://github.com/lottev1991))

## Misc
- [#1227](https://github.com/stakira/OpenUtau/pull/1227) - Fix import tracks - ([@rokujyushi](https://github.com/rokujyushi))
- [#1230](https://github.com/stakira/OpenUtau/pull/1230) - Adds github action for release - ([@stakira](https://github.com/stakira))
- [69d7ecd](https://github.com/stakira/OpenUtau/commit/69d7ecd4305d3524d2a5a0c0571fdfc8d42190a0) - build worldline for old macos versions - ([@stakira](https://github.com/stakira))

***
# ~[0.1.532 Beta](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.532) (07-27-2024)
## Misc
- [#1225](https://github.com/stakira/OpenUtau/pull/1225) - Consolidates to a single audio backend - ([@stakira](https://github.com/stakira))

***
# ~[0.1.529](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.529) (07-24-2024)
## Features
- [#1216](https://github.com/stakira/OpenUtau/pull/1216) - VOICEVOX F0 editing support and folder structure modification - ([@rokujyushi](https://github.com/rokujyushi))
- [#1182](https://github.com/stakira/OpenUtau/pull/1182) - Add 'Install singer' to singer menu in track header - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1194](https://github.com/stakira/OpenUtau/pull/1194) - Added Shebang to Generated Shell File. - ([@ochakochatblanc](https://github.com/ochakochatblanc))  
  - To run resampler on macOS wine

## Bug Fixes
- [#1176](https://github.com/stakira/OpenUtau/pull/1176) - Fix pitch misplaced when using overwrite pitch tool - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1177](https://github.com/stakira/OpenUtau/pull/1177) - Clear vibrato and MOD+ after pitch baking - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1178](https://github.com/stakira/OpenUtau/pull/1178) - Show progress dialog when loading rendered pitch (and potentially other time-consuming batch edits) - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1195](https://github.com/stakira/OpenUtau/pull/1195) - Fix pitch curve 'add point' misplaced - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1197](https://github.com/stakira/OpenUtau/pull/1197) - Fix very long note produced by knife tool - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1198](https://github.com/stakira/OpenUtau/pull/1198) - Fix issue when using exe wavtools on Linux - ([@parallelepiped2718](https://github.com/parallelepiped2718))
- [#1220](https://github.com/stakira/OpenUtau/pull/1220) - Fix several bugs on pressing Ctrl+Z in TextBoxes - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))

## Translation
- [#1173](https://github.com/stakira/OpenUtau/pull/1173) - Update Strings.pl-PL.axaml - ([@KluelessKisa](https://github.com/KluelessKisa))
- [#1180](https://github.com/stakira/OpenUtau/pull/1180) - Updated Korean strings - ([@EX3exp](https://github.com/EX3exp))
- [#1210](https://github.com/stakira/OpenUtau/pull/1210) - Updated zh-CN strings - ([@ssmzhn](https://github.com/ssmzhn))
- [#1218](https://github.com/stakira/OpenUtau/pull/1218) - Update Strings.pl-PL.axaml - ([@KluelessKisa](https://github.com/KluelessKisa))

## Misc
- [#1162](https://github.com/stakira/OpenUtau/pull/1162) - Include frq files when publishing voice banks - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1174](https://github.com/stakira/OpenUtau/pull/1174) - Remove NAudio midi importer - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1175](https://github.com/stakira/OpenUtau/pull/1175) - Show error message to install Visual C++ - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1181](https://github.com/stakira/OpenUtau/pull/1181) - GitHub actions test won't be canceled if it fails on one OS - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1213](https://github.com/stakira/OpenUtau/pull/1213) - Update System.Text.Json to 8.0.4 because of vulnerability - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1217](https://github.com/stakira/OpenUtau/pull/1217) - Add .ustx file association on Windows and MacOS - ([@RedBlackAka](https://github.com/RedBlackAka))

***
# ~[0.1.501 Beta](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.501) (06-09-2024)

> [!CAUTION]
> 0.1.497Beta has known bugs! Please use 0.1.501Beta.

## Features
- [#1134](https://github.com/stakira/OpenUtau/pull/1134) - Organising the reset menu , add reset all parameter menu - ([@LitMus9](https://github.com/LitMus9))
![image](https://github.com/stakira/OpenUtau/assets/130257355/cf71f900-768f-428b-88b3-40eba3a6fe96)
- [#1141](https://github.com/stakira/OpenUtau/pull/1141) - Read track names from midi, write track names into midi - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1142](https://github.com/stakira/OpenUtau/pull/1142) - Add Overwrite Pitch Tool - ([@maiko3tattun](https://github.com/maiko3tattun))  
  There are no good icons available yet ( ˘ω˘ )

  https://github.com/stakira/OpenUtau/assets/130257355/9d7db5ce-37bf-44b5-92d6-3ce3a7bec8b8
- [#1146](https://github.com/stakira/OpenUtau/pull/1146) - First linkage with setparam - ([@maiko3tattun](https://github.com/maiko3tattun))  
![image](https://github.com/stakira/OpenUtau/assets/130257355/37badc70-cfe1-449f-a8e1-5e5930ebf595)

- [#1153](https://github.com/stakira/OpenUtau/pull/1153) - Ignore slur lyrics when merging notes with Ctrl+U - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1156](https://github.com/stakira/OpenUtau/pull/1156) - Auto save even when ustx is not saved - ([@tansansuisui](https://github.com/tansansuisui))
- [#1158](https://github.com/stakira/OpenUtau/pull/1158) - Changed font size to be calculated in order of height - ([@rokujyushi](https://github.com/rokujyushi))  
![image](https://github.com/stakira/OpenUtau/assets/130257355/b806b0db-b143-4066-8da8-069f84082278)
- [#1168](https://github.com/stakira/OpenUtau/pull/1168) - Add "Open singers location" menu - ([@maiko3tattun](https://github.com/maiko3tattun))  
![image](https://github.com/stakira/OpenUtau/assets/130257355/cefd0f24-f81a-4d70-afa6-ab7f3974a7f8)

## Bug Fixes
- [#1124](https://github.com/stakira/OpenUtau/pull/1124) - Fix LyricsReplaceDialog bug - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1130](https://github.com/stakira/OpenUtau/pull/1130) - Fix importing project into an unsaved project - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1131](https://github.com/stakira/OpenUtau/pull/1131) - Enhance diffsinger error messages; diffsinger phonemizer fix - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1135](https://github.com/stakira/OpenUtau/pull/1135) - Fixed error in voice color remapping - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1136](https://github.com/stakira/OpenUtau/pull/1136) - Fix unable to open old projects that contains P flag - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1137](https://github.com/stakira/OpenUtau/pull/1137) - Fix OU not launching if project fails to open - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1140](https://github.com/stakira/OpenUtau/pull/1140) - Fix spaces being ignored in presamp.ini VCPAD - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1144](https://github.com/stakira/OpenUtau/pull/1144) - Fix openutau crash when trying to install singer from an encrypted archive file - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1154](https://github.com/stakira/OpenUtau/pull/1154) - Fix openutau crash when opening a project with a diffsinger voicebank that isn't installed on this PC - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1155](https://github.com/stakira/OpenUtau/pull/1155) - Fix OpenUtau failed to search singers when the user runs OpenUtau for the first time - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1163](https://github.com/stakira/OpenUtau/pull/1163) - Fixed crash when unzipping singer fails - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1169](https://github.com/stakira/OpenUtau/pull/1169) - Fix openutau crash when g2p lyrics helper failed to provide a suggestion - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1171](https://github.com/stakira/OpenUtau/pull/1171) - Fix wavtool not working when full path contains 2 byte characters - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1172](https://github.com/stakira/OpenUtau/pull/1172) - Fix unable to save - ([@maiko3tattun](https://github.com/maiko3tattun))

## Phonemizer Changes
- [#1132](https://github.com/stakira/OpenUtau/pull/1132) - `Various Korean` Update Korean Phonemizers (#1121 + #1122) - ([@EX3exp](https://github.com/EX3exp))
- [#1143](https://github.com/stakira/OpenUtau/pull/1143) - `JA VCV&CVVC` Fix start glottalstop - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1150](https://github.com/stakira/OpenUtau/pull/1150) - `JA VCV&CVVC` Some starting consonant fixes/adjustments - ([@lottev1991](https://github.com/lottev1991))
- [#1149](https://github.com/stakira/OpenUtau/pull/1149) - `JA VCV` Support * あ - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1147](https://github.com/stakira/OpenUtau/pull/1147) - `DISSF JA` Add Japanese monophone G2P (tailored to AI voicebanks/phonemizers) + add support to Diffsinger Japanese Phonemizer - ([@lottev1991](https://github.com/lottev1991))
- [#1161](https://github.com/stakira/OpenUtau/pull/1161) - `ZH CVVC` Fix note timing after tempo change - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1165](https://github.com/stakira/OpenUtau/pull/1165) - `EN X-SAMPA` Multiple fixes - ([@lottev1991](https://github.com/lottev1991))

## Misc
- [#1125](https://github.com/stakira/OpenUtau/pull/1125) - Fixed force activation of the main window when an error dialog is shown - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1138](https://github.com/stakira/OpenUtau/pull/1138) - Showing positions that failed to render - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1160](https://github.com/stakira/OpenUtau/pull/1160) - Add support for straycat's cache files - ([@Astel123457](https://github.com/Astel123457))
- [#1170](https://github.com/stakira/OpenUtau/pull/1170) - Show InputGesture on notes context menu - ([@maiko3tattun](https://github.com/maiko3tattun))

***
# ~[0.1.463 Beta](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.463) (05-10-2024)
## Features
- [#1126](https://github.com/stakira/OpenUtau/pull/1126) - Add option to move only the cursor and not scroll back when pausing playback - ([@maiko3tattun](https://github.com/maiko3tattun))

## Bug Fixes
- [#1100](https://github.com/stakira/OpenUtau/pull/1100) - Fix deleting expressions - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1118](https://github.com/stakira/OpenUtau/pull/1118) - Add flag marge function - ([@maiko3tattun](https://github.com/maiko3tattun))
  - Automatically merge expression flags to avoid duplication when opening old projects in a new OU.
- [#1112](https://github.com/stakira/OpenUtau/pull/1112) - fix tool selection bug when default pen is pen plus - ([@lennyservant](https://github.com/lennyservant))
- [#1113](https://github.com/stakira/OpenUtau/pull/1113) - Fix openutau crash when dragging an invalid zip file into openutau window - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1116](https://github.com/stakira/OpenUtau/pull/1116) - Fix loading and error dialog - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1129](https://github.com/stakira/OpenUtau/pull/1129) - Fix openutau unable to play if the first note starts at 0 tick - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))

## Phonemizer Changes
- [#1110](https://github.com/stakira/OpenUtau/pull/1110) - `EN VCCV` Small Fixes for EN VCCV before stable release - ([@AnAndroNerd](https://github.com/AnAndroNerd))
- [#1115](https://github.com/stakira/OpenUtau/pull/1115) - `EN X-SAMPA` Fallbacks for Canadian Raising in English X-Sampa Phonemizer - ([@AnAndroNerd](https://github.com/AnAndroNerd))
- [#1117](https://github.com/stakira/OpenUtau/pull/1117) - `New!` Add KoreanG2P and DiffsingerKoreanG2PPhonemizer - ([@Cardroid](https://github.com/Cardroid))
- [#1120](https://github.com/stakira/OpenUtau/pull/1120) - `DIFFS KO` `ENUNU KO` Improved KO DIFFS&KO ENUNU Phonemizer - ([@EX3exp](https://github.com/EX3exp))
- [#1123](https://github.com/stakira/OpenUtau/pull/1123) - `EN ARPA+` Fix `[ng g]` instances turning into `[ng]` when `CCV` is present - ([@Cadlaxa](https://github.com/Cadlaxa))

## Misc
- [#1108](https://github.com/stakira/OpenUtau/pull/1108) - Error log minor fix - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1111](https://github.com/stakira/OpenUtau/pull/1111) - [DiffSinger] Fix error message on `mel_scale` - ([@yqzhishen](https://github.com/yqzhishen))
- [#1127](https://github.com/stakira/OpenUtau/pull/1127) - Fix github action tests failing on MacOS - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))

***
# ~[0.1.443 Beta](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.443) (04-20-2024)
## Features
- [#1104](https://github.com/stakira/OpenUtau/pull/1104) - [DiffSinger] Migrate to continuous acceleration profiles - ([@yqzhishen](https://github.com/yqzhishen))
- [#1093](https://github.com/stakira/OpenUtau/pull/1093) - [DiffSinger] Add tensor caching system - ([@yqzhishen](https://github.com/yqzhishen))
- [#1090](https://github.com/stakira/OpenUtau/pull/1090) - Cache frq for MOD+ - ([@maiko3tattun](https://github.com/maiko3tattun))
  * Speeds up MOD+ significantly
- [#1092](https://github.com/stakira/OpenUtau/pull/1092) - Modification of Voicevox around licenses - ([@rokujyushi](https://github.com/rokujyushi))

## Bug Fixes
- [#1085](https://github.com/stakira/OpenUtau/pull/1085) - Fix font query result with multiple comma-separated values - ([@SoulMelody](https://github.com/SoulMelody))

## Phonemizer Changes
- [#1095](https://github.com/stakira/OpenUtau/pull/1095) - `EN VCCV` Update EnglishVCCVPhonemizer.cs - ([@GeneralNuisance0](https://github.com/GeneralNuisance0))
  * Adds support for the Canadian raising vowels of [Y] and [W]
- [#1088](https://github.com/stakira/OpenUtau/pull/1088) - `EN ARPA+` Fix **`[V V]`** diphthong sustain and Change ending **`t`** or **`d`** with **'dx'** via **`'`** suffix - ([@Cadlaxa](https://github.com/Cadlaxa))
- [#1101](https://github.com/stakira/OpenUtau/pull/1101) - `EN X-SAMPA` Vowel fallback bug fixes - ([@lottev1991](https://github.com/lottev1991))

## Translation
- [#1081](https://github.com/stakira/OpenUtau/pull/1081) - Update Japanese translations - ([@maiko3tattun](https://github.com/maiko3tattun))

## Misc
- [#1086](https://github.com/stakira/OpenUtau/pull/1086) - Translate error messages and put them in the expander - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1107](https://github.com/stakira/OpenUtau/pull/1107) - Improved translation of error messages for more flexibility - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1102](https://github.com/stakira/OpenUtau/pull/1102) - Fixed icons - ([@rokujyushi](https://github.com/rokujyushi))

***
# ~[0.1.421 Beta](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.421) (03-28-2024)
## Features
- [#1043](https://github.com/stakira/OpenUtau/pull/1043) - Add a feature to only render and play selected region - ([@liuycsd](https://github.com/liuycsd))
  - `Alt + Space` plays only the selected note and its surroundings
- [#1068](https://github.com/stakira/OpenUtau/pull/1068) - Modulation plus - ([@maiko3tattun](https://github.com/maiko3tattun))
  - Affects modulation to the pitch curve  
![image](https://github.com/stakira/OpenUtau/assets/130257355/062bc644-5f9a-45eb-9acc-8e2d92c82a62)
- [#1073](https://github.com/stakira/OpenUtau/pull/1073) - Part duration enhancement - ([@maiko3tattun](https://github.com/maiko3tattun))
  - Added storing the length of the part in ustx.
  - When entering and resizing notes, the part is automatically extended by one measure when the length of the part is less than one measure remaining.
- [#1075](https://github.com/stakira/OpenUtau/pull/1075) - VOICEVOX support - ([@rokujyushi](https://github.com/rokujyushi))
  - Partial support for the song function of the [VOICEVOX](https://voicevox.hiroshiba.jp/), popular with fans of text-to-speech!
- [#1053](https://github.com/stakira/OpenUtau/pull/1053) - [DiffSinger] Add more mel checks between vocoder and acoustic model - ([@yqzhishen](https://github.com/yqzhishen))
- [#1058](https://github.com/stakira/OpenUtau/pull/1058) - Add "Edit" menu to menu bar of main window and piano roll window (Undo, Redo, etc.) - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1059](https://github.com/stakira/OpenUtau/pull/1059) - Add Normalize (P flag) to expressions - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1074](https://github.com/stakira/OpenUtau/pull/1074) - Reset preset combo box in the note properties panel - ([@maiko3tattun](https://github.com/maiko3tattun))

## Bug Fixes
- [#1051](https://github.com/stakira/OpenUtau/pull/1051) - fix bugged piano roll when first opened while the project is playing - ([@lennyservant](https://github.com/lennyservant))
- [#1055](https://github.com/stakira/OpenUtau/pull/1055) - fix strings startswith "\t- " in yaml - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1060](https://github.com/stakira/OpenUtau/pull/1060) - Fix plugin failing to run when OU path contains space - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1061](https://github.com/stakira/OpenUtau/pull/1061) - Diffsinger: fix openutau unable to load the other voicebanks if one diffsinger has mistake. - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1071](https://github.com/stakira/OpenUtau/pull/1071) - Fix singer name translation - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1072](https://github.com/stakira/OpenUtau/pull/1072) - Fix UPhonemeOverride.phoneme - ([@maiko3tattun](https://github.com/maiko3tattun))

## Phonemizer Changes
- [#1038](https://github.com/stakira/OpenUtau/pull/1038) - `New!` Add ARPAsing Plus Phonemizer - ([@Cadlaxa](https://github.com/Cadlaxa))
- [#1077](https://github.com/stakira/OpenUtau/pull/1077) - `EN X-SAMPA` Add Support for VV Split Fallback for Xsampa vb's especially to Delta 5 vbs - ([@Cadlaxa](https://github.com/Cadlaxa))
- [#1052](https://github.com/stakira/OpenUtau/pull/1052) - `JA VCV & CVVC` The color of VC will be that of CV unless otherwise specified, and bug fixes - ([@maiko3tattun](https://github.com/maiko3tattun))

## Translation
- [#1067](https://github.com/stakira/OpenUtau/pull/1067) - Update Korean translation - ([@EX3exp](https://github.com/EX3exp))
- [#1080](https://github.com/stakira/OpenUtau/pull/1080) - update simplified Chinese localization - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))

## Misc
- [#1057](https://github.com/stakira/OpenUtau/pull/1057) - Move hanzi to pinyin converter to 'lyrics' category - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1076](https://github.com/stakira/OpenUtau/pull/1076) - Update README.md (add g2p compiling wiki) - ([@Cadlaxa](https://github.com/Cadlaxa))
- [#1078](https://github.com/stakira/OpenUtau/pull/1078) - Improved view position when pasting note - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1079](https://github.com/stakira/OpenUtau/pull/1079) - Move save status(*) to the top of window title - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1052](https://github.com/stakira/OpenUtau/pull/1052) - Add phonemizer expression - ([@maiko3tattun](https://github.com/maiko3tattun))

***
# ~[0.1.397 Beta](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.397) (02-25-2024)
## Features
- [#1047](https://github.com/stakira/OpenUtau/pull/1047) - Add a singer publish tool to pack a singer into a zip file - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1037](https://github.com/stakira/OpenUtau/pull/1037) - Add toggle for defaulting to pen plus too - ([@Astel123457](https://github.com/Astel123457))
- [#1045](https://github.com/stakira/OpenUtau/pull/1045) - [DiffSinger] Add support for tension and voicing - ([@yqzhishen](https://github.com/yqzhishen))
## Bug Fixes
- [#1042](https://github.com/stakira/OpenUtau/pull/1042) - Fix keyboard input: fix focus onMenuClose and fix some key bindings - ([@liuycsd](https://github.com/liuycsd))
- [#1046](https://github.com/stakira/OpenUtau/pull/1046) - Fix NoteProperiesPanel bug - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1041](https://github.com/stakira/OpenUtau/pull/1041) - Open voicebank icon file read-only - ([@liuycsd](https://github.com/liuycsd))
- [#1050](https://github.com/stakira/OpenUtau/pull/1050) - Small bug fix for last VCCV merge - ([@AnAndroNerd](https://github.com/AnAndroNerd))
## Phonemizer Changes
- [#1034](https://github.com/stakira/OpenUtau/pull/1034) - Support "- C" in JA VCV&CVVC Phonemizer - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1035](https://github.com/stakira/OpenUtau/pull/1035) - DiffSinger phonemizers: Return error if lyric isn't found in the dictionary - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1029](https://github.com/stakira/OpenUtau/pull/1029) - Eng VCCV Updates and Fixes - ([@AnAndroNerd](https://github.com/AnAndroNerd))
## Translation
- [#1049](https://github.com/stakira/OpenUtau/pull/1049) - Update Japanese translations - ([@maiko3tattun](https://github.com/maiko3tattun))
## Misc
- [#1048](https://github.com/stakira/OpenUtau/pull/1048) - Add "no value" to expression - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1044](https://github.com/stakira/OpenUtau/pull/1044) - Clear solo flag on copied tracks - ([@liuycsd](https://github.com/liuycsd))

***
# ~[0.1.384 Beta](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.384) (02-06-2024)
## Features
- [#1025](https://github.com/stakira/OpenUtau/pull/1025) - Add batch edit "Add breath" - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1018](https://github.com/stakira/OpenUtau/pull/1018) - Add a button to change the tempo of the project without changing the positions of each note (in seconds) - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1030](https://github.com/stakira/OpenUtau/pull/1030) - diffsinger renderer: stricter vocoder-acoustic compatibility check - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
## Bug Fixes
- [#1033](https://github.com/stakira/OpenUtau/pull/1033) - Fix the string duplicate issue - ([@Astel123457](https://github.com/Astel123457))
- [#1032](https://github.com/stakira/OpenUtau/pull/1032) - fix not loading vogen voicebanks if "load all depth folders" is turned off - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1008](https://github.com/stakira/OpenUtau/pull/1008) - Add case check on case-insensitive systems in voicebank check - ([@sdercolin](https://github.com/sdercolin))
## Phonemizer Changes
- [#1027](https://github.com/stakira/OpenUtau/pull/1027) - Create DiffSingerGermanPhonemizer.cs - ([@nobodyP](https://github.com/nobodyP))
- [#1031](https://github.com/stakira/OpenUtau/pull/1031) - ZH CVVC: v_R shouldn't be too long for long notes, refactor ZH-YUE CVVC to be derived from ZH CVVC to reduce repeat code - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
## Misc
- [#1017](https://github.com/stakira/OpenUtau/pull/1017) - Add track expression logic - ([@maiko3tattun](https://github.com/maiko3tattun))

***
# ~[0.1.374 Beta](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.374) (02-02-2024)
## Features
- [#1011](https://github.com/stakira/OpenUtau/pull/1011) - Add singer favorite function - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#1021](https://github.com/stakira/OpenUtau/pull/1021) - Show the current selection when setting encoding, singer type and default phonemizer - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
## Bug Fixes
- [#1026](https://github.com/stakira/OpenUtau/pull/1026) - Fix ReleaseSingersNotInUse bug - ([@maiko3tattun](https://github.com/maiko3tattun))
## Phonemizer Changes
- [#1006](https://github.com/stakira/OpenUtau/pull/1006) - DiffSinger: support different dictionaries for Chinese, Japanese and Cantonese - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1022](https://github.com/stakira/OpenUtau/pull/1022) - diffsinger phonemizers: support glide phonemes - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
## Misc
- [#1007](https://github.com/stakira/OpenUtau/pull/1007) - language name localization - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1024](https://github.com/stakira/OpenUtau/pull/1024) - Save recent open singer/project directory - ([@maiko3tattun](https://github.com/maiko3tattun))

***
# ~[0.1.367 Beta](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.367) (01-25-2024)
## Features
- [#1012](https://github.com/stakira/OpenUtau/pull/1012) - Add option to load only top directories of singers - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#996](https://github.com/stakira/OpenUtau/pull/996) - Add an option to import tempo when importing tracks - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
## Bug Fixes
- [#1009](https://github.com/stakira/OpenUtau/pull/1009) - Fix file system path handling by adding surrounding "" - ([@sdercolin](https://github.com/sdercolin))
- [#1002](https://github.com/stakira/OpenUtau/pull/1002) - Diffsinger: fix unable to load sample and portrait height from character.yaml - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1003](https://github.com/stakira/OpenUtau/pull/1003) - Enable IME input on X11 platforms such as Linux - ([@porime42](https://github.com/porime42))
- [#976](https://github.com/stakira/OpenUtau/pull/976) - Fix singer window goes behind the main window - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#985](https://github.com/stakira/OpenUtau/pull/985) - Fix openutau crash when opening a ustx project whose first time signature isn't at 0 - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#966](https://github.com/stakira/OpenUtau/pull/966) - Fix #Charaset - ([@maiko3tattun](https://github.com/maiko3tattun))
## Phonemizer Changes
- [#1014](https://github.com/stakira/OpenUtau/pull/1014) - Add Spanish and Italian Phonemizers for DiffSinger - ([@spicytigermeat](https://github.com/spicytigermeat))
- [#1019](https://github.com/stakira/OpenUtau/pull/1019) - Diffsinger Rhythmizer phonemizer: Support hanzi input - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#1001](https://github.com/stakira/OpenUtau/pull/1001) - [ES SYL] Phonemizer refactor + custom dictionary support - ([@lottev1991](https://github.com/lottev1991))
- [#1000](https://github.com/stakira/OpenUtau/pull/1000) - G2p: add IsGlide method; EN ARPA: support glide phonemes. - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#995](https://github.com/stakira/OpenUtau/pull/995) - [EN X-SAMPA] Distinguish between current word CC and previous word CC - ([@lottev1991](https://github.com/lottev1991))
- [#994](https://github.com/stakira/OpenUtau/pull/994) - Add ENUNUKoreanPhonemizer - ([@EX3exp](https://github.com/EX3exp))
- [#993](https://github.com/stakira/OpenUtau/pull/993) - Add DiffSingerKoreanPhonemizer - ([@EX3exp](https://github.com/EX3exp))
- [#992](https://github.com/stakira/OpenUtau/pull/992) - Add KoreanCVPhonemizer - ([@EX3exp](https://github.com/EX3exp))
- [#991](https://github.com/stakira/OpenUtau/pull/991) - Improve KoreanCBNNPhonemizer - ([@EX3exp](https://github.com/EX3exp))
- [#990](https://github.com/stakira/OpenUtau/pull/990) - Add BaseKoreanPhonemizer - ([@EX3exp](https://github.com/EX3exp))
- [#989](https://github.com/stakira/OpenUtau/pull/989) - Add KoreanPhonemizerUtil - ([@EX3exp](https://github.com/EX3exp))
- [#984](https://github.com/stakira/OpenUtau/pull/984) - Move DIFFS ZH-YUE and VOGEN ZH-YUE to ZH-YUE category - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
## Translation
- [#982](https://github.com/stakira/OpenUtau/pull/982) - Improve Korean Translation, Add missing translation - ([@ppapman1](https://github.com/ppapman1))
## Misc
- [#983](https://github.com/stakira/OpenUtau/pull/983) - DiffSinger: Free memory for singers no longer in use - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#986](https://github.com/stakira/OpenUtau/pull/986) - Add a github action to run unit tests for each PR - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))

***
# ~[0.1.338 Beta](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.338) (12-16-2023)
## Features
- [#981](https://github.com/stakira/OpenUtau/pull/981) - Support using worldline resampler together with external wavtool - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#980](https://github.com/stakira/OpenUtau/pull/980) - Add an option to disable showing singer icons on piano roll - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#979](https://github.com/stakira/OpenUtau/pull/979) - When opening phonetic assistant, use the g2p used last time - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
## Bug Fixes
- [#977](https://github.com/stakira/OpenUtau/pull/977) - fix error when opening singer view if the singer used in the ustx doesn't exist - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
## Phonemizer Changes
- [#961](https://github.com/stakira/OpenUtau/pull/961) - Add Cantonese CVVC Phonemizer - ([@lottev1991](https://github.com/lottev1991))
- [#959](https://github.com/stakira/OpenUtau/pull/959) - Add Cantonese "Syo-style" Phonemizer - ([@lottev1991](https://github.com/lottev1991))
- [#973](https://github.com/stakira/OpenUtau/pull/973) - [ZH CVVC] Automatically add syllable ending if present (if next neighbor is null) - ([@lottev1991](https://github.com/lottev1991))
- [#975](https://github.com/stakira/OpenUtau/pull/975) - [Japanese Presamp Phonemizer] Add option for MUSTVC - ([@lottev1991](https://github.com/lottev1991))
## Misc
- [#978](https://github.com/stakira/OpenUtau/pull/978) - Refactor affix assignment as protected virtual method - ([@The-UTAU-Black-Supermarket](https://github.com/The-UTAU-Black-Supermarket))

***
# ~[0.1.327](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.327) (12-02-2023)
There are too many changes to keep track of!
### December
- [#963](https://github.com/stakira/OpenUtau/pull/963) - Check file name case on windows - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#962](https://github.com/stakira/OpenUtau/pull/962) - Fix default font family name on linux for CJK locales - ([@SoulMelody](https://github.com/SoulMelody))
- [#948](https://github.com/stakira/OpenUtau/pull/948) - Fix creation of empty Oto from blank line in otoini - ([@maiko3tattun](https://github.com/maiko3tattun))

### November
- [#922](https://github.com/stakira/OpenUtau/pull/922) - Use filename as alias - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#956](https://github.com/stakira/OpenUtau/pull/956) - Add a "Install Dependency (.oudep)" item in Tools menu - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#946](https://github.com/stakira/OpenUtau/pull/946) - Fix exception catching in audio transcribe - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#950](https://github.com/stakira/OpenUtau/pull/950) - Add zh cvvc phonemizer test - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#953](https://github.com/stakira/OpenUtau/pull/953) - Fix diffsinger phoneme misplace if lyric contains space; separate diffsinger Chinese phonemizer - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#955](https://github.com/stakira/OpenUtau/pull/955) - Change export menu order - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#945](https://github.com/stakira/OpenUtau/pull/945) - DiffSinger: Verify input names before running inference sessions - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#951](https://github.com/stakira/OpenUtau/pull/951) - Update Strings.ru-RU.axaml - ([@KagamineP](https://github.com/KagamineP))
- [#957](https://github.com/stakira/OpenUtau/pull/957) - Show a dialog when dropping file if the file format is unsupported, Support ".midi" as an equivalent of ".mid" on dragging and dropping. - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#954](https://github.com/stakira/OpenUtau/pull/954) - Improved stability of preferences - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#947](https://github.com/stakira/OpenUtau/pull/947) - Make the URL in message box look like hyperlink - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#949](https://github.com/stakira/OpenUtau/pull/949) - Improved stability of exporting error report - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#952](https://github.com/stakira/OpenUtau/pull/952) - Improved stability of rendering - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#942](https://github.com/stakira/OpenUtau/pull/942) - Add support for a custom vocoder for DiffSinger singer - ([@spicytigermeat](https://github.com/spicytigermeat))
- [#911](https://github.com/stakira/OpenUtau/pull/911) - Audio transcription with SOME - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#940](https://github.com/stakira/OpenUtau/pull/940) - Update simplified chinese localization - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#939](https://github.com/stakira/OpenUtau/pull/939) - [SyllableBasedPhonemizer API] Make alias extension restriction to same subbank optional - ([@lottev1991](https://github.com/lottev1991))
- [#937](https://github.com/stakira/OpenUtau/pull/937) - Fix openutau crashing when double clicking on the oto table of ENUNU and DiffSinger voicebanks - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#936](https://github.com/stakira/OpenUtau/pull/936) - Lyric edit and general lyric replacement: apply to the whole part if no note is selected - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#935](https://github.com/stakira/OpenUtau/pull/935) - Fix ENUNU phonemizer broken after BPM editing. - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#933](https://github.com/stakira/OpenUtau/pull/933) - Add Korean-to-Japanese Phonemizer - ([@lottev1991](https://github.com/lottev1991))
- [#932](https://github.com/stakira/OpenUtau/pull/932) - [DE VCCV Phonemizer] Add missing vowel sound + consonant length adjustment - ([@lottev1991](https://github.com/lottev1991))
- [#929](https://github.com/stakira/OpenUtau/pull/929) - Set SingerType in SingersWindow - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#927](https://github.com/stakira/OpenUtau/pull/927) - Fix Korean translation - ([@EX3exp](https://github.com/EX3exp))
- [#912](https://github.com/stakira/OpenUtau/pull/912) - Add "View" menu in PianoRollWindow - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#897](https://github.com/stakira/OpenUtau/pull/897) - add mandarin/cantonese g2p - ([@wolfgitpr](https://github.com/wolfgitpr))
- [#858](https://github.com/stakira/OpenUtau/pull/858) - Fix voicebank error check - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#892](https://github.com/stakira/OpenUtau/pull/892) - Show loading dialog / Set try-catch - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#887](https://github.com/stakira/OpenUtau/pull/887) - Check wav file writeable when exporting - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#906](https://github.com/stakira/OpenUtau/pull/906) - Fix TextBox font - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#926](https://github.com/stakira/OpenUtau/pull/926) - [ZH CVVC Phonemizer] Fix CV handling: Starting CV fix + separate CV and VC voice color + Add VEL length calculation for VC - ([@lottev1991](https://github.com/lottev1991))
- [#925](https://github.com/stakira/OpenUtau/pull/925) - [EN X-SAMPA Phonemizer] Adjustment to recent SBP subbank refactor - ([@lottev1991](https://github.com/lottev1991))
- [#941](https://github.com/stakira/OpenUtau/pull/941) - Faster startup - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#917](https://github.com/stakira/OpenUtau/pull/917) - Fix OpenUtau freezing when using classic plugins if there are overlapping notes - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#916](https://github.com/stakira/OpenUtau/pull/916) - Editing macro: fix overlapping notes - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#915](https://github.com/stakira/OpenUtau/pull/915) - Update Strings.ru-RU.axaml - ([@KagamineP](https://github.com/KagamineP))
- [#913](https://github.com/stakira/OpenUtau/pull/913) - Add hover tooltips for mute/solo toggle button and track settings button - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#903](https://github.com/stakira/OpenUtau/pull/903) - Update ID Translation (by pyorririn) - ([@Astel123457](https://github.com/Astel123457))
- [#909](https://github.com/stakira/OpenUtau/pull/909) - Fix rendering track No. - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#907](https://github.com/stakira/OpenUtau/pull/907) - Fix note property panel - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#905](https://github.com/stakira/OpenUtau/pull/905) - Fix underlines are not displayed in Button - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#904](https://github.com/stakira/OpenUtau/pull/904) - Don't show save dialog for new project - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#902](https://github.com/stakira/OpenUtau/pull/902) - Copy error to clipboard - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#901](https://github.com/stakira/OpenUtau/pull/901) - Update Japanese translation, English appearance - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#900](https://github.com/stakira/OpenUtau/pull/900) - Support resizing notes from their heads - ([@yqzhishen](https://github.com/yqzhishen))
- [#899](https://github.com/stakira/OpenUtau/pull/899) - [ZH CVVC] Make VC use pitch of previous note - ([@lottev1991](https://github.com/lottev1991))
- [#898](https://github.com/stakira/OpenUtau/pull/898) - [KO VCV Phonemizer] Voice color fix + alternate support + extend end breath support - ([@lottev1991](https://github.com/lottev1991))
- [#896](https://github.com/stakira/OpenUtau/pull/896) - Better testing for phoneme attributes in multi-phoneme notes - ([@The-UTAU-Black-Supermarket](https://github.com/The-UTAU-Black-Supermarket))

### October
- [#874](https://github.com/stakira/OpenUtau/pull/874) - Scale degree display - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#893](https://github.com/stakira/OpenUtau/pull/893) - singer name localization - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#894](https://github.com/stakira/OpenUtau/pull/894) - [DiffSinger] Fix invalid tensor in memory when errors occur during *.emb loading - ([@yqzhishen](https://github.com/yqzhishen))
- [#895](https://github.com/stakira/OpenUtau/pull/895) - [DiffSinger] Fix note pitch masked unexpectedly when applying nearest interpolation - ([@yqzhishen](https://github.com/yqzhishen))
- [#890](https://github.com/stakira/OpenUtau/pull/890) - [English X-SAMPA Phonemizer] ValidateAlias() bug fix/refinement + some vowel fixes/refinements - ([@lottev1991](https://github.com/lottev1991))
- [#888](https://github.com/stakira/OpenUtau/pull/888) - Display track No. currently rendering - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#886](https://github.com/stakira/OpenUtau/pull/886) - ctrl-click to add note into selection without deselecting the other notes - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#867](https://github.com/stakira/OpenUtau/pull/867) - Fix parse pitchbend from plugins - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#878](https://github.com/stakira/OpenUtau/pull/878) - improve classic pitch algorithm - ([@lennyservant](https://github.com/lennyservant))
- [#882](https://github.com/stakira/OpenUtau/pull/882) - Add DiffSinger Support - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#881](https://github.com/stakira/OpenUtau/pull/881) - fix note bend entanglement when changing portamento in note properties - ([@lennyservant](https://github.com/lennyservant))
- [#879](https://github.com/stakira/OpenUtau/pull/879) - fix unable to load portraits shorter than 800px - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#876](https://github.com/stakira/OpenUtau/pull/876) - Show location for vogen voicebank - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#877](https://github.com/stakira/OpenUtau/pull/877) - fixed:classic pitch when changing tempo - ([@delta-kimigatame](https://github.com/delta-kimigatame))
- [#875](https://github.com/stakira/OpenUtau/pull/875) - Fix import/export prefixmap - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#872](https://github.com/stakira/OpenUtau/pull/872) - Fix openutau crashing when the sample isn't a valid audio file - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#871](https://github.com/stakira/OpenUtau/pull/871) - fix piano roll keyboard shortcuts blocking text box input - ([@lennyservant](https://github.com/lennyservant))
- [#870](https://github.com/stakira/OpenUtau/pull/870) - Editing macro: Reset phoneme aliases - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#868](https://github.com/stakira/OpenUtau/pull/868) - Fix paste param dialog bug - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#861](https://github.com/stakira/OpenUtau/pull/861) - Add import / export prefix.map - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#860](https://github.com/stakira/OpenUtau/pull/860) - [vLabeler integration] Use existing lbp file before creating a new one - ([@sdercolin](https://github.com/sdercolin))
- [#863](https://github.com/stakira/OpenUtau/pull/863) - fix openutau crash when trying to play sample for enunu or vogen singer - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#865](https://github.com/stakira/OpenUtau/pull/865) - Fix singer dialog - ([@rokujyushi](https://github.com/rokujyushi))
- [#862](https://github.com/stakira/OpenUtau/pull/862) - Fixed classic pitch - ([@delta-kimigatame](https://github.com/delta-kimigatame))
- [#852](https://github.com/stakira/OpenUtau/pull/852) - [Singers window] Add button to show readme.txt - ([@lottev1991](https://github.com/lottev1991))
- [#859](https://github.com/stakira/OpenUtau/pull/859) - Update Strings.it-IT.axaml - ([@IDOLTRASH](https://github.com/IDOLTRASH))
- [#840](https://github.com/stakira/OpenUtau/pull/840) - Refactor search dialog to a searchbar like in browsers and text editors - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#849](https://github.com/stakira/OpenUtau/pull/849) - Update Strings.ru-RU.axaml - ([@KagamineP](https://github.com/KagamineP))
- [#851](https://github.com/stakira/OpenUtau/pull/851) - Update simplified Chinese localization - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#853](https://github.com/stakira/OpenUtau/pull/853) - [Singer window] Play sample on click + [Wave.cs] Support reading AIFF format - ([@lottev1991](https://github.com/lottev1991))
- [#854](https://github.com/stakira/OpenUtau/pull/854) - Add github codespace support - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#855](https://github.com/stakira/OpenUtau/pull/855) - Linking vibrato and volume - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#856](https://github.com/stakira/OpenUtau/pull/856) - editing macro: Insert slur lyric - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#857](https://github.com/stakira/OpenUtau/pull/857) - [Portrait height] Set default int to 0 (no default height if below 800px) - ([@lottev1991](https://github.com/lottev1991))

### September
- [#847](https://github.com/stakira/OpenUtau/pull/847) - Allow to change keyboard color in PianoRoll Window - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#846](https://github.com/stakira/OpenUtau/pull/846) - Reflect track color in ghost notes - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#844](https://github.com/stakira/OpenUtau/pull/844) - Fix Note Properties and Add vibrato drift (RERE) - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#848](https://github.com/stakira/OpenUtau/pull/848) - [character.yaml] Option to set portrait height (width will be relative) - ([@lottev1991](https://github.com/lottev1991))
- [#839](https://github.com/stakira/OpenUtau/pull/839) - Fix unable to install vb from Mac on Windows - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#841](https://github.com/stakira/OpenUtau/pull/841) - Check voice color when edit subbanks - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#842](https://github.com/stakira/OpenUtau/pull/842) - Sort language groups of phonemizers alphabetically - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#843](https://github.com/stakira/OpenUtau/pull/843) - Refactor phonemizer test utility method - ([@The-UTAU-Black-Supermarket](https://github.com/The-UTAU-Black-Supermarket))
- [#830](https://github.com/stakira/OpenUtau/pull/830) - Fix pitch paste bug - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#832](https://github.com/stakira/OpenUtau/pull/832) - [PinyinLyricsHelper] Convert pinyin to lower variant in PinyinLyricsHelper - ([@lottev1991](https://github.com/lottev1991))
- [#834](https://github.com/stakira/OpenUtau/pull/834) - Check and Remapping voice color - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#835](https://github.com/stakira/OpenUtau/pull/835) - Small bug fixes - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#836](https://github.com/stakira/OpenUtau/pull/836) - Update avalonia to 11.0.4 - ([@lilyinstarlight/upd](https://github.com/lilyinstarlight/upd))
- [#838](https://github.com/stakira/OpenUtau/pull/838) - Correction of structure names, etc. - ([@rokujyushi](https://github.com/rokujyushi))
- [#829](https://github.com/stakira/OpenUtau/pull/829) - Alias search is now available at ENUNU. - ([@rokujyushi](https://github.com/rokujyushi))
- [#825](https://github.com/stakira/OpenUtau/pull/825) - Fix unable to save oto when the voicebank contains wavs that haven't been oto'd - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#827](https://github.com/stakira/OpenUtau/pull/827) - [JA Presamp Phonemizer] Supports "っ", etc - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#817](https://github.com/stakira/OpenUtau/pull/817) - Update Japanese translations - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#821](https://github.com/stakira/OpenUtau/pull/821) - Make it easier to extend the tail of a project - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#826](https://github.com/stakira/OpenUtau/pull/826) - Set icon for singers - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#820](https://github.com/stakira/OpenUtau/pull/820) - Add legacy plugins shortcuts - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#819](https://github.com/stakira/OpenUtau/pull/819) - Add option to change default renderer (for classic voicebanks) - ([@lottev1991](https://github.com/lottev1991))
- [#818](https://github.com/stakira/OpenUtau/pull/818) - Add option to automatically clear cache on quit - ([@lottev1991](https://github.com/lottev1991))
- [#816](https://github.com/stakira/OpenUtau/pull/816) - Add Search Note - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#815](https://github.com/stakira/OpenUtau/pull/815) - Add "Select and paste parameters" and related methods - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#811](https://github.com/stakira/OpenUtau/pull/811) - [German VCCV Phonemizer] VCC refactor + CC refactor + ValidateAlias() fix + split diphthong fix - ([@lottev1991](https://github.com/lottev1991))
- [#810](https://github.com/stakira/OpenUtau/pull/810) - Add Lengthen crossfades in batch menu - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#804](https://github.com/stakira/OpenUtau/pull/804) - Save displayed expressions in Ustx - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#807](https://github.com/stakira/OpenUtau/pull/807) - [BREAKING] Rename "ENDeltaPhonemizer" to "EnXSampaPhonemizer" + some fixes - ([@lottev1991](https://github.com/lottev1991))
- [#808](https://github.com/stakira/OpenUtau/pull/808) - Merge Notes - ([@hilmiyafia](https://github.com/hilmiyafia))
- [#806](https://github.com/stakira/OpenUtau/pull/806) - [JA CVVC & Presamp] Semi-fix for voice color fallbacks - ([@lottev1991](https://github.com/lottev1991))

### August
- [#797](https://github.com/stakira/OpenUtau/pull/797) - [EN Delta] Refactoring code + fix ValidateAlias bugs + restore proper VCC connections + fix single consonants - ([@lottev1991](https://github.com/lottev1991))
- [#799](https://github.com/stakira/OpenUtau/pull/799) - Auto Legato Removes Rests and Overlaps - ([@hilmiyafia](https://github.com/hilmiyafia))
- [#778](https://github.com/stakira/OpenUtau/pull/778) - Fix voice color resetting - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#798](https://github.com/stakira/OpenUtau/pull/798) - Reworded missing info message - ([@The-UTAU-Black-Supermarket](https://github.com/The-UTAU-Black-Supermarket))
- [#801](https://github.com/stakira/OpenUtau/pull/801) - Tweaked piano roll menus - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#802](https://github.com/stakira/OpenUtau/pull/802) - ZH CVV: _uai should fall back to _ai - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#803](https://github.com/stakira/OpenUtau/pull/803) - Add German UI language - ([@schustobias](https://github.com/schustobias))

### July
- [#793](https://github.com/stakira/OpenUtau/pull/793) - Fix the scale of icon in pianoroll window - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#794](https://github.com/stakira/OpenUtau/pull/794) - [ES to JA Phonemizer] Consonant bug fixes - ([@lottev1991](https://github.com/lottev1991))
- [#795](https://github.com/stakira/OpenUtau/pull/795) - [Phonetic Assistant] Add German Lyrics Helper + missing Spanish view model option - ([@lottev1991](https://github.com/lottev1991))
- [#773](https://github.com/stakira/OpenUtau/pull/773) - [EN DELTA] Starting CC + ValidateAlias refinement - ([@lottev1991](https://github.com/lottev1991))
- [#776](https://github.com/stakira/OpenUtau/pull/776) - ZH CVV: custom dictionary support - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#779](https://github.com/stakira/OpenUtau/pull/779) - Fix a bug when creating a new project - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#780](https://github.com/stakira/OpenUtau/pull/780) - Ignore SearchTerms exception when loading singers - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#781](https://github.com/stakira/OpenUtau/pull/781) - fix unable to import midi in "import tracks" - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#782](https://github.com/stakira/OpenUtau/pull/782) - add an editing macro to remove tail "R" or tail "-" - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#785](https://github.com/stakira/OpenUtau/pull/785) - Add Japanese contracted sound processing to EditLyrics - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#783](https://github.com/stakira/OpenUtau/pull/783) - EN to JA test suite and fixes - ([@The-UTAU-Black-Supermarket](https://github.com/The-UTAU-Black-Supermarket))
- [#787](https://github.com/stakira/OpenUtau/pull/787) - Show a dialog when editing macros throw an error - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#789](https://github.com/stakira/OpenUtau/pull/789) - [German for OU] Add German G2P, phonemizers, tests, custom dicts - ([@lottev1991](https://github.com/lottev1991))
- [#790](https://github.com/stakira/OpenUtau/pull/790) - Support ufdata import - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#772](https://github.com/stakira/OpenUtau/pull/772) - For fine control of volume and panning. - ([@rokujyushi](https://github.com/rokujyushi))
- [#768](https://github.com/stakira/OpenUtau/pull/768) - Fix unable to use classic plugins when using machine learning renderers - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#765](https://github.com/stakira/OpenUtau/pull/765) - Add Track color - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#767](https://github.com/stakira/OpenUtau/pull/767) - EN ARPA and ENUNU EN: support extending syllables with +~ or +* - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#766](https://github.com/stakira/OpenUtau/pull/766) - [JA CVVC & JA Presamp] Add "m" consonant fallback - ([@lottev1991](https://github.com/lottev1991))
- [#762](https://github.com/stakira/OpenUtau/pull/762) - Fix solo and mute - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#763](https://github.com/stakira/OpenUtau/pull/763) - Fix Preferences dialog - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#761](https://github.com/stakira/OpenUtau/pull/761) - Fix wordline-R stop on pitch snaps - ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#751](https://github.com/stakira/OpenUtau/pull/751) - [WIP] Add Note Params panel - ([@maiko3tattun](https://github.com/maiko3tattun))

***
# [0.1.158](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.158)~[0.1.157b](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.157) (06-19-2023)

## Major Changes
- [d60f403](https://github.com/stakira/OpenUtau/commit/d60f403) - Upgrade to avalonia 11 ([@stakira](https://github.com/stakira))
    - Version upgrade + series of fixes to breaking changes. See `Misc` for further relevant commits.
    - Keep an eye out for bugs!
- [08d7693](https://github.com/stakira/OpenUtau/commit/08d7693) - Installer version available (nsis installer) ([@stakira](https://github.com/stakira))
- [#738](https://github.com/stakira/OpenUtau/pull/738) - Solo and Mute Improvements - ([@maiko3tattun](https://github.com/maiko3tattun))
- [#746](https://github.com/stakira/OpenUtau/pull/746) - Add a dialog when installing .dll phonemizers ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
    - Added a dialog when installing .dll phonemizers because hackers can disguise .dll as .ustx
![Screenshot of dialogue reading "Installing phonemizer"](https://i.imgur.com/KDNq1jd.png)

## Bug Fixes
- [b020209](https://github.com/stakira/OpenUtau/commit/b020209) - fix UST tempo parsing ([@stakira](https://github.com/stakira))
- [ee91432](https://github.com/stakira/OpenUtau/commit/ee91432) - Fix nullness in release configuration ([@stakira](https://github.com/stakira))
- [78fc333](https://github.com/stakira/OpenUtau/commit/78fc333) - Fix tab key for lyric box ([@stakira](https://github.com/stakira))
- [91bc579](https://github.com/stakira/OpenUtau/commit/91bc579) - Fix Mac build ([@stakira](https://github.com/stakira))
- [5a47b79](https://github.com/stakira/OpenUtau/commit/5a47b79) + [bf0c8be](https://github.com/stakira/OpenUtau/commit/bf0c8be) + [22a674f](https://github.com/stakira/OpenUtau/commit/22a674f) - UI fixes 
- [8c92eb3](https://github.com/stakira/OpenUtau/commit/8c92eb3) - fix crash scrolling slightly beyond bottom note ([@stakira](https://github.com/stakira))

## Phonemizer Changes
- [#736](https://github.com/stakira/OpenUtau/pull/736) - `VOGEN` Fix consonant timing ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#731](https://github.com/stakira/OpenUtau/pull/731) - `ES SYL` Starting CCV + VV transition fix ([@lottev1991](https://github.com/lottev1991))
- [#732](https://github.com/stakira/OpenUtau/pull/732) - `ES VCCV` Code and function optimization ([@lottev1991](https://github.com/lottev1991))
- [#734](https://github.com/stakira/OpenUtau/pull/734) - `JA CVVC` Read CV append voice color ([@lottev1991](https://github.com/lottev1991))
- [#737](https://github.com/stakira/OpenUtau/pull/737) - `VIE VCV` Phonemizer Update ([@lottev1991](https://github.com/lottev1991))
- [#743](https://github.com/stakira/OpenUtau/pull/743) - `KO CVC` Fix tense consonant VC + add batchim end breath support ([@lottev1991](https://github.com/lottev1991))
- [#745](https://github.com/stakira/OpenUtau/pull/745) - `FR VCCV` Starting - CC and ending CC - behaviour fix ([@mmemim](https://github.com/mmemim))

## Translations
- [#747](https://github.com/stakira/OpenUtau/pull/747) - fix translations ([@maiko3tattun](https://github.com/maiko3tattun))

## Misc
- [704b54c](https://github.com/stakira/OpenUtau/commit/704b54c) - Clean up views ([@stakira](https://github.com/stakira))
- [723109f](https://github.com/stakira/OpenUtau/commit/723109f) - Fix pianoroll interactions ([@stakira](https://github.com/stakira))
- [1e1a052](https://github.com/stakira/OpenUtau/commit/1e1a052) - Rewrite oto view ([@stakira](https://github.com/stakira))
- [d33a440](https://github.com/stakira/OpenUtau/commit/d33a440) - Better waveform drawing  ([@stakira](https://github.com/stakira))
([@stakira](https://github.com/stakira))
- [839ac40](https://github.com/stakira/OpenUtau/commit/839ac40) - Fix dropping file  ([@stakira](https://github.com/stakira))
- [8227dee](https://github.com/stakira/OpenUtau/commit/8227dee) - Update packages, refactor file picker and nullness ([@stakira](https://github.com/stakira))
- [a52c64d](https://github.com/stakira/OpenUtau/commit/a52c64d) - Add select singer type step to install ([@stakira](https://github.com/stakira))
- [a227d56](https://github.com/stakira/OpenUtau/commit/a227d56) - tweak singer setup view ([@stakira](https://github.com/stakira))
- [#748](https://github.com/stakira/OpenUtau/pull/748) + [#747](https://github.com/stakira/OpenUtau/pull/747) - Changed the behavior of DrawPitchTool (RE) ([@maiko3tattun](https://github.com/maiko3tattun))
- [#742](https://github.com/stakira/OpenUtau/pull/742) - Display ENUNU phonemes in the SingersList ([@rokujyushi](https://github.com/rokujyushi))
    - Allows ENUNU phoneme information (from .hed files) to be seen in the singer window. This works even without a dummy voicebank (wav + oto.ini) packaged with the model.
- [#633](https://github.com/stakira/OpenUtau/pull/633) - Update README ([@CarpetBook](https://github.com/CarpetBook))

***

# ~[0.1.119](https://github.com/stakira/OpenUtau/releases/tag/build%2F0.1.119) (05-28-2023)

## Features
- [#691](https://github.com/stakira/OpenUtau/pull/691) - Singer Window Improvements, etc ([@maiko3tattun](https://github.com/maiko3tattun))
    - General improvements to the singer window have been made! Primary additions are alias search, as well as pre-selecting the singer based on active part. <br>
    ![example of alias search function](https://imgur.com/1rTdCKL.gif)
- [#711](https://github.com/stakira/OpenUtau/pull/711) - General Lyrics Replacement tool ([@maiko3tattun](https://github.com/maiko3tattun))
    - This new macro uses regular expressions to convert lyrics. It is highly scalable and simplifies replacement of any language. Adding and sharing new presets is encouraged!
    <br>![example animation of 'General lyrics replacement' in action](https://imgur.com/BFib5mt.gif)
- [#712](https://github.com/stakira/OpenUtau/pull/712) - Drag and drop to install .dll phonemizers, .exe resamplers and wavtools ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
    - Externally provided phonemizers, resamplers and wavtools should no longer require manual folder management. Just drag and drop to install! 
    ```Diff
    OS-specific feedback required: Mac and Linux
    ```
    ![example of .exe install via drag and drop](https://user-images.githubusercontent.com/54425948/239664701-1fffee4f-3626-43ab-b4db-d7c7b3b32f47.png)
- [#713](https://github.com/stakira/OpenUtau/pull/713) - Add support for Classic Ust Flags ([@arkfinn](https://github.com/arkfinn))
    - [94b00a5](https://github.com/stakira/OpenUtau/commit/94b00a5) fixes some issues with the original implementation.

## Bug Fixes

- [#708](https://github.com/stakira/OpenUtau/pull/708) - `Pitch Baking` Fix PITD erasing region misplaced, process the whole part by default ([@oxygen-dioxide](https://github.com/oxygen-dioxide))

## Phonemizer Changes
- [#693](https://github.com/stakira/OpenUtau/pull/693) - `ES VCCV` VCC/CC fix + ValidateAlias for "E" semivowel ([@lottev1991](https://github.com/lottev1991))
- [#707](https://github.com/stakira/OpenUtau/pull/707) - `ZH CVV` Use new mapping style + voice color support + "yan" vowel fix + "_un" ending alternative
- [#709](https://github.com/stakira/OpenUtau/pull/709) - `KO CVC` "ch" VC fix (romaja/mixed VC) ([@lottev1991](https://github.com/lottev1991))
- [#710](https://github.com/stakira/OpenUtau/pull/710) - `Various JA phoemizers` PhoneticHint support and Unicode countermeasures ([@maiko3tattun](https://github.com/maiko3tattun))
- [#716](https://github.com/stakira/OpenUtau/pull/716) - `EN VCCV` phonemizer refactor ([@mmemmim](https://github.com/mmemim) & [@cubialpha](https://github.com/cubialpha))
- [#720](https://github.com/stakira/OpenUtau/pull/720) - `ES VCCV` Add different consonant lengths support ([@lottev1991](https://github.com/lottev1991))

## Misc
- [11fa8cc](https://github.com/stakira/OpenUtau/commit/11fa8cc) - nicer version compare  ([@stakira](https://github.com/stakira))

***

# ~[0.1.96](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.96) (05-21-2023)
```Diff
@@ Major Change @@
```
From this point on, OpenUtau has a [Stable](https://github.com/stakira/OpenUtau/tree/stable) and [Beta](https://github.com/stakira/OpenUtau/tree/master) branch. You may opt into the Beta in-program by going to `Tools`>`Preferences`>`Advanced`, and toggling `Beta` to On. Doing so may open you up to experiencing bugs, so exercise caution!

## Misc
- [dd2d0f2](https://github.com/stakira/OpenUtau/commit/dd2d0f2) - adds stale workflow and increases releases kept ([@stakira](https://github.com/stakira))
- [bd5641c](https://github.com/stakira/OpenUtau/commit/bd5641c) - Setup beta and stable release channels ([@stakira](https://github.com/stakira))
    - [225b97d](https://github.com/stakira/OpenUtau/commit/225b97d) corrects beta releases link, title and description.

***

# ~[0.1.92](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.92) (05-16-2023)

## Misc
- [#af16021](https://github.com/stakira/OpenUtau/commit/af16021) - Refactor locale initialization ([@stakira](https://github.com/stakira))
    - Preventative measures for situations similar to the 0.1.90 bug, general refactoring.
    - This commit also changes the `mid` on the `stereo panning slider` to **`C`** (for Center).
***

# ~[0.1.91](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.91) (05-15-2023)

## Bug Fixes
- [#689](https://github.com/stakira/OpenUtau/pull/689) - fix en-US language saving and loading ([@lennyservant](https://github.com/lennyservant))
    - This should resolve the critical errors (preferences crash, singers not loading) from 0.1.90. Sorry for the inconvenience!
    - If still encountering issues, navigate to the `prefs.json` file in your OpenUtau folder structure, and remove the line `"language": "axaml",` and save.

***
# ~[0.1.90](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.90) (05-15-2023)

> [!CAUTION]
> This build has known bugs!

- Selecting `preferences` currently causes OpenUtau to crash. Fix incoming at [#689](https://github.com/stakira/OpenUtau/pull/689). 

Fix note: If you at any point updated to this version and ran it, and have been experiencing persistent issues even after updating to new versions -- you may need to remove the "languages" line from your prefs.JSON, or simply delete the prefs.JSON wholly (warning: this will reset any customization OpenUtau stores in preferences to the default).

## Features
- [#668](https://github.com/stakira/OpenUtau/pull/668) - Stereo Panning Slider ([@nfrid](https://github.com/nfrid))
    - Stereo panning now available in the `track header`, under the `volume slider`. It works similarly to volume; left click and hold to drag, and right click will set the slider to mid. <br>
    ![example animation of 'Stereo Panning Slider' set to mid](https://user-images.githubusercontent.com/13046595/234082612-b803c922-7328-476c-9ff7-55113ed9fcca.png) <br>
    ![example animation of 'Stereo Panning Slider' set to left](https://user-images.githubusercontent.com/13046595/234082697-c123fdcd-12dd-4f17-8b09-7a24bd954bbc.png) <br>
    ![example animation of 'Stereo Panning Slider' set to right](https://user-images.githubusercontent.com/13046595/234082665-3ef4ec83-6d42-4d59-b025-99a934effca7.png)

- [#676](https://github.com/stakira/OpenUtau/pull/676) - Move Suffix to Voice Color ([@maiko3tattun](https://github.com/maiko3tattun))
    - A macro to remove suffixes from lyrics and move them to the voice color panel if a matching suffix is found in the voice color settings. If not found, the suffix will remain in the lyric.
    ![example animation of 'Move Suffix to Voice Color' in action](https://i.imgur.com/p108qe0.gif)

## Phonemizer Changes
- [#667](https://github.com/stakira/OpenUtau/pull/667) - **Removed Phonemizer: `EN Teto`** ([@adlez27](https://github.com/adlez27))
    - Depreciated. It is recommended to use `EN Delta` Phonemizer when using Kasane Teto's English voicebank. The seperately compiled version of `EN Teto` can be found here if necessary: https://github.com/adlez27/OpenUtau/releases/tag/Teto-0.1.0
- [#681](https://github.com/stakira/OpenUtau/pull/681) - **Merged Phonemizers: `EN Delta V1` and `EN Delta V2`** ([@lottev1991](https://github.com/lottev1991))
    - `EN Delta V1` and `EN Delta V2` are now merged into one Phonemizer: **`EN Delta`**. 
        - Split strings are now handled automatically rather than having to manually select which version you require.
- [#674](https://github.com/stakira/OpenUtau/pull/674) + [#677](https://github.com/stakira/OpenUtau/pull/677)- **Add Spanish and Italian G2P** ([@lottev1991](https://github.com/lottev1991))
    - G2P allows you to write words that may not appear in the dictionary. It will use the data it was trained on to take a guess at the phonemes for the word written, rather than just resulting in a `word not found` error. Support for this has been added to *all* current Spanish Phonemizers, and `IT SYL`!
- [#680](https://github.com/stakira/OpenUtau/pull/680) - `JA VCV & CVVC` Add presamp.ini `VCPAD` support, fix a bug when single pitch voicebank ([@maiko3tattun](https://github.com/maiko3tattun))
- [#675](https://github.com/stakira/OpenUtau/pull/675) - `ES VCCV`  Starting CCV bug fix ([@lottev1991](https://github.com/lottev1991))
- [#684](https://github.com/stakira/OpenUtau/pull/684) - `ES VCCV` Add stop consonant/affricate CC ValidateAlias ([@lottev1991](https://github.com/lottev1991))
- [#688](https://github.com/stakira/OpenUtau/pull/688) - `Vietnamese Phonemizers` Updated to fix Voice Color support ([@janikyou](https://github.com/janikyou))


## Translation
- [#676](https://github.com/stakira/OpenUtau/pull/676) - Add and improve Japanese translations ([@maiko3tattun](https://github.com/maiko3tattun))
- [#679](https://github.com/stakira/OpenUtau/pull/679) - Fix around language ([@maiko3tattun](https://github.com/maiko3tattun))
    - Fixed a bug that caused the language to run in the same language as InstalledUICulture the first time it was launched, but reset to en-US when the preference window was opened

## Misc
- [#4dca53d](https://github.com/stakira/OpenUtau/commit/4dca53d78ddfd9569a01c975e0e961c948ee53bf) - Adds g2p training code ([@stakira](https://github.com/stakira))
- [#669](https://github.com/stakira/OpenUtau/pull/669) - Refactor PluginRunner to OpenUtau.Core and make testable ([@arkfinn](https://github.com/arkfinn))
- [#676](https://github.com/stakira/OpenUtau/pull/676) - Add and fix LyricBatchEdits ([@maiko3tattun](https://github.com/maiko3tattun))
    - _Fix RemoveToneSuffix_
    - _Add ChangeVoiceColorCommand in NoteCommand_
- [#680](https://github.com/stakira/OpenUtau/pull/680) - Add PresampSamplePhonemizer and fixes ([@maiko3tattun](https://github.com/maiko3tattun))
    - _Sample for developers. Not included in release build_
- [#682](https://github.com/stakira/OpenUtau/pull/682) - Defaults to paging instead of scrolling ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
- [#686](https://github.com/stakira/OpenUtau/pull/686) - Flag filter based on resampler manifests ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
    - Support for an `expression-filter` feature in resampler manifests. To quote: 
    > Many resamplers are unable to parse flags correctly when there are moresampler-specific flags, because most resamplers only use single-character flags, but moresampler uses multi-character flags, such as "Mt", "Me", "Mb". To solve this issue, we can pass only the supported flags (specified in resampler manifest) into the resampler."
    - This is one part of a broader feature implementation. See also `Let renderers provide expression suggestions` - [#599](https://github.com/stakira/OpenUtau/pull/599). 

***

# [0.1.57](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.57)~[0.1.73](https://github.com/stakira/OpenUtau/releases/tag/build/0.1.73) (04-23-2023)

**Past release notes:** This is the first! If you need to know about previous releases, please see the github commit history. Efforts will be made to make sure that features up until this point are documented on the wiki. See [Getting Started](https://github.com/stakira/OpenUtau/wiki/Getting-Started).

## Features
- [#661](https://github.com/stakira/OpenUtau/pull/661) - Pitch Baking ([@oxygen-dioxide](https://github.com/oxygen-dioxide))
    - A macro has been added under the `notes` topline menu item in the piano roll: `convert PITD to pitch control points`:
        
        ![example animation of 'convert PITD to pitch control points' in action](https://i.imgur.com/JcbJlRs.gif)
- [#662](https://github.com/stakira/OpenUtau/pull/662) - Support for importing and exporting time signatures in MIDI files ([@liuycsd](https://github.com/liuycsd))


## Bug Fixes
- [#89550fe](https://github.com/stakira/OpenUtau/commit/89550fe94cbdf5e6f808904626154cf5ebf5ce62) - revert macos dylib hack from #6fc7b35 ([@stakira](https://github.com/stakira))
    - **This should address the mac builds from 0.1.53 though 0.1.57 giving a Failed to render error on MacOS.** 
- [#657](https://github.com/stakira/OpenUtau/pull/657) - Fix disappearing notes on plugin execution ([@arkfinn](https://github.com/arkfinn))

## Phonemizer Changes
- [#644](https://github.com/stakira/OpenUtau/pull/644) - `EN Delta V1` VCC ending fix ([@lottev1991](https://github.com/lottev1991))
- [#646](https://github.com/stakira/OpenUtau/pull/646) - `JA CVVC` Add crossfade CV support for non-vowels ([@lottev1991](https://github.com/lottev1991))
- [#655](https://github.com/stakira/OpenUtau/pull/655) - **New Phonemizer: `JA VCV & CVVC`** ([@maiko3tattun](https://github.com/maiko3tattun))
    - `JA VCV & CVVC` allows support of multiple voicebank formats in one phonemiser. It supports CV, VCV and CVVC Japanese voicebanks (including pitches or colors of differing formats within the same hierarchy). With the settings one can adjust within a presamp.ini file, this is a powerful addition to the Phonemizer roster. Please give it a try if it suits your needs. 
        - Introduces a new base class for phonemizers that work with the existing presamp.ini file type.
- [#656](https://github.com/stakira/OpenUtau/pull/656) - Improved loading of Append.maps for multi-prefix maps ([@maiko3tattun](https://github.com/maiko3tattun))
    - Within this PR, full implementation of the presamp.ini parsing for `JA VCV & CVVC` is included. Relevant tests have also been added at [#06c8475](https://github.com/stakira/OpenUtau/pull/656/commits/06c8475fbae109beabe925c7169916e2185406bf).
- [#659](https://github.com/stakira/OpenUtau/pull/659) - Adjustments to Phonemizer and SyllableBasedPhonemizer to allow automated testing ([@adlez27](https://github.com/adlez27))
    - Some example tests have been provided. It is encouraged to write tests for SBP phonemizers both existing and in development. [#666](https://github.com/stakira/OpenUtau/pull/666) - Read dictionary sync when testing is related.
- [#663](https://github.com/stakira/OpenUtau/pull/663), [#664](https://github.com/stakira/OpenUtau/pull/664), [#665](https://github.com/stakira/OpenUtau/pull/665) - `EN Delta V1` Add additional X-SAMPA vowels + misc fixes ([@lottev1991](https://github.com/lottev1991))
    - The dictionary template has also been updated to support these.


## Misc
- [#647](https://github.com/stakira/OpenUtau/pull/647) - Add .vscode folder into gitignore ([@oxygen-dioxide](https://github.com/oxygen-dioxide))

***

>_OpenUtau's version numbers increase per accepted PR request. As such, these changelogs are grouped with the date of acceptance treated as a "release"._