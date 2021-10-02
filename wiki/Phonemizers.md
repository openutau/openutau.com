This page is written for end users. Developers interested in working on new phonemizers should refer to the [API Doc](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/Api/README.md).

When phonemizers break notes into multiple phonemes, you can adjust the envelopes and parameters for each of these independently.

## CV (Default)
No phonemization is applied.
You can input `...` to extend the previous lyric over multiple notes.  
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
![multisyllable](https://i.imgur.com/VLksjSR.png)

Auxiliary dictionary files:

- You can find an example `arpasing.yaml` file in Plugins folder. You can add new entries to it.
- A copy of `arpasing.yaml` file can be added to singer folder for a specific singer. You can even distribute an `arpasing.yaml` file with your voicebank.
- The lookup order is `plugin dictionary` -> `singer dictionary` -> `default dictionary`.

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

## KR CVC (Korean CVC)
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

## KR CVVC (Korean CVVC)
You should write the lyrics in Hangeul. Romaji will be updated soon.  
Automatically insert VC between CV and CV.
![kr cvvc](https://i.imgur.com/vrftrEJ.png)

you can write final consonant(`ㄴ`, `ㅁ`, `ㅇ`, `ㄹ`, `ㄱ`, `ㄲ`, `ㅂ`, `ㅍ`, `ㅅ`, `ㄷ`, `ㅌ`)
You can fill it out right after the note like CV.
Even if CV comes after final consonant, VC is not generated.
![kr cvvc final consonant](https://i.imgur.com/2RQfG4F.png)

When entering Vowel and Vowel, it is converted like VCV.
![kr cvvc vowel](https://i.imgur.com/ubiRAgb.png)

## KR CVVC (Korean CVVC standard pronuciation)
Followed the standard pronunciation method for Hangul.
This support all Korean final consonants, consonant assimilation(자음동화), 된소리되기, abbreviate consonants(자음 축약), 탈락, sandhi(연음).

![Korean CVVC standard pronuciation](https://i.imgur.com/unXXxVq.png)