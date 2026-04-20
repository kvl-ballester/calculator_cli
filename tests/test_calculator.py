from calculator.calculator import Calculator

def test_add():
    calculator = Calculator()
    assert 4 == calculator.sumar(2, 2)