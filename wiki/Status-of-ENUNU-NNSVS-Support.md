- Note: ENUNU/NNSVS support is **experimental**. There will be quirks. Be **patient**. Be **ready to troubleshoot**.
- Note: **This page will change regularly**.

## How to use (0.0.703)
- Currently Windows only.
- Delete old ENUNU plugins.
- Add ENUNU 0.3.1 plugin to Plugins folder.
- Start ENUNU as a legacy plugin just once so that it will download and install pytorch. It takes a while.
- After pytorch is installed, it functions as a normal renderer. I.e., no need to run it as a legacy plugin.
- Supported expressions: PITD, DYN, TENC, BREC, VOIC, GENC.
- Use "DEFAULT" phonemizer.
- No "extensions" support. For OpenUtau calling an external exe is generally considered an anti-pattern. If anything, it needs to be cross-platform.

## FAQ
### Q: All lyrics are invalid.
A: It is assumed the ENUNU voicebank contains a CV voicebank like Ritsu, and use the oto to validate lyrics. If your ENUNU voicebank doesn't have CV samples, an oto file without samples will work too.

### Q: FileNotFoundException: Could not find file '...\acoustic-f0.npy'.
A: it's an NNSVS issue (https://github.com/r9y9/nnsvs/issues/94), sometimes it generates invalid data and fails by itself. Tweaking timing (the vertical red line in phoneme view) by just a little usually solves it.

### Q: It's very slow.
A: Yes it is very slow when notes and lyrics are modified (editing curves should be very fast). The way it works now is that python.exe is started for every phrase (a group of consecutive notes). Python is not great at startup speed. Every time python.exe is started, there are a few seconds wasted loading python packages. There are ways to improve, but that's the status quo.

## Roadmap
![Roadmap](https://i.imgur.com/V6Fof9A.png)