This page is written for end users. Developers interested in working on new phonemizers should refer to the [API Doc](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/Api/README.md).

When phonemizers break notes into multiple phonemes, you can adjust the envelopes and parameters for each of these independently.

## CV (Default)
No phonemization is applied.
You can input "..." to extend the previous lyric over multiple notes.  
![... extension](https://i.imgur.com/2pR43nx.png)

## EN ARPA (English ARPAsing)
You may input lyrics in three different ways.
1. Plain English words (eg. "live")  
![plain english words](https://i.imgur.com/PZJe73G.png)
2. Plain English words + phonetic hint (eg. "live[l ih v]")  
![english word + hint](https://i.imgur.com/YmvhUaL.png)
3. Phonetic hint only (eg. "[l ih v]")  
![hint only](https://i.imgur.com/6hKOYsn.png)

For multisyllabic words, type the whole word in the first note, then use "..." to extend it across the following notes.  
If the syllables are misaligned, add numbers after "..." to force alignment to the nth phoneme in the word.  
![multisyllable](https://i.imgur.com/VLksjSR.png)

## ZH CVV (Chinese CVV)
Lyrics should be written in pinyin. The phonemizer will insert endings for syllables that need them.  
![zh cvv](https://i.imgur.com/TJfiNit.png)

## JA CVVC (Japanese CVVC)
Lyrics should be written in hiragana. If your lyrics are written in romaji, you can convert it to hiragana using the Romaji to Hiragana transformer.  
![roma to hira](https://i.imgur.com/XmfItiZ.png)

The phonemizer will insert VCs and convert vowels to VV. The default VC length is the preutterance of the following CV. presamp.ini settings from the voicebank are not supported yet.  
![ja cvvc](https://i.imgur.com/GDaGjLu.png)

## JA VCV (Japanese VCV)
Lyrics should be written in hiragana. If your lyrics are written in romaji, you can convert it to hiragana using the Romaji to Hiragana transformer.  
![roma to hira](https://i.imgur.com/XmfItiZ.png)

The phonemizer will automatically convert CV to VCV. If a VCV sample isn't available in the voicebank, it will fall back on CV. presamp.ini settings from the voicebank are not supported yet.  
![ja vcv](https://i.imgur.com/QYp3J3J.png)