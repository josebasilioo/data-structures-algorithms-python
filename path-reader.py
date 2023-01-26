class Path:
  def __init__(self, value):
    self.value = value
 
class Node:
  def __init__ (self, data):
    self.data = data
    self.next = None
    self.prev = None

class Stack:
  def __init__ (self):
    self.head = None
    self.tail = None
 
  def push(self, value):
    NewNode = Node(value)     

    if self.head is None:
      self.head = NewNode
      self.tail = NewNode
      return

    current_node = self.tail
    if (self.tail.next is None):
        current_node.next = NewNode
        self.tail = NewNode
        self.tail.prev = current_node
 
  def pop(self):
    node = self.tail

    if (node is None):
      self.head = None
      return

    if (node.prev is not None):
      self.tail = node.prev
      self.tail.next = None
      return

    if (node.prev is None):
      self.head = None
      self.tail = None
      return

  def clear(self):
     while(self.tail is not None):
       self.pop()

  def show(self):
    node = self.head
    path = '/'
    
    while (node is not None):
      if (node.data != None):
        if (node.prev is None):
          path = path + node.data.value
        else:
          path = path + '/' + node.data.value
      node = node.next

    print(path)

stack = Stack()

def pop_path():
  stack.pop()

def insert(value):
  stack.push(Path(value))

if __name__ == '__main__':
    while True:
      try:
          option = input()

          paths = option.split('/')
          
          for path in paths:
            length = len(path.split())
            
            if (path == '..'):
              pop_path()
            else:
              if (path != '' and path != '.' and length > 0):
                insert(path)

          stack.show()
          stack.clear()
      except:
          break
