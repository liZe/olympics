from olympics.__main__ import main
import pytest
import argparse

def test_countries():
    argv = ['countries']
    main(argv)


def test_collective():
    argv = ['collective', '--top', '5']
    main(argv)


def test_individual():
    argv = ['individual', '--top', '3']
    main(argv)

def test_invalid_command():
    argv = ['invalid_command']
    try:
        main(argv)
    except SystemExit as e:
        assert e.code != 0

def test_non_integer_top():
    argv = ['individual', '--top', 'abc']
    try:
        main(argv)
    except SystemExit as e:
        assert e.code != 0

def test_top_non_positive():
    with pytest.raises(argparse.ArgumentTypeError):
        main(['countries', '--top', '-1'])

    with pytest.raises(argparse.ArgumentTypeError):
        main(['countries', '--top', '0'])

# test pour 'search' avec --query valide
def test_search_valid_query():
    argv = ['search', '--query', 'uga']
    main(argv)

# test pour 'search' sans --query
def test_search_missing_query():
    with pytest.raises(argparse.ArgumentTypeError):
        main(['search'])  # Appel sans --query
