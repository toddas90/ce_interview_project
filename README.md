## CE Interview Project Submission
This is my submission for the CE Intern position.

I would like to preface this by saying that I spent more time researching the problem
than actually coding. I'd never been given a problem like this before, so I wasn't
even sure what this type of problenm was called.

I went with a count-based approach because I thought that adding in meaning
would result in some false positives. The "Bag of Words" approach seemed nice
and easy, but it looked like they had a few shortcomings.

The reason that I decided to not go with the IDF approach is because I
thought that it would struggle with short documents. I wanted this example
to work on more than one document.

The reason that I went with a BM25 formula is because it seemed like
the best way to tackle a problem like this. From my limited research,
it seems like this formula is used by search engines to rank documents.
This [article](https://www.elastic.co/blog/practical-bm25-part-2-the-bm25-algorithm-and-its-variables) was really helpful in deciding which way to go.

I decided to use the [BM25L](http://www.cs.otago.ac.nz/homepages/andrew/papers/2014-2.pdf) formula to rank the lines because
it addresses the problem of document length bias unlike the standard
BM25 formula.

## Dependencies
The library I used for implementing the algorithm was [Rank-BM25](https://pypi.org/project/rank-bm25/)

To install it, run:

```
pip install --user rank_bm25
```

## Running
To run the script, you first need to be in the python directory:

```
cd python
```

Then you can run it with:

```
python submission.py
```

If you would like debugging information, you can run it with the debug flag

```
python submission.py --debug
```

## Research Used
[String Similarity Basic Guide](https://itnext.io/string-similarity-the-basic-know-your-algorithms-guide-3de3d7346227)

[Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity)

[Jaccard Index](https://en.wikipedia.org/wiki/Jaccard_index)

[Sørensen–Dice Coefficient](https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient)

[Tversky Index](https://en.wikipedia.org/wiki/Tversky_index)

[Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance)

[Text Vectorization](https://www.deepset.ai/blog/what-is-text-vectorization-in-nlp)

[BM25 Algorithm](https://www.elastic.co/blog/practical-bm25-part-2-the-bm25-algorithm-and-its-variables)

[Python BM25 Implementation](https://pypi.org/project/rank-bm25/)

[Improvements to BM25 and Language Models Examined](http://www.cs.otago.ac.nz/homepages/andrew/papers/2014-2.pdf)
