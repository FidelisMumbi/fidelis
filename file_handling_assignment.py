import datetime

def create_and_write_file():
  """Creates a new text file 'my_file.txt' and writes content to it."""
  try:
    with open("my_file.txt", "w") as f:
      f.write("This is the first line of text.\n")
      f.write(str(42) + " is the answer to the ultimate question of life, the universe, and everything.\n")
      f.write("Here's another line of text with a number: 3.14159\n")
      print("Successfully created and wrote to 'my_file.txt'.")
  except PermissionError:
    print("Error: You don't have permission to create the file.")
  except Exception as e:  # Catch any other unexpected errors
    print(f"An error occurred while creating the file: {e}")

def read_and_display_file():
  """Reads the contents of 'my_file.txt' and displays them."""
  try:
    with open("my_file.txt", "r") as f:
      contents = f.read()
      print("\nContents of 'my_file.txt':")
      print(contents)
  except FileNotFoundError:
    print("Error: 'my_file.txt' does not exist.")
  except Exception as e:
    print(f"An error occurred while reading the file: {e}")

def append_to_file():
  """Opens 'my_file.txt' in append mode and writes additional lines."""
  try:
    with open("my_file.txt", "a") as f:
      f.write("\nAm very cool:\n")
      f.write("this is my first file automation..\n")
      f.write("tech is amazing!!.\n")
      f.write(f"achievement data: {datetime.datetime.now()}.\n")
      print("\nSuccessfully appended content to 'my_file.txt'.")
  except PermissionError:
    print("Error: You don't have permission to append to the file.")
  except Exception as e:
    print(f"An error occurred while appending to the file: {e}")

if __name__ == "__main__":
  create_and_write_file()
  read_and_display_file()
  append_to_file()
  read_and_display_file()  # Read again to show appended content
