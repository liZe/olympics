from olympics.__main__ import main


def test_countries():
    argv = ['countries']
    main(argv)  


def test_collective():
    argv = ['collective', '--top', '5']
    main(argv)  


def test_individual():
    argv = ['individual', '--top', '3']
    main(argv)  


def test_negative_top():
    argv = ['countries', '--top', '-5']
    try:
        main(argv)
    except SystemExit as e:
        assert str(e) == "1"  


def test_zero_top():
    argv = ['individual', '--top', '0']
    try:
        main(argv)
    except SystemExit as e:
        assert str(e) == "1"  # Cela va check si le code de sortie est 1 pour une erreur
