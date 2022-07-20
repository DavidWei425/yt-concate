from yt_concate.pipeline.steps.get_vedioID import GetVideoID
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.utils import Utils
from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.postflight import Postflight

channel_id = "UCKSVUHI9rbbkXhvAXK-2uxA"

def main():
    inputs = {
        'channel_id': channel_id,
    }
    steps = [
        Preflight(),
        GetVideoID(),
        DownloadCaptions(),
        Postflight(),
    ]
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':  # 檢查程式的進入點是否為main,是的話才執行main(),否則break
    main()
