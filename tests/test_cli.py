from io import StringIO

from olympics import cli


def test_top_countries():
    string = StringIO()
    cli.top_countries(file=string)
    text = string.getvalue()
    assert 'Top' in text
    
def test_top_countries():
    output = StringIO()
    cli.top_countries(file=output)
    result = output.getvalue()
    assert 'Top' in result

def test_top_collective():
    output = StringIO()
    cli.top_collective(file=output)
    result = output.getvalue()
    assert 'Top' in result
