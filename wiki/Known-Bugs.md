## Known bugs
 
### Part always snap to measure line
If the starting position of a part isn't in the current page, when dragging the part, it can only snap to measure line, and we can't change the position of the part more precisely.
![](https://github.com/stakira/OpenUtau/assets/54425948/68193f7b-bb6e-4edb-a4e2-4b533e7b18ec)

### WORLDLINE-R audio distortion when changing gender factor curve's default value
If the gender factor default value is set to a negative value, such as -15, the synthesized audio will get heavily distorted. This bug does not occur when the gender factor value is set to 0
![image](https://github.com/stakira/OpenUtau/assets/54425948/356f157a-cc3a-454a-bebd-6c2efb4a3ec7)

Related issue: [#756](https://github.com/stakira/OpenUtau/issues/756)

### __MACOSX folder causes issues when installing
When a ZIP is made on a Mac, it creates a "__MACOSX" folder in the ZIP; this folder stores additional Metadata. Trying to install this ZIP with this folder will cause OpenUTAU to fail installing the Singer. MacOS automatically hides this folder from the user, making it impossible to delete, which means a user using OpenUTAU on a Mac can't install a singer from a ZIP file if it was made on another Mac.

### OpenUTAU not crossfading correctly compared to UTAU

In classic UTAU, when your overlap is half of the pre-utterance or more, the pre-utterance of the next note will go all the way into the previous note.
![utau](https://github.com/stakira/OpenUtau/assets/87346264/16cc7f1f-566e-463c-915e-793ba2b0c3ec)

In OpenUTAU, when your overlap is half of your pre-utterance or more, the pre-utterance of the next note will go nearly all the way into the previous note
![image](https://github.com/stakira/OpenUtau/assets/87346264/c01d5d34-2689-4274-b47d-f3d0bbe2f9f1)

### Error when pressing Ctrl+Z in "Edit Lyrics" dialog
![image](https://github.com/user-attachments/assets/f91846e3-a5bf-4017-a762-f788a1fae87f)

Clicking "Apply" will make OpenUtau crash

## Known bugs in stable version
These bugs are already solved in the latest beta version. If you encountered one of these bugs, you can solve it by upgrading to the latest beta version.

### After installing a diffsinger voicebank, all my singers are gone
Solved in PR [#1061](https://github.com/stakira/OpenUtau/pull/1061)