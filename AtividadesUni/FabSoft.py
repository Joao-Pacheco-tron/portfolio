def Notas():  # Criando as variaveis que vão conter as notas
  nota_A = float(input("Digite a nota A:\n"))
  nota_B = float(input("Digite a nota B:\n"))
  nota_C = float(input("Digite a nota C:\n"))
  media = ((nota_A * 0.2) + (nota_B * 0.3) + (nota_C * 0.5))  #  Realiza o calculo da média

  print(f"MEDIA = {media:.1f}")  # Printa a média
  
Notas()  # Chama a função