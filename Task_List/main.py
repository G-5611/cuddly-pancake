'''

MostrarListaPendentes                   Done
MostrarListaConcluidas                  Done
Adicionar Tarefas                       Done
Remover Tarefes.                        Done
Concluir Tarefas.                       Done
Sair Programa                           Done

'''


#ListaDone.append(ListaPendent[i])

def menu():
    options =[0,1,2,3,4,5]
    option_user = int

    while option_user not in options:

        print("O que deseja fazer? \n Digite [1] para vizualizar a lista de tarefas \n Digite [2] para adicionar uma tarefa \n Digite [3] para remover uma tarefa \n Digite [4] para marcar uma tarefa como concluida \n Digite [5]  para visualizar a lista de tarefas concluidas \n Digite [0] para sair do programa")
        option_user = int(input())

        if option_user not in options:

            print("Opção inválida, tente novamente")

    return option_user


def addTask():

        getListPendent()
        newtask = str(input("Digite o nome da tarefa que deseja adicionar ou digite STOP para voltar ao menu: "))
        while True:
            if newtask.lower() == "stop":
                break
            else:
                ListPendent.append(newtask)
                print("Tarefa Adicionada")
                return


def getListPendent():
    if listPendent_not_empty() == True:
        for index, i in enumerate (ListPendent):
            print(index, '-', i)
        return
    else:
        return


def getListDone():
    if listDone_not_empty() == True:
        for index, i in enumerate (ListDone):
            print(index, '-', i)
        return
    else:
        return


def removeTask():
    if listPendent_not_empty() == True:
        getListPendent()
        task_remover = int(input(" Digite o indice da tarefa que deseja remover"))
        ListPendent.pop(task_remover)
        print("Tarefa removida")
        getListPendent()
        return
    else:
        return


def listPendent_not_empty():
    situation = bool(ListPendent)
    if not situation:
        print(" A lista está vazia ")
    return situation

def listDone_not_empty():
    situation = bool(ListDone)
    if not situation:
        print(" A lista está vazia ")
    return situation

def checkTask():

    if listPendent_not_empty() == True:
        getListPendent()
        taskcheck = int(input("Digite o indice da tarefa que deseja marcar como concluida"))

        try:

            ListDone.append(ListPendent[taskcheck])
            ListPendent.pop(taskcheck)
            print(" A tarefa foi concluida")
        except IndexError as e:
            print('Erro IndexError:',e)

        except Exception as e:
            print('Erro Exception:',e)


    else:
        return
















if __name__ == '__main__':

    ListPendent = []
    ListDone = []


    while True:
        action = menu()

        if action == 1:
            getListPendent()

        elif action == 2:
            addTask()

        elif action == 3:
            removeTask()

        elif action == 4:
            checkTask()

        elif action == 5:
            getListDone()

        elif action == 0:
            break




