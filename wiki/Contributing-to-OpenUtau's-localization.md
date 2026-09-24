OpenUtau uses crowdin for localization, which provides a friendly UI for users. Even if you don't know how to code, you can contribute to OpenUtau's localization.

## Usage
Visit [OpenUtau's Crowdin page](https://crowdin.com/project/oxygen-dioxideopenutau), log in

![image](https://github.com/user-attachments/assets/b8828f8a-8a4b-4ee5-b6c6-158301ea6878)

Select the language you want to contribute to, and click "Strings.xaml"

![image](https://github.com/user-attachments/assets/8a44cfcd-e2bc-4993-bd12-52bd32d98413)

You can edit each string item. Untranslated strings are listed first. After editing, click "save".

## How it works
In Crowdin, English is treated as the original language, and other languages are treated as translations.

At 12:00 UTC+8 every day, [Crowdin GitHub Actions](https://github.com/oxygen-dioxide/OpenUtau/actions/workflows/crowdin.yml) runs, which does the following things:
- Sync English strings from OpenUtau official repo to Crowdin.
- Sync translations from Crowdin to [oxygen-dioxide/OpenUtau:crowdin-translated](https://github.com/oxygen-dioxide/OpenUtau/tree/crowdin-translated)

Before each OpenUtau release, a pull request will be made from oxygen-dioxide/OpenUtau:crowdin-translated to official repo that applies latest updates to OpenUtau build.

## Notes for power users
- To keep track of what's going on in Crowdin, see https://crowdin.com/project/oxygen-dioxideopenutau/activity-stream
- For a list of what has been changed on crowdin since the last OpenUtau release (syncs from crowdin every day), in other words, what we will see in the next update, see https://github.com/stakira/OpenUtau/compare/master...oxygen-dioxide:OpenUtau:crowdin-translated 

## FAQ
### I'm a code contributor. I want to introduce a new feature with new strings. What should I do?
When creating your pull request to OpenUtau, **only add new strings to the English String.axaml**.

If you want to add this string to another language that you speak, after your pull request is merged, wait a day, and update strings on Crowdin.

Note: Never use machine translation to localize strings. For languages you don't understand, leave it blank and wait until a native contributor picks it up. Falling back to English string is still better than a confusing localized string.

### I've posted my contributions to Crowdin. When will it be applied to OpenUtau?
Crowdin updates won't be applied to your OpenUtau installation immediately. It will be applied on each OpenUtau release. You can [switch to beta version](https://github.com/stakira/OpenUtau/wiki/Getting-Started#beta-version) which is more updated, but you still need to wait until next beta release (Usually once a month) to see latest string updates.