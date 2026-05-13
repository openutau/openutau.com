- Note: ENUNU/NNSVS support is **experimental**. There will be quirks. Be **patient**. Be **ready to troubleshoot**.
- Note: **This page will change regularly**.

- Version list of ENUNU for OpenUtau (Click here to download)
  - Official [ENUNU for OpenUtau](https://github.com/stakira/ENUNU/releases) (ENUNU-0.4.0)
  - Unofficial [ENUNUServer](https://github.com/rokujyushi/ENUNU/releases) (ENUNU-1.0.0 ...)
  - Unofficial [SimpleENUNUServer](https://github.com/rokujyushi/SimpleEnunu/releases) (SimpleEnunuServer-0.5.0 ...)

## What is ENUNU/NNSVS?
NNSVS (Neural Network-based Singing Voice Synthesis) is an open source AI singing voice synthesis engine which allows users to make their own voicebank with their singing voice.

ENUNU is the mostly-used distro of NNSVS. In current community discussions, "ENUNU" can be considered a synonym for "NNSVS".

## How to use
Download the suitable ENUNU server version according to the voicebank you want to use. Unzip it.

Before opening OpenUtau, double click enunu_server.bat to launch the server and leave it open.

To use NNSVS generated pitch, finish rendering first, then execute "Notes -> Load Rendered Pitch" from the piano roll menu. You can select some phrases to load or load the entire part. Only the pitch of phrases finished rendering will be loaded.

If there is a problem with the operation, please put the following in **config.yaml**.  
If you do not want to perform timing correction, delete the timing_editor line.  
If you turn off the wav_synthesizer setting, you can edit the Pitch, but the quality is very low.  

ENUNU-0.4.0,SimpleEnunuServer-0.2.0+0.local.9.1
```yaml
extensions:
    timing_editor: "%v/timing_auto_correct/enunu_timing_auto_correct.py"
    wav_synthesizer: synthe
    acoustic_calculator: nnsvs
    timing_calculator: nnsvs
    ust_converter: built-in

```
SimpleEnunuServer-0.5.0
```yaml
extensions:
    timing_editor_2: "%v/timing_auto_correct/enunu_timing_auto_correct.py"
```

## Notes for voicebank developers
For ENUNU or SimpleENUNU compatible models, please add the following to character.yaml.

```yaml
singer_type: Enunu
```

To control expressions other than voice colour, define style_format and styles as follows.  
reference:[NNSVS/ENUNU　波音リツ CRISSCROSS　5スタイル #4130](https://www.canon-voice.com/voicebanks/#enunu)
#### Please write the following content in **config.yaml**.
```yaml
extensions:
# Other settings....
  style_format:
    p9: #Flag key to write to UST
      format: "{0}{1}{2}{3}" #Flag format Please enclose in "
      index: [ldst, loud, nrml, soft] #Key Set for Expression
    p16: 
      format: "s{0}s{1}r{2}b{3}p{4}"
      index: [Std, swt, rock, brth, pop]
  styles:
    ldst: #Key to Expression
      name: Loudest #Expression name
      type: Numerical #Expression control type: Currently, only numeric values are supported.
      min: 0
      max: 3
      default_value: 0
      flag: p9 #Flag key to write to UST
      
    loud:
      name: Loud 
      type: Numerical 
      min: 0
      max: 3
      default_value: 0
      flag: p9 
      
    nrml:
      name: Normal 
      type: Numerical 
      min: 0
      max: 3
      default_value: 0
      flag: p9 
      
    soft:
      name: Soft 
      type: Numerical 
      min: 0
      max: 3
      default_value: 0
      flag: p9 
      
    Std:
      name: Standard 
      type: Numerical 
      min: 0
      max: 3
      default_value: 0
      flag: p16 
      
    swt:
      name: Sweet 
      type: Numerical 
      min: 0
      max: 3
      default_value: 0
      flag: p16 
      
    rock:
      name: Rock 
      type: Numerical 
      min: 0
      max: 3
      default_value: 0
      flag: p16 
      
    brth:
      name: Breathy 
      type: Numerical 
      min: 0
      max: 6
      default_value: 0
      flag: p16 
      
    pop:
      name: Pop 
      type: Numerical 
      min: 0
      max: 3
      default_value: 0
      flag: p16 
```

## FAQ
### Q: FileNotFoundException: Could not find file '...\acoustic-f0.npy'.
A: it's an NNSVS issue (https://github.com/r9y9/nnsvs/issues/94), sometimes it generates invalid data and fails by itself. Tweaking timing (the vertical red line in phoneme view) by just a little usually solves it.

**Update**: a retry mechanism has been implemented to "fix" (actually workaround) this issue. It pads the start of input with a very short silence, then trims this silence from the output. This tiny difference in input is usually enough to make the issue disappear. Let me know if you still see it.

### Q: It's very slow.
A: Yes it is very slow when notes and lyrics are modified (editing curves should be very fast). The way it works now is that python.exe is started for every phrase (a group of consecutive notes). Python is not great at startup speed. Every time python.exe is started, there are a few seconds wasted loading python packages. There are ways to improve, but that's the status quo.

## Roadmap
![Roadmap](https://i.imgur.com/V6Fof9A.png)