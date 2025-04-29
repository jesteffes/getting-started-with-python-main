# Give the class a name
class PersonalAssistant:
  # Add an __init__ function here
  def __init__(self, todos):
    
    self.todos = todos

  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    if todo_item in self.todos:
      # Get the todo_item index in list
      index = self.todos.index(todo_item)
      # pop the index for todo_item in todos list
      self.todos.pop(index)
    else:
      print("Todo is not in list!")

  def get_todos(self):
    return self.todos
  
  def get_birthday(self, name):
    if name == "Mali":
      print("Birthday is 08/09/08!")
    elif name == "Raider":
      print("Birthday is 11/22/07!")
    elif name == "Jack":
      print("Birthday is 09/17/05!")
    else:
      print("Can't find a birthday for this person.")

  # Complete the get_contact function code
  def get_contact(self, name):
    if name in self.contacts: 
      return self.contacts[name]
    else:
      return "There is no contact with that name."
       


# Code to test output of the class
# assistant = PersonalAssistant()
# assistant.add_todo("Pick up groceries")
# print(assistant.get_todos())
# Change name to one from your contacts
# print(assistant.get_contact("Max"))
# print(assistant.get_birthday("Raider"))