import os
# 在seetings資料夾定義global variable
# 在settings資料夾設定之後產生的檔案要存在哪個資料夾
DOWNLOADS_DIR = 'downloads'  # 影片原始檔下載後存放的資料夾
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions')  # 字幕產生後存放的資料夾,在DOWNLOADS之下,用os的join定義路徑
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos')  # 影片存放的資料夾,在DOWNLOADS之下,用os的join定義路徑

