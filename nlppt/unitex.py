import os
import marisa_trie


class Unitex():
    """
        Class contains methods for dealing with unitex delaf dictionary
    """
    TRIE_PATH = os.path.join(os.path.dirname(__file__), 'data', 'lexicon', 'DELAF_PT.marisa')

    def __init__(self):
        self.trie = marisa_trie.Trie()
        self.trie.load(self.TRIE_PATH)

    def lemma(self, token, pos='N'):
        if self.trie.has_keys_with_prefix(token + '$'):
            if self.trie.has_keys_with_prefix(token + '$' + pos + '$'):
                return self.trie.keys(token + '$' + pos + '$')[0].split('$')[-2]
            elif self.trie.has_keys_with_prefix(token + '$' + pos + '+'):
                return self.trie.keys(token + '$' + pos + '+')[0].split('$')[-2]
            else:
                return self.trie.keys(token + '$')[0].split('$')[-2]
        else:
            return token
