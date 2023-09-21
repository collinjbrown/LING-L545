# A Report on Segmentation & Tokenization
## The Segmenter
 While I was initially tempted to set up my neural network to
 segment this text, I'd run into a bottleneck computationally
 while working on my Tibetan neural segmenter which will
 require I optimize my backpropagation algorithm; not wanting to
 get far behind on this assignment by working on that, I thought
 it might be a wiser move to use a simple segmenter written
 in Python.

 This is a rather naive implementation of a segmenter for
 Basque that does have tests for abbreviations and other
 finnicky bits but is altogether not very impressive. It simply
 moves through the text, character by character, making certain
 decisions about sentence boundaries when it runs into
 punctuation marks. Specifically, it checks a number of
 characters ahead of the punctuation and applies certain basic
 rules to determine the rough likelihood that the character is
 end of a sentence, an abbreviation, or something else entirely.
 This, of course, requires that we make certain assumptions that
 may not always be accurate but which hold *most* of the time.

 Given a random selection from the corpus, the segmenter
 performed well, marking all the sentence boundaries correctly.
 However, this is likely because while I was perusing the
 corpus in preparation for writing the segmenter, I noticed
 certain potentially pernicious sequences and accounted for
 them while writing the code. For example, the Euskaltzaindia
 recommends the use of the full-stop after Roman numerals
 in names such as "Henry V." and in ordinal numbers. For
 example, "the 16th century" is rendered "XVI.go" which
 would have confused our segmenter had it not been accounted
 for.