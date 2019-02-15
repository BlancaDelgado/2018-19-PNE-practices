# File with Seq class for working with sequences.


class Seq:
    """
    Class for working with sequences.

    METHODS
    ----
    1.-Class initialization
    2.-len()
    3.-complement()
    4.-reverse()
    5.-count(base)
    6.-perc(base)


    ATTRIBUTES
    ----
    1.- strbase: contains the sequence as a string


    """

    def __init__(self, strbase):
        """
        Passes string with sequence when creating the object.
        """
        self.strbase = strbase  # attribute self.strbase created

    def len(self):
        """
        Obtains length of the sequence.
        """
        return len(self.strbase)

    def complement(self):
        """
        Obtains complement sequence of the object's sequence.
        """

        dict_complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

        # CREATE AN ORDERED LIST WITH COMPLEMENTARY BASES
        complement_list = []
        for b in self.strbase:
            complement_list.append(dict_complement[b])

        # JOIN LIST TO CREATE STRING
        complement = ''.join(complement_list)

        return complement

    def reverse(self):
        """
        Returns reverse of the complement sequence.
        """

        # SUM NEW VALUE FIRST (last in seq)
        # TO THE ALREADY SAVED CHARACTERS (first in original seq)
        reverse = ''
        for i in self.complement():
            reverse = i + reverse  # each new value takes the first position

        return reverse

    def count(self, base):
        """
        :param base: chosen nucleotide of the DNA sequence (A, C, G, T)
        :return: number of times 'base' appears
        """
        counter = 0
        for i in self.strbase:
            if i == base:
                counter += 1

        return counter

    def perc(self, base):
        """
        :param base: chosen nucleotide of the DNA sequence (A, C, G, T)
        :return: percentage of 'base' over total number of bases
        """
        t_len = self.len()
        num_base = self.count(base)

        try:
            perc = round(100.0 * num_base / t_len, 1)

        except ZeroDivisionError:
            perc = 0.0

        return perc
