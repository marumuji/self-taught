profile = dict()

profile = { "music": "oasis", 
            "tall": "180cm",
            "food": "curry",
            "drink": "scotch",
            "hobby": "marathon",
          }

print(profile)
key = input("input info: ")

if key in profile:
  print(profile[key])