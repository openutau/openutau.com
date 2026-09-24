# What Is a Singer?
Since OpenUtau supports not only UTAU voice banks but also machine learning models such as DiffSinger, we collectively refer to these voicebanks as "Singers."

# Conditions for Using Singers in OpenUtau
OpenUtau loads voice banks located in the "Singers" folder and in the "Additional Singer Path."
The location of the "Singers" folder varies depending on your OS and installation method (whether you used the installer version or the portable version).
You can specify the "Additional Singer Path" in the preferences.

Singers are loaded based on the `character.txt` file. Banks that do not include a `character.txt` will not be recognized as singers.

For classic UTAU voice banks, basic formats such as wav and oto.ini conform to the original UTAU standards.
The wav formats you can use depend on the resampler you want to use.
While the original UTAU only loaded wav files located in the voice bank’s subfolders, OpenUtau loads all wav files even in deep subfolders beyond the second level. Additionally, there is effectively no limit on the number of aliases.

# Singer Window
You can open the Singer Window from the `Tools > Singers` menu in the Main Window.
In the Singer Window, you can primarily configure Singer settings, otoing, and Voice Color (equivalent to prefix.map).

## Singer Settings
You can configure various Singer settings by clicking the gear button.

Notes: The settings configured here are saved to `character.yaml`. This is a file specific to OpenUtau and does not affect the settings when loading the voice bank into the original UTAU.

- Set Icon and Portrait: You can select a small icon and a character sprite to display as the piano roll background.
- Set Encoding: Setting the appropriate text encoding ensures that text files such as `oto.ini` can be loaded without garbled characters.
- Set Singer Type: Set the type, such as `utau`, `enunu`, or `diffsinger`. If the wrong type is selected, rendering may not work properly.
- Set Default Phonemizer: If you select a default Phonemizer here, it will be automatically applied when you choose a singer.
- Use Filename as Alias: Some older Japanese CV banks are distributed without aliases, assuming the filename will be used as-is. This option is provided for backward compatibility.
- Publish Singer: You can create a ZIP file for distributing the voice bank.
- Merge with another voicebank: You can load an append voicebank into the main voicebank and merge them.
- Generate Singer Error Report: You can check for any issues with the oto or the WAV file format.

## Oto settings
There is a simple otoing editor.
You can also call external oto editors (vLabeler and setParam).

Right-clicking on each line allows you to open the wav folder or regenerate the frq file.

## Voice Color
Voice Color is a feature that integrates append bank management with prefix.map.

### What is prefix.map?
Essentially, prefix.map is a system for handling multi-pitch banks.
By appending recorded pitches—such as "a_C4" or "a_F4"—to the suffix of an alias, and mapping the pitch range to the suffix, the system automatically switches between sub-banks based on the note’s pitch.
For example, you can configure it to use "a_C4" in the lower register and "a_F4" in the higher register.

While the prefix.map file allows you to enter both a prefix (like `C4/a`) and a suffix (like `a_C4`), the prefix is a specification from UTAU’s early days and is rarely used.

### What is Voice Color?
In UTAU voicebanks that include append banks like Power or Soft, the recorded pitches may differ for each append banks.
This means you would need to prepare a separate `prefix.map` file for each append banks, but this is not part of the original UTAU specification.
Therefore, as a feature unique to OpenUTAU, we have Voice Color—a system that allows you to register expression names and suffixes for each pitch range for each append bank.

This means that even with voicebanks that have complex structures, you can seamlessly switch between the wav sources just by selecting a Voice Color.

### Editing Voice Color
Click the "Edit Subbanks" button in the Singer window to open the dialog where you can set suffixes for each vocal range.

First, select a Color in the upper-right corner. `(main)` is the default Color.
To add a new Color, click "Add Color."

Select a pitch (hold down Shift to select multiple), enter the suffix in the field on the right, and click "Set" to apply the changes.

If you already have a prefix.map file, you can import it. It will be imported as the map for the currently selected Color.

Click "Save" to save the settings to `character.yaml`.