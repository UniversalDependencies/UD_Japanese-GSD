# UD_Japanese-GSD Dependency Parsing Leader Board

## はじめに
このページではUD_Japanese-GSDを学習や精度評価に利用したUD解析系をリストアップしています。
追加登録を希望される方はIssueにてご連絡ください。

## Leader Board

UD_Japanese-GSD v2.6-NEを使用して学習・評価を実施。

|Rank|   Analyzer    |  MLAS   |   LAS   |   UAS   |  UPOS   | ENT(参考) |
|:---:|:---:| ---:| ---:| ---:| ---:| ---:|
|  1 | GiNZA v4.0.4  |**0.868**|**0.888**|**0.908**|  0.953  |  0.714  |
|  2 | spaCy v2.3.2  |  0.854  |  0.873  |  0.892  |  0.953  |  0.747  |
|  3 | Stanza v1.0.1 |  0.801  |  0.877  |  0.890  |  0.952  |**0.805**|

### Training Conditions

- Ginza v4.0.4
  - Library: https://github.com/megagonlabs/ginza
  - Model: Custom (UD_Japanese-GSD v2.6-NE with GiNZA specific parameter settings)
- spaCy v2.3.2
  - Library: https://github.com/explosion/spaCy
  - Model: https://spacy.io/models/ja#ja_core_news_md
- Stanza v1.0.1
  - Library: https://github.com/stanfordnlp/stanza
  - Model: Custom (UD_Japanese-GSD v2.6-NE)
