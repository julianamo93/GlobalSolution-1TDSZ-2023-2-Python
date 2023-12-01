import datetime

# Definindo a classe Paciente
class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.historico = []

    def adicionar_evento(self, evento):
        self.historico.append(evento)

# Definindo a classe EventoSaude
class EventoSaude:
    def __init__(self, descricao, data):
        self.descricao = descricao
        self.data = data

# Definindo a classe Triagem
class Triagem:
    def __init__(self, pressao_arterial, temperatura, sintomas, data):
        self.pressao_arterial = pressao_arterial
        self.temperatura = temperatura
        self.sintomas = sintomas
        self.data = data

    def verificar_estado_saude(self):
        if self.temperatura > 37.8:
            return "\nATENÇÃO: Este paciente precisa de atendimento médico! Dentro de alguns minutos um de nossos profissionais entrará em contato."
        else:
            return "Este paciente está sem febre."

# Definindo a classe AyuCare
class AyuCare:
    def __init__(self):
        self.pacientes = {}

    def cadastrar_paciente(self, paciente):
        self.pacientes[paciente.nome] = paciente

    def realizar_triagem(self, paciente):
        pressao_arterial = input(f"\nDigite a pressão arterial para {paciente.nome}: ")
        temperatura = float(input(f"\nDigite a temperatura para {paciente.nome}: "))
        sintomas = input(f"\nDescreva os sintomas para {paciente.nome}: ")
        data_triagem = datetime.date.today()

        triagem = Triagem(pressao_arterial, temperatura, sintomas, data_triagem)
        paciente.adicionar_evento(triagem)

        resultado_triagem = triagem.verificar_estado_saude()
        print(f"\nTriagem realizada para paciente {paciente.nome}.\n {resultado_triagem}")

    def monitorar_saude(self, paciente):
        descricao = input(f"\nLembrando que toda doença sempre se inicia no mental antes de vir para o corpo físico.\nComo você está se sentindo hoje {paciente.nome}? ")
        data = datetime.date.today()
        evento = EventoSaude(descricao, data)
        paciente.adicionar_evento(evento)
        print(f"\nEvento de saúde registrado, o paciente se sente {descricao}")

    def exibir_historico(self, paciente):
        print(f"\nHistórico armazenado de {paciente.nome}:")
        for evento in paciente.historico:
            if isinstance(evento, Triagem):
                print(f"\n--> Triagem <--")
                print(f"\nData: {evento.data}\nPressão arterial: {evento.pressao_arterial}\nTemperatura: {evento.temperatura}\nSintomas: {evento.sintomas}")
                resultado_triagem = evento.verificar_estado_saude()
                print(resultado_triagem)
            elif isinstance(evento, EventoSaude):
                print(f"Em {evento.data}: {paciente.nome} estava {evento.descricao}")

def obter_informacoes_paciente():
    nome = input("\nDigite o nome do paciente que está sendo cadastrado: ")
    idade = int(input("\nDigite a idade: "))
    return Paciente(nome, idade)

# Início do programa principal
if __name__ == "__main__":
    ayucare = AyuCare()

    while True:
        print("\n-------------------------------")
        print("\n--- Diário de Saúde AyuCare ---")
        print("\nLembre-se que o preenchimento do diário é de suma importância para que conheçamos você e sua rotina.\n")
        print("1. Cadastrar Paciente")
        print("2. Realizar Triagem")
        print("3. Monitorar Humor")
        print("4. Exibir Histórico de um Paciente")
        print("5. Sair")

        escolha = input("\nDigite o número da opção desejada: ")

        if escolha == "1":
            novo_paciente = obter_informacoes_paciente()
            ayucare.cadastrar_paciente(novo_paciente)
        elif escolha == "2":
            print("\n--- Lista de Pacientes ---")
            for i, paciente in enumerate(ayucare.pacientes.values(), 1):
                print(f"{i}. {paciente.nome}")
            
            escolha_paciente = int(input("\nEscolha o número do paciente para realizar a triagem: "))
            pacientes = list(ayucare.pacientes.values())
            
            if 1 <= escolha_paciente <= len(pacientes):
                ayucare.realizar_triagem(pacientes[escolha_paciente - 1])
            else:
                print("Opção inválida. Tente novamente.")
        elif escolha == "3":
            print("\n--- Lista de Pacientes ---")
            for i, paciente in enumerate(ayucare.pacientes.values(), 1):
                print(f"{i}. {paciente.nome}")
            
            escolha_paciente = int(input("\nEscolha o número do paciente para realizar o monitoramento: "))
            pacientes = list(ayucare.pacientes.values())
            
            if 1 <= escolha_paciente <= len(pacientes):
                ayucare.monitorar_saude(pacientes[escolha_paciente - 1])
            else:
                print("Opção inválida. Tente novamente.")
        elif escolha == "4":
            print("\n--- Lista de Pacientes ---")
            for i, paciente in enumerate(ayucare.pacientes.values(), 1):
                print(f"{i}. {paciente.nome}")
        
            escolha_paciente = int(input("\nEscolha o número do paciente para exibir o histórico: "))
            pacientes = list(ayucare.pacientes.values())
    
            if 1 <= escolha_paciente <= len(pacientes):
                ayucare.exibir_historico(pacientes[escolha_paciente - 1])
            else:
                print("Opção inválida. Tente novamente.")
        elif escolha == "5":
            print("Encerrando seu Diário por aqui! Não se esqueça de voltar todos os dias e sempre que sentir algo diferente.")
            break
        else:
            print("Opção inválida. Tente novamente.")
