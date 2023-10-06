def arithmetic_arranger(problems):
  '''
    Arrange the problems giving back a formatted string.
    exe: problems = ["32 + 698", "3801 - 2"]
    arranged_problems = ["32   3801","+698  -2 "]

    It's a problem of string manipulation.
    '''
  arranged_problems = ''
  
  first_row = ""
  second_row = ""
  separator = ""
  
  #Non devo avere più di 5 problemi
  num_problems = len(problems)
  if num_problems > 5:
    arranged_problems = 'Error: Too many problems.'
    return arranged_problems

  #Le uniche operazioni possibili sono + e -
  #per farlo devo -> parse the string
  possibile_operation = {'+', '-'}  #set of operation
  for index, values in enumerate(problems):
    operation = values.split(' ')  #['32', '+', '698']

    if operation[1] not in possibile_operation:
      arranged_problems = "Error: Operator must be '+' or '-'."
      return arranged_problems
  
    if operation[0].isdigit() and operation[2].isdigit() != True:
      return "Error: Numbers must only contain digits."
    else:
      value_1 = int(operation[0])
      value_2 = int(operation[2])
      

    if (len(operation[0]) > 4 or len(operation[2])) > 4 != False:
      arranged_problems = "Error: Numbers cannot be more than four digits."
      return arranged_problems
    
    
    #take the max lenght of operands in the operation
    
    longest_value  = max(len(operation[0]), len(operation[2]))
    width = longest_value + 2 
    width_sign_operand = len(operation[0])- len(operation[2])
    
    #add spaces to each line
    line_1 = f"{operation[0]:>{width}}"
    first_row = first_row + ' '*4 + line_1
    
    line_2 = f'{operation[1]} '+ ' '*width_sign_operand + f'{operation[2]}'
    second_row += ' '*4 + f"{line_2:>{width}}"
    
    separator += ' '*4 + '-'*width 
    
    arranged_problems = first_row+'\n'+second_row+'\n'+separator 
  
    #line_2 = f'{operation[1]} '+ ' '*width_sign_operand + f'{operation[2]}' 
    #output = f"{operation[0]:>{width}}\n{line_2:>{width}} \n{'-'*width}"

  return arranged_problems
