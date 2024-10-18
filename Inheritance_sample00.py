class Clothing:
  material = ""

  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.name,self.material))

#Clotingクラスを継承し、Shirtクラスを新たに作成し、materialの属性にはCottonを指定している。
class Shirt(Clothing):
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()
