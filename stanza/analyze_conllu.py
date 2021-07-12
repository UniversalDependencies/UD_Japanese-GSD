import sys
import stanza

nlp = stanza.Pipeline("ja")

for line in sys.stdin:
  for sent in nlp(line.rstrip()).sentences:
    print("# text =", sent.text)
    for token in sent.tokens:
      for w in token.words:
        print(w.id, w.text, w.lemma, w.upos, w.xpos, "_", w.head, w.deprel, "_", "_", sep="\t")
    print()
