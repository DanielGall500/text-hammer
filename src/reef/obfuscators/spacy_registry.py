from typing import Any

import spacy

_models = {}

def get_spacy_nlp(pipeline="ner") -> Any:
    if pipeline not in _models:
        if pipeline == "ner":
            _models[pipeline] = spacy.load("en_core_web_sm", disable=["parser", "tagger"])
        elif pipeline == "full":
            _models[pipeline] = spacy.load("en_core_web_sm")
    return _models[pipeline]
