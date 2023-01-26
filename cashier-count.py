class Counter:
  def __init__(self, value):
    self.value = value
 
class Node:
  def __init__ (self, data):
    self.data = data
    self.next = None
    self.prev = None

class list:
  def __init__ (self):
    self.head = None
    self.tail = None
    self.total = 0
 
  def push (self, value):
    NewNode = Node(value)

    self.total += value.value
    
    if self.head is None:
      self.head = NewNode
      self.tail = NewNode
      return

    if (self.tail.next is None):
        self.tail.next = NewNode
        self.tail = NewNode
 
  def delete (self):
    node = self.head

    if (node is None):
      self.tail = None
      return

    if (self.total > 0):
      self.total -= node.data.value
 
    # remove head
    if (node.prev is None):
      new_node = node.next
 
      if (new_node is not None):
        new_node.prev = None
        
        if (new_node.next is not None):
            new_node.next.prev = new_node

      self.head = new_node
      return

counter_one = list()
counter_two = list()
counter_three = list()

def show():
  print('Caixa 1: ' + str(counter_one.total))
  print('Caixa 2: ' + str(counter_two.total))
  print('Caixa 3: ' + str(counter_three.total))

def update_counters(counter):
  if counter == 1:
      counter_one.delete()
  elif counter == 2:
      counter_two.delete()
  elif counter == 3:
      counter_three.delete()

def insert_counter_one(value):
  counter_one.push(Counter(value))

def insert_counter_two(value):
  counter_two.push(Counter(value))

def insert_counter_three(value):
  counter_three.push(Counter(value))

if __name__ == '__main__':
    while True:
        try:
          option, quantity = input().split()
          
          if option == 'PROXIMO':
            update_counters(int(quantity))
          elif option == '1':
            insert_counter_one(int(quantity))
          elif option == '2':
            insert_counter_two(int(quantity))
          elif option == '3':
            insert_counter_three(int(quantity))
            
        except:
          break
        
    show()
      
