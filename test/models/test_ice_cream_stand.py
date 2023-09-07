import pytest

from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    sem_estoque = []
    com_estoque = ['Ovomaltine', 'Avelã', 'Nata goiaba']

    @pytest.fixture
    def setup_ice_cream_stand(self, estoque):
        return IceCreamStand('Sorveteria Quero Mais', 'sorvete', estoque)

    @pytest.fixture
    def setup_ice_cream_stand_no_estoque(self):
        return IceCreamStand('Sorveteria Quero Mais', 'sorvete', [])

    @pytest.mark.parametrize('estoque, expected_result',
                             [(com_estoque, '\nNo momento temos os seguintes sabores de sorvete disponíveis:'
                              '\n\t-Ovomaltine\n\t-Avelã\n\t-Nata goiaba\n'),
                              (sem_estoque, 'Estamos sem estoque atualmente!\n')])
    def test_flavors_available(self, setup_ice_cream_stand, estoque, expected_result, capsys):
        # Setup
        sorveteria = setup_ice_cream_stand

        # Chamada
        sorveteria.flavors_available()
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == expected_result

    @pytest.mark.parametrize('estoque, flavor, expected_result',
                             [(com_estoque, 'Ovomaltine', 'Temos no momento Ovomaltine!\n'),
                              (com_estoque, '', 'Por favor, informe um sabor válido.\n'),
                              (com_estoque, 'Flocos', 'Não temos no momento Flocos!\n'),
                              (sem_estoque, 'Ovomaltine', 'Estamos sem estoque atualmente!\n'),
                              (sem_estoque, '', 'Estamos sem estoque atualmente!\n'),
                              (sem_estoque, 'Flocos', 'Estamos sem estoque atualmente!\n')])
    def test_find_flavor(self, setup_ice_cream_stand, flavor, expected_result, capsys):
        # Setup
        sorveteria = setup_ice_cream_stand

        # Chamada
        sorveteria.find_flavor(flavor)
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == expected_result

    @pytest.mark.parametrize('estoque, flavor, expected_result',
                             [(com_estoque, 'Flocos', 'Flocos adicionado ao estoque!\n'),
                              (com_estoque, 'Avelã', 'Avelã já disponível!\n'),
                              (com_estoque, '', 'Por favor, informe um sabor válido.\n'),
                              (sem_estoque, 'Flocos', 'Flocos adicionado ao estoque!\n'),
                              (sem_estoque, '', 'Por favor, informe um sabor válido.\n')])
    def test_add_flavor(self, setup_ice_cream_stand, flavor, expected_result, capsys):
        # Setup
        sorveteria = setup_ice_cream_stand

        # Chamada
        sorveteria.add_flavor(flavor)
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == expected_result
