This page is written for end users. Developers interested in working on new phonemizers should refer to the [API Doc](https://github.com/stakira/OpenUtau/wiki/Developing-new-phonemizers).

When phonemizers break notes into multiple phonemes, you can adjust the envelopes and parameters for each of these independently.

In order to change the phonemizer, click DEFAULT on the vocal track and choose the phonemizer from there.

![phonemizer](https://i.imgur.com/mBf2VOY.png)

## *How does VCV/CVVC/VCCV/etc. work?
- VCV and CVVC voicebanks, also known as "continuous sound" or 連続音 (*renzokuon*), use natural transitions between notes to smoothly blend sounds together during rendering. The standard method to organize these sounds is to directly type sound aliases from the `oto.ini` file into notes. Effectively, this is like hand-picking samples from the voicebank and connecting them together manually.  
If this style is preferred, it can be utilized via the "Default" phonemizer in OpenUtau.
- OpenUtau offers special phonemizers for many languages to handle aliases from VCV or CVVC banks automatically. Phonemizers emulate old UTAU plugins, such as presamp or AutoCVVC, with different advantages:  
    1. Phonemizers operate in realtime while editing lyrics.
    2. Results from phonemizers are displayed intuitively in the envelope editor below the notes.  
    3. In the envelope editor, the timing of the sound can be easily adjusted.  
- Not all voicebanks will play nicely with OpenUtau. Some banks have specific quirks that the phonemizer cannot use, and OpenUtau does not support every type of voicebank in every language.

## DEFAULT
No phonemization is applied.
You can input `+` to extend the previous lyric over multiple notes.  
(Older versions of OpenUtau may use `...` instead of `+`.)

![+ extension](https://i.imgur.com/JlHc6bq.png)

## EN ARPA (English ARPAsing)
[Reclist](https://arpasing.tubs.wtf/en/directories/reclists)

You may input lyrics in three different ways.
- Plain English words (eg. `live`)  
![plain english words](https://i.imgur.com/PZJe73G.png)
- Plain English words + phonetic hint (eg. `live[l ih v]`)  
![english word + hint](https://i.imgur.com/YmvhUaL.png)
- Phonetic hint only (eg. `[l ih v]`)  
![hint only](https://i.imgur.com/6hKOYsn.png)

For multisyllabic words, type the whole word in the first note, then use `+` to extend it across the following notes.  
If the syllables are misaligned, add numbers after `+` to force alignment to the nth phoneme in the word.  
(Older versions of OpenUtau may use `...` instead of `+`.)

![multisyllable](https://i.imgur.com/zjoVXxP.png)

### Auxiliary dictionary files:

- You can find an example `arpasing.yaml` file in Plugins folder. You can add new entries to it.
- A copy of `arpasing.yaml` file can be added to singer folder for a specific singer. You can even distribute an `arpasing.yaml` file with your voicebank.
- The lookup order is `plugin dictionary` -> `singer dictionary` -> `default dictionary`.

## EN ARPA+ (English ARPAsing+)
[Reclist](https://arpasing.tubs.wtf/en/directories/reclists)

- Same mechanics for lyric input 
- Supports more alias formats such as: `cv`, `c v`, `ccv`, `cc v`, `v v`, `splitted vv`, `v c`, `v cc`, `c c`, `c cc` and so on
### Auxiliary dictionary files:
- #### Symbols
    - Add a new symbol and define its symbol type for the phonemizer to recognize (`vowel`, `stop`, `affricate`, `fricative`, `aspirate`, `liquid`, `nasal`, `semivowel`, `tail`).
    - `affricate`'s are prioritized because they produce a sound.
    - indicate the phoneme as `tail` to use them as a trailing tail note.
    - encapsulate the whole symbol with `' '` if it starts with a special symbol.
    ```
    symbols:
      - {symbol: ea, type: vowel}
      - {symbol: ix, type: vowel}
      - {symbol: dd, type: tap}
      - {symbol: j, type: fricative}
      - {symbol: '@r', type: vowel}
    ```
- #### Fallbacks
    - Fallbacks missing phoneme/alias to the mapped phoneme/alias.
    - supports `1:1` phoneme mappings only.
    ```
    fallbacks:
    # 1:1 (one-to-one mappings)
      - {from: ax, to: ah}
      - {from: ch oy, to: ch ow}

    # format can be like this
        - from: b@
        to: bV
        - from: b
        to: bh
    ```
- #### Replacements
    - Replaces certain phoneme or sequence of phonemes defined in the replacements entry.
    - supports `1:1`, `1:M`, `M:1`, `M:M` phoneme replacements.
    ```
    replacements:
    # 1:1 (one-to-one mappings)
      - {from: ax, to: ah}
      - {from: cl, to: q}
    # 1:M (one-to-many mappings) (splitting)
      - {from: dr, to: [d, r]}
      - {from: tr, to: [t, sh, r]}
      - {from: aw, to: [aa, w]}
    # M:1 (many-to-one mappings) (merging)
      - {from: [ih, ng], to: ing}
      - {from: [eh, ax, m], to: eam}
    # M:M (many-to-many mappings)
      - {from: [ih, ng], to: [ix, ng]}
      - {from: [ay, l], to: [ay, ax, el]}

    # format can be like this
        - from: [ae, n]
        to: [eh, ax, n]
        - from: b
        to: bh
    ```
- #### Timings
    - Defines the certain phoneme to be in this phoneme group's phoneme length.
    - Overrides specific alias to be in that length (in seconds).
    ```
    timings:
      - {symbol: dh, value: 1.2}
      - {symbol: vf, value: 2.8}
      - {symbol: st, value: 3.5}
      - {symbol: a r, value: 0.5}
      - {symbol: e r, value: 0.5}
      - {symbol: i r, value: 0.5}
    ```
- #### Entries
    - Add a new dictionary entry to override certain word pronunciations.
    - no limit to characters as long as it covered by unicode so you can add kana, hangul, hieroglyphics grapheme etc entries to `arpasing.yaml`.
    ```
    entries:
      - {grapheme: hello, phonemes: [hh, ax, l, ow]}
      - {grapheme: 안녕하세요, phonemes: [aa, n, y, ao, ng, hh, ah, s, eh, y ao]}
    # format can be like this
      - grapheme: stars
        phonemes: s, t, aa, r, z
      - grapheme: drops
        phonemes: dr, aa, p, s
    ```
## EN C+V

- Same mechanics for lyric input 
- Supports more alias formats such as: `v`, `c`, `cc`, `v c` and so on
- Supported alias varieties `spaced`, `no-space`
- `Note that the new version of the [en-cPv.yaml] will be created in OU version 0.1.566, the old yaml file will be renamed as [en-cPv_backup.yaml]`

### Auxiliary dictionary files:
- #### Symbols
    - Add a new symbol and define its symbol type for the phonemizer to recognize (`vowel`, `stop`, `affricate`, `fricative`, `aspirate`, `liquid`, `nasal`, `semivowel`, `tail`, `diphthong`).
    - `affricate`'s are prioritized because they produce a sound.
    - indicate the phoneme as `tail` to use them as a trailing tail note.
    - encapsulate the whole symbol with `' '` if it starts with a special symbol.
    ```
    symbols:
      - {symbol: ea, type: vowel}
      - {symbol: ix, type: vowel}
      - {symbol: dd, type: tap}
      - {symbol: j, type: fricative}
      - {symbol: '@r', type: vowel}
    ```
- #### Fallbacks
    - Fallbacks missing phoneme/alias to the mapped phoneme/alias.
    - supports `1:1` phoneme mappings only.
    ```
    fallbacks:
    # 1:1 (one-to-one mappings)
      - {from: ax, to: ah}
      - {from: ch oy, to: ch ow}

    # format can be like this
        - from: b@
        to: bV
        - from: b
        to: bh
    ```
- #### Replacements
    - If the vb you're using in not in arpabet, you can remap them to the desired phoneme system with this method.
    - Replaces certain phoneme or sequence of phonemes defined in the replacements entry.
    - supports `1:1`, `1:M`, `M:1`, `M:M` phoneme replacements.
    ```
    replacements:
    # 1:1 (one-to-one mappings)
      - {from: ax, to: ah}
      - {from: cl, to: q}
    # 1:M (one-to-many mappings) (splitting)
      - {from: dr, to: [d, r]}
      - {from: tr, to: [t, sh, r]}
      - {from: aw, to: [aa, w]}
    # M:1 (many-to-one mappings) (merging)
      - {from: [ih, ng], to: ing}
      - {from: [eh, ax, m], to: eam}
    # M:M (many-to-many mappings)
      - {from: [ih, ng], to: [ix, ng]}
      - {from: [ay, l], to: [ay, ax, el]}

    # format can be like this
        - from: [ae, n]
        to: [eh, ax, n]
        - from: b
        to: bh
    ```
- #### Timings
    - Defines the certain phoneme to be in this phoneme group's phoneme length.
    - Overrides specific alias to be in that length (in seconds).
    ```
    timings:
      - {symbol: dh, value: 1.2}
      - {symbol: vf, value: 2.8}
      - {symbol: st, value: 3.5}
      - {symbol: a r, value: 0.5}
      - {symbol: e r, value: 0.5}
      - {symbol: i r, value: 0.5}
    ```
- #### Diphthongs
    - Defines the certain phoneme as a diphthong in the symbols list so it splits the phoneme into 2.
      ```
      symbols:
        - {symbol: aU, type: dihpthong}
        - {symbol: A, type: dihpthong}
      ```
    - Default dipthong splitting will be `V-`.
    - Can furthre customize the diphthong phoneme splitting with these parameter

    ```
    diphthong:
      - {from: aw, to: _aw}
      - {from: EI, to: EI--}
    ```
- #### Entries
    - Add a new dictionary entry to override certain word pronunciations.
    - no limit to characters as long as it covered by unicode so you can add kana, hangul, hieroglyphics grapheme etc entries to `en-cPv.yaml`.
    ```
    entries:
      - {grapheme: hello, phonemes: [hh, ax, l, ow]}
      - {grapheme: 안녕하세요, phonemes: [aa, n, y, ao, ng, hh, ah, s, eh, y ao]}
    # format can be like this
      - grapheme: stars
        phonemes: s, t, aa, r, z
      - grapheme: drops
        phonemes: dr, aa, p, s
    ```
## FIL VCV & CVVC
- Same mechanics for lyric input 
- Takes the notes and splits them into phonemes depending in the phonemes listed in the yaml file
- Supports more alias formats such as: `cv`, `c v`, `ccv`, `cc v`, `v v`, `splitted vv`, `v c`, `v cc`, `c c`, `c cc` and so on
- Supports separate starting C's or starting CV's
### Auxiliary dictionary files:
- #### Symbols
    - Add a new symbol and define its symbol type for the phonemizer to recognize (`vowel`, `stop`, `affricate`, `fricative`, `aspirate`, `liquid`, `nasal`, `semivowel`, `tail`).
    - `affricate`'s are prioritized because they produce a sound.
    - indicate the phoneme as `tail` to use them as a trailing tail note.
    - encapsulate the whole symbol with `' '` if it starts with a special symbol.
    ```
    symbols:
      - {symbol: ea, type: vowel}
      - {symbol: ix, type: vowel}
      - {symbol: dd, type: tap}
      - {symbol: j, type: fricative}
      - {symbol: '@r', type: vowel}
    ```
- #### Fallbacks
    - Fallbacks missing phoneme/alias to the mapped phoneme/alias.
    - supports `1:1` phoneme mappings only.
    ```
    fallbacks:
    # 1:1 (one-to-one mappings)
      - {from: a, to: A}
      - {from: ts, to: ch}

    # format can be like this
        - from: b@
        to: bV
        - from: b
        to: bh
    ```
- #### Replacements
    - Replaces certain phoneme or sequence of phonemes defined in the replacements entry.
    - supports `1:1`, `1:M`, `M:1`, `M:M` phoneme replacements.
    ```
    replacements:
    # 1:1 (one-to-one mappings)
      - {from: ax, to: ah}
      - {from: cl, to: q}
    # 1:M (one-to-many mappings) (splitting)
      - {from: dr, to: [d, r]}
      - {from: tr, to: [t, sh, r]}
      - {from: aw, to: [aa, w]}
    # M:1 (many-to-one mappings) (merging)
      - {from: [ih, ng], to: ing}
      - {from: [eh, ax, m], to: eam}
    # M:M (many-to-many mappings)
      - {from: [ih, ng], to: [ix, ng]}
      - {from: [ay, l], to: [ay, ax, el]}

    # format can be like this
        - from: [ae, n]
        to: [eh, ax, n]
        - from: b
        to: bh
    ```
- #### Timings
    - Defines the certain phoneme to be in this phoneme group's phoneme length.
    - Overrides specific alias to be in that length (in seconds).
    ```
    timings:
      - {symbol: dh, value: 1.2}
      - {symbol: vf, value: 2.8}
      - {symbol: st, value: 3.5}
      - {symbol: a r, value: 0.5}
      - {symbol: e r, value: 0.5}
      - {symbol: i r, value: 0.5}
    ```
- #### Entries
    - Add a new dictionary entry to override certain word pronunciations.
    - no limit to characters as long as it covered by unicode so you can add kana, hangul, hieroglyphics grapheme etc entries to `filipino.yaml`.
    ```
    entries:
      - {grapheme: hello, phonemes: [hh, ax, l, ow]}
      - {grapheme: 안녕하세요, phonemes: [aa, n, y, ao, ng, hh, ah, s, eh, y ao]}
    # format can be like this
      - grapheme: stars
        phonemes: s, t, aa, r, z
      - grapheme: drops
        phonemes: dr, aa, p, s
    ```

## ZH CVV (Chinese CVV)
Lyrics should be written in pinyin. The phonemizer will insert endings for syllables that need them.  
![zh cvv](https://i.imgur.com/TJfiNit.png)

## JA Presamp (Japanese VCV & CVVC)
You can use all of CV, VCV and CVVC voicebank.  
The phonemizer first tries VCV, and if it isn't available in the voice bank, it will falls back to CVVC, then CV.  
Preference is given to CVVC with matching color over VCV with default color.  
![presamp](https://imgur.com/SKzYtIb.png)  

The phonemizer converts romaji to hiragana (see below for details).  
![presamp romaji](https://imgur.com/bNSFg6g.png)  
Glottal stops should be written as [あ・].  

This phonemizer follows the behavior of presamp. If voicebank has `presamp.ini`, use it.  
Supporting `presamp.ini` features:  
[VOWEL][CONSONANT][PRIORITY][REPLACE][ALIAS(VCPAD,VCVPAD)]  

The default [REPLACE] includes romaji to hiragana conversion, so the phonemizer converts romaji to hiragana if there is no `presamp.ini` or there are descriptions in [REPLACE] of `presamp.ini` to convert romaji to hiragana.(Only for exact matches)  
The default VC length is the preutterance of the following CV.  

If phonetic hint is entered, use it and do not convert to VCV or CVVC.  
![JaPhoneticHint](https://i.imgur.com/vgVHiJ2.png)

## JA CVVC (Japanese CVVC)
Lyrics should be written in hiragana. If your lyrics are written in romaji, you can convert it to hiragana using the Romaji to Hiragana transformer.  
![roma to hira](https://i.imgur.com/XmfItiZ.png)

The phonemizer will insert VCs and convert vowels to VV. The default VC length is the preutterance of the following CV. `presamp.ini` settings from the voicebank are not supported yet.  
![ja cvvc](https://i.imgur.com/GDaGjLu.png)

If phonetic hint is entered, use it and do not convert to CVVC.  
![JaPhoneticHint](https://i.imgur.com/WRp2vub.png)

## JA VCV (Japanese VCV)
Lyrics should be written in hiragana. If your lyrics are written in romaji, you can convert it to hiragana using the Romaji to Hiragana transformer.  
![roma to hira](https://i.imgur.com/XmfItiZ.png)

The phonemizer will automatically convert CV to VCV. If a VCV sample isn't available in the voicebank, it will fall back on CV. `presamp.ini` settings from the voicebank are not supported yet.  
![ja vcv](https://i.imgur.com/QYp3J3J.png)

If phonetic hint is entered, use it and do not convert to VCV.  
![JaPhoneticHint](https://i.imgur.com/vgVHiJ2.png)


## KO CVC (Korean CVC)
This is a program to modify existing oto.ini file for use in OpenUtau (made by myself)  
└> https://app.box.com/s/t973p0rznirqg0naa04436p8re0ktfyy  
You can write lyrics in Romaji and Hangul, and the phonemizer will automatically insert VCs between each CV.  
![kr cvc](https://i.imgur.com/6w87k41.png)  
you can write final consonant(`n`, `m`, `ng`, `l`, `k`, `p`, `t`),  
but you should write the vowel of preNote in front of final consonant without spaces (ex. `an(안)`, `im(임)`, `ung(웅)`, `el(엘)`, `ok(옥)`, `eup(읍)`, `eot(엇)`).  
final consonant is classified as CV, but VC isn't inserted next note.  
![kr cvc final consonant](https://i.imgur.com/yB012mW.png)  
There's no insert VC behind vowel and `w`, `y`, `l` note (ex. `a`, `ya`, `weo`, `li`)  
![kr cvc vowel](https://i.imgur.com/WsTELSm.png)  
write Hangeul, you can use combine final consonants  
![kr cvc](https://i.imgur.com/Ffn0mNK.jpg)  
write lyrics in Hangeul, apply phonological rules(연음화 / 유기음화 / 경음화 / 구개음화 / 비음화 / 유음화 / 탈락 / 음절끝소리규칙)  

## KO CVVC (Korean CVVC)
You should write the lyrics in Hangeul. Romaji will be updated soon.  
Automatically insert VC between CV and CV.  
![kr cvvc](https://i.imgur.com/vrftrEJ.png)

you can write final consonant(`ㄴ`, `ㅁ`, `ㅇ`, `ㄹ`, `ㄱ`, `ㄲ`, `ㅂ`, `ㅍ`, `ㅅ`, `ㄷ`, `ㅌ`)
You can fill it out right after the note like CV.
Even if CV comes after final consonant, VC is not generated.  
![kr cvvc final consonant](https://i.imgur.com/2RQfG4F.png)

When entering Vowel and Vowel, it is converted like VCV.  
![kr cvvc vowel](https://i.imgur.com/ubiRAgb.png)

## KO CVVC (Korean CVVC standard pronuciation)
Followed the standard pronunciation method for Hangul.
This support all Korean final consonants, consonant assimilation(자음동화), 된소리되기, abbreviate consonants(자음 축약), 탈락, sandhi(연음).  

![Korean CVVC standard pronuciation](https://i.imgur.com/unXXxVq.png)

## KO VCV (Korean VCV)
Lyrics can be input in Hangul (ex. `한 글`) or as an Arpasing-style phonetic hint (ex. `[h a n] [g eu l]`). When a note has both a lyric and a phonetic hint, the phonetic hint takes precedence.

![Hangul and phonetic hint support](https://i.imgur.com/1CKRtFl.png)

The phonemizer supports both lowercase and uppercase batchim aliases. No need to worry about modifying the oto.ini files.

![Lowercase batchim alias support](https://i.imgur.com/uw72Arh.png)
![Uppercase batchim alias support](https://i.imgur.com/eA5yfCo.png)

When inputting phonetic hints, take note of the following:
* Each syllable must be in its own note (`[h a n] [g eu l]` O / `[h a n g eu l]` X).
* ㅐ, ㅒ, and ㅙ can be written as `ae`, `yae`, and `wae`, respectively. You do not need to convert them to an `e` vowel.
* ㄲ, ㄸ, and ㅃ can be written as `gg / kk`, `dd / tt`, and `bb / pp`, respectively.
* ㅢ can be written as `eui` or `ui`.
* ㅚ can be written as `oi` or `oe`.
* Each sound *must* be separated with spaces (`[h a n]` O / `[han]` X).
* Glides (`w` and `y`) are part of the vowel and should *not* be treated as an initial consonant (`[wae]` O / `[w ae]` X).

Phonetic hints and Hangul can be used together, which may be useful for voicebanks that offer English sounds like /f/ and /v/.

![Hangul and phonetic hint mixing](https://i.imgur.com/k0lux1a.png)

Although the phonemizer supports all Hangul jamo, it is strongly recommended to rewrite the lyrics in phonetic Hangul (such as the pronunciation guides on the Naver Korean Dictionary or Wiktionary) for best results, especially with words that go through consonant sound changes (ex. 입력 → 임녁, 꽃잎 → 꼰닙, 있어 → 이써, etc.).

## KO CV (Korean CV) & KO CBNN (Korean Combination/CBNN) 
Phonemizer for Korean CV, [Korean CBNN](https://github.com/EX3exp/UTAU-Korean-CBNN). <br>
한국어 단독음, [한국어 CBNN](https://github.com/EX3exp/UTAU-Korean-CBNN) 포네마이저의 설명입니다. <br>

###  Common Features (공통 가이드)
1. Supports almost all Korean phoneme variations, except `palatalization` and `ㄴ addition`. <br>
`구개음화`와 `ㄴ첨가` 이외의 거의 모든 음운변동을 반영합니다. 
![image](https://github.com/stakira/OpenUtau/assets/100339835/c13dfb89-6f5b-4cd9-bcd6-55559fa4ecdf) <br>

2. Can extend phonemes by `+`. <br>
`+`로 음소를 연장합니다. 
![image](https://github.com/stakira/OpenUtau/assets/100339835/1c4d4c9a-2f8c-49e8-9861-07749f8cec85) <br>

3. Can insert phonemes by `[` `]`. 
- Supports flexible VV phoneme input.
- (If phonemes include `a i`, but if current singer doesn't have `a i` (but has `i`) : Phonemizer automatically puts `i` instead of `a i` and vice versa.) <br> <br>
`[`와 `]`를 사용해 발음 기호를 넣습니다.
- 유연한 VV 음소 입력을 지원합니다.
- (발음 기호에 `a i`가 포함되어 있지만 노래중인 음원에겐 `a i`가 없을 때, 음소화기가 자동으로 `a i`대신 `i`를 붙여줍니다. 반대도 성립합니다.)
![image](https://github.com/stakira/OpenUtau/assets/100339835/8fae60c4-f677-4d36-b0b0-729cfa2b510d) <br>

4. Supports two special phoneme symbols about phoneme variation, `!` and `.`. <br>
음운변동을 조정하는 고유 발음기호 `!`와 `.`를 지원합니다. <br>

- `!`(Ex: !가) : Ignores all phoneme variation regarding current note. Previour and next note will be not affected by current note which starts with `!`.
- `!`(Ex: !가) : 현 노트와 연관된 모든 음운변동을 무시합니다. 현 노트는 이웃 노트들의 음운변동에서도 배제됩니다.

![image](https://github.com/stakira/OpenUtau/assets/100339835/ed42c984-5a9d-40fc-a951-304d11d75b73) <br>

- `.`(Ex: 가.) : Regard current note as *end of word*, and applies different phoneme variation rule.
- `.`(Ex: 가.) : 현 노트에서 *단어가 끝난 것*으로 간주하고, 음운 변동을 알맞게 바꾸어 적용합니다.

![image](https://github.com/stakira/OpenUtau/assets/100339835/2cce0c35-ff0e-4f86-8a16-4453ccd73514) <br>

### KO CV (Korean CV)
![image](https://github.com/stakira/OpenUtau/assets/100339835/8e94a40f-1287-4736-83f0-b1c435944e65)

#### Ko-CV.ini
```
[CV]
Use rentan=False 
Use 'shi' for '시'(otherwise 'si')=False
Use 'i' for '의'(otherwise 'eui')=False

[BATCHIM]
Use 'aX' instead of 'a X'=False
```
- Config file, to handle *various form of Korean CV voicebanks*.
- If singer doesn't have `Ko-CV.ini`, it automatically generates file with default one. 
- *형태가 다양한 한국어 단독음 음원*을 모두 다루기 위한 설정 파일입니다. 
- 음원이 `Ko-CV.ini`를 보유하고 있지 않을 경우, 자동으로 파일이 생성됩니다. <br> <br>

##### How to Use (가이드)
- **Use rentan**: handles singer which is RENTAN. <br> 
> Uses `- <CV>`(example: - ka) when *True*, otherwise not(example: ka). <br>
> If `- <CV>` not exists when *True*, uses `<CV>` instead. 
- **Use 'shi' for '시'(otherwise 'si')** : handles phoneme of `시`
> Uses `shi` for input character `시` when *True*, otherwise not.(uses `si` for input character `시`). 
- **Use 'i' for '의'(otherwise 'eui')** : handles phoneme of `의`
> Uses `i` instead of  for vowel `ㅢ` when *True*, otherwise not.(uses `eui` for vowel `ㅢ`). <br>
> If `eui` not exists when *False*, uses `i` instead.
- **Use 'aX' instead of 'a X'** : handles Batchim phoneme's format.
> Uses `<vowel><batchim>`(example: ang) when *True*, otherwise not.(uses `<vowel> <batchim>`(example: a ng)
<br>  

- **Use rentan** : 연단음 음원 여부. 
> *True*이면`- <CV>`(예: - ka)사용, *False*이면 `<CV>`(예: ka)사용. <br>
> 설정값이 *True*더라도, 음원이 `- <CV>`를 미보유했다면 상응하는 `<CV>`를 사용합니다.
- **Use 'shi' for '시'(otherwise 'si')** : `시`의 발음기호 결정.
> *True*이면 `시`에 `shi`를 사용, *False*이면 `시`에 `si`를 사용. <br> 
- **Use 'i' for '의'(otherwise 'eui')** : `ㅢ`의 발음기호 결정.
>  *True*이면 `ㅢ`에 `i` 사용, *False*이면 `ㅢ`에 `eui` 사용. <br>
> 설정값이 *False*더라도, 음원이 `eui`를 미보유했다면 상응하는 `i`를 사용합니다.
- **Use 'aX' instead of 'a X'** : 
> *True*이면 받침 음소에 `<모음><받침>`(예: ang) 사용, *False*면 받침 음소에 `<vowel> <batchim>`(example: a ng)사용
### KO CBNN (Korean CBNN)
![image](https://github.com/stakira/OpenUtau/assets/100339835/86a9b181-7e59-4be4-8da7-45f9bc7c0238)


## PT-BR CVC (Brazilian Portuguese CVC)
Made with [BRAPA](https://github.com/Team-BRAPA/BRAPA) conotation, this phonemizer uses a built-in G2P Dictionary. The main accent is the `Neutral`

### Uses
1. Portuguese Words (eg. `leite`)  
![ptbr cvc with dictionary - ptbr words](https://i.imgur.com/nMqi6Ai.png)  
2. Portuguese Words + phonetic hint (eg. `leite[l e y t e]`)  
![ptbr cvc with dictionary - ptbr words + phonetic hint](https://i.imgur.com/dHOMSPf.png)  
3. Phonetic hint only (eg. `[l e y t e]`)  
![ptbr cvc with dictionary - only phonetic hint](https://i.imgur.com/d4K5kaY.png)  

### Common Feature
With or without a dictionary, you can use the features listed below:

1. Separate words or phonemes by syllable using `+`.  
![ptbr cvc - separating syllables](https://i.imgur.com/Jr3CwY5.png)  
2. Extend a syllable or phonemes using `+*` or `+~`.  
![ptbr cvc - extending syllables](https://i.imgur.com/WS6aCM5.png)  
3. Using a single phoneme with `?`.  
Obs. If exists a linked note behind that finishes with `V-`, `VC-` or `VC` + `C-`, this function removes those samples in order to cross fade with previous `V` or `CV`.  
![ptbr cvc - ? function](https://i.imgur.com/iYtHmlz.png)  

### Special Feature
1. Support to VV and _V  
Even tho CVC don't have vowel connections by default, the phonemizer supports it for extras. The priority is `VV` -> `_V` -> `V`  
![ptbr cvc - vv connections](https://i.imgur.com/4sehINo.png)  
2. rh CV connection  
`rh` is a rhotic vowel only found in front of a vowel or in between a vowel and a consonant. If somehow, during the usage, they are found in between vowels, the phoneme `r` will show up to make a connection, since it's their natural approximant. Like the example: `par a par`  
![ptbr cvc - rh connection](https://i.imgur.com/vSmKcs1.png)  

## EN to JA (English to Japanese)
This phonemizer converts English lyrics to phonemes for Japanese voicebanks. It will automatically adapt to CV, VCV, and CVVC voicebanks.

Standard input  
![en to ja standard](https://i.imgur.com/EqCxHM5.png)

Phonetic input  
![en to ja phonetic](https://i.imgur.com/5jAAJ9N.png)

Consonants: `b by ch d dh f g gy h hy j k ky l ly m my n ny ng p py r ry s sh t th v w y z zh`  
Vowels: `a i u e o ay ey oy ow aw`

Forced input  
Prefix the lyric with `?` to use a specific alias from the voicebank.  
![en to ja forced](https://i.imgur.com/676moY0.png)

Use `+` to extend multisyllable words across multiple notes.  
![en to ja extend](https://i.imgur.com/hFkEWut.png)

Use `+*` or `+~` to extend the previous syllable instead of going to the next syllable  
![en to ja extend special](https://i.imgur.com/jzbSJQJ.png)

Example with VCV voicebank  
![en to ja vcv](https://i.imgur.com/k1hqCdR.png)

Example with CVVC voicebank  
![en to ja cvvc](https://i.imgur.com/SfLHlle.png)

Example with VCV+CVVC voicebank  
![en to ja vcv cvvc](https://i.imgur.com/rVorLTO.png)  
When both VCV and CVVC phonemes are available, CVVC is prioritized.

If the voicebank has no VC phonemes, it is recommended to edit the timing of the final consonant to remove the vowel sound.  
![en to ja final consonant](https://i.imgur.com/qSAMRht.png)

## FR CVVC (French CVVC+)

This phonemizer is compatible with [Fraloids](https://fraloids.wixsite.com/collection) UTAUs, [Petit Mot](https://simelomad.wixsite.com/crabkids/copie-de-gros-mot) & [Gros Mot](https://simelomad.wixsite.com/crabkids/about-new), it can support basic CVVC, CVVC+ and VCV-VC. For more information on compatible UTAUs, tutorials and help with French UTAUs you can go [here](https://frenchutauhelp.carrd.co/).

### Setup
It works with a [dictionary](https://github.com/mmemim/OpenUTAU-French-Dictionary) (version 1.2 and higher) available [here](https://github.com/mmemim/OpenUTAU-French-Dictionary). For the phonemizer to work, you need to download `cmudict-fr.txt` and put it in your `Dictionaries` folder. If there's no Dictionaries folder, create one at the root of your OpenUtau install folder.

![dictionary goes in the dictionaries folder at the root](https://i.imgur.com/szewSA7.png)

There is also a [sample package](https://drive.google.com/file/d/1FpZTf2FOjWz-BjpWcGZEha-ZBhanEyDj/view?usp=sharing) available with a ustx that showcases the basic rules of the dictionary as well as ustx with French lyrics.

### Lyric input & lyrics helper input
You can input lyrics, phonetic hints `[]` or force input with `?` (note that force input will break the phonemizer transitions). Phonetic hints will need to be input in Mot or Fraloid aliasing depending on the aliasing the voicebank is using.
Use `+` to break words into syllables and `+~` or `+*` to extend a syllable.

![fr cvvc lyric input vs phonetic input vs force input](https://i.imgur.com/qaPUUNH.png)

Sentences with apostrophes like "j'aime" or "j't'aime" need to be input `j' aime` and `j' t' aime`. You can also input "est-ce" as `est -ce`. Please note the **space** between the two words. 

Some common word combinations such as `j'ai` or `qu'elle` have been added for easier input, though you should always default to `C' + word`.

![fr cvvc handling of apostrophes](https://i.imgur.com/y1ovzSm.png)


Since French has a lot of silent sounds, you will sometimes need a second or third form of the word depending on the context (silent "e", liaison...). Usually, `word` is the basic form, `word(2)` adds the silent "e", `word(3)` adds the liaison **&** silent "e" and `word(4)` adds the liaison but no silent "e". 

However, there may be exceptions to this rule. 

![fr cvvc alternative forms](https://i.imgur.com/9dqeGbs.jpg)

_If this doesn't work as intended, please ensure that your dictionary is **version 1.2 or higher**. Version number should be written at the start of the .txt._

If you encounter a **"word not found"** error, you can use the French G2p Lyrics Helper. To use it, go to **Tools > Preferences > Advanced **and choose **FrenchG2pLyricsHelper**. You can now use it to input unknown words in the dictionary.

![french lyrics helper](https://i.imgur.com/alQCc4N.png)

### Additional support
The phonemizer can also read hiragana (with approximate French sounds).

![hiragana support](https://i.imgur.com/52cjlcf.png)

With the phonetic hint, you can input additional sounds that are voicebank-specific. In this example you can see glottal stops `.` & long end breaths `R`, but you could also use additional consonants or vowels (like English `h` or Japanese `4`...)

![additionalsounds](https://i.imgur.com/OuZ8t5c.png)

### Resources
These rules are showcased in more detail in the PhonemizerInputHelp.ustx, available in the [sample package](https://drive.google.com/file/d/1FpZTf2FOjWz-BjpWcGZEha-ZBhanEyDj/view?usp=sharing). 

For more information on compatible UTAUs, tutorials and help with French UTAUs you can go [here](https://frenchutauhelp.carrd.co/).

## ES SYL (Spanish Syllable-Based Phonemizer)
### Setup
While this phonemizer uses Teren000's Spanish CVVC list as a base, it's intended to support many different methods, including VCV (with some caveats; more on that below).

Downloading a separate dictionary is no longer necessary. Instead, it now uses the in-built Spanish G2P. As a result, it can now read words that are not in the dictionary.

### Lyric input
With the help of the dictionary linked above, you can write Spanish words directly on the first note:

![Dictionary input with extender notes](https://i.ibb.co/4JZZ9ZR/Dictionary-input.png)
As seen in the above image, you can extend the word over multiple notes by typing a ``+`` on the next notes (otherwise, all syllables will be on the same note).

If you want to extend only a specific syllable in a word, you can do that by typing either ``+*`` or ``+~`` on the next note(s):

![Syllable extender note example](https://i.ibb.co/rFkZYnX/Syllable-extender-note.png)

### Phonetic input
You can also input lyrics phonetically, this can be done on separate notes as well. Note to write the phonemes in brackets (``[]``), separated with spaces, otherwise they won't be recognized:

![Phonetic input in brackets, on separate notes, with spaces in-between](https://i.ibb.co/FXkkKvx/Phonetic-input.png)

There's also the option to input phonetic suggestions after the lyrical input, in brackets after the lyric (this has to be done on the first syllable):

![Lyric input with phonetic suggestion in brackets](https://i.ibb.co/3rMjBMt/Phonetic-suggestion.png)

#### Phoneme list
Consonants: b, ch, d, **dz**, f, g, h, **hh**, j, k, l, ll, m, n, nh, p, r, rr, s, **sh**, t, **ts**, w, y, z, **zz**, **zh**

Vowels: a, e, i, o, u

The bolded letters are sounds that don't natively occur in Spanish and only work through phonetic input. Please also note that the phonemizer by default uses ``j`` for ``ll`` (and ``h`` for ``j/gi/ge``).

Sounds not listed above, but that are present in the voicebank, can still be used through phonetic input, eg. ``x`` or ``ah``.

### Alternate aliases
Does your voicebank use ``bia`` instead of ``bya`` and/or ``bua`` instead of ``bwa`` etc.? (Replace ``b`` with any consonant.) No problem, the phonemizer applies the correct spelling automatically:

![Using "W" (default behavior)](https://i.ibb.co/ZmpRRdY/Buena-with-W-default.png)
![Using "U" (alternative method)](https://i.ibb.co/gZ82Px8/Buena-with-U-alternate.png)

Alternatively, if your voicebank doesn't have ``z``, it will use ``s`` instead (known as "seseo" in Spanish). This is useful for voicebanks with Latin-American-based pronunciation:

!["Seseo" for when no "z" is present](https://i.ibb.co/4mm8Swk/Seseo.png)

Similarly, many (if not most) Spanish voicebanks use ``ny`` for ``ñ``, so this will be applied automatically as well if the voicebank doesn't have ``nh`` (which is the default):

![Default usage: "nh"](https://i.ibb.co/sjRpcZ4/Default-nh-usage.png)
![Alternate usage: "nh"](https://i.ibb.co/4JZZ9ZR/Dictionary-input.png)

If you need to insert a consonant in a cluster that doesn't exist in the voicebank as a CC transition (usually an ``s``), it will insert it by itself as a standalone consonant:

![Loose consonant insertion (with CC)](https://i.ibb.co/9WpWpqW/Consonant-insertion-2.png)
![Loose consonant insertion (no CC)](https://i.ibb.co/hKZBQNd/Consonant-insertion-1.png)

**IMPORTANT:** Please note that the vowel fallback function has been removed, as it was causing issues. As a result, _please_ make sure to amend the oto to include a loose consonant if a CC transition does not exist. Apologies for the inconvenience!

### Important notes on VCV
Currently, the phonemizer does not support automatic "syllable splitting" with semivowels. This is common with Spanish VCV banks, but also occurs sometimes with other methods. This function is planned however, so please stay tuned!

For now though, you can alleviate it with a phonetic suggestion (in this case, you need to treat the semivowel as a separate "full" vowel, so make sure to insert a ``+`` (_not_ ``+~/+*``! ) to split the notes):

![Phonetic suggestion alternative for semivowels](https://i.ibb.co/RzJzTzF/Glide-alternative.png)

### Consonant length adjustment
This likely won't be a problem with full VCV banks due to the oto, but it can be a problem with CVVC (even when it has some VCV support). In this case, sometimes a syllable ending VC can come off as a little short (this is somewhat accounted for in the phonemizer, but there's a limit to that without ruining other functions). It's recommended to lengthen the VC in that case, which you can do by stretching the phoneme in question (the exact part is highlighted in the image):

![Short VC before stretching](https://i.ibb.co/Bc1HqxJ/VC-stretch-before.png)

Afterward, it should look something like this:

![Longer VC after stretching](https://i.ibb.co/ZxsbkWg/VC-stretch-after.png)

The exact length is difficult to predict, so you're suggested to do it by ear until the point you think it sounds good.

## ES VCCV (Spanish VCCV Phonemizer)
### Setup
This phonemizer was based on the nJokis VCCV method.

Downloading a separate dictionary is no longer necessary. Instead, it now uses the in-built Spanish G2P. As a result, it can now read words that are not in the dictionary.

### Lyric input
With the help of the dictionary linked above, you can write Spanish words directly on the first note:

![Dictionary input with extender notes](https://i.ibb.co/MsXBZSh/Example1.png)

As seen in the above image, you can extend the word over multiple notes by typing a ``+`` on the next notes (otherwise, all syllables will be on the same note).

If you want to extend only a specific syllable in a word, you can do that by typing either ``+*`` or ``+~`` on the next note(s):

![Syllable extender note example](https://i.ibb.co/s3zBHJK/Example2.png)

### Phonetic input
You can also input lyrics phonetically, this can be done on separate notes as well. Note to write the phonemes in brackets (``[]``), separated with spaces, otherwise they won't be recognized:

![Phonetic input in brackets, on separate notes, with spaces in-between](https://i.ibb.co/712NKKG/Example3.png)

There's also the option to input phonetic suggestions after the lyrical input, in brackets after the lyric (this has to be done on the first syllable):

![Lyric input with phonetic suggestion in brackets](https://i.ibb.co/Tk34tx6/Example4.png)

#### Phoneme list
Consonants: b, B, ch, d, D, E, f, g, G, h, I, jj, k, l, L, m, n, nJ, p, r, rr, s, sh, t, U, w, x, y, z

Vowels: a, e, i, o, u, **BB** ,**DD** ,**ff** ,**GG** ,**ll** ,**mm** ,**nn** ,**rrr** ,**ss** ,**xx**

The bolded vowels aren't actual vowels (rather syllabic consonants), but are treated as such by the phonemizer. They only work through phonetic input.

Note that you can add any type of extra consonants (but not vowels) to your bank that aren't listed, since the phonemizer will automatically recognize it. Though, like above, they will only work through phonetic input.

### Alternate aliases
This phonemizer uses phonetic substitutes for when a consonant sound isn't present, this is achived through ``ValidateAlias()``.

For example, if your voicebank doesn't have ``z``, it will use ``s`` instead (known as "seseo" in Spanish). This is useful for voicebanks with Latin-American-based pronunciation:

!["Seseo" for when no "z" is present](https://i.ibb.co/89V9nRS/Example5.png)

Similarly, ``h`` is a substitute for ``x``, while ``sh`` and ``L`` are substitutes for "jj".

Note that Latin-American-style aspirated endings (where ``h`` is used in place of ``s`` at the end of syllables) can only be achieved through phonetic input, since it's technically an informal style of pronunciation.

### Auxiliary dictionary files (uses njokis.yaml):
**`Note: only 1:1 replacements are supported for now and multiple phoneme replacements are still pending in `**[**pr 1534**](https://github.com/stakira/OpenUtau/pull/1534)

- #### Symbols
    - Add a new symbol and define its symbol type for the phonemizer to recognize.
    - encapsulate the whole symbol with `' '` if it starts with a special symbol
```
symbols:
    - {symbol: ea, type: vowel}
    - {symbol: ix, type: vowel}
    - {symbol: dd, type: tap}
    - {symbol: j, type: fricative}
    - {symbol: '@r', type: vowel}
```
- #### Replacements
    - Replaces certain symbol or sequence of symbols defined in the replacements entry
    - supports `1:1`, `1:M`, `M:1`, `M:M` phoneme replacements
```
replacements:
# 1:1 (one-to-one mappings)
  - {from: ax, to: ah}
  - {from: cl, to: q}
# 1:M (one-to-many mappings) (splitting)
  - {from: dr, to: [d, r]}
  - {from: tr, to: [t, sh, r]}
  - {from: aw, to: [aa, w]}
# M:1 (many-to-one mappings) (merging)
  - {from: [ih, ng], to: ing}
  - {from: [eh, ax, m], to: eam}
# M:M (many-to-many mappings)
  - {from: [ih, ng], to: [ix, ng]}
  - {from: [ay, l], to: [ay, ax, el]}

# format can be like this
    - from: [ae, n]
      to: [eh, ax, n]
    - from: b
      to: bh
```
- #### Entries
    - Add a new dictionary entry to override certain word pronunciations
    - no limit to characters as long as it covered by unicode so you can add kana, hangul, hieroglyphics grapheme etc entries to `arpasing.yaml`
```
entries:
    - {grapheme: hello, phonemes: [hh, ax, l, ow]}
    - {grapheme: 안녕하세요, phonemes: [aa, n, y, ao, ng, hh, ah, s, eh, y ao]}
# format can be like this
    - grapheme: stars
      phonemes: s, t, aa, r, z
    - grapheme: drops
      phonemes: dr, aa, p, s
```

## ES MAKKU (Spanish Makkusan-style Phonemizer)
### Setup
This phonemizer was created to be used with Italian voicebanks using Makkusan's reclist, as long as it contains extra sounds for Spanish. It works similarly to the Italian Syllable-Based phonemizer.

Downloading a separate dictionary is no longer necessary. Instead, it now uses the in-built Spanish G2P. As a result, it can now read words that are not in the dictionary.

### Lyric input
With the help of the dictionary linked above, you can write Spanish words directly on the first note:

![Dictionary input with extender notes](https://i.ibb.co/P5pgbnh/Example1.png)

As seen in the above image, you can extend the word over multiple notes by typing a ``+`` on the next notes (otherwise, all syllables will be on the same note).

If you want to extend only a specific syllable in a word, you can do that by typing either ``+*`` or ``+~`` on the next note(s):

![Syllable extender note example](https://i.ibb.co/KmGBK4S/Example2.png)

### Phonetic input
You can also input lyrics phonetically, this can be done on separate notes as well. Note to write the phonemes in brackets (``[]``), separated with spaces, otherwise they won't be recognized:

![Phonetic input in brackets, on separate notes, with spaces in-between](https://i.ibb.co/b3mZPf8/Example3.png)

There's also the option to input phonetic suggestions after the lyrical input, in brackets after the lyric (this has to be done on the first syllable):

![Lyric input with phonetic suggestion in brackets](https://i.ibb.co/5nqNGBk/Example4.png)

#### Phoneme list
Consonants: b, d, **dz**, **dZ**, f, g, gn, **j**, k, l, m, **M**, n, **N**, p, r, rr, s, **S**, t, **ts**, tS, **v**, w, y, **z**, B, D, G, h, T, x, Y, ' (apostrophe for vocal fry)

Vowels: a, e, i, o, u, **3**, **0**

The bolded sounds are sounds that occur in Italian and only work through phonetic input in this phonemizer. Some of these can possibly occur in specific Spanish dialects.

### Alternate aliases

This phonemizer uses phonetic substitutes for when a consonant sound isn't present, this is achived through ``ValidateAlias()``.

For example, if your voicebank doesn't have ``T``, it will use ``s`` instead (known as "seseo" in Spanish). This is useful for voicebanks oriented towards a more Latin-American-based pronunciation.

Similarly, ``h`` is a substitute for ``x``, while ``y`` is a substitute for ``Y``.

Another example occurs between voiced stops and their intervocalic fricative counterparts: ``b`` for ``B``, ``d`` for ``D``, and ``g`` for ``G``.

## EN VCCV (Cz's English VCCV phonemizer) 

This is a temporary solution of a phonemizer for [Cz's VCCV method](http://utaulanguageresources.weebly.com/czs-vccv.html), it is right now not a plug and play solution. If you wish for one, please use [Lyric Parser 2.1](https://snowphones.weebly.com/lyric-parser-20.html) which is fully compatible with Open Utau.

- `Note that the new version of the [envccv.yaml] will be created in OU version 0.1.566, the old yaml file will be renamed as [envccv_backup.yaml]`

### Lyric input
You can input lyrics in plain English `love`, plain English + phonetic hint `love [l u v]` or phonetic hint only `[l u v]`. 

![vccv_phonemeinput](https://user-images.githubusercontent.com/35538523/168469343-1519dbe9-b85f-4807-9d08-daf7d2aadb17.png)

You can then use `+` to break words into syllables, and `+*`or `+~` to extend a sound.

Use the pink line to stretch or shorten a sound so that the pronunciation is good. You can also switch sounds by double clicking on the box below to change the alias, so that you can switch between `V C`, `VC` or `VC-` as you please.

![vccv_phonemetweak](https://user-images.githubusercontent.com/35538523/168469015-823cf9fc-bd5a-4c0a-ac43-d9736caa4d40.png)

### Custom dictionary
Since the phonemizer uses an arpabet dictionary there may be conflicts with some sounds. If there are missing sounds, you can double click on the box below to change the sound used. However, you can now download a converted version of snowphones' Lyric Parser dictionary [here](https://github.com/mmemim/OU-EN-VCCV-Custom-Dictionary) and put it in `OpenUtau/Plugins`.

If there are any other issue, don't hesitate to share them on the Discord.

### Auxiliary dictionary files (uses envccv.yaml):
**`Note: only 1:1 replacements are supported for now and multiple phoneme replacements are still pending in `**[**pr 1534**](https://github.com/stakira/OpenUtau/pull/1534)

- #### Symbols
    - Add a new symbol and define its symbol type for the phonemizer to recognize.
    - encapsulate the whole symbol with `' '` if it starts with a special symbol
```
symbols:
    - {symbol: ea, type: vowel}
    - {symbol: ix, type: vowel}
    - {symbol: dd, type: tap}
    - {symbol: j, type: fricative}
    - {symbol: '@r', type: vowel}
```
- #### Replacements
    - Replaces certain symbol or sequence of symbols defined in the replacements entry
    - supports `1:1`, `1:M`, `M:1`, `M:M` phoneme replacements
```
replacements:
# 1:1 (one-to-one mappings)
  - {from: ax, to: ah}
  - {from: cl, to: q}
# 1:M (one-to-many mappings) (splitting)
  - {from: dr, to: [d, r]}
  - {from: tr, to: [t, sh, r]}
  - {from: aw, to: [aa, w]}
# M:1 (many-to-one mappings) (merging)
  - {from: [ih, ng], to: ing}
  - {from: [eh, ax, m], to: eam}
# M:M (many-to-many mappings)
  - {from: [ih, ng], to: [ix, ng]}
  - {from: [ay, l], to: [ay, ax, el]}

# format can be like this
    - from: [ae, n]
      to: [eh, ax, n]
    - from: b
      to: bh
```
- #### Entries
    - Add a new dictionary entry to override certain word pronunciations
    - no limit to characters as long as it covered by unicode so you can add kana, hangul, hieroglyphics grapheme etc entries to `arpasing.yaml`
```
entries:
    - {grapheme: hello, phonemes: [hh, ax, l, ow]}
    - {grapheme: 안녕하세요, phonemes: [aa, n, y, ao, ng, hh, ah, s, eh, y ao]}
# format can be like this
    - grapheme: stars
      phonemes: s, t, aa, r, z
    - grapheme: drops
      phonemes: dr, aa, p, s
```

## ES to JA (Spanish to Japanese Phonemizer)
### Setup
This phonemizer lets you make Japanese voicebanks sing in Spanish. It works similarly to the EN to JA Phonemizer, sharing many of its functions.

This phonemizer uses the same dictionary as the Spanish Syllable-Based Phonemizer, which you can download [here](https://github.com/lottev1991/OpenUTAU-Spanish-Dictionary). This dictionary should go into OpenUtau's ``Dictionaries`` folder; if it doesn't exist, make it. (If a word is missing in the dictionary, or a transcription is incorrect, feel free to push merge requests on the dictionary repo. I am more than willing to expand the word list and correct errors.)

### Lyric input
Just like in the ES SYL phonemizer, you type in a Spanish word on the first note of the word. This phonemizer will then use Japanese sounds to create the closest match to Spanish sounds. It will use CV, VCV and/or CVVC combinations, depending on what's in the voicebank:

#### CV:
![CV example](https://i.ibb.co/Vt9kpjJ/Espa-ol-CV.png)

#### CVVC:
![CVVC example](https://i.ibb.co/59Frh5p/Espa-ol-CVVC.png)

#### VCV:
![VCV example](https://i.ibb.co/4ZmHLYh/Espa-ol-VCV.png)

### Phonetic input
You can also input lyrics phonetically, this can be done on separate notes as well. Note to write the phonemes in brackets (``[]``), separated with spaces, otherwise they won't be recognized:

![Phonetic input in brackets, on separate notes, with spaces in-between](https://i.ibb.co/rG5q3vX/Espa-ol-Phonetic.png)

There's also the option to input phonetic suggestions after the lyrical input, in brackets after the lyric (this has to be done on the first syllable):

![Lyric input with phonetic suggestion in brackets](https://i.ibb.co/TKj3DH7/Espa-ol-Phonetic-After-Lyric.png)

As you can see above, you can type "+" on the successive notes in order to spread the syllables over several notes, instead of just the first one.

If you want to extend only a specific syllable in a word, you can do that by typing either ``+*`` or ``+~`` on the next note(s):

![Syllable extender note example](https://i.ibb.co/bsy0dc1/Vowel-Extension.png)

#### Phoneme list
Consonants: b, B, ch, d, D, f, g, G, h, **hh**, j, k, l, m, n, ny, p, r, rr, s, t, w, y, z

Vowels: a, e, i, o, u

The "hh"-sound here is used for end breaths and gets mapped to "息". It only works through phonetic input.

This phonemizer also doesn't use "nh" for "ñ", instead it always uses "ny".

Please also note that this phonemizer **always uses seseo**, even when you do type a phonetic "z". This is because the Japanese "z" is very different from the Spanish "z":

![Example of consistent seseo usage](https://i.ibb.co/dpRv97s/Always-Seseo.png)

If you _really_ wish to use the Japanese "z" for your Spanish (which is usually **not recommended** unless the voicebank in question already has an Iberian Spanish accent), you can double-click on the note in question in the bottom bar to override the alias:

![Override Alias text box, before applying](https://i.ibb.co/KNdC6Wj/Override-Alias-Before.png)
![After applying Override Alias](https://i.ibb.co/hD1qWw7/Override-Alias-After.png)

You can also do this for other sounds, for instance when you want to use an "l" in the voicebank (the phonemizer defaults to "r" for "l", even with phonetic input).

### Rolled "r"
As we all know, Spanish has a rolled "r"-sound, also known as the "double r". This sound does not appear by default in most Japanese voicebanks (although it does sometimes appear in Japanese speech and occasionally singing). This phonemizer substitutes it with several consecutive "r" notes containing the same initial (semi-)vowel as the main note:

![Rolled "r" with "full" vowel](https://i.ibb.co/7SFxVbG/RolledR1.png)

![Rolled "r" with semivowel](https://i.ibb.co/ww0mDsw/RolledR2.png)

Keep in mind that depending on the accent of the voicebank, the rolled "r" could possibly sound a bit odd. This sadly isn't something that the phonemizer can fix.

### Consonant length adjustment
Sometimes, it just so happens that an ending consonant is too long or too short. In that case, you can adjust the length manually by dragging the note at the bottom bar (the exact part is highlighted in the images):

#### Lengthening:
![Lengthening a consonant](https://i.ibb.co/j5YD4jL/Consonant-Lengthening.png)

#### Shortening:
![Shortening a consonant](https://i.ibb.co/4VzxgfX/Consonant-Shortening.png)

The exact length is difficult to predict, so you're suggested to do it by ear until the point you think it sounds good.
## Vietnamese CVVC/VCV Phonemizer
* Support marking in Vietnamese
* Extensions include: <br>
R : exhale at the end of the note <br>
breath : take a breath
1. **Vietnamese CVVC Phonemizer**
![](https://drive.google.com/u/0/uc?id=17PiS964StogOMIXV_8YFCMuUdGJWKPIj&export=download)
2. **Vietnamese VCV Phonemizer**
![](https://drive.google.com/u/0/uc?id=1JT4aPsaaeIPKnXP2P2dVKRdj3Xps38YN&export=download)

## EN X-SAMPA (English X-SAMPA phonemizer)
Compatible reclists
- [Delta-style English Lists](https://tl.tubs.wtf/2020/11/09/delta-eng)
- [Salem-Style English CVVC](https://wastelandutau.neocities.org/en/overview)
- [GrayGlish](https://assbackwardsp.wixsite.com/utaubackwards/reclists)
- More to be added

**NOTE:** This phonemizer used to be called the "English Delta Phonemizer", but as the scope of the phonemizer has increased, it has been renamed to the more general "English X-SAMPA phonemizer".
### Setup
This phonemizer is pretty similar to the Teto English phonemizer. However, there are a few important differences:
- This phonemizer was made to support X-SAMPA-encoded English banks in general, not just Delta banks (and not only Kasane Teto, although her English bank is supported). Some examples are:
  - Split diphthongs, when applicable (this is a known feature of some Delta reclists);
  - Some alternate aliasing methods, outside of the Delta scope (e.g. English Vocaloid-style X-SAMPA);
  - Aliasing fallbacks, in case a voicebank merges some vowels;
  - Support for spaced CV's (similar to Arpasing/diphonic voicebanks), as in ``[C V]``;
- This phonemizer accepts VCV for all consonants (including clusters), if the voicebank contains them;
- This phonemizer has support for some extra sounds that aren't in the dictionary by default, but should be supported through custom dictionaries and/or phonetic hints.

### Lyric input
You write the word on the first note, then spread the syllables by writing a ``+`` on the next notes:

![Lyrics showcase example with syllable extender notes](https://i.ibb.co/K28FqLC/Example.png)

If you only want to extend one syllable in the word, you can use either ``+*`` or ``+~``:

![Showcasing syllable extender notes](https://i.ibb.co/LPxnnGK/Example2.png)

### Phonetic input
You can also use phonetic hints after lyrics, you put those in between brackets (``[]``) with spaces in-between. This is handy when certain phonemes aren't quite right, or for pure stylistic reasons. You write the hint on the first note of the word:

![Showcasing phonetic hints](https://i.ibb.co/6P5wvFD/Example3.png)

You can also opt for pure phonetic input instead, it works the same as above except not right after a lyric:

![Showcasing pure phonetic input](https://i.ibb.co/mGPL9g2/Example4.png)

### Split diphthongs and affricates

This phonemizer now supports automatic splitting of Diphthongs and affricates, depending on the voicebank:

![Automatic affricate splitting](https://i.ibb.co/QJ5CnHF/Affricate-Splitting.png)

**Note:** This phonemizer used to have an issue where the second half of a split diphthong had to be treated as if it were a different syllable. However, this problem has since been resolved and this method is no longer necessary, splitting them within the same syllable instead:

![The phonemizer now splits diphthongs within the same syllable](https://i.ibb.co/DMcGKvx/Correct-Diphthong-Splitting.png)

If you only want to extend one syllable in the word, you can use either ``+*`` or ``+~``:

![Syllable extender notes](https://i.ibb.co/bd4w5NV/Lightning2.png)

#### Phoneme list
Consonants: b, d, f, g, h, j, k, l, m, n, p, r, s, t, v, w, z, 4, D, N, S, T, Z, dZ, tS, ・, _

Vowels: a, A, @, {, V, O, aU, aI, E, 3, eI, I, i, oU, OI, U, u, Q, Ol, Ql, aUn, e@, eN, IN, e, o, Ar, Qr, Er, Ir, Or, Ur, ir, ur, aIr, aUr, A@, Q@, E@, I@, O@, U@, i@, u@, aI@, aU@, @r, @l, @m, @n, @N, 1, e@m, e@n, y, I\\, M, U\\, Y, @\\, @\`\, 3\`\, A\`\, Q\`\, E\`\, I\`\, O\`\, U\`\, i\`\, u\`\, aI\`\, aU\`\, }, 2, 3\, 6, 7, 8, 9, &, {\~\, I\~\, aU\~\, VI, VU, @U, i:, u:, O:, e@0, E\~\, e\~\, 3r, ar, or, {l, Al, al, El, Il, il, ul, Ul, mm, nn, ll, NN

Among the phonemes are:
- General X-SAMPA vowels. You can find more information about X-SAMPA [here](https://en.wikipedia.org/wiki/X-SAMPA);
- Sounds used by the UTAU [Peiton](https://www.supergoodboi.com/peiton.html/)'s English voicebank, as well any other voicebanks that might use that list. By default, they only work through phonetic input, unless a custom dictionary is created;
- Sounds used in Salem's S-CVVC English reclist;
- English Vocaloid-style sounds (including extra sounds found in Vocaloid 4 onward);
- Canadian raising;
- Alternate ways for rhoticization and nasalization.

These extra sounds mostly only work either through phonetic input, or a custom dictionary. However, some automatically work through ``ValidateAlias()`` and associated booleans.

#### Custom dictionary
This phonemizer now has support for custom dictionaries. The dictionary should be named either `en-xsampa.yaml` or `xsampa.yaml` (the latter for legacy support/backwards compatibility with existing voicebanks) and be put in the main/top folder of a specific voicebank. For an idea on what a custom dictionary should look like, you can look at the `arpasing.yaml` file that comes with OpenUtau by default.

**!!IMPORTANT NOTE!!:** Certain X-SAMPA symbols should be contained within single quotes ('') when included in the custom dictionary file, otherwise your dictionary will not load. Some of the affected phonemes are:

* `{` and any phoneme that contains it;
* `}` and any phoneme that contains it;
* `@` and any phoneme starting with it (but not when at the end/center), ex. `@l` (but not `e@`);
* `&` and any phoneme that contains it;
* Any phoneme containing a colon (`:`);
* Any phoneme containing a slash (`\` or `/`);
* Some other, non-English/non-default X-SAMPA symbols might also be affected. It is highly recommended to test which specific ones beforehand.

Note that the Arpabet symbols included by default in the CMU Pronouncing Dictionary can also be used to note down custom words, though for any symbols that aren't included, X-SAMPA notation is required.

### Auxiliary dictionary files:
- #### Symbols
    - Add a new symbol and define its symbol type for the phonemizer to recognize (`vowel`, `stop`, `affricate`, `fricative`, `aspirate`, `liquid`, `nasal`, `semivowel`, `tail`).
    - `affricate`'s are prioritized because they produce a sound.
    - indicate the phoneme as `tail` to use them as a trailing tail note.
    - encapsulate the whole symbol with `' '` if it starts with a special symbol.
    ```
    symbols:
      - {symbol: ea, type: vowel}
      - {symbol: ix, type: vowel}
      - {symbol: dd, type: tap}
      - {symbol: j, type: fricative}
      - {symbol: '@r', type: vowel}
    ```
- #### Fallbacks
    - Fallbacks missing phoneme/alias to the mapped phoneme/alias.
    - supports `1:1` phoneme mappings only.
    ```
    fallbacks:
    # 1:1 (one-to-one mappings)
      - {from: a, to: A}
      - {from: ts, to: ch}

    # format can be like this
        - from: b@
        to: bV
        - from: b
        to: bh
    ```
- #### Replacements
    - Replaces certain phoneme or sequence of phonemes defined in the replacements entry.
    - supports `1:1`, `1:M`, `M:1`, `M:M` phoneme replacements.
    ```
    replacements:
    # 1:1 (one-to-one mappings)
      - {from: ax, to: ah}
      - {from: cl, to: q}
    # 1:M (one-to-many mappings) (splitting)
      - {from: dr, to: [d, r]}
      - {from: tr, to: [t, sh, r]}
      - {from: aw, to: [aa, w]}
    # M:1 (many-to-one mappings) (merging)
      - {from: [ih, ng], to: ing}
      - {from: [eh, ax, m], to: eam}
    # M:M (many-to-many mappings)
      - {from: [ih, ng], to: [ix, ng]}
      - {from: [ay, l], to: [ay, ax, el]}

    # format can be like this
        - from: [ae, n]
        to: [eh, ax, n]
        - from: b
        to: bh
    ```
- #### Timings
    - Defines the certain phoneme to be in this phoneme group's phoneme length.
    - Overrides specific alias to be in that length (in seconds).
    ```
    timings:
      - {symbol: dh, value: 1.2}
      - {symbol: vf, value: 2.8}
      - {symbol: st, value: 3.5}
      - {symbol: a r, value: 0.5}
      - {symbol: e r, value: 0.5}
      - {symbol: i r, value: 0.5}
    ```
- #### Entries
    - Add a new dictionary entry to override certain word pronunciations.
    - no limit to characters as long as it covered by unicode so you can add kana, hangul, hieroglyphics grapheme etc entries to `xsampa.yaml` or `en-xsampa.yaml`.
    ```
    entries:
      - {grapheme: hello, phonemes: [hh, ax, l, ow]}
      - {grapheme: 안녕하세요, phonemes: [aa, n, y, ao, ng, hh, ah, s, eh, y ao]}
    # format can be like this
      - grapheme: stars
        phonemes: s, t, aa, r, z
      - grapheme: drops
        phonemes: dr, aa, p, s
    ```

## Italian Syllable-Based Phonemizer (IT SYL)
### Setup
**!!IMPORTANT NOTE!!** This phonemizer is **NOT** to be confused with the older Italian CVVC Phonemizer. The biggest difference is that the Italian Syllable-Based Phonemizer uses a dictionary (see below), whereas the older Italian CVVC Phonemizer is a simple port of the Japanese CVVC Phonemizer. However, both are based upon [Makkusan's Italian reclist](https://drive.google.com/file/d/1KHLocNVjC87pW74xFE1NuzW2Mvp1IJrF/view).

Downloading a separate dictionary is no longer necessary. Instead, it now uses the in-built Italian G2P. As a result, it can now read words that are not in the dictionary.

Please note that at this time, this phonemizer only supports the above-mentioned Makkusan method. However, I might add support for other methods if there's demand for it.

### Lyric input
You write the word on the first note, then spread the syllables by writing a ``+`` on the next note(s):

![Lyrics showcase example with syllable spreading notes](https://i.ibb.co/bJPdfLJ/giorno.png)

![Showcasing syllable extender notes](https://i.ibb.co/v4G5z5S/giorno2.png)

Note that falling diphthongs (aka semivowels at the end of a note) should essentially be treated as a separate syllable, since they are treated as regular vowels in both the dictionary and the phonemizer:

![Showcasing correct treatment of falling diphthongs](https://i.ibb.co/8Pbhvq7/Falling-Diphthongs-Correct.png)

Whereas if you don't do that, the latter half of the diphthongs will accidentally spread over to the next note:

![How NOT to do falling diphthongs](https://i.ibb.co/qx3mCNx/Falling-Diphthongs-Wrong.png)

Note that when followed by a vowel within the same word, the phonemes ``y`` (for short ``i``) and ``w`` (for short ``u``) are used instead, so this does not apply in those cases.

Also note that as of writing, the phonemizer sadly does not yet support ``[V]i R`` and ``[V]u R`` etc. semivowel endings notes (where ``[V]`` represents a "full" vowel). This is on the roadmap, but is predicted to be difficult to implement.

### Phonetic input
You can also use phonetic hints after lyrics, you put those in between brackets (``[]``) with spaces in-between. This is handy when certain phonemes aren't quite right, or for pure stylistic reasons. You write the hint on the first note of the word:

![Showcasing phonetic hints](https://i.ibb.co/RQnndyq/Phonetic-Hint1.png)

You can also opt for pure phonetic input instead, it works the same as above except not right after a lyric:

![Showcasing pure phonetic input](https://i.ibb.co/R63rCc3/Phonetic-Hint2.png)

### Phoneme list
Vowels: a, e, i, o, u, 3, 0

Consonants: b, d, dz, dZ, f, g, gn, j, k, l, m, M, n, N, p, r, rr, s, S, t, ts, tS, v, w, y, z, **B**, **D**, **G**, **h**, **T**, **x**, **Y**, '

The bolded phonemes are extra sounds for Spanish. They're not in the dictionary and only work through phonetic input (the latter also counts for ``'``, which represents vocal fry).

## German Diphone Phonemizer
### Setup
This phonemizer works similarly to the Arpasing phonemizer, as it uses the same API. Custom dictionaries are supported. (For an example of what a custom dictionary should look like, take a look at the `arpasing.yaml` file in the `Plugins` folder of OpenUtau.)

This phonemizer uses the in-built German G2P, so downloading an external dictionary is not necessary. However, since the G2P isn't error-free, users are encouraged to override incorrect transcriptions in a custom dictionary, if they encounter any errors.

### Lyric input
You write the word on the first note, then spread the syllables by writing a ``+`` on the next note(s):

![Lyrics showcase example with syllable spreading notes](https://i.ibb.co/Wx0XDZL/Example1.png)

### Phonetic input
You can also use phonetic hints after lyrics, you put those in between brackets (``[]``) with spaces in-between. This is handy when certain phonemes aren't quite right, or for pure stylistic reasons. You write the hint on the first note of the word:

![Showcasing phonetic hints](https://i.ibb.co/zb0LLw3/Phonetic-Hint.png)

You can also opt for pure phonetic input instead, it works the same as above except not right after a lyric:

![Showcasing pure phonetic input](https://i.ibb.co/VLPBLFQ/Phonetic-Hint-Pure.png)

Note that the rhotic sound `ex` ("bess**er**", "He**r**z") should always be treated as a separate vowel; this is because of the in-built dictionary used by OpenUtau.

### Phoneme list (default)
Vowels: aa, ae, **ah**, ao, aw, ax, ay, ee, eh, **er**, ex, ih, iy, oe, ohh, ooh, oy, ue, uh, uw, yy

Consonants: b, cc, ch, d, **dh**, f, g, hh, **jh**, k, l, m, n, ng, p, pf, q, **r**, rr, s, sh, t, **th**, ts, v, **w**, x, y, z, **zh**

The **bolded** letters represent foreign sounds, most of which come from English. They represent the same sounds as their Arpasing counterparts (more on that below). They do get used in the German G2P for loanwords, however fallbacks do exist in the phonemizer.

### Combined English-German diphonic (Arpasing) banks
Due to the easy compatibility between English Arpasing and the German diphonic system, you could make a combined English-German diphonic bank (aka, a German addon for Arpasing, or an English arpasing addon for a German bank). Here is a list of required extra phonemes you will need for this combined bank style:

#### German addon for English bank
##### Extra vowels:
- `ax` - Schwa (often already present in Arpasing banks);
- `ee` - Long german "e" (e.g. "g**eh**e");
- `ex` - German rhotic vowel (e.g. "bess**ex**"); also used for "r" at the end of syllables/words;
- `oe` - Short German "ö" (e.g. "l**ö**schen");
- `ohh` - Long German "ö" (e.g. "b**ö**se");
- `ooh` - Long German "o" (e.g. "Br**o**t");
- `ue` - Long German "ü" (e.g. "f**ü**r");
- `yy` - Short German "ü" (e.g. "m**ü**ssen").

##### Extra consonants:
- `cc` - Ich-Laut (e.g. "di**ch**");
- `pf` - Bilabial affricate (e.g. "**Pf**effer");
- `q` - Glottal stop (often already present in Arpasing banks);
- `rr` - German "r" at the beginning of words/syllables (e.g. "**R**eise");
- `ts` - Dental affricate (e.g. "**z**u");
- `x` - Acht-Laut (e.g. "ma**ch**en").

#### English addon for German bank
##### Extra vowels:
- `ey`;
- `ow`.

All the other necessary vowels, as well as the required extra consonants, are already listed above. However, any other sound can still be added, e.g. "dx" (dental flap/tap), "el"/"em"/"en" (syllabic consonants; can also be used in German), etc.

## German VCCV Phonemizer
### Setup
This phonemizer was based on the system used for [Felix German VCCV](https://utau.fandom.com/wiki/Felix), which is essentially X-SAMPA. Custom dictionaries are supported. (For an example of what a custom dictionary should look like, take a look at the `arpasing.yaml` file in the `Plugins` folder of OpenUtau.)

This phonemizer uses the in-built German G2P, so downloading an external dictionary is not necessary. However, since the G2P isn't error-free, users are encouraged to override incorrect transcriptions in a custom dictionary, if they encounter any errors.

### Lyric input
You write the word on the first note, then spread the syllables by writing a ``+`` on the next note(s):

![Lyrics showcase example with syllable spreading notes](https://i.ibb.co/Wx0XDZL/Example1.png)

**Note:** This phonemizer used to have an issue where the second half of a split diphthong had to be treated as if it were a different syllable. However, this problem has since been resolved and this method is no longer necessary, splitting them within the same syllable instead:

![Split diphthongs working correctly](https://i.ibb.co/bHqp9QG/Correct-Splits.png)

Note that the rhotic sound `6` ("bess**er**", "He**r**z") should still always be treated as a vowel; this is because of the in-built dictionary used by OpenUtau.

### Phonetic input
You can also use phonetic hints after lyrics, you put those in between brackets (``[]``) with spaces in-between. This is handy when certain phonemes aren't quite right, or for pure stylistic reasons. You write the hint on the first note of the word:

![Showcasing phonetic hints](https://i.ibb.co/sRDF1YC/Phonetic-Hint1.png)

You can also opt for pure phonetic input instead, it works the same as above except not right after a lyric:

![Showcasing pure phonetic input](https://i.ibb.co/tQPZ93W/Phonetic-Hint2.png)

### Phoneme list
Vowels: a, 6, e, E, 2, 9, i, I, y, Y, u, U, o, O, @, aU, OY, aI

Consonants: -, b, C, d, f, g, h, j, k, kh, l, m, n, N, p, ph, R;, s, S, t, th, v, x, z, Z, dZ, ks, pf, st, St, tS, w

Please note that at this time, custom vowels are not supported in user dictionaries, though custom consonants are.

## Korean-to-Japanese Phonemizer
### Description
#### Input
This phonemizer is for making Japanese banks sing Korean, like so:

**CV (with crossfade):**

![Testing Hangul input with Japanese CV voicebank](https://i.ibb.co/DYZ7zz7/Hangul-Test-Cv.png)

**CVVC:**

![Testing Hangul input with Japanese CVVC voicebank](https://i.ibb.co/rdRQk0t/Hangul-Test-Cvvc.png)

**VCV+CVVC:**

![Testing Hangul input with Japanese VCV+CVVC voicebank](https://i.ibb.co/MGDP5YY/Hangul-Test-Mix.png)

**VCV:**

![Testing Hangul input with Japanese VCV voicebank](https://i.ibb.co/HFTF4rb/Hangul-Test-Vcv.png)

As you can see, crossfade aliases are supported, this includes final consonants.

The best result is given with either a CVVC voicebank or a VCV+CVVC mixed voicebank. For CV and VCV, it's advised to adjust the length of the final consonant manually until it sounds good.

Note that Korean [sandhi](https://en.wikipedia.org/wiki/Sandhi) (liaison) rules are not implemented, due to being complicated to code. Because of this, it's advised to use use pronunciation-based spelling for Hangul input. (This is similar to the Korean VCV Phonemizer, on which a lot of the code was based.)

Instead of Hangul input, phonetic hint is also possible (note that this is based on Japanese phonemes, since those are the ones being used):

![Testing phonetic hint input](https://i.ibb.co/fCTQfWT/Phonetic-Hint.png)

Note that diphthongs are treated as a separate vowel:

![Testing phonetic hint diphthongs](https://i.ibb.co/WfN0H6p/Phonetic-Hint2.png)

As you can also see, it will use ``しゃ`` for this particular instance; this has to do with Korean pronunciation, which has similar [palatalization](https://en.wikipedia.org/wiki/Palatalization_(phonetics)) rules as Japanese.

##### Romaja-based Hangul QWERTY keyboard for Windows
For non-Korean users on Windows who'd like to use Hangul, I can recommend the [Nalgaeset Input System](http://moogi.new21.org/en/ngs/index.htm). This way, you can easily type Hangul with a QWERTY keyboard layout, based on Revised Romanization. (You can also create your own layout, e.g. QWERTZ- or AZERTY-based.) This is also convenient for the other Korean phonemizers.

### Mechanism
Usually, the phonemizer prioritizes VCV over anything else, however there are a few exceptions:
- Syllables featuring _batchim_ (final consonants, so essentially closed syllables). It will use a VC alias if present, else it will look for VCV, then a crossfade alias, and finally CV.
- Fallbacks. Let's just say ``くぁ`` is present in the oto, but only as a CV alias. VCV only has e.g. ``a か``. In this case, it will use the CV ``くぁ`` over the VCV, due to having more accurate pronunciation. It will also insert a VC if present.

### Other functions
#### Consonant velocity
Similarly to the Japanese CVVC Phonemizer, Japanese Presamp Phonemizer and Chinese CVVC phonemizer, the length of VC (and CC) samples can be changed by changing the consonant velocity of the base CV note.

#### Extra sounds
The phonemizer supports the following extra sounds: f, v, z, ts, sh

## Other phonemizers
Here is a list of separately distributed phonemizers for OpenUtau. To install, place the `.dll` file in the Plugins folder of your OpenUtau installation.

* [Cyrillic Japanese Phonemizer](https://github.com/adlez27/OpenUtau/releases/tag/Cyrilji-0.1.0) by adlez27
* [Korean CVVC+ Phonemizer](https://github.com/lottev1991/Korean-CVVC-Plus-Phonemizer/releases) by Lotte V
* [SHO Phonemizer](https://github.com/adlez27/OpenUtau/releases/tag/SHO-0.1.1) by adlez27
* [Teto English Phonemizer](https://github.com/adlez27/OpenUtau/releases/tag/Teto-0.1.0)  by adlez27
* [Syllable-based ARPAsing Phonemizer (ARPA+)](https://github.com/Cadlaxa/Syllable-Based-ARPAsing-Phonemizer) by Cadlaxa