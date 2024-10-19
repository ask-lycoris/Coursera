# Animalクラスは、基本的な動物の属性と動作を定義
class Animal:
    name = ""
    category = ""
    
    def __init__(self, name):
        self.name = name
    
    def set_category(self, category):
        self.category = category

# TurtleクラスはAnimalを内部に持つ
class Turtle(Animal):
    category = "reptiles"
    
    def __init__(self, name="turtle"):
        self.animal = Animal(name)
        self.animal.set_category(self, Turtle.category)

# インスタンス化を忘れずに！
turtle = Turtle()
# これはインスタンス化であって、変数定義とは別物。
# なのでturtleがこれ以降のコードで使用されていなくても問題ない
# ※変数定義のための記述：クラスやインスタンスが持つデータを定義するために行う（クラス変数、インスタンス変数）。
# ※インスタンス化のための記述：クラスから実際のオブジェクトを生成し、そのオブジェクトを使ってメソッドやデータを操作するために行う。


print(Turtle.category)

### Pythonでは例えばsuper() を使用して、多重継承（複数の親クラスから継承する）が可能ですが、継承の階層が複雑になると、
### どの親クラスからどの機能が引き継がれるかを追跡するのが困難になることがあります。
### コンポジションはこの問題を避け、オブジェクトの構造をシンプルに保てます。
