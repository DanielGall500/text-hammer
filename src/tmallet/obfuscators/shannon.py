from tmallet.obfuscators.base import Obfuscator
from tmallet.shannon.calc import ShannonBERT
from typing import Dict
from nltk.tokenize.treebank import TreebankWordDetokenizer

DEFAULT_MODEL = "bert-base-cased"

DEFAULT_CONFIG = {"threshold": 10, "replace_with": "_"}


class ShannonObfuscator(Obfuscator):
    """
    Removes tokens depending on their Mutual Information, as assigned
    by an NLU model from Hugging Face e.g. bert-base-cased.

    Recommended to run this using at least a GPU.
    """

    def __init__(self, device: str = "cpu"):
        self.shannon = ShannonBERT(model_name=DEFAULT_MODEL, device=device)
        self.detok = TreebankWordDetokenizer()

    def obfuscate(self, text: str, config: Dict = DEFAULT_CONFIG) -> str:
        max_mutual_info = config["threshold"]
        obfuscatory_token = config["replace_with"]

        shannon_stats_text = self.shannon.get_text_stats(text)
        words = shannon_stats_text.get_words()
        surviving_words = [
            w.word if (w.mutual_information < max_mutual_info) else obfuscatory_token
            for w in words
        ]

        reconstructed = self.detok.detokenize(surviving_words)
        return reconstructed
