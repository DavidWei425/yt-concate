from abc import ABC  # ABC是一個helper class
from abc import abstractmethod


class Step(ABC):  # Step這個class繼承了ABC這個class的相關屬性
    def __init__(self):
        pass  # 因為是抽象class所以用空的method

    @abstractmethod  # 使用abstractmethod後,子class繼承後都需要宣告下面的method
    def process(self, data, inputs, utils):  # 所以繼承Step的子class就要宣告process這個method以及自己要使用到inputs字典裡的什麼參數
        pass


class StepException(Exception):  # 定義StepException來中止程式當運行時出現錯誤時,此class繼承python內建的Exception class
    pass
