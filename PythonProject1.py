name_to_age = {" Many": ["Age", "14"],
            	   "Judie": ["Age","15"],
            	   "John": ["Age", "16"],
              	   "Robert": ["Age", "15"]
               }

print(name_to_age)




def invert(d):
  inverse = dict()
  for key in d:
    val = d[key]
    for item in val:
      if item not in inverse:
        inverse[item] = [key]
      else:
        inverse[item].append(key)
  return inverse 


inverted_shellter = invert(name_to_age)
print(inverted_shellter)

