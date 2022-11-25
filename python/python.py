file = open ('fileOne.txt','r')
data = file.read()
file.close()

symbols= ["_","-","/","_","-","/","_","-","/","_","-","/","_","-","/"]
splitted=data.split()
count=len(splitted)
print(count)
i=0
for word in splitted:
        with open ('fileTwo.txt','a') as file:
                file.write(word)
                if i == (count-1):
                        break
                file.write(symbols[i])
                i+=1
                    
