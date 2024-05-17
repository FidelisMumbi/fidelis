class Person:
  """Represents a person with name, age, and gender attributes."""

  def __init__(self, name, age, gender):
    """Initializes the Person object with the provided details."""
    self.name = name
    self.age = age
    self.gender = gender

  def introduce(self):
    """Prints a message introducing the person with their details."""
    print(f"Hello! My name is {self.name}. I am {self.age} years old and identify as {self.gender}.")

# Create an instance of the Person class
person1 = Person("Fidelis", 30, "Female")

# Call the introduce method to display person1's information
person1.introduce()
