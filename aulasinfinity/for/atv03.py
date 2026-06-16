palavra = input("digite uma palavra: ")
vogais = "aeiouáéíóúâêîôûãõ"
total_vogais = 0

for letra in palavra:
     if letra.isalpha():
         if letra.lower() in vogais:
             total_vogais += 1
print(f"A quantidade de vogais da palavra {palavra} é: {total_vogais}")