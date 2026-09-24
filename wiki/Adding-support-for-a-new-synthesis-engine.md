OpenUtau is an open source singing synthesis platform. Anyone who develops their singing synthesis engine can use OpenUtau as its UI. This article introduces how to add support for a new synthesis engine, taking [DiffSinger](https://github.com/stakira/OpenUtau/pull/882) as an example. DiffSinger is a typical machine learning based singing synthesis engine that uses the classic packaging format

## Design singer packaging format
Singer packaging format is how users of your synthesis engine will build and distribute their voicebanks. We suggest using the classic packaging format if possible, which is the same packaging format that UTAU, ENUNU and DiffSinger singers use. Using the classic packaging format will make your voicebank compatible with the latest universal features of OpenUtau in future updates.

Here is the folder structure of classic packaging format
```
your_singer
├─ character.txt
├─ character.yaml
├─ ...the other files and folders containing the voice data.
```

character.txt and character.yaml contain the basic information of your voicebank, including the name of your voicebank, type of your voicebank and the phonemizer it uses

character.txt example:
```ini
name=Zhibin Diffsinger
image=zhibin.png
author=Chisong
voice=Chisong
web=http://zhibin.club/
```

character.yaml example:
```yaml
text_file_encoding: utf-8
portrait_opacity: 0.67
default_phonemizer: OpenUtau.Core.DiffSinger.DiffSingerPhonemizer
singer_type: diffsinger
```

Tips for designing your packaging format:
- Use only lower-cased ascii characters for filenames if possible, because ascii characters don't get garbled on a PC in different locales.
- Use a special prefix for file names and folder names. For example, in DiffSinger voicebanks, `dsdur`, `dspitch`, `dsvariance`, `dsconfig` and `dsvocoder` start with "ds". This perfix clearly states that these files are used by diffsinger renderer.

## Define singer type
To define a singer type, you'll need to create a singer class that inherits [USinger](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/Ustx/USinger.cs#L205). Here are some important features you need to implement in this class:
- object initializer: Load avatar, subbanks (voice colors), phonemes list in object initializer
- `FreeMemory`: If your voicebank stores large resources in memory, use this function to free them when the singer is no longer used. Note that the voicebank may be used again even after this method is called, and this method may be called even when the singer has not been used.

An example is [DiffSingerSinger](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/DiffSinger/DiffSingerSinger.cs)

You also have to regist your singer type to everywhere else in OpenUtau's codebase that works differently according to singer type, including:
- [OpenUtau.Core/Ustx/USinger.cs](https://github.com/stakira/OpenUtau/blob/d4b3cc2bd180d7fdcb7c459ec6aa99bde4273cf7/OpenUtau.Core/Ustx/USinger.cs#L188-L203)
- [OpenUtau.Core/Classic/ClassicSingerLoader.cs](https://github.com/stakira/OpenUtau/blob/d4b3cc2bd180d7fdcb7c459ec6aa99bde4273cf7/OpenUtau.Core/Classic/ClassicSingerLoader.cs#L10-L15)
- [OpenUtau.Core/Render/Renderers.cs](https://github.com/stakira/OpenUtau/blob/d4b3cc2bd180d7fdcb7c459ec6aa99bde4273cf7/OpenUtau.Core/Render/Renderers.cs#L11-L36) (associate your singer type to your renderer)
- [OpenUtau/ViewModels/SingerSetupViewModel.cs](https://github.com/stakira/OpenUtau/blob/master/OpenUtau/ViewModels/SingerSetupViewModel.cs#L33)

## Add a renderer for your synthesis engine
Starting from here, we'll add our synthesis code into OpenUtau. Create a new folder under [OpenUtau.Core](https://github.com/stakira/OpenUtau/tree/master/OpenUtau.Core) and put all the code for your synthesis engine there.

A renderer should implement [IRenderer](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/Render/IRenderer.cs). Here are the main features of a renderer:
- `Render`: Synthesize audio based on RenderPhrase input
- `LoadRenderedPitch`: Auto generate pitch curve based on RenderPhrase input (optional, use `SupportsRenderPitch` to declare)
- `SupportsExpression`: Declare the expressions that your engine supports.
- `GetSuggestedExpressions`: If your engine supports custom expressions, use this API to provide them to the user.

An example is [DiffSingerRenderer](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/DiffSinger/DiffSingerRenderer.cs)

## Add phonemizers for your synthesis engine
OpenUtau's phonemizer is independent from renderer. If existing phonemizers already meet your needs, you won't need to write your own phonemizers.

If you're going to write a phonemizer, see [[Developing new phonemizers]]

If your phonemizer is based on machine learning models, you can inherite [MachineLearningPhonemizer](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/MachineLearningPhonemizer.cs) where you need to implement the `ProcessPart` function that takes phrases and write the timing results into `partResult`. [DiffSingerBasePhonemizer](https://github.com/stakira/OpenUtau/blob/master/OpenUtau.Core/DiffSinger/DiffSingerBasePhonemizer.cs) is an example.