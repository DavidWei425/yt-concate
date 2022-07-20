from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

from yt_concate.pipeline.steps.step import Step


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        for ids in data:
            try:
                caption = YouTubeTranscriptApi.get_transcript(ids)
                formatter = TextFormatter()
                # .format_transcript(transcript) turns the transcript into a Text string.
                text_formatted = formatter.format_transcript(caption)
                # Now we can write it out to a file.
            except:
                print('captions error for video', ids)
                continue
            with open(utils.get_caption_path(ids), 'w', encoding='utf-8') as text_file:
                text_file.write(text_formatted)
        return caption
