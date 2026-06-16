registros = [("João", 8.5), ("Maria", 9.0), ("Pedro", 7.5)]

melhor_aluno = ''
melhor_nota = 0

for registro in registros:
    if registro[1] > melhor_nota:
        melhor_nota = registro[1]
        melhor_aluno = registro[0]  
        
user1, user2, user3 = registros        
notas = [user1[1], user2[1], user3[1]]
media = sum(notas)/len(notas)

print(f'{media:.2f}')
print (melhor_aluno)
print (melhor_nota)

# media = sum(x,y,z)/len(x,y,z)
# print(media)

