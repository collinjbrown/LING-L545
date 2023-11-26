# Morphological Disambiguation
## Tagger Disambiguation
 UDPipe scores 94.69%, and the errors it does make seem to be more
 marginal. Specifically, it seems to tend to mistake certain word-suffix
 combinations as similar lexical items that lack suffixes (or feature
 different suffixes / clitics), and it tends to misidentify the lemma onto
 which certain suffixes attach. I imagine this is because of the
 agglutinative complexity of Finnish; it has a lot of suffixes and to my
 knowledge a somewhat complex morphophonological system determining the
 form of the root onto which they attach. We would expect then the
 perceptron to make similar errors in addition to broader, part-of-speech
 errors.

 The perceptron scores 90.36%. As expected, it more often totally
 mislabels the part-of-speech. It seems to frequently mistake adjectives
 for nouns; I don't know enough about Finnish grammar to say whether this
 is because of some feature of the language, though it wouldn't surprise
 me if it had to do with the fact that Finnish adjectives agree with their
 respective noun in terms of case and number. It also seems to have
 trouble with adverbs; it will mark them as nouns which seems a little
 strange since I would expect them to pattern quite differently, whereas I
 can see adjectives and nouns patterning similarly.

 In any case, UDPipe significantly outperforms the perceptron and while
 this isn't exactly surprising given that UDPipe is more developed and
 robust, I decided it would be interesting to try it out on another
 language: Standard Chinese.

 UDPipe scores 91.36% (admittedly a bit lower than I was expecting),
 whereas the perceptron scores 89.94%. I was curious to see if the
 difference would be less noticeable with a more analytic language, and
 while the two do perform similarly, I wonder whether this isn't due to
 the difference in the size of the training dataset between the two
 languages; the dataset for Standard Chinese is considerably smaller than
 for Finnish, probably contributing to the weaker performance of both
 taggers. However, it is interesting to note that there was less of a
 difference between the performance of the perceptron tagger on the
 Standard Chinese data and the Finnish data, whereas UDPipe scored
 significantly worse on the former.