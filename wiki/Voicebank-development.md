**This page is work in progress**

Anyone can make a voicebank with their voice and use it in OpenUtau. There are basically two types of voicebanks: UTAU concatenative voicebanks and Machine learning voicebanks. 

## UTAU voicebank development
To make a UTAU voicebank, you need to record all the syllables in a language and label them.

### How does it work
- The user inputs lyrics and notes
- The **phonemizer** converts the notes and lyrics into a list of concatenate units.
- For each concatenate unit, the **resampler** loads the corresponding sample from the voicebank, change the duration and pitch of the sample, and apply flags to them.
- The **wavtool** joins all the audio slices produced by resampler together and output the final audio.

### Recording
Firstly, find a reclist suitable for your language. A reclist is a text file that has all syllables or phonemes and their combinations in a language. Here are some publically available reclists:

|Phonemizer|Reclist|
|-|-|
|EN VCCV|[Core American English VCCV](https://www.mediafire.com/download/wef9lg11dmccxqx/CORE_American_English_VCCV.zip) by PaintedCz|
|EN ARPA|[ARPAsing resource website](https://arpasing.neocities.org/)
|EN XSAMPA|[Delta-style English reclists](https://tl.tubs.wtf/2020/11/09/delta-eng)
|JA VCV & CVVC|[Japanese reclists](https://wastelandutau.neocities.org/jp/overview)|
|ZH CVVC|[Hr.J Chinese CVVC](https://utaujc.jimdofree.com/hr-j-cvvc/) by haru|

Theoretically you can record a voicebank with any software you like. However, a delicated reclist recorder application can autometically prompt you to record line by line and save them using the text of the line as file names. The recommended software is [recstar](https://github.com/sdercolin/recstar) 

#### Multi-pitch voicebanks
You can record multiple subbanks in one voicebank. For example, you can record in multiple pitches to make its range wider, or record in multiple vocal modes to let the user choose between different singing styles. Each subbank is a full voicebank and should contain all the voice lines in your reclist. 

You can start developing your voicebank with only one subbank, and add more subbanks in the future. 

### otoing
After recoding, you need to make oto.ini files. 

oto.ini is a mark-up language that tells OpenUtau where each phoneme is in the voicebank. 

The recommended way to make oto.ini for an voicebank is using [Vlabeler](https://github.com/sdercolin/vlabeler). 

If you want a tutorial that covers how to oto most voicebanks, [Yin's tutorial](https://yinsototutorial.weebly.com/) is commonly recommended by the community. It uses older tools than Vlabeler, but the basic logic is the same.

### Other files
Create a subfolder inside your OpenUtau's `Singers` folder, and put your voice folders (wav and oto.ini) into it. You still need these files and informations in your voicebank:

#### character.txt
character.txt is the file that tells OpenUtau this is a voicebank, and the name of the voicebank. Create a new text file in your voicebank named `character.txt` and edit it. Here is a minimal example of your character.txt:
```
name=name_of_your_voicebank
```
#### Set up Subbanks
If your voicebank contains multiple subbanks, you'll need to set them up in OpenUtau with `Tools → Singers → Edit subbanks` where you can assign each subbank to a certain pitch range in a voice color.

#### Default phonemizer
Launch OpenUtau. In `Tools → Singers`, click `⚙ → Default Phonemizer` and select the phonemizer that your voicebank supports. After the user chooses your voicebank, the phonemizer will be autometically chosen.

### Packing UTAU voicebank
In `Tools → Singers`, click `⚙ → Publish Singer`. You'll get a zip file of your singer for distributing.

## Machine Learning voicebank development
Machine learning voicebanks produce more fluent singing voice with less manual edits, but you'll need a GPU to train them. OpenUtau supports two engines that allow making voicebanks by yourself: NNSVS and DiffSinger. To make a machine learning voicebank, you need to record your singing voice, label them and train a machine learning model.

### Recording
Record any song in this language with any recording software you like. Just ensure that:
- all the lyrics are in the language your voicebank supports
- your dataset contains all the phonemes in the language.

### Labelling
After recording, make phoneme-level labels for your voicebank. You can use [vlabeler](https://github.com/sdercolin/vlabeler) to make labels.

[SVS Singing voice database - tutorial](https://docs.google.com/document/d/1uMsepxbdUW65PfIWL1pt2OM6ZKa5ybTTJOpZ733Ht6s/view) by PixPrucer

There are also automated tools that make labels for you:
- [SOFA](https://github.com/qiuqiao/SOFA)
- [LabelMakr](https://github.com/spicytigermeat/LabelMakr) (a GUI for SOFA)

### Training
After labelling your dataset, you can either train a DiffSinger voicebank or an ENUNU voicebank.

[DiffSinger](https://github.com/openvpi/diffsinger)
- [DiffSinger Colab Notebook MLo7](https://github.com/MLo7Ghinsan/DiffSinger_colab_notebook_MLo7)
- [DiffTrainer local training kit](https://github.com/agentasteriski/DiffTrainer)

[ENUNU](https://github.com/oatsu-gh/Enunu)
- [ENUNU training kit](https://github.com/oatsu-gh/enunu_training_kit)