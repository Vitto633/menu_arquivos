
# quando o cara digitar w ele vai dar um open("nome_do_arquivo", "w") => nesse caso apaga o que tava no arquivo antes
# quando o cara digitar r ele vai dar um open("nome_do_arquivo", "r") => para ler o arquivo
# quando o cara digitar a ele vai dar um open("nome_do_arquivo", "a") => nesse caso edita o arquivo sem apagar o que ta la
# quando o cara digitar x ele vai dar um open("nome_do_arquivo", "x") => nesse caso ele vai criar um novo arquivo

def writeFunction(arquivo):
    arquivoAberto = open(arquivo, "w")
    texto = input("Digite o que você quer colocar no arquivo: ")
    arquivoAberto.write(texto)
    arquivoAberto.close()

def readFunction(arquivo):
    arquivoLeitura = open(arquivo, "r")
    print(arquivoLeitura.read())
    input("\n Pressione algo para continuar.")
    arquivoLeitura.close()

def appendFunction(arquivo):
    arquivoAppend = open(arquivo, "a")
    texto = input("Digite o texto que você quer adicionar: ")
    arquivoAppend.write(texto)
    arquivoAppend.close()
def exclusiveFunction(arquivo):
        novoArquivo = open(arquivo, "x")
        novoArquivo.close()

isRunning = True

while isRunning:
    print("""
        +=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+
        |            MENU EXERCICIOS            |
        |                                       | 
        |   Escolha uma das opções:             |
        |                                       | 
        |   w => write - gravar                 |
        |   r => read - ler                     |
        |   a => append = editar o arquivo      |
        |   x => gravação em arquivo exclusivo  |
        |   0 => para sair                      |
        |                                       |
        +=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+
    """)

    opcao = input("Escolha uma opção: ")
    match opcao:
        case 'w':
            arquivo = input("Digite o nome do arquivo com a extensão que deseja alterar: ")
            writeFunction(arquivo)
        case 'r':
            arquivo = input("Digite o nome do arquivo com a extensão que deseja ler: ")
            try:
                readFunction(arquivo)
            except:
                print("Arquivo não existe")
                input("\nPressione algo para continuar.")
        case 'a':
            arquivo = input("Digite o nome do arquivo com a extensão que deseja alterar: ")
            appendFunction(arquivo)
        case 'x':
            arquivo = input("Digite o nome do arquivo com a extensão que deseja criar: ")
            try:
                exclusiveFunction(arquivo)
            except:
                print("Arquivo já existente")
                input("\nPressione algo para continuar.")
        case '0':
            isRunning = False
        case _:
            print("Opção inválida")
            input("\nPressione algo para continuar.")