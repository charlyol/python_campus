from python_project.guardian import Guardian


def test_construction():
    g = Guardian('Max', 'Verstappen')
    assert 'Max' == g.first_name
    assert 'Verstappen' == g.last_name
