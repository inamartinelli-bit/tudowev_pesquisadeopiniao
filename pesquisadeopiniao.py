import os # Verifica o sistema e limpa a tela
# os.name =='nt' identifica se o sistema é Windows, executando o comando o comando 'cls' para limpar a tela. 
# Caso contrário (else), para sistemas Linux ou Mac (baseados em Unix), o comando 'clear' é utilizado.
# os.name == 'nt' significa que o sistema operacional é Windows, enquanto 'posix' indica Linux ou Mac.
# os.name retorna 'nt' para Windows e 'posix' para Linux/Mac
if os.name == 'nt':  # Windows
    os.system('cls')
else:  # Linux/Mac
    os.system('clear')

# **Início do programa:**
print("\n             TUDO WEB") # Início do programa com o nome da empresa.
print("===================================")
print("Pesquisa de Atendimento ao Cliente:") # Início do programa com o título da pesquisa.
print("===================================")
# **Entrada de dados pelos usuários:**
total_entrevistados = 50 # Solicita ao usuário que insira o número total de entrevistados para a pesquisa de opinião.
qtd_excelente = 0 # Inicializa a variável qtd_excelente para contar a quantidade de respostas "EXCELENTE" na pesquisa de opinião.
qtd_ruim = 0 # Inicializa a variável qtd_ruim para contar a quantidade de respostas "RUIM" na pesquisa de opinião.
# **Processamento e saída de dados:**
for i in range(1, total_entrevistados + 1): 
     nome = input("\nPor favor, digite o seu nome: ") 
     idade = int(input("Qual a sua idade? "))
     pesquisa = int(input("Qual a sua opinião sobre o nosso atendimento? Insira: 1 para EXCELENTE | 2 para BOM | 3 para RUIM: "))
     print("\nAtendimento:", pesquisa)
     print("=================================") 
     
     if pesquisa == 1: 
        qtd_excelente += 1 
     elif pesquisa == 3:
          qtd_ruim += 1 
# Saída dos dados.
print("\nAVALIAÇÕES:") #
print("Quantidade de respostas EXCELENTE: ", qtd_excelente)
print("Quantidade de respostas RUIM: ", qtd_ruim)
