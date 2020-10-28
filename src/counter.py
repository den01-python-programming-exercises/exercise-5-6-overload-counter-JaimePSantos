class Counter:
  def __init__(self,start_value=0):
    self.value = start_value
  
  @classmethod
  def with_start_value(cls,start_value):
    return cls(start_value)
  
  def value(self):
    return self.value
  
  def increase(self,increase_by=None):
    if increase_by is not None:
      self.value += increase_by
    else:
      self.value+=1
    return self.value
  
  def decrease(self,decrease_by=None):
    if decrease_by is not None:
      if decrease_by>0:
        self.value -= decrease_by
      else:
        return self.value
    else:
      self.value-=1
    return self.value
