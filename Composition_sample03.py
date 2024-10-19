# Animalクラスは、基本的な動物の属性と動作を定義
class Animal:
    name = ""
    category = ""

    # 初期化
    def __init__(self, name):
        self.name = name

    # nameだけ毎回初期化して、categoryは別のメソッドにしているのは、コンポジションを使用する前提で記述してるから
    # 書こうと思えば、categoryもコンストラクタの中に記述できる
    # class Animal:
    # def __init__(self, name, category):   こんな感じに。
    # 柔軟性が求められる場合や、外部依存の要素がある場合、コンストラクタ内に最初からすべてのattributesを
    # 入れると設計が固くなりすぎるため、set_ メソッドのようなものを使って後から設定する方法が適している。
    # コンストラクタは初期化を行う重要な部分だが、必ずしもすべての設定をそこで行う必要はなく、
    # 状況に応じて柔軟に設計することが重要である。詳細はsample04に記載する。
        
        # インスタンス変数の初期化
        self.name = name  # 各インスタンスに固有の名前を設定
        self.category = category  # 各インスタンスに固有のカテゴリーを設定

# インスタンス化するときにコンストラクタが自動で呼ばれる
lion = Animal("Lion", "Mammal")
elephant = Animal("Elephant", "Mammal")

print(lion.name)  # 出力: Lion
print(elephant.category)  # 出力: Mammal

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

### 次に、動物園にたくさんの種類の動物（カメやヘビなど）がいるとして、同じカテゴリ(哺乳類や爬虫類など)の動物は
### 合計で何種類いるのか合計を計算するプログラムを作成する。
class Zoo:
    # 初期化
    def __init__(self):
        self.current_animals = {}
    
    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category
    
    def total_of_category(self, category):
        result = 0
        # 辞書型のキー(今回はname)に対応する値(今回はcategory)だけ取り出すため、.values
        for animal_category in self.current_animals.values():
            if animal_category == category:
                result += 1
        return result

# インスタンス化忘れずに！
zoo = Zoo()
turtle = Turtle()
snake = Snake()

# 関数を動作させる
zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_of_category("reptiles")) #how many zoo animal types in the reptile category
