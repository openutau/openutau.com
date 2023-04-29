This page is written for end users. Developers interested in working on new phonemizers should refer to the [API Doc](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/Api/README.md).

When phonemizers break notes into multiple phonemes, you can adjust the envelopes and parameters for each of these independently.

In order to change the phonemizer, click DEFAULT on the vocal track and choose the phonemizer from there.

![phonemizer](https://i.imgur.com/mBf2VOY.png)

## DEFAULT
No phonemization is applied.
You can input `+` to extend the previous lyric over multiple notes.  
(Older versions of OpenUtau may use `...` instead of `+`.)

![+ extension](https://i.imgur.com/JlHc6bq.png)

## EN ARPA (English ARPAsing)
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

## Teto English (English Delta CVVC)
This phonemizer is not complete. Voicebanks that follow Kasane Teto's English voicebank's aliasing should work without issues (including banks recorded with Delta list #3.) Other Delta English lists will need extra phoneme editing to work. A phonemizer that properly supports every Delta list is planned.
You can input lyrics the following ways:
- Plain English words (eg. `live`)

![delta eng](https://i.imgur.com/biB7yoF.png)
- Word + phonetic hint (eg. `live[l I v]`)

![delta wp](https://i.imgur.com/T5cJR38.png)
- Phonetic hint (eg. `[l I v]`)

![delta p](https://i.imgur.com/GHzWJyc.png)
- Manual input (eg. `?- lI` `?I v-`)

![delta manual](https://i.imgur.com/dFIzRiO.png)

More information on Delta English can be found [here](https://tl.tubs.wtf/2020/11/09/delta-eng) if needed.

## ZH CVV (Chinese CVV)
Lyrics should be written in pinyin. The phonemizer will insert endings for syllables that need them.  
![zh cvv](https://i.imgur.com/TJfiNit.png)

## JA VCV & CVVC (Japanese VCV & CVVC)
You can use all of CV, VCV and CVVC voicevank.  
Use `presamp.ini` settings from the voicebank.  
The phonemizer converts romaji to hiragana if there is no `presamp.ini` or there are descriptions in [REPLACE] of `presamp.ini` to convert romaji to hiragana.

This phonemizer is still under development and this description is incomplete.

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

## KO CBNN (Korean Combination/CBNN)
This phonemizer is for [Korean Combination reclist(조합식 한국어 리스트)](https://github.com/EX3exp/UTAU-Korean-CBNN). (Reclist & Phonemizer made by same person)<br>
And this phonemizer bases on `KO CVC Phonemizer(by NANA)`.<br>
<br>
<img src="https://user-images.githubusercontent.com/100339835/216803418-7098136f-08cb-4b9e-b437-831625956fd8.png" height="350"/><br>
<img src="https://user-images.githubusercontent.com/100339835/216803425-1634e6b9-92c3-40cc-978c-333db853881e.png" height="350"/>
<img src="https://user-images.githubusercontent.com/100339835/216803424-9eccb60c-9ebf-4824-ba2b-ac7540a3991d.png" height="350"/><br>
<br>
- Supports Hangeul input.<br>
- Uses `-` as end breath symbols. <br>
- This phonemizer might apply some Phonological rules correctly, but sometimes it might misapply rules. <br>
So it's recommended to insert lyric *as which it sounds.* (For example: insert `종로에서 국화꽃을 샀다` as `종노에서 구콰꼬츨 사따`)<br>
- Others are just like `Default Phonemizer`.<br>

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

It's recommended that you use this phonemizer with a dictionary, which doesn't come with OpenUtau by default. Instead, you can download it [here](https://github.com/lottev1991/OpenUTAU-Spanish-Dictionary). This dictionary should go into OpenUtau's ``Dictionaries`` folder; if it doesn't exist, make it. (If a word is missing in the dictionary, or a transcription is incorrect, feel free to push merge requests on the dictionary repo. I am more than willing to expand the word list and correct errors.)

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

It's recommended that you use this phonemizer with a dictionary, which doesn't come with OpenUtau by default. Instead, you can download it [here](https://github.com/lottev1991/OpenUTAU-Spanish-Dictionary). This dictionary should go into OpenUtau's ``Dictionaries`` folder; if it doesn't exist, make it. (If a word is missing in the dictionary, or a transcription is incorrect, feel free to push merge requests on the dictionary repo. I am more than willing to expand the word list and correct errors.)

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

## ES MAKKU (Spanish Makkusan-style Phonemizer)
### Setup
This phonemizer was created to be used with Italian voicebanks using Makkusan's reclist, as long as it contains extra sounds for Spanish. It works similarly to the Italian Syllable-Based phonemizer.

It's recommended that you use this phonemizer with a dictionary, which doesn't come with OpenUtau by default. Instead, you can download it [here](https://github.com/lottev1991/OpenUTAU-Spanish-Dictionary). This dictionary should go into OpenUtau's ``Dictionaries`` folder; if it doesn't exist, make it. (If a word is missing in the dictionary, or a transcription is incorrect, feel free to push merge requests on the dictionary repo. I am more than willing to expand the word list and correct errors.)

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

### Lyric input
You can input lyrics in plain English `love`, plain English + phonetic hint `love [l u v]` or phonetic hint only `[l u v]`. 

![vccv_phonemeinput](https://user-images.githubusercontent.com/35538523/168469343-1519dbe9-b85f-4807-9d08-daf7d2aadb17.png)

You can then use `+` to break words into syllables, and `+*`or `+~` to extend a sound.

Use the pink line to stretch or shorten a sound so that the pronunciation is good. You can also switch sounds by double clicking on the box below to change the alias, so that you can switch between `V C`, `VC` or `VC-` as you please.

![vccv_phonemetweak](https://user-images.githubusercontent.com/35538523/168469015-823cf9fc-bd5a-4c0a-ac43-d9736caa4d40.png)

### Custom dictionary
Since the phonemizer uses an arpabet dictionary there may be conflicts with some sounds. If there are missing sounds, you can double click on the box below to change the sound used. However, you can now download a converted version of snowphones' Lyric Parser dictionary [here](https://github.com/mmemim/OU-EN-VCCV-Custom-Dictionary) and put it in `OpenUtau/Plugins`.

If there are any other issue, don't hesitate to share them on the Discord.

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

## EN Delta (Ver1) (Delta English Phonemizer (Version 1))
### Setup
This phonemizer is pretty similar to the Teto English phonemizer, as both are based on the classic Delta English list. However, there are a few important differences:
- As the name implies, the Teto English phonemizer was made specifically for Kasane Teto's English bank. While it does use the classic Delta method, it contains some Teto-specific functions that might not work well with other voicebanks.
- The way this phonemizer handles consonants is slightly different. I've attempted to streamline it a bit more in both general Delta phonemizers.
- This phonemizer accepts VCV for all consonants (including clusters), if the voicebank contains it.
- This phonemizer contains some extra sounds that were inspired by Cz's English VCCV method, except they're written in X-SAMPA instead. These sounds are not in any of the Delta lists but were added more for personal use (more on that below).
- This phonemizer now has custom dictionary support.

#### Differences with the 2nd version of this phonemizer (more info on that below)
- The main difference is that diphthongs are handled differently. This version of the phonemizer counts them as one phoneme (e.g. "light" is written as ``[l aI t]``.
- This phonemizer also contains more "non-Delta" sounds than Version 2, though even more can be added if needed in a custom dictionary file (more information below).

Which version you should use depends on the voicebank. It's a good idea to check the .wav files and oto.ini to be sure.

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

#### Phoneme list
Consonants: b, d, f, g, h, j, k, l, m, n, p, r, s, t, v, w, z, **4**, D, N, S, T, Z, dZ, tS, **・**, _**(underscore)**_

Vowels: A, E, I, O, U, i, u, {, V, 3, @, aI, eI, OI, aU, oU, _a_, _e_, _o_, **Q**, **Ol**, **aUn**, _**Ar**_, _**Er**_, _**Ir**_, _**Or**_, _**Ur**_, _**@l**_, _**@m**_, _**@n**_, _**@N**_, **eN**, _**IN**_, _**1**_, **e@**, _**e@m**_, _**e@n**_

The bolded letters and symbols do not occur by default in any of the standard Delta lists. They were mostly based on North-American dialects of English and aren't used by default by the phonemizer, only working through manual phonetic input (unless a custom dictionary file is created). They were based on X-SAMPA, you can find more information on it [here](https://en.wikipedia.org/wiki/X-SAMPA). The exception is ``・`` which is a glottal stop (in classic UTAU, ``?`` is used to ignore ``prefix.map``s).

The cursive symbols were taken from other version of the Delta lists. Just like the bolded sounds, they are not used by default and only work through phonetic input. 

The symbols that are both bolded and cursive are exclusive to [Peiton](https://www.supergoodboi.com/peiton.html/)'s English voicebank, as well any other voicebanks that might use that list. By default, they only work through phonetic input, unless a custom dictionary is created.

#### Custom dictionary
This phonemizer now has support for custom dictionaries. The dictionary should be named `xsampa.yaml` and be put in the main/top folder of a specific voicebank. For an idea on what a custom dictionary should look like, you can look at the `arpasing.yaml` file that comes with OpenUtau by default.

**!!IMPORTANT NOTE!!:** Certain X-SAMPA symbols should be contained within single quotes ('') when included in the custom dictionary file, otherwise your dictionary will not load. Some of the affected phonemes are:

* `{` and any phoneme that contains it;
* `}` and any phoneme that contains it;
* `@` and any phoneme starting with it (but not when at the end/center), ex. `@l` (but not `e@`);
* Some other, non-English/non-default X-SAMPA symbols might also be affected. It is highly recommended to test which specific ones beforehand.

Note that the Arpabet symbols included by default in the CMU Pronouncing Dictionary can also be used to note down custom words, though for any symbols that aren't included, X-SAMPA notation is required.

## EN Delta (Ver2) (Delta English Phonemizer (Version 2))
### Setup
This phonemizer works similarly to Version 1, but with a few differences:
- The main difference is that diphthongs are handled differently. This version of the phonemizer still treats them as the same phoneme, but splits them on the notes (e.g. "light" is written as ``[l a I t]``, though writing ``[l aI t]`` should still work).
- This phonemizer also contains less "non-Delta" sounds than Version 1, though more can be added if needed in a custom dictionary file (more information below).

For the rest, they work pretty similar. Which version you should use depends on the voicebank. It's a good idea to check the .wav files and oto.ini to be sure.

### Lyric input
You write the word on the first note, then spread the syllables by writing a ``+`` on the next notes:

![Lyric usage example](https://i.ibb.co/kcK2861/Lightning.png)

As you can see, since this phonemizer splits diphthongs, the second half of the diphthong should essentially be treated as if it's a separate syllable. If you don't do that, this happens:

![How not to treat diphthongs in this phonemizer](https://i.ibb.co/3rtWv0T/Lightning-WRONG.png)

As you can see, the second half lands on the wrong syllable. This can be prevented by using the correct method shown above.

If you only want to extend one syllable in the word, you can use either ``+*`` or ``+~``:

![Syllable extender notes](https://i.ibb.co/bd4w5NV/Lightning2.png)

### Phonetic input
You can also use phonetic hints after lyrics, you put those in between brackets (``[]``) with spaces in-between. This is handy when certain phonemes aren't quite right, or for pure stylistic reasons. You write the hint on the first note of the word:

![Showcasing phonetic hints](https://i.ibb.co/6P5wvFD/Example3.png)

You can also opt for pure phonetic input instead, it works the same as above except not right after a lyric:

![Showcasing pure phonetic input](https://i.ibb.co/mGPL9g2/Example4.png)

#### Phoneme list
Consonants: b, d, f, g, h, j, k, l, m, n, p, r, s, t, v, w, z, **4**, D, N, S, T, Z, dZ, tS, **・**, _**(underscore)**_

Vowels: A, E, I, O, U, a, e, i, o, u, {, V, 3, @, aI, eI, OI, aU, oU, _**1**_, **Q**

The bolded letters and symbols do not occur by default in any of the standard Delta lists. They were mostly based on North-American dialects of English and aren't used by default by the phonemizer, only working through manual phonetic input (unless a custom dictionary is created). They were based on X-SAMPA, you can find more information on it [here](https://en.wikipedia.org/wiki/X-SAMPA). The exception is ``・`` which is a glottal stop (in classic UTAU, ``?`` is used to ignore ``prefix.map``s).

The symbols that are both bolded and cursive were taken from [Peiton](https://www.supergoodboi.com/peiton.html/)'s English voicebank and only work through phonetic input. Note though that this phonemizer does not contain proper support for Peiton, instead Version 1 is recommended.

The extra sounds that are present in Version 1 of the phonemizer, but are absent in Version 2, have been omitted because they were either diphthongs or followed by a specific consonant. Most importantly, no known Delta-based voicebank uses any of the omitted sound combinations, as they'd be tricky to record and implement with the split diphthong method.

#### Custom dictionary

This phonemizer now has support for custom dictionaries. The dictionary should be named `xsampa.yaml` and be put in the main/top folder of a specific voicebank. For an idea on what a custom dictionary should look like, you can look at the `arpasing.yaml` file that comes with OpenUtau by default.

**!!IMPORTANT NOTE!!:** Certain X-SAMPA symbols should be contained within single quotes ('') when included in the custom dictionary file, otherwise your dictionary will not load. Some of the affected phonemes are:

* `{` and any phoneme that contains it;
* `}` and any phoneme that contains it;
* `@` and any phoneme starting with it (but not when at the end/center), ex. `@l` (but not `e@`) (Please note that custom diphthongs and colored vowels are not recommended for use in this version of the phonemizer, instead Version 1 is recommended for this usecase);
* Some other, non-English/non-default X-SAMPA symbols might also be affected. It is highly recommended to test which specific ones beforehand.

Note that the Arpabet symbols included by default in the CMU Pronouncing Dictionary can also be used to note down custom words, though for any symbols that aren't included, X-SAMPA notation is required.

## Italian Syllable-Based Phonemizer (IT SYL)
### Setup
**!!IMPORTANT NOTE!!** This phonemizer is **NOT** to be confused with the older Italian CVVC Phonemizer. The biggest difference is that the Italian Syllable-Based Phonemizer uses a dictionary (see below), whereas the older Italian CVVC Phonemizer is a simple port of the Japanese CVVC Phonemizer. However, both are based upon [Makkusan's Italian reclist](https://drive.google.com/file/d/1KHLocNVjC87pW74xFE1NuzW2Mvp1IJrF/view).

The dictionary for this phonemizer can be downloaded [here](https://github.com/lottev1991/OpenUtau-Italian-Dictionary). Please put the ``cmudict_it.txt`` file in the ``Dictionaries`` folder of your OpenUtau install; if it doesn't exist, make it.

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

#### Phoneme list
Vowels: a, e, i, o, u, 3, 0

Consonants: b, d, dz, dZ, f, g, gn, j, k, l, m, M, n, N, p, r, rr, s, S, t, ts, tS, v, w, y, z, **B**, **D**, **G**, **h**, **T**, **x**, **Y**, '

The bolded phonemes are extra sounds for Spanish. They're not in the dictionary and only work through phonetic input (the latter also counts for ``'``, which represents vocal fry).

## Other phonemizers
Here is a list of separately distributed phonemizers for OpenUtau. To install, place the `.dll` file in the Plugins folder of your OpenUtau installation.

* [Cyrillic Japanese Phonemizer](https://github.com/adlez27/OpenUtau/releases/tag/Cyrilji-0.1.0) by adlez27
* [SHO Phonemizer](https://github.com/adlez27/OpenUtau/releases/tag/SHO-0.1.1) by adlez27
* [Teto English Phonemizer](https://github.com/adlez27/OpenUtau/releases/tag/Teto-0.1.0)  by adlez27