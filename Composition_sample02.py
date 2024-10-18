# エンジンクラス
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

# ガソリンエンジン
class GasolineEngine(Engine):
    def __init__(self):
        super().__init__(horsepower=150)

# 電気エンジン
class ElectricEngine(Engine):
    def __init__(self):
        super().__init__(horsepower=200)

# 車クラス
class Car:
    def __init__(self, make, model, color, engine):
        self.make = make      # 車のメーカー
        self.model = model    # 車のモデル
        self.color = color    # 車の色
        self.engine = engine  # エンジン（別クラスのオブジェクト）

    # 車の情報を一度に返すメソッド
    def __str__(self):
        return f"{self.color} {self.make} {self.model}, Engine: {self.engine.horsepower} horsepower"

# 初期の車を作成（ガソリンエンジン搭載）
my_car = Car("Toyota", "Corolla", "Red", GasolineEngine())

# 車の情報を表示（__str__メソッドが自動的に呼ばれる）
print(my_car)

# ここがコンポジション
# Carクラスの中のエンジン属性だけを電気エンジンクラスに変更
my_car.engine = ElectricEngine()

# 再び車の情報を表示
print(my_car)



#?# 属性が定義されているのに、メソッド内で使われていないという現象は、実際に起こり得る。
#?# この場合、それが問題かどうかは設計意図による。
### 1. 将来的な拡張が考慮されているケース
###    プログラムの将来的な拡張を考えて属性を定義しておき、まだメソッド内では使っていないため、
###    設計上は問題ない。今後の機能追加や新たなメソッドの実装に備えている状態と捉えること。
### 2. 外部から直接アクセスするための属性であるケース
###    属性がメソッド内で使われていなくても、外部から直接アクセスされるために用意されているため、
###    問題ない。この場合、属性は外部からの参照において機能しており、同一クラス内のメソッドで使われていない
###    ことは特に問題ではない。なお、外部からの参照を回避するためには以下のように"_"をつけることで保護できる。
```
class Car:
    def __init__(self, make, model, color, engine):
        self._make = make  # 属性を保護
        self._model = model
        self._color = color
        self._engine = engine
```
### 3. その属性がどこでも使われておらず、設計上の理由がない場合、削除するべき(Dead Code)。冗長化を引き起こします。  
