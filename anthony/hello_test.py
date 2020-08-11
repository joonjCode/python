import hello
import pytest

def test_main(capsys):
    hello.main(['Joon'])

    out, err = capsys.readouterr()
    assert out == 'Hello Joon\n'
    assert err == ''

def test_main_error_with_emptystring(capsys):
    
    assert hello.main([''])

    out, err = capsys.readouterr()
    assert out == ''
    assert err == "Persons's name must not be empty\n"
