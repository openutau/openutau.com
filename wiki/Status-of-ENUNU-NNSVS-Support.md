- Note: ENUNU/NNSVS support is **experimental**. There will be quirks. Be **patient**. Be **ready to troubleshoot**.
- Note: **This page will change regularly**.

## About ENUNU v0.5.0
It is reported that replacing files in ENUNU-server with ENUNU v0.5.0 files makes ENUNU-server work with v0.5.0 voicebanks. Feel free to try ar your own risk.

## How to use (0.0.743)
See [ENUNU v0.4.0 for OpenUtau](https://github.com/stakira/ENUNU/releases/tag/v0.4.0-openutau)

## How to use (0.0.732)
- Currently Windows only.
- Delete old ENUNU plugins.
- Add ENUNU 0.3.1 plugin to Plugins folder.
- Start ENUNU as a legacy plugin just once so that it will download and install pytorch. It takes a while.
- After pytorch is installed, it functions as a normal renderer. I.e., no need to run it as a legacy plugin.
- Supported expressions: PITD, DYN, TENC, BREC, VOIC, GENC.
- Use "ENUNU" phonemizer.
- No "extensions" support. For OpenUtau calling an external exe is generally considered an anti-pattern. If anything, it needs to be cross-platform.
- You can put words or phonemes as lyrics, separated by whitespaces, e.g. "か k a", as long as they exist in the table file or hed file.
- To use NNSVS generated pitch, finish rendering first, then execute "Notes -> Load Rendered Pitch" from the piano roll menu. You can select some phrases to load or load the entire part. Only the pitch of phrases finished rendering will be loaded.

## FAQ
### Q: FileNotFoundException: Could not find file '...\acoustic-f0.npy'.
A: it's an NNSVS issue (https://github.com/r9y9/nnsvs/issues/94), sometimes it generates invalid data and fails by itself. Tweaking timing (the vertical red line in phoneme view) by just a little usually solves it.

**Update**: a retry mechanism has been implemented to "fix" (actually workaround) this issue. It pads the start of input with a very short silence, then trims this silence from the output. This tiny difference in input is usually enough to make the issue disappear. Let me know if you still see it.

### Q: It's very slow.
A: Yes it is very slow when notes and lyrics are modified (editing curves should be very fast). The way it works now is that python.exe is started for every phrase (a group of consecutive notes). Python is not great at startup speed. Every time python.exe is started, there are a few seconds wasted loading python packages. There are ways to improve, but that's the status quo.

## Roadmap
![Roadmap](https://i.imgur.com/V6Fof9A.png)