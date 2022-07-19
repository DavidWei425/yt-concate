from yt_concate.pipeline.steps.get_vedioID import GetVideoID
from yt_concate.pipeline.pipeline import Pipeline

channel_id = "UCKSVUHI9rbbkXhvAXK-2uxA"


def main():
    inputs = {
        'channel_id': channel_id,
    }
    steps = [
        GetVideoID(),
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':  # 檢查程式的進入點是否為main,是的話才執行main(),否則break
    main()
