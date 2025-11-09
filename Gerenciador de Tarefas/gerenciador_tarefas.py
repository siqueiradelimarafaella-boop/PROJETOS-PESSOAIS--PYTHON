# Desenvolver um mini sistema de gerenciamento de tarefas no terminal usando Python.

# Instruções do projeto:

# Exibir um menu com opções:
#  Adicionar uma nova tarefa
# Remover uma tarefa
# Listar todas as tarefas
# Sair do programa

# Cada tarefa deve ser armazenada como um dicionário, contendo:
# id (um número único incrementado automaticamente)
# nome da tarefa (informado pelo usuário)
# Todas as tarefas devem ficar guardadas em uma lista de tarefas.
# O programa deve tratar entradas inválidas (como digitar letras quando o programa espera números).
# O programa deve continuar mostrando o menu até o usuário escolher sair.

tarefas = []
id_contador = 1

def adicionar_tarefa ():
    global id_contador

    nome = input ('Digite a sua tarefa: ')

    tarefa = {'id':id_contador, 'nome': nome}

    tarefas.append(tarefa)
    id_contador += 1

    print ('Inclusão de tarefa concluída!')

def listar_tarefas():
      if not tarefas:
        print(" Nenhuma tarefa cadastrada ainda.")
        return
      
      print("\n=== LISTA DE TAREFAS ===")
      for tarefa in tarefas:
        print(f"ID: {tarefa['id']} | Nome: {tarefa['nome']}")  

def remover_tarefa ():
    listar_tarefas()

    try:
        tarefa_id = int(input("\nDigite o ID da tarefa para remover: "))
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return

    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            tarefas.remove(tarefa)
            print("✅ Tarefa removida com sucesso!")
            return  


    print("❌ ID não encontrado.")



def main():
    menu = '''

    ======= Gerenciador de Tarefas ========
    Escolha uma opção:
    
[+] Adicionar uma nova tarefa
[r] Remover uma tarefa
[l] Listar todas as tarefas
[s] Sair do sistema

===============================================
=> '''

    while True:
        selecao = input(menu)
        if selecao == '+':
             adicionar_tarefa()
           
        elif selecao == 'r':
            remover_tarefa()

        elif selecao == 'l': 
            listar_tarefas()  

        elif selecao == 's':
            print("Encerrando o programa...")
            break
        else: 
            print( "Operação inválida. Tente novamente.")


main()