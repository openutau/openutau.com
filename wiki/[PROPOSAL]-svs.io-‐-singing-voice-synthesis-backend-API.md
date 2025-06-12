[Discussion Here](https://github.com/stakira/OpenUtau/discussions/433)

This proposal describes a msgpack-based API for SVS backends.

ML based SVS often has **different data flows**. Some intakes notes and outputs audio samples, end to end. Some have intermediate steps, such as phonemes and f0 curve. To accommodate such needs, this API is designed to be flexible. It defines some data structs and a single API `ops`, and allows the backend to **document its own API graph**. Then the frontend finds out the order to call these APIs from the graph.

There is not a hard requirement, but the preferred transport of these msgpack objects is ZeroMQ. The choice is based on ZeroMQ's simplicity and flexibility. Without going into too many details here, it's a very easy IPC setup, and works locally or remotely. 

```
 ┌──────────────────────────────┐          ┌───────────────────────────────┐
 │                              │          │                               │
 │  ┌──────────┐  ┌──────────┐  │          │  ┌──────────┐  ┌───────────┐  │
 │  │          │◄─┤          │◄─┼──────────┼──┤          │◄─┤           │  │
 │  │    UI    │  │  svs.io  │  │  ZeroMQ  │  │  svs.io  │  │ algorithm │  │
 │  │          ├─►│          ├──┼──────────┼─►│          ├─►│           │  │
 │  └──────────┘  └──────────┘  │          │  └──────────┘  └───────────┘  │
 │           Frontend           │          │            Backend            │
 └──────────────────────────────┘          └───────────────────────────────┘
```

## Data Structs
### `note_sequence`
```json
{
  "time_unit": "ms", // s, ms or us
  "notes": [
    {
      "lyric": "", // rest note. practically all note sequences should start with a rest note since the voice usually starts before the note.
      "duration": 500.0,
      "key": 60,
      "flag:timbre": "Falsetto", // flags are optional, names can be arbitrary, backend can decide how to use them.
      "flag:gender": 0,
    }, {
      "lyric": "hua",
      "duration": 500.0,
      "key": 60, // midi spec, C4 = 60
    }
  ]
}
```
### `phoneme_sequence`
```json
{
  "time_unit": "ms",
  "phonemes": [
    {
      "note_index": 0, // used by frontend to map phonemes to notes
      "phoneme": "", // rest note
      "duration": 400.0,
      "key": 60,
      "flag:timbre": "Falsetto", // flags are optional, names can be arbitrary, backend can decide how to use them.
      "flag:gender": 0
    }, {
      "note_index": 1,
      "phoneme": "h", // h from hua, starts 100ms before first note
      "duration": 200.0,
      "key": 60
    }, {
      "note_index": 2,
      "phoneme": "ua", // ua from hua
      "duration": 400.0,
      "key": 60
    }, {
      "note_index": 3,
      "phoneme": "", // rest note
      "duration": 500.0,
      "key": 60
    } 
  ]
}
```
### `f0`
`f0` is a curve that can be edited by the user after generation.
```json
{
  "time_unit": "ms",
  "frame_duration": "5", // 5ms per frame
  "f0": [6000, 6000, 6000, 6000, 6000, ...] // cents (MIDI key * 100) , each number is a frame
}
```
### `curve:<name>`
If a curve name appears only in inputs, it becomes a user input.
If a curve name appears in both inputs and outputs, it becomes pass-through data. I.e., one API generates and the frontend passes it to another API.
```json
{
  "time_unit": "ms",
  "frame_duration": "5", // 5ms per frame
  "range": [-100, 100], // only used if editable
  "scale": "linear", // "linear", "log", "log2", "log10" or "db",
  "curve": [0, 0, 0, 0, 0, ...]
}
```
### `world_mgc`, `world_sp`, `world_bap`, `world_ap`
```json
{
  "time_unit": "ms",
  "frame_duration": 5, // 5ms per frame
  "width": 60,
  "world_mgc": [
    [0, 0, 0, ...], // first frame, length = 60
    [0, 0, 0, ...], // second frame, length = 60
    ...
  ]
}
```
### `audio_samples`
```json
{
  "channels": 1, // probably should always be 1
  "sample_rate": 44100, // or 22500, 48000, etc.
  "sample_format": "int16", // "int8", "int16", "int32" or "float"
  "channels": [
    "samples": [0, 0, 0, ...]
  ]
}
```
## API
### `ops`:
This API describes all available operations of a backend. This helps the frontend to understand how to call the APIs to transform note sequences to audios.

Example request:
```json
{
  "op": "ops"
}
```
Example Response (NNSVS):
```json
{
  "name": "ENUNU",
  "version": "0.5.0",
  "ops": [
    {
      "op": "phonemize", // op names are free for backends to define
      "inputs": {
        "note_sequence": {
          "required": true,
        }
      }, // input and output data structs are predefined as above
      "outputs": {
        "phoneme_sequence": {
        }
      }
    },
    {
      "op": "synth_world_features",
      "inputs": {
        "phoneme_sequence": {
          "required": true,
        }
      },
      "outputs": {
        "world_mgc": {
          "time_unit": "ms",
          "frame_duration": 5,
          "width": 60
        },
        "world_bap": {
          "time_unit": "ms",
          "frame_duration": 5,
          "width": 5
        },
        "f0": {
          "time_unit": "ms",
          "frame_duration": 5
        }
      }
    }
  ]
}
```
Example Response (Renderer with ML vocoder):
```json
{
  "name": "SomeRenderer",
  "version": "1.0",
  "ops": [
    {
      "op": "phonemize",
      "inputs": {
        "note_sequence": {
          "required": true,
        }
      },
      "outputs": {
        "f0": {
          "time_unit": "ms",
          "frame_duration": 5
        },
        "phoneme_sequence": {
        }
      }
    },
    {
      "op": "synth_audio_samples",
      "inputs": {
        "f0": {
          "required": true,
          "time_unit": "ms",
          "frame_duration": 5
        },
        "phoneme_sequence": {
          "required": true
        },
        "curve:gender": {
          "required": false,
          "range": [-100, 100],
          "scale": "linear",
        },
        "curve:tension": {
          "required": false,
          "range": [-100, 100],
          "scale": "linear",
        },
        "curve:strength": {
          "required": false,
          "range": [-20, 20],
          "scale": "db",
        }
      },
      "outputs": {
        "audio_samples": {
          "channels": 1,
          "sample_rate": 44100,
          "sample_format": "int16"
        }
      }
    }
  ]
}
```

- At minimal, a renderer should implement a direct or indirect path from `note_sequence` to:
  - Either (`world_mgc` or `world_sp`) and (`world_bap` or `world_ap`)
  - Or `audio_samples`
- `f0` is optional. The frontend can use it as a base for further user editing. Otherwise, the frontend still can use `f0` created by the user.
- This is the only required API for a backend. Any other APIs are defined by the backend and returned via this API.
- This API can also be used to check if the backend is started, or still alive. If the backend does not return in 1 second, it is considered offline.

Other than the `ops` API, other APIs are very simple. Just constructs a msgpack object with the `op` name and required data structs.

### Example API: NNSVS `phonemize`

Example request:
```json
{
  "op": "phonemize",
  "note_sequence": {
    "phoneme_sequence": [...] // as defined earlier
  }
}
```
Example Response:
```json
{
  "phoneme_sequence": [...] // as defined earlier
}
```

### Example API: NNSVS `synth_world_features`

Example request:
```json
{
  "op": "synth_world_features",
  "phoneme_sequence": [...] // as defined earlier
}
```
Example Response:
```json
{
  "world_mgc": [...],
  "world_bap": [...],
  "f0": [...]
}
```
