
# Page configuration for the OpenUtau docs site.
# title: sidebar title | parent/ord: nav position | lang_of: English counterpart permalink
PAGES = {
    "Home": dict(title="Home", ord=1),
    "Install": dict(title="Install", parent="Home", ord=1),
    "Getting-Started": dict(title="Getting Started", parent="Home", ord=2),
    "Keyboard-Shortcuts": dict(title="Keyboard Shortcuts", parent="Home", ord=3),
    "FAQ": dict(title="FAQ", parent="Home", ord=4),
    "Expressions-(Flags)": dict(title="Expressions (Flags)", parent="Home", ord=5),
    "Phonemizers": dict(title="Phonemizers", parent="Home", ord=6),
    "Resamplers-and-Wavtools": dict(title="Resamplers and Wavtools", parent="Home", ord=7),
    "Singer-Settings-and-Requirements": dict(title="Singer Settings and Requirements", parent="Home", ord=8),
    "Tutorials": dict(title="Tutorials", parent="Home", ord=9),
    "DiffSinger-support": dict(title="DiffSinger Support", parent="Home", ord=10),
    "ENUNU-NNSVS-Support": dict(title="ENUNU & NNSVS Support", parent="Home", ord=11),
    "VOICEVOX-support": dict(title="VOICEVOX Support", parent="Home", ord=12),
    "Legacy-Plugins": dict(title="Legacy Plugins", parent="Home", ord=13),
    "Known-Bugs": dict(title="Known Bugs", parent="Home", ord=14),
    "Release-Notes": dict(title="Release Notes", parent="Home", ord=15),

    "Developer-Guide": dict(title="Developer Guide", ord=2),
    "Compiling-from-source": dict(title="Compiling from Source", parent="Developer Guide", ord=1),
    "Compiling-G2p-Models": dict(title="Compiling G2p Models", parent="Developer Guide", ord=2),
    "Dependency": dict(title="Dependency", parent="Developer Guide", ord=3),
    "Developing-new-phonemizers": dict(title="Developing New Phonemizers", parent="Developer Guide", ord=4),
    "Adding-support-for-a-new-synthesis-engine": dict(title="Adding a Synthesis Engine", parent="Developer Guide", ord=5),
    "Voicebank-development": dict(title="Voicebank Development", parent="Developer Guide", ord=6),
    "USTX-file-format": dict(title="USTX File Format", parent="Developer Guide", ord=7),
    "Fork-OpenUtau-and-develop-a-new-editor": dict(title="Fork OpenUtau for a New Editor", parent="Developer Guide", ord=8),
    "Contributing-to-OpenUtau's-localization": dict(title="Contributing to Localization", parent="Developer Guide", ord=9),
    "tech-note-\u2010-character.yaml": dict(title="Tech Note: character.yaml", parent="Developer Guide", ord=10),
    "tech-note-\u2010-music-is-music,-phonetics-is-phonetics-(also-why-you-don't-need-legacy-plugins)":
        dict(title="Tech Note: Music is Music, Phonetics is Phonetics", parent="Developer Guide", ord=11),
    "[PROPOSAL]-svs.io-\u2010-singing-voice-synthesis-backend-API":
        dict(title="[PROPOSAL] svs.io Backend API", parent="Developer Guide", ord=12),

    # localized variants: reachable, but out of the main sidebar
    "FAQ\uff08\u65e5\u672c\u8a9e\uff09": dict(title="FAQ (日本語)", lang_of="FAQ"),
    "Home\uff08\u65e5\u672c\u8a9e\uff09": dict(title="Home (日本語)", lang_of="Home"),
    "Phonemizers\uff08\u65e5\u672c\u8a9e\uff09": dict(title="Phonemizers (日本語)", lang_of="Phonemizers"),
    "Resampler\u3068Wavtool(\u65e5\u672c\u8a9e)": dict(title="ResamplerとWavtool (日本語)", lang_of="Resamplers-and-Wavtools"),
    "スターターガイド-(日本語)": dict(title="スターターガイド (日本語)", lang_of="Getting-Started"),
    "チュートリアル-(日本語)": dict(title="チュートリアル (日本語)", lang_of="Tutorials"),
    "従来のプラグイン（日本語）": dict(title="従来のプラグイン (日本語)", lang_of="Legacy-Plugins"),
    "技術メモ-\u2010-character.yaml": dict(title="技術メモ: character.yaml", lang_of="tech-note-\u2010-character.yaml"),
    "教程汇总-(中文)": dict(title="教程汇总 (中文)", lang_of="Tutorials"),
    "한국어-시작-가이드": dict(title="한국어 시작 가이드", lang_of="Getting-Started"),
}

# manual fixes for links to pages that no longer exist
RETIRED = {
    "Status-of-ENUNU-NNSVS-Support": "ENUNU-NNSVS-Support",
}
