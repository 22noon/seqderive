# Architecture

Version 1 core pipeline:

    Sequences
        |
        v
    Tokenizer
        |
        v
    Differences + Context
        |
        v
    Initial Derivation
        |
        v
    Rewrite Rules
        |
        v
    Derivation Forest
        |
        v
    Scoring
        |
        v
    Ranked Derivations

The domain model is deliberately independent of tokenizers and
reasoning algorithms.
