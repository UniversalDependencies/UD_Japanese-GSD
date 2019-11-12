# Summary

This Universal Dependencies (UD) Japanese treebank is based on the definition of UD Japanese convention described in the UD documentation.  The original sentences are from Google UDT 2.0.


# Introduction

The Japanese UD treebank contains the sentences from Google Universal Dependency Treebanks v2.0 (legacy): https://github.com/ryanmcd/uni-dep-tb.  First, Google UDT v2.0 was converted to UD-style with bunsetsu-based word units (say "master" corpus).

The word units in "master" is significantly different from the definition of the documents based on Short Word Unit (SWU) [1], then the sentences are automatically re-processed by Hiroshi Kanayama in Feb 2017.  It is the Japanese_UD v2.0 and used in the CoNLL 2017 shared task.
In November 2017, UD_Japanese v2.0 is merged with the "master" data so that the manual annotations for dependencies can be reflected to the corpus. It reduced the errors in the dependency structures and relation labels.

Still there are slight differences in the word unit between UD_Japanese v2.1 and UD_Japanese-KTC 1.3.  The manual segmentation work is ongoing by the group of Masayuki Asahara so that the divergence of the two Japanese treebanks should be fixed in the future.



# Acknowledgments

The original treebank was provided by:

- Adam LaMontagne
- Milan Souček
- Timo Järvinen
- Alessandra Radici

via

- Dan Zeman.

The corpus was converted by:

- Hiroshi Kanayama

through discussion and validation with

- Yusuke Miyao
- Masayuki Asahara
- Takaaki Tanaka
- Yuji Matsumoto
- Shinsuke Mori
- Sumire Uematsu

# License

See file LICENSE.txt


# Reference

[1] Tanaka, T., Miyao, Y., Asahara, M., Uematsu, S., Kanayama, H., Mori, S., & Matsumoto, Y. (2016). Universal Dependencies for Japanese. In LREC.

[2] Asahara, M., Kanayama, H., Tanaka, T., Miyao, Y., Uematsu, S., Mori, S., Matsumoto, Y., Omura, M, & Murawaki, Y. (2018). Universal Dependencies Version 2 for Japanese. In LREC.


# Changelog

* 2019-11-15 v2.5
  * Google gave permission to drop the "NC" restriction from the license.
    This applies to the UD annotations (not the underlying content, of which Google claims no ownership or copyright).
2018-11-1   v2.3
  * Updates for v2.3.  More consistent with the labeling convensions discussed in UD Japanese team.  Many errors in morphologies have been fixed, and unknown words and dep labels are reduced.  XPOS is newly added.
2017-11-   v2.1
  * Updates for v2.1.  Several errors are removed by adding PoS/label rules and merging the manual dependency annotations in the original bunsetsu-style annotations in Google UDT 2.0.
2017-03-01 v2.0
  * Converted to UD v2 guidelines.
2016-11-15 v1.4
  * Initial release in Universal Dependencies.


```
===================================
Universal Dependency Treebanks v2.0
(legacy information)
===================================

=========================
Licenses and terms-of-use
=========================

For the following languages

  German, Spanish, French, Indonesian, Italian, Japanese, Korean and Brazilian
  Portuguese

we will distinguish between two portions of the data.

1. The underlying text for sentences that were annotated. This data Google
   asserts no ownership over and no copyright over. Some or all of these
   sentences may be copyrighted in some jurisdictions.  Where copyrighted,
   Google collected these sentences under exceptions to copyright or implied
   license rights.  GOOGLE MAKES THEM AVAILABLE TO YOU 'AS IS', WITHOUT ANY
   WARRANTY OF ANY KIND, WHETHER EXPRESS OR IMPLIED.

2. The annotations -- part-of-speech tags and dependency annotations. These are
   made available under a CC BY-SA 4.0. GOOGLE MAKES
   THEM AVAILABLE TO YOU 'AS IS', WITHOUT ANY WARRANTY OF ANY KIND, WHETHER
   EXPRESS OR IMPLIED. See attached LICENSE file for the text of CC BY-NC-SA.

Portions of the German data were sampled from the CoNLL 2006 Tiger Treebank
data. Hans Uszkoreit graciously gave permission to use the underlying
sentences in this data as part of this release.

Any use of the data should reference the above plus:

  Universal Dependency Annotation for Multilingual Parsing
  Ryan McDonald, Joakim Nivre, Yvonne Quirmbach-Brundage, Yoav Goldberg,
  Dipanjan Das, Kuzman Ganchev, Keith Hall, Slav Petrov, Hao Zhang,
  Oscar Tackstrom, Claudia Bedini, Nuria Bertomeu Castello and Jungmee Lee
  Proceedings of ACL 2013

=======
Contact
=======

ryanmcd@google.com
joakim.nivre@lingfil.uu.se
slav@google.com
See https://github.com/ryanmcd/uni-dep-tb for more details
```



=== Machine-readable metadata =================================================
Data available since: UD v1.4
License: CC BY-SA 4.0
Includes text: yes
Genre: news blog
Lemmas: automatic with corrections
UPOS: converted with corrections
XPOS: converted with corrections
Features: not available
Relations: converted with corrections
Contributors: Kanayama, Hiroshi; Asahara, Masayuki; Miyao, Yusuke; Tanaka, Takaaki; McDonald, Ryan; Nivre, Joakim; Zeman, Daniel; Matsumoto, Yuji; Mori, Shinsuke; Uematsu, Sumire
Contributing: here
Contact: hkana@jp.ibm.com
===============================================================================
(Original treebank contributors: LaMontagne, Adam; Souček, Milan; Järvinen, Timo; Radici, Alessandra)
