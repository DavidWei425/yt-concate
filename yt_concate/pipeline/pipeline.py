from yt_concate.pipeline.steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps  # 為了讓pipeline class在main主程式裡面能夠呼叫steps

    def run(self, inputs):  # 定義在run這個class的時候要取用main主程式裡面的inputs
        data = None  # 每個step要把資料接收後加工然後再傳出去,所以要定義這個要用來傳遞的參數,而易剛開始沒有值,所以用None
        for step in self.steps:
            try:
                data = step.process(data, inputs)
            except StepException as e:
                print('Exception happened : ', e)
                break
        # 可視情況看要不要把data給return出來給下一個step用
