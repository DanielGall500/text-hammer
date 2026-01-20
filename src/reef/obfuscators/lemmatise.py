from reef.obfuscators.base import Obfuscator
from spacy.tokens import Doc


class LemmaObfuscator(Obfuscator):
    def obfuscate(self, doc: Doc) -> str:
        return self._lemmatise(doc)

    def _lemmatise(self, doc: Doc) -> str:
        lemmatised_text = "".join([token.lemma_ + token.whitespace_ for token in doc])
        return lemmatised_text
