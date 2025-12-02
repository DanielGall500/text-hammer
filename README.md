# REconstructability of Expressions Framework (REEF)

Tools for the conversion of text into a Derived Text Format. This prevents reconstructability of the original text.

When we think about how strings can be altered for obfuscation, we can look at the following aspects:
* Word Forms (the character sequence)
* Root Forms (lemmas)
* Syntactic and Morpho-Syntactic Features
* Meanings
* Grammatical Relations (hierarchical structure)
* Sequence Information (linear structure)

Each of the above categories contributes a certain amount of *information* to an expression. Languages vary significantly in which they most rely on for certain features, for instance English relies heavily on structure for assigning grammatical case while German relies more on morphological adjustments with relatively free word order.

The goal of REEF is to give you the ability to obfuscate these various aspects in order to convert the text to a format that is difficult to reconstruct and hence more suitable for privacy and copyright protection.
