# UD_Japanese-GSD Dependency Parsing Leader Board

## About
In this page, we show the evaluation results of the models trained on UD_Japanese-GSD.
Send us a pull request if you want to add your model.

## Leader Board

All models are trained and evaluated on [UD_Japanese-GSD r2.8-NE](https://github.com/megagonlabs/UD_Japanese-GSD/releases/tag/r2.8-NE).

|Rank| Analyzer                                            | UPOS&LAS|   LAS   |   UAS   |  NER F  |  UPOS   | TOKENIZE|
|:---:|:--- |:---:|:---:|:---:|:---:|:---:|:---:|
|  1 | spaCy v3.1 + morphologizer + bert_v2                |**0.915**|**0.920**|**0.930**|**0.848**|**0.971**|**0.981**|
|  2 | spaCy v3.1 + morphologizer + bert_char_v2 (basic)   | *0.901* | *0.908* | *0.919* |**0.847**|**0.967**|**0.981**|
|  3 | spaCy v3.1 + chiVe35k + morphologizer               |  0.874  |  0.886  |  0.904  |  0.672  |  0.955  |**0.981**|
|  4 | spaCy v3.1 + chiVe35k                               |  0.842  |  0.881  |  0.900  |  0.682  |  0.934  |**0.981**|
|  - | (Stanza v1.2.1 offical model)                       |  0.900  |  0.904  |  0.915  |    -    |  0.956  |  0.969  |

### Training Conditions

- spaCy v3.1 + morphologizer + bert_v2
  - Library: https://github.com/explosion/spaCy
  - Transformers model: https://huggingface.co/cl-tohoku/bert-base-japanese-v2
  - Model: https://github.com/megagonlabs/UD_Japanese-GSD/releases/tag/r2.8-NE -> ja_gsd_bert_v2-3.1.2.tar.gz

- spaCy v3.1 + morphologizer + bert_char_v2 (basic)
  - Library: https://github.com/explosion/spaCy
  - Transformers model: https://huggingface.co/cl-tohoku/bert-base-japanese-char-v2
  - Model: https://github.com/megagonlabs/UD_Japanese-GSD/releases/tag/r2.8-NE -> ja_gsd_bert_char_v2_basic-3.1.3.tar.gz

- spaCy v3.1 + chiVe35k + morphologizer
  - Library: https://github.com/explosion/spaCy
  - Model: https://github.com/megagonlabs/UD_Japanese-GSD/releases/tag/r2.8-NE -> ja_gsd-3.1.1.tar.gz

- spaCy v3.1 + chiVe35k
  - Library: https://github.com/explosion/spaCy
  - Model: https://github.com/megagonlabs/UD_Japanese-GSD/releases/tag/r2.8-NE -> ja_gsd-3.1.0.tar.gz

### spaCy model configuration

- train
```console
cd ./spacy
python -m spacy train spacy/config/ja_gsd_bert_v2.cfg --output ja_gsd_bert_v2 --paths.train spacy/ja_gsd-ud-train.ne.random_sents.spacy --paths.dev ja_gsd-ud-dev.ne.random_sents.spacy --gpu-id 0
```
- evaluate
```console
python spacy/evaluate_model.py ja_gsd_bert_v2/model-last/ spacy/ja_gsd-ud-test.ne.1.json
```
or
```console
mkdir -p eval
python -m spacy evaluate ja_gsd_bert_v2/model-last/ spacy/ja_gsd-ud-test.ne.1.spacy
```
- package
```console
python spacy/config/setup_meta.py spacy/config/ja_gsd_bert_v2.meta.json ja_gsd_bert_v2/model-last/meta.json > meta.json
mv meta.json ja_gsd_bert_v2/model-last/
mkdir -p dist
python -m spacy package ja_gsd_bert_v2/model-last/ dist/
mv dist/ja_gsd_bert_v2-*/dist/*.tar.gz .
rm -r dist/
```
