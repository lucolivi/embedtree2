#Probabilistic Fuzzy Set Inference
#Autor: Lucas V. Oliveira

from collections import Counter

class PFSI(object):
    """Base class for implementation of a PFSI algorithm."""

    def inference(self, query_set, query_samples_cut=1.0, n_query_similar=10):
        assert isinstance(query_set, FuzzySet)

        query_similars = self.get_n_similar(query_set, query_samples_cut, n_query_similar)

        return query_similars

    def get_n_similar(self, query_set, cut_value=1.0, n=None):
        """Function to return the n similar sets to the passed query set."""
        assert isinstance(query_set, FuzzySet)

        n_similar = Counter()
        for set_obj in self.sets():
            similarity_value = query_set.similarity(set_obj)
            if similarity_value >= cut_value:
                n_similar[set_obj] = similarity_value

        return n_similar.most_common(n)


    def sets(self):
        """Abstract method that returns a iterable collection."""
        raise NotImplementedError

class FuzzySet(Counter):
    """Implementation of a simple fuzzyset based on collections.Counter."""

    def similarity(self, set_obj):
        """Computes the similarity from the range [0,1] between this set and the target set."""
        raise NotImplementedError
