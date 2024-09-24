class Veiculo:
    def __init__(self, placa, modelo, ano, disponivel=True):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.disponivel = disponivel

    def is_disponivel(self):
        return self.disponivel

    def set_disponivel(self, disponivel):
        self.disponivel = disponivel

    def __str__(self):
        return f"Modelo: {self.modelo}, Placa: {self.placa}, Ano: {self.ano}, Disponível: {'Sim' if self.disponivel else 'Não'}"


class Carro(Veiculo):
    def __init__(self, placa, modelo, ano, numero_de_portas, disponivel=True):
        super().__init__(placa, modelo, ano, disponivel)
        self.numero_de_portas = numero_de_portas

    def __str__(self):
        return super().__str__() + f", Número de portas: {self.numero_de_portas}"


class CarroLuxo(Carro):
    def __init__(self, placa, modelo, ano, numero_de_portas, ar_condicionado, disponivel=True):
        super().__init__(placa, modelo, ano, numero_de_portas, disponivel)
        self.ar_condicionado = ar_condicionado

    def __str__(self):
        return super().__str__() + f", Ar-condicionado: {'Sim' if self.ar_condicionado else 'Não'}"


class SistemaDeAluguel:
    def __init__(self):
        self.veiculos = []

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

    def listar_veiculos_disponiveis(self):
        if not any(veiculo.is_disponivel() for veiculo in self.veiculos):
            print("Nenhum veículo disponível no momento.")
            return

        for veiculo in self.veiculos:
            if veiculo.is_disponivel():
                print(veiculo)

    def encontrar_veiculo_por_placa(self, placa):
        for veiculo in self.veiculos:
            if veiculo.placa == placa:
                return veiculo
        return None

    def alugar_veiculo(self, placa):
        veiculo = self.encontrar_veiculo_por_placa(placa)
        if veiculo is not None and veiculo.is_disponivel():
            veiculo.set_disponivel(False)
            return True
        return False

    def devolver_veiculo(self, placa):
        veiculo = self.encontrar_veiculo_por_placa(placa)
        if veiculo is not None and not veiculo.is_disponivel():
            veiculo.set_disponivel(True)
            return True
        return False


def main():
    sistema = SistemaDeAluguel()

    sistema.adicionar_veiculo(Carro("ABC1234", "Fusca", 1980, 4))
    sistema.adicionar_veiculo(CarroLuxo("XYZ5678", "Ferrari 458", 2020, 2, True))
    sistema.adicionar_veiculo(Carro("DEF5678", "Civic", 2022, 4))
    sistema.adicionar_veiculo(CarroLuxo("LMN9012", "Tesla", 2023, 2, False))


    while True:
        print("\nBem-vindo à XY Veículos")
        print("        _______      \n" +
              "       //  ||\\ \\     \n" +
              " _____//___||_\\ \\___ \n" +
              " )  _    XY    _    \\\n" +
              " |_/ \\________/ \\___|\n" +
              "   \\_/        \\_/ ")
        print("\n1. Listar veículos disponíveis")
        print("2. Alugar veículo")
        print("3. Devolver veículo")
        print("4. Sair")

        while True:
            opcao = input("Escolha uma opção: ").strip()
            if opcao in {"1", "2", "3", "4"}:
                break
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")

        if opcao == "1":
            sistema.listar_veiculos_disponiveis()
        elif opcao == "2":
            while True:
                placa_aluguel = input("Digite a placa do veículo que deseja alugar: ").strip()
                if sistema.alugar_veiculo(placa_aluguel):
                    print("Veículo alugado com sucesso!")
                    break
                else:
                    print("Veículo não encontrado ou não disponível. Tente novamente.")
        elif opcao == "3":
            while True:
                placa_devolucao = input("Digite a placa do veículo que deseja devolver: ").strip()
                if sistema.devolver_veiculo(placa_devolucao):
                    print("Veículo devolvido com sucesso!")
                    break
                else:
                    print("Veículo não encontrado ou não está alugado. Tente novamente.")
        elif opcao == "4":
            print("Saindo...")
            break

        while True:
            resposta = input("Deseja fazer mais alguma coisa? (s/sim/n/não): ").strip().lower()
            if resposta in {"s", "sim"}:
                break
            elif resposta in {"n", "não", "nao", "Não", "Nao", "N"}:
                print("Saindo...")
                return  # Use return para sair da função main
            else:
                print("Resposta inválida. Por favor, digite 's', 'sim', 'n' ou 'não'.")


if __name__ == "__main__":
    main()
