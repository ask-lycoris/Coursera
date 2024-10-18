### Cityクラスは次の属性を持っています：名前、国（都市がある場所）、標高（メートルで測定）、人口（最近の統計による概算）。
### max_elevation_city関数の空白を埋めて、指定された最小人口に対して定義された3つのインスタンスを比較するときに、
### 都市の名前とその国の名前（カンマで区切られています）を返します。
### 例えば、最小人口が100万人の場合にこの関数を呼び出すと、 max_elevation_city(1000000) は "Sofia, Bulgaria" を返します。 

# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
	# Initialize the variable that will hold 
# the information of the city with 
# the highest elevation 
# 空の返り値インスタンスを設けている。
	return_city = City()

	# Evaluate the 1st instance to meet the requirements:
	# does city #1 have at least min_population and
	# is its elevation the highest evaluated so far?
	# 最初の return_city.elevation の値は０。これと各都市のevaluationを比較して、より高い標高を持つ
	# 都市があればreturn_cityに置き換える。
	if city1.population >= min_population and city1.elevation > return_city.elevation:
		print(return_city.elevation)  #最初置き換えられる前は0
		return_city = city1
		print(return_city.elevation)  #置き換えられた後は数値が入っている

	# Evaluate the 2nd instance to meet the requirements:
	# does city #2 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city2.population >= min_population and city2.elevation > return_city.elevation:
		return_city = city2

	# Evaluate the 3rd instance to meet the requirements:
	# does city #3 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city3.population >= min_population and city3.elevation > return_city.elevation:
		return_city = city3

	#Format the return string
  #仮にreturn_ciry.nameがTrueだった場合、国名と都市名を結合してstringとして返す。 
	if return_city.name:
		return f"{return_city.name}, {return_city.country}"
	else:
		return ""

print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""
