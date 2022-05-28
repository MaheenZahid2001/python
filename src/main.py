def even_no(no):
  if no % 2 == 0:
    return True
  else:
    return False

def chg_no(no):
  we_no = even_no(no)
  if we_no == False:
    num = no + 1
  else:
    num = no
  return num
  
a = chg_no(1)
print(a)
  
  

  
  

