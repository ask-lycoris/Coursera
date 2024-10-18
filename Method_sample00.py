class Person:
  def __init__(self, name):
      self.name = name
  def greeting(self):
      # Should return "hi, my name is " followed by the name of the Person.
      return f"hi, my name is {self.name}"

# Create a new instance with a name of your choice
some_person = Person("Google")  #ここ注意。some_person = "Google" を入れないように！
# Call the greeting method
print(some_person.greeting())
