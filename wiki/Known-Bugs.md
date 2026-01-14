# Known bugs
### `WORLDLINE-R`: Audio distortion when changing gender factor curve's default value
If the gender factor default value is set to a negative value, such as -15, the synthesized audio will get heavily distorted. This bug does not occur when the gender factor value is set to 0
![image](https://github.com/stakira/OpenUtau/assets/54425948/356f157a-cc3a-454a-bebd-6c2efb4a3ec7)

Related issue: [#756](https://github.com/stakira/OpenUtau/issues/756)

### `Mac OS`: Piano Roll window requires resizing before it will display
![image](https://github.com/user-attachments/assets/0616279c-a632-4bc6-b099-4a6d2edf7f85)

# Known bugs in stable version
`These bugs are already solved in the latest beta version. If you encountered one of these bugs, you can solve it by upgrading to the latest beta version.`

### Missing characters when typing in the lyrics editor or phoneme editor when using third-party Vietnamese IMEs (UniKey, EVKey, GoTiengViet, …)

This is a bug in the UI framework that OpenUTAU uses — Avalonia. Since this issue comes from the UI framework itself, we currently cannot fully fix it, and there is no indication that Avalonia has addressed it yet.

There are a few available workarounds:

* If your IME supports a buffer mode (for example, iBus-Bamboo with **mode 1 (with underline while typing)**), please use that mode.
* If not, configure your IME to use Clipboard mode (most popular IMEs still keep this mode as a fallback).

  * **UniKey**: chọn **Mở rộng (Expand)** → tick chọn **Luôn sử dụng clipboard cho unicode (Always use clipboard for unicode)**.
  * **EVKey**: tab **Cơ bản (General)** → chọn **Sử dụng Clipboard để gửi phím (Use Clipboard for send key)**.
  * **GoTiengViet**: tab **Hệ thống (System)** → chọn **Luôn dùng clipboard để gửi ký tự (Always use clipboard to send characters)**.
    For other IMEs, please refer to their documentation for instructions.

:warning: **Warning**: Using Clipboard mode may interfere with your clipboard history if you rely on it. Please make sure to save/pin important items to avoid potential data loss!

If none of the above workarounds help, please use Microsoft IME:
Go to **Settings > Time & Language > Language & Region > Add a language**, search for **Vietnamese (Tiếng Việt)**, and install it. Then press **Windows + Space** to switch to Vietnamese. **Note:** remember to disable other IMEs to avoid conflicts.

Related issue: [AvaloniaUI/Avalonia#12446](https://github.com/AvaloniaUI/Avalonia/issues/12446)

## Potential bugs that need investigation

### __MACOSX folder causes issues when installing
When a ZIP is made on a Mac, it creates a "__MACOSX" folder in the ZIP; this folder stores additional Metadata. Trying to install this ZIP with this folder will cause OpenUTAU to fail installing the Singer. MacOS automatically hides this folder from the user, making it impossible to delete, which means a user using OpenUTAU on a Mac can't install a singer from a ZIP file if it was made on another Mac.

### When trying to play a project, OpenUtau says "BadDeviceId calling waveOutOpen"

```
Failed to render
BadDeviceId calling waveOutOpen

NAudio.MmException: BadDeviceId calling waveOutOpen
at NAudio.MmException.Try(MmResult result, String function)
at NAudio.Wave.WaveOutEvent.Init(IWaveProvider waveProvider)
at NAudio.Wave.WaveExtensionMethods.Init(IWavePlayer wavePlayer, ISampleProvider sampleProvider, Boolean convertTo16Bit)
at OpenUtau.Audio.NAudioOutput.Init(ISampleProvider sampleProvider) in C:\projects\openutau\OpenUtau.Core\Audio\NAudioOutput.cs:line 52
at OpenUtau.Core.PlaybackManager.StartPlayback(Double startMs, MasterAdapter masterAdapter) in C:\projects\openutau\OpenUtau.Core\PlaybackManager.cs:line 118
at OpenUtau.Core.PlaybackManager.<>c__DisplayClass24_0.b__0() in C:\projects\openutau\OpenUtau.Core\PlaybackManager.cs:line 131

0.1.529.0
```

Changing the output devices, such as plugging a headphone in, might temporarily fix this bug.

Related issue: [#1133](https://github.com/stakira/OpenUtau/issues/1133) [#1382](https://github.com/stakira/OpenUtau/issues/1382)

***
## Addressed Bugs

> ### `WORLDLINE-R`: Crashes OpenUtau instance without error when invalid oto.ini entry or audio file encountered
> Other resamplers will throw an error dialog if unable to parse a note for these reasons, which should also happen for Worldline. 

Solved in PR [#1604](https://github.com/stakira/OpenUtau/pull/1604)

> ### CVVC phonemizers apply VCs erratically and/or cease to apply VCs when using voice colors/the CLR expression

Solved in PR [#1468](https://github.com/stakira/OpenUtau/pull/1468) and [#1462](https://github.com/stakira/OpenUtau/pull/1462)

> ### Changing the expression set will make the "Expressions" part of the "Note Properties" panel blank
> 1. Create a new project. Add a new track. Add a new part. Open piano roll, and open the "Note Properties" panel
> 2. In piano roll window, click the ⚙ icon at the button-left corner of the window, and add a new expression

> The "Expressions" part of the "Note Properties" panel will become blank. You need to close the piano roll window and reopen it.

Solved in PR [#1395](https://github.com/stakira/OpenUtau/pull/1395)
