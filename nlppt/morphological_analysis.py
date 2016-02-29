from .unitex import Unitex
unitex = Unitex()


def lemma(token, pos='N'):
    return unitex.lemma(token, pos)
