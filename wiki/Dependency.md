# Overview
Dependencies for extending features such as Transcribe and the DiffSinger vocoder available in OpenUtau  
### **Please review the terms of use for each dependency before using it.**  
Please install the dependency files either through the Packages window or by downloading the files from each release and installing them.

# Transcribe
* [SOME](https://github.com/xunmengshe/OpenUtau/releases/tag/0.0.0.0)
* [GAME](https://github.com/openvpi/GAME/releases/tag/oudep)
* [RMVPE](https://github.com/emeraldsingers/UtauV_Packages/releases/tag/rmvpe)

# Vocoder
* [nsf_hifigan](https://github.com/xunmengshe/OpenUtau/releases/tag/0.0.0.0)
* [nsf_hifigan_44.1k_hop512_128bin_2024.02](https://github.com/openvpi/vocoders/releases/tag/nsf-hifigan-44.1k-hop512-128bin-2024.02)
* [pc_nsf_hifigan_44.1k_hop512_128bin_2025.02](https://github.com/openvpi/vocoders/releases/tag/pc-nsf-hifigan-44.1k-hop512-128bin-2025.02)
* [Kouon NSF-HiFiGAN Vocoder 20240710](https://github.com/Kouon-Vocoder-Project/Kouon_Vocoder/releases/tag/V1.0.0)
* [kouon_nsf-hifigan_1031](https://github.com/Kouon-Project/Kouon_Vocoder/releases/tag/V2.0.0)
* [HiFiPLN v1](https://utau.pl/vocoders/hifipln-v1/)
* [HiFiPLN v2](https://utau.pl/vocoders/hifipln-v2/)

# External batch
* [convel-batch-edit.dll](https://github.com/AnAndroNerd/Small-VCCV-Changes/releases/tag/dll)

# For Developers
## Favor
When creating dependency files, please register the package information in [svs-index](https://openutau.github.io/svs-index/).  
You can install external dependency files using the package manager included in OpenUtau.
## oudep file specifications
A file created by changing the extension of a zip archive containing oudep.yaml.
Dependency files will be stored in the Dependencies folder.

### Structure of oudep.yaml
```yaml
# ID (only lowercase alphanumeric characters, "-", and "." are allowed). Must be unique across all software.
id: g2p-cmudict-07b
# Version notation (e.g., 1.0 or 1.0.0.0). build and revision can be omitted.
version: '1.0'
# Summary of the package
description: G2P based on CMU Pronouncing Dictionary 0.7b
# Class designation (optional)
class: G2pPackV2
```