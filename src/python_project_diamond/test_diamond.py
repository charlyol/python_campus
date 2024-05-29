from python_project_diamond.diamond import create_diamond, create_diamond_full


def test_diamond_b():
    assert create_diamond("B") == """\
 A
B B
 A"""


def test_diamond_c():
    assert create_diamond("C") == """\
  A
 B B
C   C
 B B
  A"""


def test_diamond_d():
    assert create_diamond("D") == """\
   A
  B B
 C   C
D     D
 C   C
  B B
   A"""

def test_diamond_a():
    assert create_diamond("A") == "A"


#     A
#    B B
#   C   C
#  D     D
# E       E
#  D     D
#   C   C
#    B B
#     A


def test_diamond_full():
    assert create_diamond_full("C") == """\
  A
 BAB
CBABC
 BAB
  A"""


def diamond(letter):
    if letter == "C":
        return """A\nB B\nC   C\nB B\nA"""
    if letter == "D":
        return """A\nB B\nC   C\nD     D\nC   C\nB B\nA"""
    if letter == "E":
        return """A\nB B\nC   C\nD     D\nE       E\nD     D\nC   C\nB B\nA"""
    if letter == "F":
        return """A\nB B\nC   C\nD     D\nE       E\nF         F\nE       E\nD     D\nC   C\nB B\nA"""
    if letter == "G":
        return """A\nB B\nC   C\nD     D\nE       E\nF         F\nG           G\nF         F\nE       E\nD     D\nC   C\nB B\nA"""
    if letter == "H":
        return """A\nB B\nC   C\nD     D\nE       E\nF         F\nG           G\nH             H\nG           G\nF         F\nE       E\nD     D\nC   C\nB B\nA"""
    if letter == "I":
        return """A\nB B\nC   C\nD     D\nE       E\nF         F\nG           G\nH             H\nI               I\nH             H\nG           G\nF         F\nE       E\nD     D\nC   C\nB B\nA"""
    if letter == "J":
        return """A\nB B\nC   C\nD     D\nE       E\nF         F\nG           G\nH             H\nI               I\nJ                 J\nI               I\nH             H\nG           G\nF         F\nE       E\nD     D\nC   C\nB B\nA"""
    if letter == "K":
        return """A\nB B\nC   C\nD     D\nE       E\nF         F\nG           G\nH             H\nI               I\nJ                 J\nK                   K\nJ                 J\nI               I\nH             H\nG           G\nF         F\nE       E\nD     D\nC   C\nB B\nA"""
    if letter == "L":
        return """A\nB B\nC   C\nD     D\nE       E\nF         F\nG           G\nH             H\nI               I\nJ                 J\nK                   K\nL                     L\nK                   K\nJ                 J\nI               I\nH             H\nG           G\nF         F\nE       E\nD     D\nC   C\nB B\nA"""
    if letter == "M":
        return """A\nB B\nC   C\nD     D\nE       E\nF         F\nG           G\nH             H\nI               I\nJ                 J\nK                   K\nL                     L\nM                       M\nL                     L\nK                   K\nJ                 J\nI               I\nH             H\nG           G\nF         F\nE       E\nD     D\nC   C\nB B\nA"""
    if letter == "N":
        return """A\nB B\nC   C\nD     D\nE       E\nF         F\nG           G\nH             H\nI               I\nJ                 J\nK                   K\nL                     L\nM                       M\nN                         N\nM                       M\nL                     L\nK                   K\nJ                 J\nI               I\nH             H\nG           G\nF         F\nE       E\nD     D\nC   C\nB B\nA"""
    if letter == "O":
        return """A\nB B\nC   C\nD     D\nE       E\nF         F\nG           G\nH             H\nI               I\nJ                 J\nK                   K\nL                     L\nM                       M\nN                         N\nO                           O\nN                         N\nM                       M\nL                     L\nK                   K\nJ                 J\nI               I\nH             H\nG           G\nF         F\nE       E\nD     D\nC   C\nB B\nA"""
    if letter == "P":
        return """A\nB B\nC   C\nD     D\nE       E\nF         F\nG           G\nH             H\nI               I\nJ                 J\nK                   K\nL                     L\nM                       M\nN                         N\nO                           O\nP                             P\nO                           O\nN                         N\nM                       M\nL                     L\nK                   K\nJ                 J\nI               I\nH             H\nG           G\nF         F\nE       E\nD     D\nC   C\nB B\nA"""
    if letter == "Q":
        return """A\nB B\nC   C\nD     D\nE       E\nF         F\nG           G\nH             H\nI               I\nJ                 J\nK                   K\nL                     L\nM                       M\nN                         N\nO                           O\nP                             P\nQ                               Q\nP                             P\nO                           O\nN                         N\nM                       M\nL                     L\nK                   K\nJ                 J\nI               I\nH             H\nG           G\nF         F\nE       E\nD     D\nC   C\nB B\nA"""
    if letter == "R":
        return """A\nB B\nC   C\nD     D\nE       E\nF         F\nG           G\nH             H\nI               I\nJ                 J\nK                   K\nL                     L\nM                       M\nN                         N\nO                           O\nP                             P\nQ                               Q\nR                                 R\nQ                               Q\nP                             P\nO                           O\nN                         N\nM                       M\nL                     L\nK                   K\nJ                 J\nI               I\nH             H\nG           G\nF         F\nE       E\nD     D\nC   C\nB B\nA"""
    if letter == "S":
        return """A\nB B\nC   C\nD     D\nE       E\nF         F\nG           G\nH             H\nI               I\nJ                 J\nK                   K\nL                     L\nM                       M\nN                         N\nO                           O\nP                             P\nQ                               Q\nR                                 R\nS                                   S\nR                                 R\nQ                               Q\nP                             P\nO                           O\nN                         N\nM                       M\nL                     L\nK                   K\nJ                 J\nI               I\nH             H\nG           G\nF         F\nE       E\nD     D\nC   C\nB B\nA"""
    if letter == "T":
        return """A\nB B\nC   C\nD     D\nE       E\nF         F\nG           G\nH             H\nI               I\nJ                 J\nK                   K\nL                     L\nM                       M\nN                         N\nO                           O\nP                             P\nQ                               Q\nR                                 R\nS                                   S\nT                                     T\nS                                   S\nR                                 R\nQ                               Q\nP                             P\nO                           O\nN                         N\nM                       M\nL                     L\nK                   K\nJ                 J\nI               I\nH             H\nG           G\nF         F\nE       E\nD     D\nC   C\nB B\nA"""
    if letter == "U":
        return """A\nB B\nC   C\nD     D\nE       E\nF         F\nG           G\nH             H\nI               I\nJ                 J\nK                   K\nL                     L\nM                       M\nN                         N\nO                           O\nP                             P\nQ                               Q\nR                                 R\nS                                   S\nT                                     T\nU                                       U\nT                                     T\nS                                   S\nR                                 R\nQ                               Q\nP                             P\nO                           O\nN                         N\nM                       M\nL                     L\nK                   K\nJ                 J\nI               I\nH             H\nG           G\nF         F\nE       E\nD     D\nC   C\nB B\nA"""
    if letter == "V":
        return """A\nB B\nC   C\nD     D\nE       E\nF         F\nG           G\nH             H\nI               I\nJ                 J\nK                   K\nL                     L\nM                       M\nN                         N\nO                           O\nP                             P\nQ                               Q\nR                                 R\nS                                   S\nT                                     T\nU                                       U\nV                                         V\nU                                       U\nT                                     T\nS                                   S\nR                                 R\nQ                               Q\nP                             P\nO                           O\nN                         N\nM                       M\nL                     L\nK                   K\nJ                 J\nI               I\nH             H\nG           G\nF         F\nE       E\nD     D\nC   C\nB B\nA"""
    if letter == "W":
        return """A\nB B\nC   C\nD     D\nE       E\nF         F\nG           G\nH             H\nI               I\nJ                 J\nK                   K\nL                     L\nM                       M\nN                         N\nO                           O\nP                             P\nQ                               Q\nR                                 R\nS                                   S\nT                                     T\nU                                       U\nV                                         V\nW                                           W\nV                                         V\nU                                       U\nT                                     T\nS                                   S\nR                                 R\nQ                               Q\nP                             P\nO                           O\nN                         N\nM                       M\nL                     L\nK                   K\nJ                 J\nI               I\nH             H\nG           G\nF         F\nE       E\nD     D\nC   C\nB B\nA"""
    if letter == "X":
        return """A\nB B\nC   C\nD     D\nE       E\nF         F\nG           G\nH             H\nI               I\nJ                 J\nK                   K\nL                     L\nM                       M\nN                         N\nO                           O\nP                             P\nQ                               Q\nR                                 R\nS                                   S\nT                                     T\nU                                       U\nV                                         V\nW                                           W\nX                                             X\nW                                           W\nV                                         V\nU                                       U\nT                                     T\nS                                   S\nR                                 R\nQ                               Q\nP                             P\nO                           O\nN                         N\nM                       M\nL                     L\nK                   K\nJ                 J\nI               I\nH             H\nG           G\nF         F\nE       E\nD     D\nC   C\nB B\nA"""
    if letter == "Y":
        return """A\nB B\nC   C\nD     D\nE       E\nF         F\nG           G\nH             H\nI               I\nJ                 J\nK                   K\nL                     L\nM                       M\nN                         N\nO                           O\nP                             P\nQ                               Q\nR                                 R\nS                                   S\nT                                     T\nU                                       U\nV                                         V\nW                                           W\nX                                             X\nY                                               Y\nX                                             X\nW                                           W\nV                                         V\nU                                       U\nT                                     T\nS                                   S\nR                                 R\nQ                               Q\nP                             P\nO                           O\nN                         N\nM                       M\nL                     L\nK                   K\nJ                 J\nI               I\nH             H\nG           G\nF         F\nE       E\nD     D\nC   C\nB B\nA"""
    if letter == "Z":
        return """A\nB B\nC   C\nD     D\nE       E\nF         F\nG           G\nH             H\nI               I\nJ                 J\nK                   K\nL                     L\nM                       M\nN                         N\nO                           O\nP                             P\nQ                               Q\nR                                 R\nS                                   S\nT                                     T\nU                                       U\nV                                         V\nW                                           W\nX                                             X\nY                                               Y\nZ                                                 Z\nY                                               Y\nX                                             X\nW                                           W\nV                                         V\nU                                       U\nT                                     T\nS                                   S\nR                                 R\nQ                               Q\nP                             P\nO                           O\nN                         N\nM                       M\nL                     L\nK                   K\nJ                 J\nI               I\nH             H\nG           G\nF         F\nE       E\nD     D\nC   C\nB B\nA"""
    return " A\nB B\n A"


