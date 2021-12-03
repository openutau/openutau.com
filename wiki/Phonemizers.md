This page is written for end users. Developers interested in working on new phonemizers should refer to the [API Doc](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/Api/README.md).

When phonemizers break notes into multiple phonemes, you can adjust the envelopes and parameters for each of these independently.

## CV (Default)
No phonemization is applied.
You can input `...` to extend the previous lyric over multiple notes.  
Obs. After the update 11/12/21, `...` was changed to `+`.  
![... extension](https://i.imgur.com/2pR43nx.png)

## EN ARPA (English ARPAsing)
You may input lyrics in three different ways.
1. Plain English words (eg. `live`)  
![plain english words](https://i.imgur.com/PZJe73G.png)
2. Plain English words + phonetic hint (eg. `live[l ih v]`)  
![english word + hint](https://i.imgur.com/YmvhUaL.png)
3. Phonetic hint only (eg. `[l ih v]`)  
![hint only](https://i.imgur.com/6hKOYsn.png)

For multisyllabic words, type the whole word in the first note, then use `...` to extend it across the following notes.  
If the syllables are misaligned, add numbers after `...` to force alignment to the nth phoneme in the word.  
Obs. After the update 11/12/21, `...` was changed to `+`.  
![multisyllable](https://i.imgur.com/VLksjSR.png)

### Auxiliary dictionary files:

- You can find an example `arpasing.yaml` file in Plugins folder. You can add new entries to it.
- A copy of `arpasing.yaml` file can be added to singer folder for a specific singer. You can even distribute an `arpasing.yaml` file with your voicebank.
- The lookup order is `plugin dictionary` -> `singer dictionary` -> `default dictionary`.

## EN DELTA (English Delta CVVC)
This phonemizer is not complete. Voicebanks that follow Kasane Teto's English voicebank's aliasing should work.  
Currently, only input for plain English words and direct input is allowed.
- Plain English words (eg. `live`)
- Manual input (eg. `?- lI` `?I v-`)
To get the phonemizer's dictionary working, you need to make a folder in the OpenUtau folder named `Dictionaries`, then put [cmudict-0_7b.txt](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/Api/cmudict-0_7b.txt) in it.

## ZH CVV (Chinese CVV)
Lyrics should be written in pinyin. The phonemizer will insert endings for syllables that need them.  
![zh cvv](https://i.imgur.com/TJfiNit.png)

## JA CVVC (Japanese CVVC)
Lyrics should be written in hiragana. If your lyrics are written in romaji, you can convert it to hiragana using the Romaji to Hiragana transformer.  
![roma to hira](https://i.imgur.com/XmfItiZ.png)

The phonemizer will insert VCs and convert vowels to VV. The default VC length is the preutterance of the following CV. `presamp.ini` settings from the voicebank are not supported yet.  
![ja cvvc](https://i.imgur.com/GDaGjLu.png)

## JA VCV (Japanese VCV)
Lyrics should be written in hiragana. If your lyrics are written in romaji, you can convert it to hiragana using the Romaji to Hiragana transformer.  
![roma to hira](https://i.imgur.com/XmfItiZ.png)

The phonemizer will automatically convert CV to VCV. If a VCV sample isn't available in the voicebank, it will fall back on CV. `presamp.ini` settings from the voicebank are not supported yet.  
![ja vcv](https://i.imgur.com/QYp3J3J.png)

## KO CVC (Korean CVC)
This is a program to modify existing oto.ini file for use in OpenUtau (made by myself)  
└> https://app.box.com/s/t973p0rznirqg0naa04436p8re0ktfyy  
You write lyrics in Romaji and Hangeul  
automatically insert VC between the CV and CV.  
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

## PT-BR CVC (Brazilian Portuguese CVC)
Made with Xiao's PT-BR CVC reclist conotation, this phonemizer can be used with or without a dictionary

### Without a Dictionary
1. You can input the phonemes in plain text, separated by spaces (eg. `p e h f e y s @ w`)  
![ptbr cvc typing without dictionary (perfeição)](https://i.imgur.com/BNGhl9A.png)  

### With a Dictionary
1. Portuguese Words (eg. `leite`)  
![ptbr cvc with dictionary - ptbr words](https://i.imgur.com/E1eTaV5.png)  
2. Portuguese Words + phonetic hint (eg. `leite[l e y t e]`)  
![ptbr cvc with dictionary - ptbr words + phonetic hint](https://i.imgur.com/1bhmZFl.png)  
3. Phonetic hint only (eg. `[l e y t e]`)  
![ptbr cvc with dictionary - only phonetic hint](https://i.imgur.com/Fb8n69J.png)  

### Common Feature
With or without a dictionary, you can use the features listed below:

1. Separate words or phonemes by syllable using `+`.  
![ptbr cvc - separating syllables](https://i.imgur.com/ofHlD9O.png)  
2. Extend a syllable or phonemes using `+*` or `+~`.  
![ptbr cvc - extending syllables](https://i.imgur.com/OkqTZHd.png)  
3. Using a single phoneme with `?`.  
Obs. If exists a linked note behind that finishes with `V-`, `VC-` or `VC` + `C-`, this function removes those samples in order to cross fade with previous `V` or `CV`.  
![ptbr cvc - ? function](https://i.imgur.com/MfeBe62.png)  