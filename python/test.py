import submission as s

# ----- Test Cases -----
# Test using the given example query.
def test_given_example():
    corpus = s.read_file('../lepanto.txt')
    tokenized_corpus = [line.split(" ") for line in corpus]
    
    tokenized_query = "his head a flag".split(" ")
    
    bm25 = s.BM25L(tokenized_corpus)
    
    scores = bm25.get_scores(tokenized_query)
    if s.validate_scores(scores) == False:
        answer = "No results found."
    else:
        answer = bm25.get_top_n(tokenized_query, corpus, n=1).pop()
    
    assert answer == "Holding his head up for a flag of all the free."

# Edge case: empty query.
def test_text_not_in_corpus():
    corpus = s.read_file('../lepanto.txt')
    tokenized_corpus = [line.split(" ") for line in corpus]
    
    tokenized_query = "Emsi Burning Glass".split(" ")
    
    bm25 = s.BM25L(tokenized_corpus)
    
    scores = bm25.get_scores(tokenized_query)
    if s.validate_scores(scores) == False:
        answer = "No results found."
    else:
        answer = bm25.get_top_n(tokenized_query, corpus, n=1).pop()
    
    assert answer == "No results found."
# ----- End of Test Cases -----

if __name__ == "__main__":
    test_given_example()
    test_text_not_in_corpus()
    print("All tests passed!")