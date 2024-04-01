from logic import *

'''
In a ”Knights and Knaves” puzzle, the following information is given: 
Each character is either a knight or a knave.
A knight will always tell the truth: if knight states a sentence, then that sentence is true.
Conversely, a knave will always lie: if a knave states a sentence, then that sentence is false.
The objective of the puzzle is, given a set of sentences spoken by each of the characters,
determine, for each character, whether that character is a knight or a knave.
For example, consider a simple puzzle with just a single character named A.
A says "I am both a knight and a knave". We can conclude that A is lying and that he is a knave.
With more characters and more sentences, the puzzles can get trickier!
Your task in this problem is to determine how to represent these puzzles using 
propositional logic, such that an AI running a model-checking algorithm could solve 
these puzzles for us.
'''

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight,AKnave),
    Not(And(AKnight,AKnave)),
    Implication(AKnight,And(AKnight,AKnave)),
    Implication(AKnave,Not(And(AKnight,AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO
    Or(AKnight,AKnave),
    Not(And(AKnight,AKnave)),
    Or(BKnight,BKnave),
    Not(And(BKnight,BKnave)),
    # A's statement can be done using two options:
    # Option 1
    Implication(AKnight,And(AKnight,AKnave)),
    Implication(BKnight,Not(And(BKnight,BKnave))),
    # Option 2
    Biconditional(AKnight,And(AKnave,BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # A's statement
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # B's statement
    Biconditional(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
)


# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),
    # A's statement
    Biconditional(AKnight, Or(AKnight, AKnave)),
    # B's statements
    Implication(BKnight, AKnave),
    Implication(BKnight, CKnave),
    # C's statement
    Implication(CKnight, AKnight),
)

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("   Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge,symbol):
                    print(symbol)


if __name__ == "__main__":
    main()
