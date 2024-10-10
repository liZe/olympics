from io import StringIO

from olympics import cli

    
def test_top_collective():
    output = StringIO()
    cli.top_collective(file=output)
    result = output.getvalue()
    assert 'Top' in result
    
def test_top_individual():
    output = StringIO()
    cli.top_individual(top=10, file=output)
    result = output.getvalue()
    assert 'Top' in result

def test_top_countries_specific():
    string = StringIO()
    cli.top_countries(file=string)
    text = string.getvalue()
    assert 'Top' in text
    assert 'Gold' in text
    assert 'Silver' in text
    assert 'Bronze' in text
    assert 'Total' in text
    assert 'Total' in text and 'Gold' in text and 'Silver' in text and 'Bronze' in text

def test_top_countries():
    string = StringIO()
    cli.top_countries(file=string)
    text = string.getvalue()
    assert 'Top' in text, "Le titre 'Top' devrait être présent dans la sortie"
