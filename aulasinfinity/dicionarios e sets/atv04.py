alunos = {}
print("--- Cadastro de Alunos ---")

while True:
    nome_aluno = input("Nome do aluno (ou 'sair' para encerrar): ").strip()

    if nome_aluno.lower() == "sair":
        break

    
    materias = {}

    
    while True:
        materia = input("Matéria (ou 'fim' para terminar): ").strip()

        if materia.lower() == "fim":
            break

        nota = float(input(f"Nota de {materia}: "))
        materias[materia] = nota

    
    alunos[nome_aluno] = materias


print("\n--- Alunos Cadastrados ---")

for aluno, materias in alunos.items():
    print(f"Aluno: {aluno}")

    for materia, nota in materias.items():
        print(f"{materia}: {nota}")
    print()
