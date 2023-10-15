def add_time(start, duration, starting_day_of_week=None):
  '''
  function that takes in two required parameters and one optional parameter:
  -a start time in the 12-hour clock format (ending in AM or PM)
  -a duration time that indicates the number of hours and minutes (hr:min)
  -(optional) a starting day of the week, case insensitive
  '''
  new_time = ""  #string that should be "hr:min AM|PM"
  week_days = ['Monday', "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  #settare il parametro opzionale (se c'è) in modo che la prima lettera è maiuscola e le altre minuscole
  if starting_day_of_week != None:
    starting_day_of_week = starting_day_of_week.title()
    
  
  #trasformare lo start in 24hr format
  ampm = start.split(' ')[1]  #["hr:min", "AM"]
    #trasformo le ore in min ["hr:min"] -> ["min"]
  start_hr, start_min = start.split(' ')[0].split(':')
  duration_hr, duration_min = duration.split(':')
  
  
  if ampm == "AM":
    start_in_mins = int(start_hr)*60 + int(start_min) #è un int
  else:
    start_in_mins = int(start_hr)*60 + int(start_min) + 12*60
    
  duration_in_mins = int(duration_hr)*60 + int(duration_min)
  # aggingo il nuovo orario
  new_time_in_mins = duration_in_mins + start_in_mins #è un intero
  new_time_hr = new_time_in_mins // 60
  new_time_min = new_time_in_mins % 60
  
  days = 0
  
  #ora devo vedere se supero le 24 e salvare i giorni in più
  if new_time_hr >24:
    days = new_time_hr // 24
    new_time_hr = new_time_hr - days*24
    
  if new_time_hr > 12:
    new_time_ampm = "PM"  
  elif new_time_hr == 12 and new_time_min > 0:
    new_time_ampm = "PM"
  else:
    new_time_ampm = "AM"
    
  if new_time_ampm == "AM" and new_time_hr == 0:
    new_time_hr = 12
  
  if new_time_hr > 12:
    new_time_hr -= 12
  
  if new_time_min < 10:     #aggiungere una stringa '0' se i min sono meno di 10
    new_time_min = '0'+str(new_time_min)
  else:
    new_time_min = str(new_time_min)
    
  
  new_time = str(new_time_hr)+':'+new_time_min+' '+new_time_ampm
  if starting_day_of_week != None:
    if days == 0:
      new_time += f', {starting_day_of_week}'
    else:
      i = week_days.index(starting_day_of_week) +days
      new_time +=f", {week_days[i%7]}"
      
  if days == 1:
    new_time += " (next day)"
  elif days > 1:
    new_time += f" ({days} days later)"

  return new_time
