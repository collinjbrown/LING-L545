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

## The MatchMax Tokenizer
 You can find my implementation of the MaxMatch algorithm in
 C++ here: https://github.com/collinjbrown/UD_Japanese_Maxmatch.
 You can follow the instructions and build it yourself or
 just use one of the releases (which should include both
 Windows and Linux).
 My implementation is computationally fairly performant with
 the main drag being the process of scraping the datasets for
 the necessary data. The algorithm achieves a decent degree of
 accuracy, with a WER of 12.5% over the 542 sentences in the
 test data. As in the English examples we looked at in class,
 the mistakes it makes very often begin with small words and
 compound across the rest of the sentence. For example, "は い-",
 the topic particle followed by a word beginning in "い" is
 interpreted as "はい", as can be seen in "は い ない" which is
 interpreted as "はい ない" or "は いちばん" which becomes
 "はい ば ん". This latter example is one which would be remedied
 by having another system checking to ensure that each word
 obeys Japanese phonotactics, as "ん" is not allowed to sit on
 its own (though obviously there are informal exceptions to this,
 such as in "んまい" that would have to be accounted for). That
 such a naive implementation would perform relatively well is to
 some degree surprising, and I'm curious to see how a similar
 system would work for Tibetan.