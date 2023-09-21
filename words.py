def print_upper_words(words):
    """passes a list of words in and prints all words in uppercase """
    for word in words:
        print(word.upper())


def print_upper_e_words(words):
    """passes a list of words in and prints all words
    starting with 'e'in uppercase """
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words3(words, must_start_with):
    """Print each word on sep line, uppercased, if starts with one of given

        >>> print_upper_words3(["eagle", "Edward", "Alfred", "zope"],
        ...                   must_start_with=["A", "E"])
        EDWARD
        ALFRED
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
