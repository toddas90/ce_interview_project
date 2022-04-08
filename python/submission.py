# Rather than reinventing the wheel, I decided to use a well-built library
# to handle the specific implementation.
# The library can be found here: https://pypi.org/project/rank-bm25/
# The source code can be found here: https://github.com/dorianbrown/rank_bm25
# This library implements the formulas found in the paper: http://www.cs.otago.ac.nz/homepages/andrew/papers/2014-2.pdf

import sys
from rank_bm25 import BM25L

def read_file(filename):
    """Read the file and return a list of lines.
    
    Arguments:
    filename: The name of the file to read.
    """
    with open(filename, 'r') as f:
        return f.read().splitlines()
    
def get_query():
    """Get the query from the user."""
    query = input("Enter your query: ")
    return query

def validate_scores(scores):
    """Check if any of the scores are non-zero.
    
    Arguments:
    score: A list of scores.
    """
    return any(score != 0 for score in scores)

if __name__ == "__main__":
    # debug flag for seeing some extra details.
    # If there were more options, this would be extracted into a function.
    if len(sys.argv) > 1 and (sys.argv[1] == "--debug" or sys.argv[1] == "-d"):
        debug = True
    else:
        debug = False
    
    # Read the file in and parse the words.
    # Can easily make this a command line argument.
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
    
    print('\n' + answer)
    
    # If the debug flag is set, print out the scores and the top 5 results.
    if debug:
        print('\n')
        answer = bm25.get_top_n(tokenized_query, corpus, n=5)
        for i in answer:
            print(i)
        print(scores)
        