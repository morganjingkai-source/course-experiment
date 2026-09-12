import pytest

from greetlab.cli import main


def test_normal_name(capsys):
    main(["Alice"])
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, Alice!"


def test_blank_name():
    with pytest.raises(SystemExit) as exc:
        main(["   "])
    assert exc.value.code == 2
