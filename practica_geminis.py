#problem of the 2 queen on the certamen of beauty

queenofcolombian =  0
queenofargentins =  0

# ronda de talento
print (f"queenofcolombian suming 85 points for her show, she had {queenofcolombian + 85}")
print ("but i know that winner 10 extra points for sympatic")

queenofcolombian += 95
print (queenofcolombian)

print (f"continuos with queenofargentine, for her show winner 90 points, she had {queenofargentins + 90}")
queenofargentins += 90

# verificacion de empate

print (f"now, i revise your points and first items evaluations is watching his punctuation {queenofcolombian == queenofargentins}")
print (f"so, the winner is queenofcolumbian for more punctuation {queenofargentins and queenofcolombian}")

# misterio de identidad 

queenofcolombian = ["eyes green", "stature 1.90m"]
queenofargentins = ["eyes blues", "statura 1.86m"] # Una doble idéntica

# ¿Tienen los mismos atributos?
print(queenofcolombian == queenofargentins) # True

# ¿Son la misma persona física?
print(queenofcolombian is queenofargentins) # False (Son dos objetos distintos en memoria)

# Ahora, si la reina del inicio avanza en el concurso:
reina_ganadora = queenofcolombian

# ¿Es la misma persona?
print(reina_ganadora is queenofcolombian) # True (Ambas variables apuntan al mismo ADN)