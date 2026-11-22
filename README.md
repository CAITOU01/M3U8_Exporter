# M3U8 Song Exporter

將資料夾內的 `.m3u8` 播放清單所引用的**本機檔案**，複製到與清單同名的資料夾。適合把清單中的音樂整理成可攜帶的檔案集合。

## 使用方式

需要 Python 3.10 以上，程式本身不需要額外安裝套件。

1. 將 `M3U8_exporter.py` 放在播放清單所在資料夾；或以命令列指定資料夾。
2. 確認 `.m3u8` 內的檔案路徑指向電腦上實際存在的檔案。
3. 執行：

   ```powershell
   python M3U8_exporter.py "D:\Music\Playlists"
   ```

   不指定資料夾時，會掃描程式所在資料夾。程式只掃描該資料夾第一層的 `.m3u8`。

例如 `Favorites.m3u8` 含有以下內容：

```m3u8
#EXTM3U
#EXTINF:180,Example Song
..\Music\example.mp3
```

執行後會建立 `Favorites\example.mp3`。相對路徑以播放清單所在資料夾為起點。支援 UTF-8 與含 BOM 的 UTF-8 清單；`#` 開頭的中繼資料行會略過。

現有目的檔不會覆寫。如果同名檔案內容不同，程式會顯示衝突並以非零狀態碼結束；請手動改名或調整清單。找不到來源檔案也會列出行號。這個工具只複製檔案，**不會重寫播放清單**，也不會下載網路串流網址。複製大量音樂前請確認磁碟剩餘空間，以及你對音樂檔案的使用權限。

## Windows 執行檔

已提供的 `M3U8_exporter.exe` 是獨立的舊版執行檔，操作方式是放在 `.m3u8` 旁執行。它不是由此倉庫修訂後的程式碼重新建置，建議在 GitHub **Releases** 中單獨上傳並標示為舊版，避免誤認為與目前原始碼完全一致。

若要從目前原始碼自行建置新版，先安裝 PyInstaller，再執行：

```powershell
python -m pip install pyinstaller
python -m PyInstaller --onefile --console --name M3U8_exporter M3U8_exporter.py
```

完成後的檔案位於 `dist\M3U8_exporter.exe`。建置工具是開發需求，執行 Python 原始碼不需要它。

## 驗證

```powershell
python -m unittest discover -s tests -v
```
