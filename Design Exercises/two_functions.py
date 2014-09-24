def returnAsTuple (name, age):
    # Returns two variables as a tuple
    tupleToReturn = (name, age)
    return tupleToReturn

def returnAsVars (tupleReceived):
    # Returns a tuple as two separate variables
    name = tupleReceived[0]
    age = tupleReceived[1]
    return name, age
    

tupleReturned = returnAsTuple("Michael", 17)

print("The returnAsTuple function returned:", tupleReturned)

name, age = returnAsVars(tupleReturned)

print("The returnAsVars function returned the name as:", name)
print("The returnAsVars function returned the age as:", age)

