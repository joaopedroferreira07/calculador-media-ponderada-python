# Calculador de media ponderada
p_1 = float(input("Qual foi a sua nota na prova 1?"))
p_2 = float(input("Qual foi a sua nota na prova 2?"))
p_3 = float(input("Qual foi a sua nota na prova 3?"))

mediap = (p_1 * 0.4 + p_2 * 0.4 + p_3 * 0.2)
if mediap >= 7:
  print("Aprovado")
else:
  print("Reprovado")
