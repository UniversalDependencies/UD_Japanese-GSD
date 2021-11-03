# Summary

This Universal Dependencies (UD) Japanese treebank is based on the definition of UD Japanese convention described in the UD documentation.  The original sentences are from Google UDT 2.0.


# Introduction

The Japanese UD treebank contains the sentences from Google Universal Dependency Treebanks v2.0 (legacy): https://github.com/ryanmcd/uni-dep-tb.  First, Google UDT v2.0 was converted to UD-style with bunsetsu-based word units (say "master" corpus).

The word units in "master" is significantly different from the definition of the documents based on **Short Unit Word** (SUW) [1], then the sentences are automatically re-processed by Hiroshi Kanayama in Feb 2017.  It is the Japanese_UD v2.0 and used in the CoNLL 2017 shared task.
In November 2017, UD_Japanese v2.0 is merged with the "master" data so that the manual annotations for dependencies can be reflected to the corpus. It reduced the errors in the dependency structures and relation labels.

Still there are slight differences in the word unit between UD_Japanese v2.1 and UD_Japanese-KTC 1.3.

In May 2020, we introduce UD_Japanese BCCWJ[3] like coversion method for UD_Japanese GSD v2.6.

# Specification


## Overview
The data is tokenized manually in a three layered tokenization of Short Unit Word (SUW)[4], Long Unit Word (LUW)[5], and base-phrase (bunsetsu)[5] as the `Balanced Corpus of Contemporary Written Japanese'[6]. The original morporlogical labels are based on UniDic POS tagset [7]
We use the slightly changed version of SUW as the UD word tokenization, in which the cardinal numbers are concatenated as in one word.

The (base-)phrase level dependency structures are annotated manually with the gudeline of BCCWJ-DepPara[8]. The phrase level dependency structures are converted into the word level dependency structures by the head rule of the dependency analyser CaboCha[9]. 

## LEMMA field

LEMMA is the base form of conjugated words -- verbs, adjectives, and auxiliary verbs by the UniDic schema [7].

## XPOS field

XPOS is the part-of-speech label for Short Unit Word (SUW) based on UniDic POS tagset [7].

## MISC field

- SpaceAfter: manually annotated to discriminate alphanumeric word tokens

- BunsetuPositionType: heads in a bunsetu by the head rules [9];
  - SEM_HEAD: the head content word
  - SYN_HEAD: the head functional word
  - CONT: the non-head content word
  - FUNC: the non-head functional word

- LUWPOS: the part-of-speech label for Long Unit Word (LUW) based on UniDic POS tagset [7].

- LUWBILabel: Long Unit Word (LUW) boundary labels [5]
  - B: Beginning of LUW
  - I: Inside of LUW
  
- UniDicLemma: lemma information based on UniDic [7]. The UniDic lemma normalise
 not only conjugation forms but also orthographical variants.
 
# Acknowledgments

The original treebank was provided by:

- Adam LaMontagne
- Milan Souček
- Timo Järvinen
- Alessandra Radici

via

- Dan Zeman.

The corpus was converted by:

- Mai Omura
- Yusuke Miyao
- Hiroshi Kanayama
- Hiroshi Matsuda

through annotation, discussion and validation with

- Aya Wakasa
- Kayo Yamashita
- Masayuki Asahara
- Takaaki Tanaka
- Yugo Murawaki
- Yuji Matsumoto
- Kaoru Ito
- Taishi Chika
- Shinsuke Mori
- Sumire Uematsu

# License

See file LICENSE.txt


# Reference

[1] Tanaka, T., Miyao, Y., Asahara, M., Uematsu, S., Kanayama, H., Mori, S., & Matsumoto, Y. (2016). Universal Dependencies for Japanese. In LREC.

[2] Asahara, M., Kanayama, H., Tanaka, T., Miyao, Y., Uematsu, S., Mori, S., Matsumoto, Y., Omura, M, & Murawaki, Y. (2018). Universal Dependencies Version 2 for Japanese. In LREC.

[3] Omura, M., & Asahara, M. (2020). UD-Japanese BCCWJ: Universal Dependencies Annotation for the Balanced Corpus of Contemporary Written Japanese. In UDW 2018.

[4] 小椋 秀樹, 小磯 花絵, 冨士池優美, 宮内 佐夜香, 小西 光, 原 裕 (2011).
『現代日本語書き言葉均衡コーパス』形態論情報規程集 第４版 （下）,（LR-CCG-10-05-02), 国立国語研究所, Tokyo, Japan.

[5] 小椋 秀樹, 小磯 花絵, 冨士池優美, 宮内 佐夜香, 小西 光, 原 裕 (2011).
『現代日本語書き言葉均衡コーパス』形態論情報規程集 第４版 （上）,（LR-CCG-10-05-01), 国立国語研究所, Tokyo, Japan.

[6] Maekawa, K., Yamazaki, M., Ogiso, T., Maruyama, T., Ogura, H., Kashino, W., Koiso, H., Yamaguchi, M., Tanaka, M., & Den, Y. (2014). Balanced Corpus of Contemporary Written Japanese. Language Resources and Evaluation, 48(2):345-371.

[7] Den, Y., Nakamura, J., Ogiso, T., Ogura, H., (2008). A Proper Approach to Japanese Morphologican Analysis: Dictionary, Model, and Evaluation. In LREC 2008. pp.1019-1024.

[8] Asahara, M., & Matsumoto, Y. (2016). BCCWJ-DepPara: A Syntactic Annotation Treebank on the `Balanced Corpus of Contemporary Written Japanese'. In ALR-12.

[9] Kudo, T. & Matsumoto, Y. (2002). Japanese Dependency Analysis using Cascaded Chunking, In CoNLL 2002. pp.63-69.

# Changelog
* 2020-05-   v2.6
  * Update for v2.6.  Introduce the conversion method of UD-Japanese BCCWJ [3]
  
* 2019-11-15 v2.5
  * Google gave permission to drop the "NC" restriction from the license.
    This applies to the UD annotations (not the underlying content, of which Google claims no ownership or copyright).

* 2018-11-   v2.3
  * Updates for v2.3.  Errors in morphologies are fixed, and unknown words and dep labels are reduced.  XPOS is added.
 
* 2017-11-   v2.1
  * Updates for v2.1.  Several errors are removed by adding PoS/label rules and merging the manual dependency annotations in the original bunsetu-style annotations in Google UDT 2.0.
  
* 2017-03-01 v2.0
  * Converted to UD v2 guidelines.
  
* 2016-11-15 v1.4
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
Lemmas: converted from manual
UPOS: converted from manual
XPOS: manual native
Features: not available
Relations: converted from manual
Contributors: Omura, Mai; Miyao, Yusuke; Kanayama, Hiroshi; Matsuda, Hiroshi; Wakasa, Aya; Yamashita, Kayo; Asahara, Masayuki; Tanaka, Takaaki; Murawaki, Yugo; Matsumoto, Yuji; Mori, Shinsuke; Uematsu, Sumire; McDonald, Ryan; Nivre, Joakim; Zeman, Daniel
Contributing: here
Contact: hkana@jp.ibm.com
===============================================================================
(Original treebank contributors: LaMontagne, Adam; Souček, Milan; Järvinen, Timo; Radici, Alessandra)
