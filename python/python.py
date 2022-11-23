file = open ('fileOne.txt','r')
data = file.read()
file.close()

symbols= ["_","-","/","_","-","/","_","-","/","_","-","/","_","-","/"]
splited=data.split()


i=0
for word in splited:
        with open ('fileTwo.txt','a') as file:
                file.write(word)
                file.write(symbols[i])
                i+=1
                    
