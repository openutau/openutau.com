# Known bugs

### WORLDLINE-R audio distortion when changing gender factor curve's default value
If the gender factor default value is set to a negative value, such as -15, the synthesized audio will get heavily distorted. This bug does not occur when the gender factor value is set to 0
![image](https://github.com/stakira/OpenUtau/assets/54425948/356f157a-cc3a-454a-bebd-6c2efb4a3ec7)

Related issue: [#756](https://github.com/stakira/OpenUtau/issues/756)

### OpenUTAU not crossfading correctly compared to UTAU

In classic UTAU, when your overlap is half of the pre-utterance or more, the pre-utterance of the next note will go all the way into the previous note.
![utau](https://github.com/stakira/OpenUtau/assets/87346264/16cc7f1f-566e-463c-915e-793ba2b0c3ec)

Comparatively, in OpenUTAU, when your overlap is half of your pre-utterance or more, the pre-utterance of the next note will only go part of the way into the previous note
![image](https://github.com/stakira/OpenUtau/assets/87346264/c01d5d34-2689-4274-b47d-f3d0bbe2f9f1)
>`Note` This is less a bug and more a parity/compatibility issue. 

>`Blocker` It's easy to fix the math, however solving the math alone causes UX issues regarding being able to differentiate between adjusting the timing bar and adjusting the crossfade. 

>`Suggested solution` Adding the ability to hold a modifier key (ctrl/alt/shift) in order to isolate interaction to either the crossfade or timing adjustment area.

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

# Known bugs in stable version
These bugs are already solved in the latest beta version. If you encountered one of these bugs, you can solve it by upgrading to the latest beta version.

### CVVC phonemizers apply VCs erratically and/or cease to apply VCs when using voice colors/the CLR expression
![image](https://i.imgur.com/ogwXCKJ.png)

Related issue: [#1226](https://github.com/stakira/OpenUtau/issues/1226)  
This bug will be solved in PR [#1468](https://github.com/stakira/OpenUtau/pull/1468) and [#1462](https://github.com/stakira/OpenUtau/pull/1462)

### Changing the expression set will make the "Expressions" part of the "Note Properties" panel blank
1. Create a new project. Add a new track. Add a new part. Open piano roll, and open the "Note Properties" panel
2. In piano roll window, click the ⚙ icon at the button-left corner of the window, and add a new expression

The "Expressions" part of the "Note Properties" panel will become blank. You need to close the piano roll window and reopen it.
![image](https://github.com/user-attachments/assets/338b2fa9-ddff-4e84-901a-5e287b1d3382)
Solved in PR [#1395](https://github.com/stakira/OpenUtau/pull/1395)

### Part always snap to measure line
If the starting position of a part isn't in the current page, when dragging the part, it can only snap to measure line, and we can't change the position of the part more precisely.
![](https://github.com/stakira/OpenUtau/assets/54425948/68193f7b-bb6e-4edb-a4e2-4b533e7b18ec)
Solved in PR [#1449](https://github.com/stakira/OpenUtau/pull/1449)

### Error when pressing Ctrl+Z in "Edit Lyrics" dialog
![image](https://github.com/user-attachments/assets/f91846e3-a5bf-4017-a762-f788a1fae87f)

Clicking "Apply" will make OpenUtau crash

Solved in PR [#1220](https://github.com/stakira/OpenUtau/pull/1220)

### After installing a diffsinger voicebank, all my singers are gone
Solved in PR [#1061](https://github.com/stakira/OpenUtau/pull/1061)


## Potential bugs that need investigation

### __MACOSX folder causes issues when installing
When a ZIP is made on a Mac, it creates a "__MACOSX" folder in the ZIP; this folder stores additional Metadata. Trying to install this ZIP with this folder will cause OpenUTAU to fail installing the Singer. MacOS automatically hides this folder from the user, making it impossible to delete, which means a user using OpenUTAU on a Mac can't install a singer from a ZIP file if it was made on another Mac.

