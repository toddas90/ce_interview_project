# I went with a count-based approach because I thought that adding in meaning
# would result in some false positives. The "Bag of Words" approach seemed nice
# and easy, but it looked like they had a few shortcomings.

# The reason that I decided to not go with the TF-IDF approach is because I
# thought that it would struggle with short documents. I wanted this example
# to work on more than one document.

# The reason that I went with a BM25 formula is because it seemed like
# the best way to tackle a problem like this. From my limited research,
# it seems like this formula is used by search engines to rank documents.

# I decided to use the BM25L formula to rank the lines because
# it addresses the problem of document length bias unlike the standard
# BM25 formula.

# Rather than reinventing the wheel, I decided to use a well-built library
# to handle the specific implementation.
# The library can be found here: https://pypi.org/project/rank-bm25/
# The source code can be found here: https://github.com/dorianbrown/rank_bm25
# This library implements the formulas found in the paper: http://www.cs.otago.ac.nz/homepages/andrew/papers/2014-2.pdf

import sys
from rank_bm25 import BM25L

# ----- Test Cases -----
def test_runner():
    test_given_example()
    test_numbers_as_query()
    test_text_not_in_corpus()
    print("All tests passed!")

# Test using the given example query.
def test_given_example():
    corpus = read_file('../lepanto.txt')
    tokenized_corpus = [line.split(" ") for line in corpus]
    
    tokenized_query = "his head a flag".split(" ")
    
    bm25 = BM25L(tokenized_corpus)
    
    scores = bm25.get_scores(tokenized_query)
    if validate_scores(scores) == False:
        answer = "No results found."
    else:
        answer = bm25.get_top_n(tokenized_query, corpus, n=1).pop()
    
    assert answer == "Holding his head up for a flag of all the free."
    
def test_numbers_as_query():
    corpus = read_file('../lepanto.txt')
    tokenized_corpus = [line.split(" ") for line in corpus]
    
    tokenized_query = "1 2 3 4 5 6 7 8 9 10".split(" ")
    
    bm25 = BM25L(tokenized_corpus)
    
    scores = bm25.get_scores(tokenized_query)
    if validate_scores(scores) == False:
        answer = "No results found."
    else:
        answer = bm25.get_top_n(tokenized_query, corpus, n=1).pop()
    
    assert answer == "No results found."

def test_text_not_in_corpus():
    corpus = read_file('../lepanto.txt')
    tokenized_corpus = [line.split(" ") for line in corpus]
    
    tokenized_query = "Emsi Burning Glass".split(" ")
    
    bm25 = BM25L(tokenized_corpus)
    
    scores = bm25.get_scores(tokenized_query)
    if validate_scores(scores) == False:
        answer = "No results found."
    else:
        answer = bm25.get_top_n(tokenized_query, corpus, n=1).pop()
    
    assert answer == "No results found."
# ----- End of Test Cases -----


# read a text file into a list of strings.
def read_file(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()
    
    
# get user input for the query.
def get_query():
    query = input("Enter your query: ")
    return query


def validate_scores(scores):
    return any(score != 0 for score in scores)


if __name__ == "__main__":
    # debug flag for seeing some extra details.
    # If there were more options, this would be extracted into a function.
    if len(sys.argv) > 1 and (sys.argv[1] == "--debug" or sys.argv[1] == "-d"):
        debug = True
    elif len(sys.argv) > 1 and (sys.argv[1] == "--test" or sys.argv[1] == "-t"):
        test_runner()
        exit(0)
    else:
        debug = False
        testing = False
    
    # Read the file in and parse the words.
    corpus = read_file('../lepanto.txt')
    tokenized_corpus = [line.split(" ") for line in corpus]
    
    # Get the user input and parse it.
    query = get_query()
    tokenized_query = query.split(" ")
    
    # Getting the BM25 scores for the query.
    bm25 = BM25L(tokenized_corpus)
    
    # Check to see if any of the queries have a score over 0.
    # If they dont, then the query probably isn't in the corpus.
    scores = bm25.get_scores(tokenized_query)
    if validate_scores(scores) == False:
        print("No results found.")
        exit()
        
    
    answer = bm25.get_top_n(tokenized_query, corpus, n=1).pop()
    
    print(answer)
    
    if debug:
        print('\n')
        answer = bm25.get_top_n(tokenized_query, corpus, n=5)
        for i in answer:
            print(i)
        print('\n')
        doc_scores = bm25.get_scores(tokenized_query)
        print(doc_scores)
        