from obfuscators.base import Obfuscator
from obfuscators.spacy_registry import get_spacy_nlp


class LemmaObfuscator(Obfuscator):
    @property
    def spacy_nlp(self):
        if not hasattr(self, "_nlp"):
            self._spacy_nlp = get_spacy_nlp("full")
        return self._spacy_nlp

    def obfuscate(self, text: str) -> str:
        return self._lemmatise(text)

    def _lemmatise(self, text: str) -> str:
        nlp = self.spacy_nlp
        doc = nlp(text)
        lemmatised_text = "".join([token.lemma_ + token.whitespace_ for token in doc])
        return lemmatised_text
