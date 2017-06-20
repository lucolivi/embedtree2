#Module to encapsulates similarities functions

from string import punctuation
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer,PorterStemmer


def text_match(text1, text2, match_case=False):
    """Simple text match similarity function. Return 1 if match. 0 otherwise"""
    if not match_case:
        text1 = text1.lower()
        text2 = text2.lower()

    if text1 == text2:
        return 1.0

    return 0.0




class TokenSimilarity(object):
    """Class to implement methods for matching base on tokens."""

    def __init__(self):
        self._stopwords = list()
        self._stopwords += list(punctuation)
        #self._stopwords += stopwords.words("english")

    def _get_tokens(self, sentence):
        return [token for token in word_tokenize(sentence) if token not in self._stopwords]

    def jaccard(self, text1, text2, match_case=False):
        """
        Apply jaccard similarity in the texts tokens.
        Tokens are counted only one time within each text sample.
        """
        if not match_case:
            text1 = text1.lower()
            text2 = text2.lower()

        text1_tokens = set(self._get_tokens(text1))
        text2_tokens = set(self._get_tokens(text2))

        intersection_size = len(text1_tokens.intersection(text2_tokens))
        union_size = len(text1_tokens.union(text2_tokens))

        return float(intersection_size) / union_size


class StemTokenSimilarity(TokenSimilarity):
    """TokenSimilarity class based on stemmed tokens. Uses a dict as cache."""
    def __init__(self):
        self._stemmer = PorterStemmer()
        #self._stemmer = LancasterStemmer()
        self._stem_cache = dict()
        super(StemTokenSimilarity, self).__init__()

    def _get_stem(self, word):
        if word not in self._stem_cache:
            self._stem_cache[word] = self._stemmer.stem(word)
        return self._stem_cache[word]

    def _get_tokens(self, sentence):
        tokens = super(StemTokenSimilarity, self)._get_tokens(sentence)
        return [self._get_stem(t) for t in tokens]


if __name__ == "__main__":

    def main():
        t_sim = TokenSimilarity()
        print()

    def run_tests():
        #Tests
        assert text_match("lucas", "Lucas") == 1
        assert text_match("lucas", "Lucas", True) == 0
        assert text_match("lucas", "lucas", True) == 1

        t_sim = TokenSimilarity()
        assert t_sim.jaccard("Lucas Vieira de Oliveira", "Yvone Vieira de Oliveira") == 0.6
        assert t_sim.jaccard("Lucas Vieira de Oliveira ae", "Yvone Vieira de Oliveira") == 0.5
        assert t_sim.jaccard("Lucas Vieira de Oliveira ae ae ae", "Yvone Vieira de Oliveira") == 0.5
        del t_sim

        st_sim = StemTokenSimilarity()
        assert st_sim.jaccard("I am doing", "I will do") == 0.5
        assert st_sim.jaccard("Artificial Neural Networks", "Artificial Neural Network") == 1.0
        del st_sim

        print("All tests passed.")

    run_tests()
