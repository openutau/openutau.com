- Set up IDE (Recommended: [Visual Studio](https://visualstudio.microsoft.com/) or [VS Code](https://code.visualstudio.com/))
- [Compile OpenUtau from source](./Compiling-from-source)
- Begin learning C# from [official Microsoft tutorials](https://dotnet.microsoft.com/en-us/learn/csharp)
- Read [Phonemizer API](https://github.com/stakira/OpenUtau/tree/master/OpenUtau.Core/Api)
- For languages with multi-syllable words, read [SyllableBasedPhonemizer API](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Plugin.Builtin/SyllableBasedPhonemizer.cs)

Heavily commented example implementations, from simplest to most complex:
- [DefaultPhonemizer.cs](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/DefaultPhonemizer.cs)
- [JapaneseVCVPhonemizer.cs](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Plugin.Builtin/JapaneseVCVPhonemizer.cs)
- [ArpasingPhonemizer.cs](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Plugin.Builtin/ArpasingPhonemizer.cs)

## Phonemizer API

The main method to implement is:
```
public abstract Phoneme[] Process(Note[] notes, Note? prevNeighbour, Note? nextNeighbour);
```
* `notes`: A group of notes. The first note contains the lyric. The rest are extender notes whose lyric starts with `+`.
* `prevNeighbour` and `nextNeighbour`: Useful info for creating diphones, if applicable. E.g., creating proper leading diphone in VCV.
* `returns`: An array of phonemes, positioned relative to the first note.

Tips:
- To load singer specific resouce, Implement resouce loading in SetSinger() and use singer.Location to look for files.
- If uses expensive resource, load it lazily when the phonemizer is created the first time. Use your best adjudgement to decide its lifetime.

The API is implemented in [OpenUtau.Core/Api/Phonemizer.cs](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/Api/Phonemizer.cs)

## Phonemizer Development Guidelines
### Naming rule
Usually a phonemizer's name is `<language> <type>` for classic phonemizers, or `<renderer> <language>` for machine-learning phonemizers.
- Renderer is "vogen", "nnsvs" or "diffsinger".
- Language is the spoken language that the phonemizer sings in, such as "English", "Japanese". 
- Type is the vb type supported by the phonemizer, such as "CVVC", "VCV".

A phonemizer's tag is the abbreviation of the phonemizer's name. For example, the tag of "English Arpasing Phonemizer" is "EN ARPA"
- The language should be abbreviated in programmer's style, such as `EN` and `JA` (as in `EN-US` and `JA-JP`). See [microsoft official documentation](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-lcid/a9eac961-e77d-41a6-90a5-ce1a8b0cdb9c) for the language code of each language.

### Required Features
A complete Phonemizer should:
* Produce phonemes from the lyric, and previous / next notes if exist.
* Distribute phonemes to positions relative to the first note of each group of notes.
* (For Classic phonemizers) support multi-pitch and multi-color voicebanks.

### Optional Features
Considering the characteristics of different languages, the phonemizer doesn't necessarily have to implement all the following features. However, implementing these features can maintain a consistent user experience across various phonemizers. 

These features can be quickly implemented by inheriting a phonemizer template, such as [SyllableBasedPhonemizer](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Plugin.Builtin/SyllableBasedPhonemizer.cs).

**polysyllabic word support**

For polysyllabic languages ​​such as English, it should be supported to input lyrics on the first syllable, use `+~` or `+*` in the following notes to extend the current syllable, and use `+` to distribute the next syllable.

![image](https://github.com/stakira/OpenUtau/assets/54425948/507016e4-0c97-4468-9370-7700ef18f2bb)

**Phonetic hint**

Users can manually enter space-separated phoneme sequences (aka. Phonetic hint) in square brackets, such as `read` , `read[r iy d]` and `[r iy d]`. When both phonetic hint and word exist, the phonetic hint takes precedence.

![image](https://github.com/stakira/OpenUtau/assets/54425948/5da4e790-bab9-447c-88f0-24c82a3ff687)

**G2p**

G2p (Grapheme to phoneme) can convert lyrics in natural languages to phoneme sequences. OpenUTAU has built-in G2ps for multiple languages, implemented using a machine learning model, which can cover most of the words in the language, and can predict the pronunciation of new words that have not been seen before. Using a unified G2p can make the pronunciation of the same lyrics consistent on different phonemizers.

For languages ​​with a large number of words, and words cannot be converted into phoneme sequences through simple logic, such as English, French, and Russian, please use OpenUTAU's built-in G2p.

The following G2ps are included in OpenUTAU:
* English: [ArpabetG2P](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/G2p/ArpabetG2p.cs)
* French: [FrenchG2p](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/G2p/FrenchG2p.cs)
* German: [GermanG2p](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/G2p/GermanG2p.cs)
* Italian: [ItalianG2p](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/G2p/ItalianG2p.cs)
* Portuguese: [PortugueseG2p](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/G2p/PortugueseG2p.cs)
* Russian: [RussianG2p](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/G2p/RussianG2p.cs)
* Spanish: [SpanishG2p](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/G2p/SpanishG2p.cs)

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