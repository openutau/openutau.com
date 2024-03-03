***このページは翻訳中です。このページに無いPhonemizerの情報を見たい場合は、[Phonemizers](https://github.com/stakira/OpenUtau/wiki/Phonemizers)を参照してください。***

***

このページはエンドユーザー向けです。新たなPhonemizer制作に興味のある開発者の方は、[API Doc](https://github.com/stakira/OpenUtau/wiki/Developing-new-phonemizers)を参照してください。

Phonemizerがノートを複数の音素に分割するとき、それぞれの音素のエンベロープやパラメーターを個別に調整できます。

Phonemizerを変更するには、ボーカルトラックの「DEFAULT」をクリックし、Phonemizerを選択します。

![phonemizer](https://i.imgur.com/mBf2VOY.png)

## DEFAULT
Phonemizerを使用しません。  
入力した歌詞が複数のノートにまたがるようにするには`+`を使用します。  
(古いバージョンのOpenUtauでは`+`の代わりに`...`を使う場合があります。)

![+ extension](https://i.imgur.com/JlHc6bq.png)

## JA Presamp (Japanese VCV & CVVC)
単独音、連続音、CVVC、すべての音源で使用できます。  
このPhonemizerは歌詞をまず連続音に、連続音がない場合はCVVCに、それもない場合は単独音に歌詞を変換します。  
VoiceColorが切り替わるところにCVVCがある場合、連続音よりCVVCが優先されます。  
![presamp](https://imgur.com/SKzYtIb.png)  

このPhonemizerはローマ字をひらがなに変換します（詳細は後述）。  
![presamp romaji](https://imgur.com/bNSFg6g.png)  
声門破裂音（喉切り音）は`[あ・]`のように入力してください。  

このPhonemizerはpresampの動作に準じています。音源に`presamp.ini`がある場合そちらを使用します。  

`presamp.ini`内でサポートしている要素:  
`[VOWEL][CONSONANT][PRIORITY][REPLACE][ALIAS(VCPAD,VCVPAD)]`  

presampデフォルトの[REPLACE]にローマ字からひらがなへ変換する記述が含まれています。そのため、音源に`presamp.ini`が存在しないか、音源の`presamp.ini`の[REPLACE]にローマ字からひらがなに変換する記述がある場合、このPhonemizerはローマ字からひらがなに変換します(完全一致のみ)。 
デフォルトのVCの長さは、直後のCVの先行発声です。  

発音ヒントが入力されている場合はそちらを使用し、連続音またはCVVCに変換しません。  
![JaPhoneticHint](https://i.imgur.com/vgVHiJ2.png)  

## JA CVVC (Japanese CVVC)
歌詞はひらがなで書いてください。ローマ字で書かれている場合は、「ローマ字→ひらがな」でひらがなに変換できます。  
![roma to hira](https://i.imgur.com/XmfItiZ.png)

このPhonemizerはVCを挿入し、母音を連続音に変換します。デフォルトのVCの長さは、直後のCVの先行発声です。音源の`presamp.ini`の設定はまだ対応していません。  
![ja cvvc](https://i.imgur.com/GDaGjLu.png)

発音ヒントが入力されている場合はそちらを使用し、CVVCに変換しません。  
![JaPhoneticHint](https://i.imgur.com/WRp2vub.png)

## JA VCV (Japanese VCV)
歌詞はひらがなで書いてください。ローマ字で書かれている場合は、「ローマ字→ひらがな」でひらがなに変換できます。  
![roma to hira](https://i.imgur.com/XmfItiZ.png)

このPhonemizerは単独音を自動で連続音に変換します。連続音がない場合は単独音になります。音源の`presamp.ini`の設定はまだ対応していません。  
![ja vcv](https://i.imgur.com/QYp3J3J.png)

発音ヒントが入力されている場合はそちらを使用し、連続音に変換しません。  
![JaPhoneticHint](https://i.imgur.com/vgVHiJ2.png)