## Known bugs
 
### Part always snap to measure line
If the starting position of a part isn't in the current page, when dragging the part, it can only snap to measure line, and we can't change the position of the part more precisely.
![](https://github.com/stakira/OpenUtau/assets/54425948/68193f7b-bb6e-4edb-a4e2-4b533e7b18ec)

### WORLDLINE-R audio distortion when changing gender factor curve's default value
If the gender factor default value is set to a negative value, such as -15, the synthesized audio will get heavily distorted. This bug does not occur when the gender factor value is set to 0
![image](https://github.com/stakira/OpenUtau/assets/54425948/356f157a-cc3a-454a-bebd-6c2efb4a3ec7)

Relative issue: [#756](https://github.com/stakira/OpenUtau/issues/756)

## Known bugs in stable version
These bugs are already solved in the latest beta version. If you encountered one of these bugs, you can solve it by upgrading to the latest beta version.

### After installing a diffsinger voicebank, all my singers are gone
Solved in PR [#1061](https://github.com/stakira/OpenUtau/pull/1061)