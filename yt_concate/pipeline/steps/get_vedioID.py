import scrapetube

from yt_concate.pipeline.steps.step import Step  # 用絕對路徑來import先前定義的class


class GetVideoID(Step):
    def process(self, data, inputs):  # 因為在step class裡面有宣告def process是@abstractmethod,所以子class繼承後要宣告
        videos = scrapetube.get_channel(inputs['channel_id'])
        lst1 = []
        for video in videos:
            lst1.append(video['videoId'])
        print(len(lst1))
