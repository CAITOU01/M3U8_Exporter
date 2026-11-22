import os
import shutil
import sys

def extract_songs_from_m3u8():
    # --- Auto-detect execution path ---
    if getattr(sys, 'frozen', False):
        current_dir = os.path.dirname(sys.executable)
    else:
        current_dir = os.path.dirname(os.path.abspath(__file__))

    print(f"--- M3U8 Song Extractor ---")
    print(f"Scanning directory: {current_dir}\n")

    count_total = 0
    # Iterate through all .m3u8 files in the current directory
    for filename in os.listdir(current_dir):
        if filename.lower().endswith(".m3u8"):
            m3u8_path = os.path.join(current_dir, filename)
            
            # 1. Create a folder with the same name as the M3U8 file (without extension)
            folder_name = os.path.splitext(filename)[0]
            target_dir = os.path.join(current_dir, folder_name)
            
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
                print(f" Created folder: {folder_name}")

            # 2. Read M3U8 content
            try:
                with open(m3u8_path, 'r', encoding='utf-8-sig') as f:
                    lines = f.readlines()
                
                print(f"🎵 Processing playlist: {filename}")
                
                copied_count = 0
                for line in lines:
                    line = line.strip()
                    # Skip empty lines and M3U8 metadata tags (e.g., #EXTM3U)
                    if not line or line.startswith("#"):
                        continue
                    
                    # Determine if the path is absolute or relative
                    source_path = line
                    if not os.path.isabs(source_path):
                        source_path = os.path.join(os.path.dirname(m3u8_path), line)

                    # 3. Copy the audio file
                    if os.path.exists(source_path):
                        song_name = os.path.basename(source_path)
                        dest_path = os.path.join(target_dir, song_name)
                        
                        # Skip if a file with the same name already exists
                        if not os.path.exists(dest_path):
                            shutil.copy2(source_path, dest_path)
                            copied_count += 1
                    else:
                        print(f"    File not found: {source_path}")

                print(f"    Successfully copied {copied_count} song(s).")
                count_total += copied_count
            except Exception as e:
                print(f"    Error reading {filename}: {e}")

    print(f"\n--- Task Completed ---")
    print(f"Extracted {count_total} audio file(s) in total.")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    extract_songs_from_m3u8()