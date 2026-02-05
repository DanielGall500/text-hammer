from tmallet.obfuscators.base import Obfuscator
from tmallet.surprisal.calc import ShannonBERT
from typing import Dict
from tmallet.utils.sentence_surgery import recursive_match_word, perform_surgery
from nltk.tokenize.treebank import TreebankWordDetokenizer, TreebankWordTokenizer

DEFAULT_MODEL = "bert-base-cased"

"""
def recursive_match_word(
    full_sentence: str,
    word_list: list[str],
    word_list_mask_index: int,
    skippable_tokens: list[str],
) -> int:
"""

class ShannonObfuscator(Obfuscator):
    def __init__(self, device: str = "cpu"):
        self.shannon = ShannonBERT(model_name=DEFAULT_MODEL, device=device)
        self.detok = TreebankWordDetokenizer()

    def obfuscate(self, text: str, config: Dict = { "threshold": 10 }) -> str:
        max_mutual_info = config["threshold"]

        mutual_info = self.shannon.get_text_stats(text)

        final = self.detok.detokenize(
            [w.word for w in mutual_info.word_stats 
             if w.mutual_information < max_mutual_info]
        )
        return final
