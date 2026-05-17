**This page is a work in progress. Contributions are welcomed**

Anyone can make a voicebank with their voice and use it in OpenUtau. There are basically two types of voicebanks: UTAU (concatenative) voicebanks and machine learning voicebanks. 

Before making a new voicebank, it's recommended to use existing voicebanks in OpenUtau. This will help you understand the concepts in voicebank development, and help you to make a good voicebank, as well as what you might want to include in your voicebank.

## UTAU voicebank development
To make a UTAU voicebank, you need to record all the syllables in a language and label them.

### How does it work
- The user inputs lyrics and notes
- The **phonemizer** converts the notes and lyrics into a list of concatenate units.
- For each concatenate unit, the **resampler** loads the corresponding sample from the voicebank, change the duration and pitch of the sample, and apply flags to them.
- The **wavtool** joins all the audio slices produced by resampler together and output the final audio.

### First time making UTAU voicebank
If you've never made any utau voicebanks before, it's highly recommended to follow this step by step tutorial to understand the basic process.

[wastelandutau's "Creating Your First Voicebank" written walkthrough](https://utau.felinewasteland.com/ref/firstvb)

### Recording
Find a recording list suitable for your language. A reclist is a text file that has all syllables or phonemes and their combinations in a language. Here are some publicly available reclists:

| Phonemizer | Reclist |
|-|-|
| JA VCV & CVVC | [Japanese reclists](https://wastelandutau.neocities.org/jp/overview) |
| ZH CVVC | [Hr.J Chinese CVVC](https://utaujc.jimdofree.com/hr-j-cvvc/) by haru |
| EN ARPA | [ARPAsing Reclist Directory](https://arpasing.tubs.wtf/en/directories/reclists) |
| EN XSAMPA | [Delta-style English reclists](https://tl.tubs.wtf/2020/11/09/delta-eng)<br>[Salem-Style English CVVC](https://utau.felinewasteland.com/en/overview)<br>[GrayGlish](https://assbackwardsp.wixsite.com/utaubackwards/reclists) |
| EN VCCV | [Core American English VCCV](https://www.mediafire.com/download/wef9lg11dmccxqx/CORE_American_English_VCCV.zip) by PaintedCz |
* English recorded with any of these methods have various pros and cons. You may want to try recording a language with a smaller set of vowels first, or recording and training [an AI voicebank](#machine-learning-voicebank-development) for DiffSinger.

Theoretically you can record a voicebank with any software you like. However, a dedicated reclist recorder application can automatically prompt you to record line by line and save them using the text of the line as file names. The recommended software is [recstar](https://github.com/sdercolin/recstar) 

Many people record with a "guide BGM" so that their samples are at a consistent BPM and pitch. You can find some guideBGMs to start with [here](https://wastelandutau.neocities.org/ref/guidebgm#dl) and [here](https://w.atwiki.jp/vbmaker/pages/26.html) (Japanese site). ("#-Mora" is the number of syllables in each string)

#### Multi-pitch voicebanks
You can record multiple subbanks for one voicebank. For example, you can record in multiple pitches to make its range wider, or record in multiple vocal modes to let the user choose between different singing styles. Each subbank is equivalent to a full single-pitch voicebank and should contain all the voice lines in your reclist.

You can start developing your voicebank with only one subbank, and add more subbanks in the future. 

### otoing
After recording, you will need to make oto.ini files. 

oto.ini is a mark-up language that tells OpenUtau where each phoneme is in the voicebank and how to manipulate them. 

The recommended way to make oto.ini for a voicebank is using [vLabeler](https://github.com/sdercolin/vlabeler). 

If you want a tutorial that covers how to oto most styles of voicebank, [Yin's tutorial](https://yinsototutorial.weebly.com/) is commonly recommended by the community. It uses older tools than vLabeler, but the basic logic is the same.

#### How oto.ini works

Let's look at an example oto.ini line from [Kasane Teto](https://kasaneteto.jp/utau/) in vLabeler and dissect it.

![image](https://github.com/stakira/OpenUtau/assets/37761120/5c85409d-6edc-43af-9ebf-42a46aa28ef3)

1. **Yellow line:** Offset, or left blank. The start of the phoneme.
2. **Green line:** Overlap. Everything between the left blank and overlap will be blended with the previous note.
3. **Red line:** Preutterance. The start of the musical note.
4. **Blue line:** Fixed region, or consonant. Everything before this line will not be looped/stretched.
5. **White line:** Cutoff, or right blank. The end of the phoneme. Everything between the fixed region and cutoff will be looped/stretched.

See also: [Anatomy of the OTO](https://utaforum.net/resources/anatomy-of-the-oto.321/) on UtaForum.

There are probably otoing guides specific to the type of voicebank you're recording (JP VCV/CVVC, EN VCCV, etc.) 

### Other files
Create a subfolder inside your OpenUtau's `Singers` folder, and put your voice folders (wav and oto.ini) into it. This is your voicebank. You still need these files and informations in your voicebank:

#### character.txt
character.txt is the file that tells OpenUtau this is a voicebank, and the name of the voicebank. Create a new text file in your voicebank named `character.txt` and edit it. Here is a minimal example of your character.txt:
```
name=name_of_your_voicebank
```
#### Set up Subbanks
If your voicebank contains multiple subbanks, you'll need to set them up in OpenUtau with `Tools → Singers → Edit subbanks` where you can assign each subbank to a certain pitch range in a voice color.

#### Default phonemizer
Launch OpenUtau. In `Tools → Singers`, click `⚙ → Default Phonemizer` and select the phonemizer that your voicebank supports. After the user selects your voicebank, the phonemizer will be chosen automatically.

Subbanks and default phonemizer infomation are stored in `character.yaml` inside the voicebank. See [tech note ‐ character.yaml](https://github.com/stakira/OpenUtau/wiki/tech-note-%E2%80%90-character.yaml)

### Packing UTAU voicebank
In `Tools → Singers`, click `⚙ → Publish Singer`. You'll get a zip file of your singer for distributing.

## Machine Learning voicebank development
Machine learning voicebanks produce more fluent singing voice with less manual edits, but you'll need a GPU to train them. OpenUtau supports two engines that allow making voicebanks by yourself: NNSVS (also known as ENUNU) and DiffSinger. To make a machine learning voicebank, you need to record your singing voice, label them and train a machine learning model.

### Recording
Record any song in this language with any recording software you like. Just ensure that:
- all the lyrics are in the language your voicebank supports
- your dataset contains all the phonemes in the language.

### Labelling
After recording, make phoneme-level labels for your voicebank. You can use [vLabeler](https://github.com/sdercolin/vlabeler) to make labels.

[SVS Singing voice database - tutorial](https://docs.google.com/document/d/1uMsepxbdUW65PfIWL1pt2OM6ZKa5ybTTJOpZ733Ht6s/view) by PixPrucer

There are also automated tools that make labels for you:
- [SOFA](https://github.com/qiuqiao/SOFA)
- [LabelMakr](https://github.com/spicytigermeat/LabelMakr) (a GUI for SOFA)

### Training
After labelling your dataset, you can either train a DiffSinger voicebank or an ENUNU voicebank.
While both are viable options, DiffSinger is recommended as it's higher quality and has more resources available.

[DiffSinger](https://github.com/openvpi/diffsinger)
- [DiffSinger Colab Notebook MLo7](https://github.com/MLo7Ghinsan/DiffSinger_colab_notebook_MLo7)
- [DiffTrainer local training kit](https://github.com/agentasteriski/DiffTrainer)

[ENUNU](https://github.com/oatsu-gh/Enunu)
- [ENUNU training kit](https://github.com/oatsu-gh/enunu_training_kit)