import os

from yt_concate.settings import DOWNLOADS_DIR
from yt_concate.settings import VIDEOS_DIR
from yt_concate.settings import CAPTIONS_DIR


class Utils:
    def __init__(self):
        pass

    def get_caption_path(self, ids):  # 字幕的檔案命名需要用另外一個方式執行,否則會產生重複的檔名,這邊用video id命名,且存放路徑也從settings定義好了
        return os.path.join(CAPTIONS_DIR, ids + '.txt')

    def create_dir(self):  # 自動建立資料夾
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
