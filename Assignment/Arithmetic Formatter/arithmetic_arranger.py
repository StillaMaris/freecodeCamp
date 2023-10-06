def arithmetic_arranger(problems):
  '''
    Arrange the problems giving back a formatted string.
    exe: problems = ["32 + 698", "3801 - 2"]
    arranged_problems = ["32   3801","+698  -2 "]

    It's a problem of string manipulation.
    '''
  arranged_problems = ''

  #Non devo avere più di 5 problemi
  if len(problems) > 5:
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

    if (len(operation[0]) > 4 or len(operation[2])) > 4 != False:
      arranged_problems = "Error: Numbers cannot be more than four digits."
      return arranged_problems

  return arranged_problems
