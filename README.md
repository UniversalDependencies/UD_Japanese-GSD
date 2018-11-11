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

2018-11-1   v2.3
  * Updates for v2.3.  More consistent with the labeling convensions discussed in UD Japanese team.  Many errors in morphologies have been fixed, and unknown words and dep labels are reduced.  XPOS is newly added.
2017-11-   v2.1
  * Updates for v2.1.  Several errors are removed by adding PoS/label rules and merging the manual dependency annotations in the original bunsetsu-style annotations in Google UDT 2.0.
2017-03-01 v2.0
  * Converted to UD v2 guidelines.
2016-11-15 v1.4
  * Initial release in Universal Dependencies.


=== Machine-readable metadata =================================================
Data available since: UD v1.4
License: CC BY-NC-SA 3.0 US
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
