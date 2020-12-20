"""Esse módulo é utilizado para realizar testes automáticos dos exercícios."""

import unittest
from unittest.mock import patch
import main


class Test(unittest.TestCase):
    """Classe para agregar os métodos que serão utilizados para testar."""
    def test_grande(self):
        """Função que testa um lado grande demais."""
        # Lista de valores que serão retornados pela função input.
        input_returns = [2, 2, 4]
        input_returns = map(str, input_returns)
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            mock_print.assert_called_with(
                'Os valores informados não formam um triângulo.')

    def test_negativo(self):
        """Função que testa valores negativos."""
        # Lista de valores que serão retornados pela função input.
        input_returns = [-2, 0, 0]
        input_returns = map(str, input_returns)
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            mock_print.assert_called_with(
                'Os valores informados não formam um triângulo.')

    def test_zero(self):
        """Função que testa valores nulos."""
        # Lista de valores que serão retornados pela função input.
        input_returns = [0, 0, 0]
        input_returns = map(str, input_returns)
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            mock_print.assert_called_with(
                'Os valores informados não formam um triângulo.')

    def test_equilátero(self):
        """Função que testa triângulo equilátero."""
        # Lista de valores que serão retornados pela função input.
        input_returns = [2, 2, 2]
        input_returns = map(str, input_returns)
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            mock_print.assert_called_with('O triângulo é equilátero.')

    def test_isósceles(self):
        """Função que testa triângulo isósceles."""
        # Lista de valores que serão retornados pela função input.
        input_returns = [2, 2, 3]
        input_returns = map(str, input_returns)
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            mock_print.assert_called_with('O triângulo é isósceles.')

    def test_escaleno(self):
        """Função que testa triângulo escaleno."""
        # Lista de valores que serão retornados pela função input.
        input_returns = [3, 4, 5]
        input_returns = map(str, input_returns)
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            mock_print.assert_called_with('O triângulo é escaleno.')


if __name__ == '__main__':
    unittest.main()
