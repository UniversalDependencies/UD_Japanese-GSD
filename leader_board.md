# UD_Japanese-GSD Dependency Parsing Leader Board

## About
In this page, we show the evaluation results of the models trained on UD_Japanese-GSD.
Send us a pull request if you want to add your model.

## Leader Board

All models are trained and evaluated on [UD_Japanese-GSD r2.8-NE](https://github.com/megagonlabs/UD_Japanese-GSD/releases/tag/r2.8NE).

|Rank| Analyzer                          | UPOS&LAS|   LAS   |   UAS   |  NER F  |  UPOS   | TOKENIZE|
|:---:|:---:| ---:| ---:| ---:| ---:| ---:| ---:|
|  - | spaCy v3 + bert_wwm + unidic_lite |         |         |         |         |         |         |
|  - | spaCy v3 + bert_wwm + ipdaic      |         |         |         |         |         |         |
|  - | spaCy v3 + chiVe35k               |**0.838**|**0.875**|**0.895**|**0.682**|**0.934**|**0.998**|

### Training Conditions

- spaCy v3 + bert_wwm + unidic_lite
  - Library: https://github.com/explosion/spaCy
  - Model: https://github.com/megagonlabs/UD_Japanese-GSD/releases/tag/r2.8-NE -> ja_gsd_bert_wwm_unidic_lite-3.0.0.tar.gz

- spaCy v3 + bert_wwm + ipadic
  - Library: https://github.com/explosion/spaCy
  - Model: https://github.com/megagonlabs/UD_Japanese-GSD/releases/tag/r2.8-NE -> ja_gsd_bert_wwm_ipadic-3.0.0.tar.gz

- spaCy v3 + chiVe35k
  - Library: https://github.com/explosion/spaCy
  - Model: https://github.com/megagonlabs/UD_Japanese-GSD/releases/tag/r2.8-NE -> ja_gsd-3.0.0.tar.gz
