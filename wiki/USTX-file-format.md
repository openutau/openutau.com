USTX is the project file format for OpenUtau. This document outlines the structure and semantics of the USTX format for developers building tools that process USTX files.

## Basic concepts
- Tick: the time unit in midi. 1 quarter note equals to 480 ticks.
- Midi number: tone representation in midi. C4 = 60. Unit is semitone

## File Structure
A USTX file is a YAML-based (YAML 1.2) text format in UTF-8 encoding, with the following top-level sections:

### UProject
| Field            | Type   | Description                                                                              |
|:-----------------|:-------|:-----------------------------------------------------------------------------------------|
| `name`           | string | Project name                                                                             |
| `ustx_version`   | string | USTX format version, currently 0.6                                                       |
| `resolution`     | int    | Ticks per quarter note, always 480                                                       |
| `key`            | int    | Musical key of the project, used for scale degree displaying. 0 means C major or A minor |
| `time_signature` | list   | List of time signature changes                                                           |
| `tempos`         | list   | List of tempo changes                                                                    |
| `tracks`         | list   | List of tracks                                                                           |
| `voice_parts`    | list   | List of voice parts (part containing notes for synthesis)                                |
| `wave_parts`     | list   | List of wave parts (external audio file, usually instrumental of the song)               |

`bpm`, `beat_per_bar` and `beat_unit` under the project root are deprecated. To get the tempo and time signatures, please use `tempos` and `time_signature`.

### Expressions
Defines vocal parameters (e.g., dynamics, vibrato) as curves or numerical values.  
Located under `expressions` as key-value pairs. Each expression has:
| Field           | Type   | Description                                                         |
|:----------------|:-------|:--------------------------------------------------------------------|
| `name`          | string | Human-readable name (e.g., `"dynamics (curve)"`)                    |
| `abbr`          | string | Short identifier (e.g., `"dyn"`)                                    |
| `type`          | string | `Curve`, `Options`, or `Numerical`                                  |
| `min`/`max`     | int    | Value range                                                         |
| `default_value` | int    | Default if not explicitly set                                       |
| `is_flag`       | bool   | Whether the parameter is a UTAU resampler flag                      |
| `flag`          | string | UTAU resampler flag symbol (e.g., `"g"` for gender)                 |
| `options`       | list   | For `Options` type: list of possible values (e.g., `["off", "on"]`) |

Example:
```yaml
dyn:
  name: dynamics (curve)
  abbr: dyn
  type: Curve
  min: -240
  max: 120
  default_value: 0
```


### Time and Tempo
- **Time Signatures** (`time_signatures`):  
  Defines changes in time signature. Each entry includes:
  - `bar_position`: Bar number where the change applies.
  - `beat_per_bar`: Numerator (e.g., `4` for 4/4).
  - `beat_unit`: Denominator (e.g., `4` for 4/4).

- **Tempos** (`tempos`):  
  Defines BPM changes. Each entry includes:
  - `position`: Tick position where the tempo change occurs.
  - `bpm`: BPM value.


### Tracks
Defines audio tracks under `tracks`. Each track includes:
| Field               | Type   | Description                                     |
|:--------------------|:-------|:------------------------------------------------|
| `singer`            | string | Voicebank identifier                            |
| `phonemizer`        | string | Phonemizer plugin                               |
| `track_name`        | string | Track label                                     |
| `track_color`       | string | Display color (e.g., `"Blue"`)                  |
| `mute`/`solo`       | bool   | Mute/solo state                                 |
| `volume`            | float  | Track volume (dB)                               |
| `voice_color_names` | list   | List of available voice colors in the voicebank |


### Voice Parts
Contains musical notes and phrases under `voice_parts`. Each part includes:
| Field      | Type   | Description                                    |
|:-----------|:-------|:-----------------------------------------------|
| `duration` | int    | Total duration in ticks                        |
| `name`     | string | Name of the part                               |
| `track_no` | int    | Index of the track that the part belongs to    |
| `position` | int    | Starting tick position relative to the project |
| `notes`    | list   | List of notes (see below)                      |
| `curves`   | list   | Curve expressions (see below)                  |

#### Note
Each note under `notes` has:
| Field                 | Type   | Description                                                                                           |
|:----------------------|:-------|:------------------------------------------------------------------------------------------------------|
| `position`            | int    | Start tick relative to the starting position voice part                                               |
| `duration`            | int    | Note length in ticks                                                                                  |
| `tone`                | int    | MIDI note number (e.g., `60` = C4)                                                                    |
| `lyric`               | string | Lyric text (e.g., `"san"`)                                                                            |
| `pitch`               | object | Pitch control points                                                                                  |
| `vibrato`             | object | Vibrato parameters (depth, period, fade-in/out)                                                       |
| `phoneme_expressions` | list   | Numerical and option expressions edited per phoneme by the user                                       |
| `phoneme_overrides`   | list   | Phoneme name and position (tick offset relative to the original phonemizer result) edited by the user |


Example:
```yaml
  - position: 1920
    duration: 720
    tone: 70
    lyric: san
    pitch:
      data:
      - {x: -274.03845, y: 0, shape: io}
      - {x: -158.65384, y: -32.46212, shape: io}
      - {x: 40, y: 0, shape: io}
      snap_first: true
    vibrato: {length: 0, period: 175, depth: 25, in: 10, out: 10, shift: 0, drift: 0, vol_link: 0}
    phoneme_expressions:
    - {index: 0, abbr: clr, value: 1}
    - {index: 1, abbr: clr, value: 2}
    phoneme_overrides:
    - index: 1
      phoneme: a
    - index: 0
      offset: 65
```

#### Curves
Defines automation curves (e.g., pitch, dynamics) under `curves`. 
| Field  | Type      | Description                                     |
|:-------|:----------|:------------------------------------------------|
| `xs`   | List<int> | Tick position of each sample point in the curve |
| `ys`   | List<int> | Value at each sample point                      |
| `abbr` | string    | Expression abbr                                 |

### Wave Parts
External audio files imported to the project, under `wave_parts`
| Field              | Type   | Description                                                                          |
|:-------------------|:-------|:-------------------------------------------------------------------------------------|
| `name`             | string | Name of the part                                                                     |
| `track_no`         | int    | Index of the track that the part belongs to                                          |
| `position`         | int    | Starting tick position relative to the project                                       |
| `relative_path`    | string | Path to the audio file relative to the .ustx file, absolute path if on another drive |
| `file_duration_ms` | float  | Duration of the audio file in milliseconds                                           |

## Developer notes
For python developers, please use `ruamel.yaml` when working with .ustx files, because it supports yaml 1.2 . Don't use `pyyaml`.

## References
The reading and writing of USTX files is officially implemented in [OpenUtau.Core/Ustx](https://github.com/stakira/OpenUtau/tree/master/OpenUtau.Core/Ustx)

Below are third-party implementations of USTX reading and writing:
- [Libresvip](https://github.com/SoulMelody/LibreSVIP/tree/main/libresvip/plugins/ustx), in python
- [Utaformatix](https://github.com/sdercolin/utaformatix3/blob/master/core/src/main/kotlin/core/io/Ustx.kt), in kotlin