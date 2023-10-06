def arithmetic_arranger(problems, option = False):
  '''
    Arrange the problems giving back a formatted string.
    exe: problems = ["32 + 698", "3801 - 2"]
    arranged_problems = ["32   3801","+698  -2 "]

    It's a problem of string manipulation.
    '''
  arranged_problems = ''
  
  first_row = ""
  second_row = ""
  separator_row = ""
  answer_row = ""
  
  #Non devo avere più di 5 problemi
  num_problems = len(problems)
  if num_problems > 5:
    arranged_problems = 'Error: Too many problems.'
    return arranged_problems

  #Le uniche operazioni possibili sono + e -
  #per farlo devo -> parse the string
  possibile_operation = {'+', '-'}  #set of operation
  for problem in problems:
    operation = problem.split(' ')  #['32', '+', '698']

    if operation[1] not in possibile_operation:
      arranged_problems = "Error: Operator must be '+' or '-'."
      return arranged_problems
  
    if operation[0].isdigit() and operation[2].isdigit() != True:
      return "Error: Numbers must only contain digits."
      

    if (len(operation[0]) > 4 or len(operation[2])) > 4 != False:
      arranged_problems = "Error: Numbers cannot be more than four digits."
      return arranged_problems
    
    #identare le stringhe
    largest_value = max(len(operation[0]), len(operation[2]))
    width = largest_value + 2
    
    line1 = f"{operation[0]:>{width}}"
    line2 = f"{operation[1]} {operation[2]}"
    line2 = f'{line2:>{width}}'
    separator = f"{f'-'*width}"

    answer= ''
    if option:
      answer = str(eval(problem))
      answer = f'{answer:>{width}}'
          
    if problem != problem[-1]:
      first_row += line1 + ' '*4
      second_row += line2 + ' '*4
      answer_row += answer + ' '*4
      separator_row += separator + ' '*4
    else:
      first_row += line1 
      second_row += line2 
      answer_row += answer 
      separator_row += separator      
      
  if option:    
    arranged_problems = first_row+'\n'+second_row+'\n'+separator_row+'\n'+answer_row  
  else:
    arranged_problems = first_row+'\n'+second_row+'\n'+separator_row
  return arranged_problems

