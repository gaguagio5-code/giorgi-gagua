import pytest

from bank import BankAccount

def test_initial_balance():
    assert BankAccount("Giorgi").balance==0.0
    assert BankAccount("Giorgi",100).balance==100

def test_deposit_success():
    accaunt = BankAccount("Giorgi", 100)
    assert accaunt.deposit(50) == 150
    assert accaunt.balance == 150

def test_deposit_negative():
    accaunt = BankAccount("giorgi", 100)
    with pytest.raises(ValueError, match="Amount must be positive"):
        accaunt.deposit(-10)
    with pytest.raises(ValueError, match="Amount must be positive"):
        accaunt.deposit(0)
    assert accaunt.balance == 100

def test_withdraw_success():
    accaunt = BankAccount("Giorgi", 200)
    assert accaunt.withdraw(50) == 150
    assert accaunt.balance == 150

def test_withdraw_insufficient_funds():
    accaunt = BankAccount("Giorgi", 100)
    with pytest.raises(ValueError, match="Balance is not enough"):
        accaunt.withdraw(500)
    assert accaunt.balance == 100

def test_withdraw_negative():
    accaunt = BankAccount("Giorgi", 100)
    with pytest.raises(ValueError, match="Amount must be positive"):
        accaunt.withdraw(-10)
    with pytest.raises(ValueError, match="Amount must be positive"):
        accaunt.withdraw(0)
    assert accaunt.balance ==100