class Dynamic_Array:
  def _init_(self):
    self.array = []
    self.array_size = 0
  
  def insert_beginning(self, value):
    self.array = [value] + self.array
    self.array_size += 1
    
  def insert_end(self, value):
    self.array = self.array + [value]
    self.array_size += 1

  def delete_beginning(self):
    if self.array_size == 0:
      print("empty array")
    else:
      self.array = self.array[1:]
      self.array_size -= 1

  def delete_end(self):
    if self.array_size == 0:
      print("empty array")
    else:
      self.array = self.array[:-1]
      self.array_size -= 1

  def display(self):
    print(self.array)
      
deneme = Dynamic_Array()
deneme.insert_beginning(1)
deneme.insert_end(7)
deneme.delete_end()
deneme.display()