from obfuscators.base import Obfuscator
from obfuscators.spacy_registry import get_spacy_nlp
import random


class ScrambleObfuscator(Obfuscator):
    @property
    def spacy_nlp(self):
        if not hasattr(self, "_nlp"):
            self._spacy_nlp = get_spacy_nlp("full")
        return self._spacy_nlp

    def obfuscate(self, text: str, algorithm: str = "linear", seed: int = 100) -> str:
        if algorithm == "linear":
            return self._linear_scramble(text, seed)
        elif algorithm == "hierarchical":
            return self._hierarchical_scramble(text, seed)
        else:
            raise ValueError("Invalid scramble algorithm.")

    def _linear_scramble(self, text: str, seed: int) -> str:
        words = text.split()
        random.Random(seed).shuffle(words)
        scrambled_words = " ".join(words)
        return scrambled_words

    def _hierarchical_scramble(self, text: str, seed: int) -> str:
        return ""

