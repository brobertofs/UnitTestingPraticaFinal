from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    # 3- Melhoria: Alteração na ordem das validações do metodo,
    # checando primeiro se existe um estoque, caso exista exibir a lista de sabores
    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        if not self.flavors:
            print("Estamos sem estoque atualmente!")
        else:
            print("\nNo momento temos os seguintes sabores de sorvete disponíveis:")
            for flavor in self.flavors:
                print(f"\t-{flavor}")

    # 6- BUG: Correção no retorno do metodo, para que informe o sabor e não a lista de sabores
    # 7- BUG: Adicionado retorno do metodo, quando for informado uma string vazia
    # 4- Melhoria: Alteração na ordem das validações do metodo,
    # checando primeiro se existe um estoque, se está buscando um sabor válido e se tem ou não tem o sabor no momento
    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        if not self.flavors:
            print("Estamos sem estoque atualmente!")
        elif not isinstance(flavor, str) or flavor == '':
            print("Por favor, informe um sabor válido.")
        elif flavor in self.flavors:
            print(f"Temos no momento {flavor}!")
        else:
            print(f"Não temos no momento {flavor}!")

    # 8- BUG: Removido do metodo o retorno desnecessario "Estamos sem estoque atualmente!"
    # 9- BUG: Adicionado retorno do metodo, quando for informado uma string vazia
    def add_flavor(self, flavor):
        """Adicione o sabor informado ao estoque."""
        if flavor == '':
            print("Por favor, informe um sabor válido.")
        elif flavor in self.flavors:
            print(f"{flavor} já disponível!")
        else:
            self.flavors.append(flavor)
            print(f"{flavor} adicionado ao estoque!")
