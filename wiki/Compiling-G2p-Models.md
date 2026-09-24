- G2p Resources: [OpenUtau/py](https://github.com/stakira/OpenUtau/tree/master/py)
- Set up IDE (Recommended: [Visual Studio](https://visualstudio.microsoft.com/))
- [Compile OpenUtau from source](./Compiling-from-source)
- Begin learning C# from [official Microsoft tutorials](https://dotnet.microsoft.com/en-us/learn/csharp)

**Examples of G2p Models that are included in OpenUTAU:**
* English: [ArpabetG2P](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/G2p/ArpabetG2p.cs)
* French: [FrenchG2p](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/G2p/FrenchG2p.cs)
* German: [GermanG2p](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/G2p/GermanG2p.cs)
* Italian: [ItalianG2p](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/G2p/ItalianG2p.cs)
* Portuguese: [PortugueseG2p](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/G2p/PortugueseG2p.cs)
* Russian: [RussianG2p](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/G2p/RussianG2p.cs)
* Spanish: [SpanishG2p](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/G2p/SpanishG2p.cs)
---
## Compiling the G2p Model (Internal Model)
### Adding The Data Source
  - After [packing](https://github.com/stakira/OpenUtau/tree/master/py#packing) the G2p model into a zip file, place the zip file on [`\OpenUtau\OpenUtau.Core\G2p\Data`](https://github.com/stakira/OpenUtau/tree/master/OpenUtau.Core/G2p/Data)
  - open the `Resources.resx` and drag and drop the g2p zip file on the window then save. This will automatically update the `Resources.Designer.cs` to add the zip file as a data resource.
    - ***`note:`** the `Resources.Designer.cs` has a bug that redirects the resources to `G2p.Data.Resouces` instead of the root directory `OpenUtau.Core.G2p.Data.Resources`. Please rename the line 42 in order to make the G2p's work properly.*
    - Replace `G2p.Data.Resouces` to `OpenUtau.Core.G2p.Data.Resources`.
  - Before:
  ```
  if (object.ReferenceEquals(resourceMan, null)) {
                      global::System.Resources.ResourceManager temp = new global::System.Resources.ResourceManager("G2p.Data.Resources", typeof(Resources).Assembly);
                      resourceMan = temp;
                  }
  ```
  - After:
  ```
  if (object.ReferenceEquals(resourceMan, null)) {
                      global::System.Resources.ResourceManager temp = new global::System.Resources.ResourceManager("OpenUtau.Core.G2p.Data.Resources", typeof(Resources).Assembly);
                      resourceMan = temp;
                  }
  ```
  - Create the `.cs` file on [`\OpenUtau\OpenUtau.Core\G2p`](https://github.com/stakira/OpenUtau/tree/master/OpenUtau.Core/G2p).
  - Set up the `graphemes` and `phonemes` that matches the G2p model.
  - Edit the `LoadPack` code and link the G2p zip file.
### Adding the model to `Phonetic Assistant`
  - Add the G2p to `PhoneticAssistantViewModel.cs` on [`\OpenUtau\OpenUtau\ViewModels`](https://github.com/stakira/OpenUtau/blob/master/OpenUtau/ViewModels/PhoneticAssistantViewModel.cs). The G2p name must match the name of the `.cs` file.
### Adding the model to `Lyrics Helper`
  - Add the G2p to `LyricsHelper.cs` on [`\OpenUtau\OpenUtau.Core\Util`](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/Util/LyricsHelper.cs). The G2p name must match the name of the `.cs` file.
---
## Compiling the G2p Model (External Model)
### Adding The Data Source
  - After [packing](https://github.com/stakira/OpenUtau/tree/master/py#packing) the G2p model into a zip file and created the initial external phonemizer, place the zip file on a folder called `Resources`.
  - Create the `Resources.resx` and drag and drop the G2p zip file on the window then save. Rename the `Custom Tool Namespace` same as the name of the project. `Custom Tool Namespace` are found on the properties panel or `Alt + Enter`.
  - `Resources.Designer.cs` will update as well and make sure the resources directory are correct. It should be `(project-name.Resources)`
  - Create the `.cs` file.
  - Set up the `graphemes` and `phonemes` that matches the G2p model.
  - Edit the `LoadPack` code and link the G2p zip file.
    - Example tree view:
    - ![image](https://github.com/stakira/OpenUtau/assets/92255161/f63476bc-61f4-4fa1-9f2a-bc4852963cdd)

## Prioritizing the `dict.text` over the `g2p.onnx` 
### Adding The Data Source
This will make the G2pPack class uses entries from dict.txt first. If not found, it uses g2p.onnx to generate phonemes.

  - Editing the order of the code will make the G2ppack prioritize the `dict.text` over the `g2p.onnx`.
    - from:
    ```
    private static object lockObj = new object();
    private static Dictionary<string, int> graphemeIndexes;
    private static IG2p dict;
    private static InferenceSession session;
    private static Dictionary<string, string[]> predCache = new Dictionary<string, string[]>();

    // public class name of the g2p 
            GraphemeIndexes = graphemeIndexes;
            Phonemes = phonemes;
            Dict = dict;
            Session = session;
            PredCache = predCache;
    ```
    - to:
    ```
    private static object lockObj = new object();
    private static IG2p dict;
    private static Dictionary<string, int> graphemeIndexes;
    private static InferenceSession session;
    private static Dictionary<string, string[]> predCache = new Dictionary<string, string[]>();

    // public class name of the g2p 
            Dict = dict;
            PredCache = predCache;
            GraphemeIndexes = graphemeIndexes;
            Phonemes = phonemes;
            Session = session;
    ```
---
### G2p

G2p (Grapheme to phoneme) can convert lyrics in natural languages to phoneme sequences. OpenUTAU has built-in G2ps for multiple languages, implemented using a machine learning model, which can cover most of the words in the language, and can predict the pronunciation of new words that have not been seen before. Using a unified G2p can make the pronunciation of the same lyrics consistent on different phonemizers.

For languages ​​with a large number of words, and words cannot be converted into phoneme sequences through simple logic, such as English, French, and Russian, please use OpenUTAU's built-in G2p.



**Custom pronunciation dictionary**

On the basis of G2p, considering that some voicebanks have custom phonemes, a phonemizer should support custom dictionaries. Custom dictionaries can be loaded using [G2pDictionary](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/Api/G2pDictionary.cs).

No matter which encoding the voicebank uses, yaml dictionaries should always use UTF-8 encoding.

Here is an example of custom dictionary:
```yaml
%YAML 1.2
---
symbols:
  - {symbol: aa, type: vowel}
  - {symbol: ae, type: vowel}
  - {symbol: ah, type: vowel}
  - {symbol: ao, type: vowel}
  - {symbol: aw, type: vowel}
  - {symbol: ay, type: vowel}
  - {symbol: b, type: stop}
  - {symbol: ch, type: affricate}
  - {symbol: d, type: stop}
  - {symbol: dh, type: fricative}
  - {symbol: eh, type: vowel}
  - {symbol: er, type: vowel}
  - {symbol: ey, type: vowel}
  - {symbol: f, type: fricative}
  - {symbol: g, type: stop}
  - {symbol: hh, type: aspirate}
  - {symbol: ih, type: vowel}
  - {symbol: iy, type: vowel}
  - {symbol: jh, type: affricate}
  - {symbol: k, type: stop}
  - {symbol: l, type: liquid}
  - {symbol: m, type: nasal}
  - {symbol: n, type: nasal}
  - {symbol: ng, type: nasal}
  - {symbol: ow, type: vowel}
  - {symbol: oy, type: vowel}
  - {symbol: p, type: stop}
  - {symbol: r, type: liquid}
  - {symbol: s, type: fricative}
  - {symbol: sh, type: fricative}
  - {symbol: t, type: stop}
  - {symbol: th, type: fricative}
  - {symbol: uh, type: vowel}
  - {symbol: uw, type: vowel}
  - {symbol: v, type: fricative}
  - {symbol: w, type: semivowel}
  - {symbol: y, type: semivowel}
  - {symbol: z, type: fricative}
  - {symbol: zh, type: fricative}
entries:
  - grapheme: openutau
    phonemes: [ow, p, eh, n, w, uw, t, ah, w, uw]
```

When reading and writing yaml files, OpenUtau always uses yaml 1.2 syntax. If you're developing third-party tools to parse or generate these yaml files, please use `ruamel.yaml` instead of `pyyaml` library.

**`NOTE:`** Since Openutau doesn't have a built-in dictionary editor yet. Use [Openutau Dictionary Editor](https://github.com/Cadlaxa/OpenUtau-Dictionary-Editor) for edit the YAML dictionary. This tool can be used as external plugin for Openutau by placing it to the `plugins` folder

## Appendix: Phoneme set of builtin G2Ps
### ArpabetG2p (English)
- vowels: `aa, ae, ah, ao, aw, ay, eh, er, ey, ih, iy, ow, oy, uh, uw`
- consonants: `b, ch, d, dh, f, g, hh, jh, k, l, m, n, ng, p, r, s, sh, t, th, v, w, y, z, zh`

### GermanG2p
- vowels: `aa, ae, ah, ao, aw, ax, ay, ee, eh, er, ex, ih, iy, oe, ohh, ooh, oy, ue, uh, uw, yy`
- consonants: `b, cc, ch, d, dh, f, g, hh, jh, k, l, m, n, ng, p, pf, q, r, rr, s, sh, t, th, ts, v, w, x, y, z, zh`

### ItalianG2p
- vowels: `a, a1, e, e1, EE, i, i1, o, o1, OO, u, u1`
- consonants: `b, d, dz, dZZ, f, g, JJ, k, l, LL, m, n, nf, ng, p, r, rr, s, SS, t, ts, tSS, v, w, y, z`

### PortugueseG2p
- vowels: `a, a~, e, e~, E, i, i~, o, o~, O, u, u~`
- consonants: `b, d, dZ, f, g, j, j~, J, k, l, L, m, n, p, r, R, s, S, t, tS, v, w, w~, X, z, Z`

### RussianG2p
- vowels: `a, aa, ay, ee, i, ii, ja, je, jo, ju, oo, u, uj, uu, y, yy`
- consonants: `b, bb, c, ch, d, dd, f, ff, g, gg, h, hh, j, k, kk, l, ll, m, mm, n, nn, p, pp, r, rr, s, sch, sh, ss, t, tt, v, vv, z, zh, zz`

### SpanishG2p
- vowels: `a, e, i, o, u`
- consonants: `b, B, ch, d, D, f, g, G, gn, I, k, l, ll, m, n, p, r, rr, s, t, U, w, x, y, Y, z`