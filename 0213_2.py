class Display:
    def __init__(self):
        print("文章を出力できるよ")

    def display(self, sentence):
        print(sentence)

class DecoDisplay(Display):
    def display(self, sentence):
        print("～" + sentence + "～")

display = DecoDisplay()
display.display("テスト")
