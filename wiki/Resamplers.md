
# Windows

This is a list of all UTAU resamplers tested with OpenUtau.

## Fully compatible

- doppeltler32.exe
- doppeltler64.exe
- f2resamp32.exe
- f2resamp64.exe
- fresamp11.exe
- fresamp12.exe
- fresamp14.exe
- macres.exe
- resampler.exe
- TIPS.exe
- tn_fnds.exe
- w4u.exe
- young3.exe
- vs4u.exe
- WARP.exe
- EFB-GT.exe
- EFB-PB.exe

## Compatible with adjustments

- moresampler.exe
  - Need to edit the following lines in moreconfig.txt:
    - Line 6 "resampler-compatibility" to on.
    - Line 16 "auto-update-llsm-mrq" to off.
  - The wavetool mode is not supported. But using it as a pure resampler works.
  - Generating llsm files with multiple processes can easily overload your computer. Please turn down threads to 1 or 2.

## Incompatible

# macOS

As of macOS 11.6, the below method works.

