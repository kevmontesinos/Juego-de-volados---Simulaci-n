import random
import matplotlib.pyplot as plt
import csv

def registro(información):
  
  with open('registro.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='|')
    writer.writerow(['No.'] + ['Dinero antes'] + ['Apuesta']   +   
    ['No.Aleatorio'] + ['Resultado'] + ['Dinero después'] + ["Meta"] )
    
    for i in range(len(informacion)):
      writer.writerow([informacion[i][0]] + informacion[i][1])
      for j in range(2, len(informacion[i]) - 2):
        writer.writerow([""] + informacion[i][j])
      writer.writerow([""] + informacion[i][-2] + [informacion[i][-1]])
    


apuesta = 10
meta = 50
dinero = 30
intentos= 50

ganadas = 0
quiebras = 0

probabilidades = []
informacion = []

for i in range(0,intentos):
  corrida = []
  corrida.append(str(i+1))
  while(True):
    individual = []
    
    individual.append(str(dinero))
    
    individual.append(str(apuesta))
    n_random = random.random()
    individual.append(str(n_random)[0:6].replace(".",","))
    if(n_random < 0.5):
  
      individual.append("Ganó")
      dinero += apuesta
      apuesta = 10
      if(dinero >= meta):
        ganadas += 1 
        probabilidades.append(ganadas/(i+1))

        individual.append(dinero)
        corrida.append(individual)
        corrida.append("Sí")
        probabilidades
        dinero = 30
        apuesta = 10
        break
    else:

      individual.append("Perdió")
    
      dinero -= apuesta
      if(dinero == 0):
        quiebras += 1
        probabilidades.append(ganadas/(i+1))
      
        individual.append(dinero)
        corrida.append(individual)
        corrida.append("Quiebra")
        dinero = 30
        apuesta = 10
        break
      else:
        if (dinero >= apuesta*2):
          apuesta = apuesta*2
        else:
          apuesta = dinero
   
    individual.append(dinero)
    corrida.append(individual)

  informacion.append(corrida)  


registro(informacion)

print("\n\n-------- RESULTADOS ---------")
print("Ganadas: " + str(ganadas))
print("Quiebras: " + str(quiebras))

print("Valor esperado: " + str((ganadas*20-quiebras*30)/intentos))
print("Probabilidad de ganar: " + str(ganadas/intentos))

ax = plt.gca()
ax.set_ylim([0, 1])

plt.xlabel("Juegos")
plt.ylabel("Probabilidad de ganar")

plt.plot(list(range(intentos)), probabilidades)

plt.grid()
plt.show()
    