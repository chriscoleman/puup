'''Potentially Universally Unique Phrase generator'''

__version__ = '0.1.1'

from puup.render import render


def puup(template='rran'):
    return tuple(render(template))


__all__ = ['puup']
