import spacy

from obfuscators.base import Obfuscator
from obfuscators.spacy_registry import get_spacy_nlp

class ReplaceObfuscator(Obfuscator):
    @property
    def spacy_nlp(self):
        if not hasattr(self, "_nlp"):
            self._spacy_nlp = get_spacy_nlp("ner")
        return self._spacy_nlp

    def obfuscate(self, text: str) -> str:
        return self._to_nouns(text)

    def _to_nouns(self, text: str) -> str:
        doc = self.spacy_nlp(text)
        nouns = []
        for token in doc:
            is_noun = token.pos_ == 'NOUN' or token.pos_ == 'PROPN'
            if is_noun:
                nouns.append(token.text)
        return " ".join(nouns)
