import pytest

from src.models.restaurant import Restaurant


class TestRestaurant:

    @pytest.fixture
    def restaurant_setup(self):
        # Criar uma instância do restaurante e retorná-la
        return Restaurant("Churrascão", "Carne na brasa")

    @pytest.mark.parametrize('expected_result',
                             ['Esse restaurante chama Churrascão e serve Carne na brasa.\n'
                              'Esse restaurante está servindo 0 consumidores desde que está aberto.\n'])
    def test_describe_restaurant(self, restaurant_setup, expected_result, capsys):
        # Setup
        restaurante = restaurant_setup

        # Chamada
        restaurante.describe_restaurant()
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == expected_result

    @pytest.mark.parametrize('initial_open_status, expected_result', [(False, 'Churrascão agora está aberto!\n'),
                                                                      (True, 'Churrascão já está aberto!\n')])
    def test_open_restaurant(self, restaurant_setup, initial_open_status, expected_result, capsys):
        # Setup
        restaurante = restaurant_setup
        restaurante.open = initial_open_status

        # Chamada
        restaurante.open_restaurant()
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == expected_result

    @pytest.mark.parametrize('initial_open_status, expected_result', [(True, 'Churrascão agora está fechado!\n'),
                                                                      (False, 'Churrascão já está fechado!\n')])
    def test_close_restaurant(self, restaurant_setup, initial_open_status, expected_result, capsys):
        # Setup
        restaurante = restaurant_setup
        restaurante.open = initial_open_status

        # Chamada
        restaurante.close_restaurant()
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == expected_result

    @pytest.mark.parametrize('initial_open_status, number_served, expected_result',
                             [(True, 10, 'Esse restaurante está servindo 10 consumidores desde que está aberto.\n'),
                              (True, '', 'Por favor, informe um valor válido (número inteiro)'
                                         ' para o número de clientes atendidos.\n'),
                              (True, 'um', 'Por favor, informe um valor válido (número inteiro)'
                                           ' para o número de clientes atendidos.\n'),
                              (False, 15, 'Churrascão está fechado!\n')])
    def test_set_number_served(self, restaurant_setup, initial_open_status, number_served, expected_result, capsys):
        # Setup
        restaurante = restaurant_setup
        restaurante.open = initial_open_status

        # Chamada
        restaurante.set_number_served(number_served)
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == expected_result

    @pytest.mark.parametrize('initial_open_status, number_served, increment, expected_result',
                             [(True, 50, 10, 'Esse restaurante está servindo 60 consumidores desde que está aberto.\n'),
                              (True, 50, '', 'Por favor, informe um valor válido (número inteiro)'
                                             ' para o número de clientes atendidos.\n'),
                              (True, 50, 'um', 'Por favor, informe um valor válido (número inteiro)'
                                               ' para o número de clientes atendidos.\n'),
                              (False, 50, 15, 'Churrascão está fechado!\n')])
    def test_increment_number_served(self, restaurant_setup, initial_open_status,
                                     number_served, increment, expected_result, capsys):
        # Setup
        restaurante = restaurant_setup
        restaurante.open = initial_open_status
        restaurante.number_served = number_served

        # Chamada
        restaurante.increment_number_served(increment)
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == expected_result
