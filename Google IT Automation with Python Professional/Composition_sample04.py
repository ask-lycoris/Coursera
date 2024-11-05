### コンストラクタにすべてを定義している場合 ###
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, brand, horsepower):
        self.brand = brand
        self.engine = Engine(horsepower)  # コンストラクタ内でエンジンを生成

# すべてが初期化時に設定される
car = Car("Toyota", 150)
print(f"{car.brand} with {car.engine.horsepower} HP")


### コンポジションで後から定義する場合 ###
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine = None  # 初期化時はエンジンが設定されていない
                            # 今回は記載しているが、特段記載しなくてもよい。
                            # コンポジションを使用する際に、後から設定される可能性がある属性は None で初期化しておくことは、
                            # 開発者にとって非常に優しい設計である。
                            # コードが意図通りに動作することを保証し、エラーの防止や可読性の向上が期待できる。

    def set_engine(self, engine):
        self.engine = engine  # 後からエンジンを設定できる

# Carのインスタンスを作成後にエンジンを設定
car = Car("Toyota")
engine = Engine(150)
car.set_engine(engine)

print(f"{car.brand} with {car.engine.horsepower} HP")
