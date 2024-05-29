from python_project.guardian import Guardian
from python_project.player_test import Player


def test_construction():
    p = Player('Charles', 'Leclerc')
    assert 'Charles' == p.first_name
    assert 'Leclerc' == p.last_name
    assert [] == p.guardians


def test_add_gardians():
    g = Guardian('Max', 'Verstappen')
    p = Player('Charles', 'Leclerc')
    p.add_guardian(g)
    assert [g] == p.guardians
