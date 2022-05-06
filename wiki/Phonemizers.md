This page is written for end users. Developers interested in working on new phonemizers should refer to the [API Doc](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/Api/README.md).

When phonemizers break notes into multiple phonemes, you can adjust the envelopes and parameters for each of these independently.

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

## EN DELTA (English Delta CVVC)
This phonemizer is not complete. Voicebanks that follow Kasane Teto's English voicebank's aliasing should work.
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

## FR CVVC (French CVVC)
### Setup
This phonemizer uses a slightly modified version of the [Petit Mot](https://simelomad.wixsite.com/crabkids/copie-de-pronunciation-guide) reclist by Melomad, it works with a dictionary (version 1.2 and higher) available [here](https://drive.google.com/file/d/1m-wnt5reJ0d9rGC2e1jMlZUMeioA5Lnw/view?usp=sharing). For the phonemizer to work, you need to download the .txt and put it in your Dictionaries folder. If there's no Dictionaries folder, create one at the root of your OpenUtau folder.

![dictionary goes in the dictionaries folder at the root](https://i.imgur.com/szewSA7.png)

There is also a [sample package](https://drive.google.com/file/d/1FpZTf2FOjWz-BjpWcGZEha-ZBhanEyDj/view?usp=sharing) available with a ustx that showcases the basic rules of the dictionary as well as ustx with French lyrics.

### Lyric input
You can input lyrics, phonetic hints `[]` or force input with `?` (note that force input will break the phonemizer transitions).
Use `+` to break words into syllables and `+~` to extend a syllable.

![fr cvvc lyric input vs phonetic input vs force input](https://i.imgur.com/qaPUUNH.png)

Sentences with apostrophes like "j'aime" or "j't'aime" need to be input `j' aime` and `j' t' aime`. You can also input "est-ce" as `est -ce`. Please note the **space** between the two words. 

Some common word combinations such as `j'ai` or `qu'elle` have been added for easier input, though you should always default to `C' + word`.

![fr cvvc handling of apostrophes](https://i.imgur.com/y1ovzSm.png)


Since French has a lot of silent sounds, you will sometimes need a second or third form of the word depending on the context (silent "e", liaison...). Usually, `word` is the basic form, `word(2)` adds the silent "e", `word(3)` adds the liaison **&** silent "e" and `word(4)` adds the liaison but no silent "e". 

However, there may be exceptions to this rule. 

![fr cvvc alternative forms](https://i.imgur.com/9dqeGbs.jpg)


If this doesn't work as intended, please ensure that your dictionary is **version 1.2 or higher**. Version number should be written at the start of the .txt.

### Additional support
The phonemizer can also read hiragana (with approximate French sounds).

![hiragana support](https://i.imgur.com/52cjlcf.png)

With the phonetic hint, you can input additional sounds that are voicebank-specific. In this example you can see glottal stops `.` & long end breaths `R`.

![additionalsounds](https://i.imgur.com/OuZ8t5c.png)

### Ressources
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

If you need to insert a consonant in an ending cluster that doesn't exist in the voicebank (usually an ``s``), it will automatically add a vowel after it (it will still sound decent in the program, trust me). If such a loose consonant exists in the voicebank, it will insert it by itself instead, and if it has a CC transition, it will use that:

![Loose consonant insertion (no CC)](https://i.ibb.co/hKZBQNd/Consonant-insertion-1.png)
![Loose consonant insertion (with CC)](https://i.ibb.co/9WpWpqW/Consonant-insertion-2.png)
![Loose consonant with vowel fallback](https://i.ibb.co/q9cgMcF/Vowel-insertion-fallback.png)

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

## Multi (Time Saver)
To get or build the config.ini go [here](https://mrcookiesexe.github.io/ConfigIniBuilder/).

The lyric input can have more then 1 word (eg. `'m=m`):
![Two words in the same lyric](https://user-images.githubusercontent.com/91439949/167221185-26841918-416d-455b-b856-ffdae63546a2.png)

To extend a syllable can be use `+~` `+*` `+-` and the ending is placed if don't have a note after or a note with `-`:
![Extended syllable and ending](https://user-images.githubusercontent.com/91439949/167221782-5dd4e716-8782-4af2-917a-f8122c1e9d73.png)

A manual input can be done by a note that's starts with a `?` or `+?` (if between syllable):
![Manual input](https://user-images.githubusercontent.com/91439949/167222681-dc4fc62c-6433-4aa9-91b4-0665a1942041.png)

The `+?` will always remove the **`V C` `V CC` `VC`** and will be before the **`CC`**:
![Manual input warning](https://user-images.githubusercontent.com/91439949/167223036-47aa9a7a-d897-41f8-80e3-2aaeaed08c46.png)

**If you'll do a config file, place it at the vb folder or the phonemizer don't will work properly.**