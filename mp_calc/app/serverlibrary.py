

def merge(array:list, p:int, q:int, r:int, byfunc):
  left_length = q - p + 1
  right_length = r - q
  left_array = array[p:q+1]
  right_array = array[q+1:r+1]
  left_idx = 0
  right_idx = 0
  master_idx = p
  while left_idx < left_length or right_idx < right_length:
      if left_idx == left_length:
          array[master_idx] = right_array[right_idx]
          right_idx += 1
      elif right_idx == right_length:
          array[master_idx] = left_array[left_idx]
          left_idx += 1
      elif byfunc(left_array[left_idx]) < byfunc(right_array[right_idx]):
          array[master_idx] = left_array[left_idx]
          left_idx += 1
      elif byfunc(left_array[left_idx]) > byfunc(right_array[right_idx]):
          array[master_idx] = right_array[right_idx]
          right_idx += 1
      elif byfunc(left_array[left_idx]) == byfunc(right_array[right_idx]):
          array[master_idx] = left_array[left_idx]
          left_idx += 1
      master_idx += 1
            
def mergesort_recursive(array:list, p:int, r:int, byfunc):
    q = (p + r) // 2
    if p >= r:
        pass
    else:
        mergesort_recursive(array, p, q, byfunc)
        mergesort_recursive(array, q+1, r, byfunc)
        merge(array, p, q, r, byfunc)
 
def mergesort(array:list, byfunc) -> None:
    p = 0
    r = len(array)
    mergesort_recursive(array, p, r-1, byfunc)

class Stack:
  def __init__(self):
      self.items = []
  
  def push(self, item):
      self.items.append(item)
  
  def pop(self):
      return self.items.pop() if not self.is_empty() else None
  
  def peek(self):
      return self.items[-1] if not self.is_empty() else None
  
  def is_empty(self):
      return len(self.items) == 0

class EvaluateExpression:
  global valid_char, operator
  valid_char = '0123456789+-*/() '
  operator = '+-*/()'
  def __init__(self, string=""):
    self.expr = string

  @property
  def expression(self):
    return self.expr

  @expression.setter
  def expression(self, new_expr):
    is_valid = True
    self.expr = new_expr
    while is_valid:
      for item in new_expr:
        if item not in valid_char:
          self.expr = ""
          is_valid = False
      break

  def insert_space(self):
        result = ""
        for char in self.expr:
            if char in operator:
                result += f" {char} "
            else:
                result += char
        return result
    
  def process_operator(self, operand_stack, operator_stack):
    
    operator = operator_stack.pop()
        
    right = operand_stack.pop()
    left = operand_stack.pop()
        
    if operator == '+':
        result = left + right
    elif operator == '-':
        result = left - right
    elif operator == '*':
        result = left * right
    elif operator == '/':
        result = left // right  
        
    operand_stack.push(result)


  def evaluate(self):
        operand_stack = Stack()
        operator_stack = Stack()

        expression = self.insert_space()
        tokens = expression.split()

        for token in tokens:
            if token.isdigit():
                operand_stack.push(int(token))
            elif token == '(':
                operator_stack.push(token)
            elif token == ')':
                while operator_stack.peek() != '(':
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.pop()  # Remove '('
            elif token in '+-':
                while (not operator_stack.is_empty() and
                       operator_stack.peek() not in '()'):
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.push(token)
            elif token in '*/':
                while (not operator_stack.is_empty() and
                       operator_stack.peek() in '*/'):
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.push(token)

        # Phase 2: Process remaining operators
        while not operator_stack.is_empty():
            self.process_operator(operand_stack, operator_stack)

        return operand_stack.pop()
  
def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





