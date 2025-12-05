# Knowledge-Based Agents

A Python implementation of AI agents that solve logic puzzles using propositional logic and model checking. This project demonstrates how to represent and solve "Knights and Knaves" puzzles through knowledge-based reasoning.

## Overview

This project implements a knowledge-based agent capable of solving logic puzzles where characters are either knights (who always tell the truth) or knaves (who always lie). The agent uses propositional logic to represent puzzle constraints and employs model checking to determine the nature of each character.

## Features

- **Propositional Logic Engine**: Complete implementation of logical sentences including:
  - Symbols
  - Logical operators: NOT, AND, OR
  - Implication and Biconditional operators
  - Model checking algorithm
  
- **Puzzle Solver**: Solves "Knights and Knaves" puzzles by:
  - Encoding puzzle constraints as propositional logic
  - Using model checking to determine which characters are knights/knaves
  - Supporting multiple puzzle scenarios with varying complexity

## Files

- `logic.py`: Core propositional logic library implementing:
  - `Sentence` base class for logical sentences
  - Logical operators (`Symbol`, `Not`, `And`, `Or`, `Implication`, `Biconditional`)
  - `model_check()` function for determining logical entailment
  
- `puzzle.py`: Knights and Knaves puzzle implementations:
  - Puzzle 0: Single character claiming to be both knight and knave
  - Puzzle 1: Two characters with conflicting statements
  - Puzzle 2: Characters making statements about similarity
  - Puzzle 3: Complex puzzle with three characters and multiple statements

## How It Works

### Knights and Knaves Rules

- Each character is either a knight or a knave
- A knight always tells the truth
- A knave always lies
- Given statements made by characters, determine who is a knight and who is a knave

### Model Checking

The `model_check(knowledge, query)` function determines if a knowledge base entails a query by:

1. Extracting all symbols from the knowledge base and query
2. Generating all possible truth assignments for these symbols
3. Checking if the query is true in every model where the knowledge base is true

## Usage

Run the puzzle solver:

```bash
python puzzle.py
```

This will output the solution for each puzzle, identifying which characters are knights and which are knaves.

## Example

**Puzzle 0**: A says "I am both a knight and a knave."

Since no one can be both a knight and a knave simultaneously, A must be lying. Therefore, A is a knave.

**Knowledge Representation**:

```python
knowledge0 = And(
    Or(AKnight, AKnave),           # A is either a knight or knave
    Not(And(AKnight, AKnave)),     # A cannot be both
    Implication(AKnight, And(AKnight, AKnave)),  # If A is knight, statement is true
    Implication(AKnave, Not(And(AKnight, AKnave)))  # If A is knave, statement is false
)
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

An Artificial Intelligence (CS485) lab based on the "Knights & Knaves" logic puzzle in fall 2023.
