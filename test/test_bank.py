from src.bank import Bank


def test_create_new_bank():
    b = Bank('Chase')
    assert b.name == 'Chase'
    assert len(b.clients) == 0
