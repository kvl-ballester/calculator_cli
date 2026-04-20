
class Calculator():
    def __init__(self):
        pass

    def sumar(self, num1, num2):
        """
        Suma dos números.
        :param num1: El primer número a sumar.
        :param num2: El segundo número a sumar.
        :return: La suma de los dos números.
        """
        
        return num1 + num2

    def restar(self, num1, num2):
        """
        Resta dos números.
        :param num1: El primer número a restar.
        :param num2: El segundo número a restar.
        :return: La resta de los dos números.
        """

        return num1 - num2

    def multiplicar(self, num1, num2):
        """
        Multiplica dos números.
        :param num1: El primer número a multiplicar.
        :param num2: El segundo número a multiplicar.
        :return: El producto de los dos números.
        """

        return num1 * num2

    def dividir(self, num1, num2):
        """
        Divide dos números.
        :param num1: El dividendo.
        :param num2: El divisor.
        :return: El cociente de la división.
        :raises ValueError: Si el divisor es cero.
        """

        if num2 == 0:
            raise ValueError("No se puede dividir por cero")
        
        return num1 / num2