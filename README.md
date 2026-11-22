# M3U8 Song Exporter

Copy local audio files referenced by `.m3u8` playlists into folders named after their playlists. This is useful for collecting the files in a playlist into a portable folder.

## Requirements

- Python 3.10 or newer
- No third-party packages are required to run the Python script

## Usage

1. Put `M3U8_exporter.py` in the folder containing your playlists, or pass that folder as an argument.
2. Make sure the paths in each `.m3u8` playlist point to files that exist on your computer.
3. Run:

   ```powershell
   python M3U8_exporter.py "D:\Music\Playlists"
   ```

If you omit the folder argument, the program scans the folder containing the script or executable. It scans only `.m3u8` files directly in that folder, without searching subfolders.

For example, given `Favorites.m3u8`:

```m3u8
#EXTM3U
#EXTINF:180,Example Song
..\Music\example.mp3
```

The program creates `Favorites\example.mp3`. Relative paths are resolved from the playlist's folder. UTF-8 playlists with or without a byte order mark (BOM) are supported. Empty lines and metadata lines beginning with `#` are ignored.

Existing destination files are never overwritten. If another source file has the same name but different contents, the program reports a collision and exits with a nonzero status. Missing source files are reported with their playlist line numbers. Resolve these issues by renaming the files or adjusting the playlist.

This tool copies files; it does **not** rewrite playlists or download files from streaming URLs. Check available disk space before copying large collections, and make sure you have the rights to use the audio files.

## Windows executable

The previously supplied `M3U8_exporter.exe` is a standalone build of an **earlier version**. Place it next to your `.m3u8` files and run it. It was not rebuilt from the revised source code in this repository. If you publish that file, attach it separately to a GitHub Release and label it as an older build so users do not assume it matches the current source.

To build a new executable from the current source, install PyInstaller and run:

```powershell
python -m pip install pyinstaller
python -m PyInstaller --onefile --console --name M3U8_exporter M3U8_exporter.py
```

The resulting file is `dist\M3U8_exporter.exe`. PyInstaller is only needed to build an executable; it is not needed to run the Python script.

## Tests

```powershell
python -m unittest discover -s tests -v
```

## License

No open-source license is currently granted. All rights are reserved. Public access to this source code does not grant permission to copy, modify, or redistribute it. A license can be added later if the owner chooses to grant those rights.
