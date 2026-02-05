from tmallet.obfuscators.base import SpaCyObfuscator
from spacy.tokens import Doc


class LemmaObfuscator(SpaCyObfuscator):
    def obfuscate(self, doc: Doc) -> str:
        return self._lemmatise(doc)

    def _lemmatise(self, doc: Doc) -> str:
        lemmatised_text = "".join([token.lemma_ + token.whitespace_ for token in doc])
        return lemmatised_text
