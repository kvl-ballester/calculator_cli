from calculator.calculator import Calculator
import pytest

def test_add():
    calculator = Calculator()
    assert 4 == calculator.sumar(2, 2)

def test_restar():
    calculator = Calculator()
    assert 4 == calculator.restar(10, 6)

def test_multiplicar():
    calculator = Calculator()
    assert 4 == calculator.multiplicar(2, 2)

def test_dividir():
    calculator = Calculator()
    assert 4 == calculator.dividir(8, 2)

def test_dividir_por_cero():
    calculator = Calculator()

    with pytest.raises(ValueError):
        calculator.dividir(10,0)