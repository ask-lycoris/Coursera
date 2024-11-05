# エンジンクラス
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower  # エンジンの馬力

    def start(self):
        return "Engine started with {} horsepower.".format(self.horsepower)

# 車クラス
class Car:
    def __init__(self, engine):
        self.engine = engine  # エンジンを持っている（has-a 関係）

    def start(self):
        return self.engine.start()  # 車のエンジンを始動

# エンジンを作成
my_engine = Engine(150)

# 車を作成し、エンジンを渡す
my_car = Car(my_engine)

# 車のエンジンを始動
print(f"Normal {my_car.start()}")  # "Normal Engine started with 150 horsepower."

# ガソリンエンジン
class GasolineEngine(Engine):
    def __init__(self):
        super().__init__(horsepower=120)

# 電気エンジン
class ElectricEngine(Engine):
    def __init__(self):
        super().__init__(horsepower=200)

# ここがコンポジション
# 車にエンジンを取り付け
# Carクラスに別のクラスGasolineEngineクラスを取り付ける
gas_car = Car(GasolineEngine())
# Carクラスに別のクラスElectricEngineクラスを取り付ける
electric_car = Car(ElectricEngine())

#?# 今回はCarクラスに1つの属性(搭載エンジン)しか存在しなかったから単純に上記のようにコンポジション
#?# 記載できるが、通常は複数の属性の中の一部を変更する感じになるのでsample02ではそこをみていく。

print(f"Gasoline {gas_car.start()}")  # "Gasoline Engine started with 120 horsepower."
print(f"EV {electric_car.start()}")  # "EV Engine started with 200 horsepower."
