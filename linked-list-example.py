 
class linked_list:
  def __init__ (self):
    self.head = None
 
  def push (self, value):
    NewNode = Node(value)
    
    if self.head is None:
      self.head = NewNode
      return

    current_node = self.head
    while (current_node.next is not None):
      current_node = current_node.next

    if (current_node.next is None):
        current_node.next = NewNode
        NewNode.prev = current_node

  def search (self, name):
    last_node = self.head

    if (last_node is None):
      print('Pokemons vazios')
      return

    while (last_node.data.name != name and last_node.data.name != None):
      last_node = last_node.next
 
    if (last_node.data.name is None):
      print('Not found')
      return
    
    print('Nome: ' + last_node.data.name + ' -- ' + 'Idade :', last_node.data.age)
 
  def delete_list (self, name):
    node = self.head
 
    while (node.data.name != name):
      node = node.next

    # remove head
    if (node.prev is None):
      new_node = node.next

      if (new_node is not None):
        new_node.prev = None
        
        if (new_node.next is not None):
            new_node.next.prev = node
        
      self.head = new_node
      return

    # remove last
    if (node.next is None):
      node.prev.next = None
      return

    node.prev.next = node.next
    node.next.prev = node.prev
    
  def show_list (self):
    value = self.head
    if (value is None):
      print('Pokemons vazios')
      return
    
    while value is not None:
      print('Nome: ' + value.data.name + ' -- ' + 'Idade :', value.data.age)
      value = value.next
  
list = linked_list()
 
def insert():
  name = ''
  age = None
  try:
      name = input('Nome: ')
      age = int(input('Idade: '))
  except:
      print('Falhou ...')
 
  list.push(Pokemon(name, age))
 
def search():
  name = ''
  try:
      name = input('Busque pelo nome: ')
  except:
      print('Falhou ...')
  list.search(name)
 
def delete():
  name = ''
  try:
      name = input('Nome: ')
  except:
      print('Falhou ...')
 
  list.delete_list(name)
 
menu_options = {
    1: 'Inserir um Pokemon',
    2: 'Procurar um Pokemon',
    3: 'Remover um Pokemon',
    4: 'Imprimir todos Pokemons',
}
 
def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key])
 
if __name__ == '__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Escolha uma opção: '))
        except:
            print('Wrong input. Please enter a number ...')
 
        if option == 1:
          insert()
        elif option == 2:
          search()
        elif option == 3:
          delete()
        elif option == 4:
          list.show_list()
