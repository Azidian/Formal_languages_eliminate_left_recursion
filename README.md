# Formal_languages_eliminate_left_recursion

## Introduction
This program implements a systematic algorithm to eliminate left recursion from context-free grammars. Left recursion occurs when a nonterminal A can derive a string that begins with A itself (A ⇒+ Aα). This is problematic for top-down parsers, which can enter infinite loops when encountering left-recursive productions

## Authors

* Isabella Cadavid Posada
* Wendy Vanessa Atehortua Chaverra

## Class Number

Lenguajes Formales - C2566-SI2002-5

# Software and Environment
- Operating System: Windows 11
- Programming Language: Python 3.11+ 
- Tools: Standard Python library (only sys and string modules)

## Description
This program eliminates **left recursion** (both direct and indirect) from a context-free grammar, following the algorithm described in **Aho, Sethi & Ullman – _Compilers: Principles, Techniques, and Tools (2nd Edition)_, Section 4.3.3**.

Given a grammar in which:
* Nonterminals are **uppercase letters** (e.g., `S`, `A`, `B`)
* Terminals are **lowercase letters** ( a, b, c)
* `e` denotes the **empty string** (ε)
* There are **no ε-productions** or **cycles** in the input

# Algorithm Explanation
The program implements the algorithm from Aho et al. (2006) 11 in two main phases:

1. Elimination of Indirect Left RecursionThe algorithm first processes the nonterminals in a fixed order (the order they appear in the input), A_1, A_2, ..., A_n. It iterates through each nonterminal A_i and ensures that all its productions only refer to nonterminals A_k where k >= i.

for i from 1 to n:
  for j from 1 to i-1:
    // Replace productions of the form Ai -> Aj γ
    // with Ai -> δ1 γ | δ2 γ | ...
    // where Aj -> δ1 | δ2 | ... are all current productions for Aj

This is handled in the main eliminate_left_recursion function. After this double loop, any remaining left recursion for A_i must be direct.

2. Elimination of Direct Left Recursion
   After the first phase, the productions for A_i are processed to remove direct left recursion. The productions for A_i are grouped into two forms:

   - Recursive: A_i -> A_iα1 | A_iα1  | ...
   - Non-recursive: A_i -> β_1 | β_2 | ...

     These productions are replaced by introducing a new nonterminal (e.g., $Z$, $Y$, etc., per the assignment requirement 12):
     A_i -> β_1Z | β_2Z | ...
     Z -> α1Z | α2Z | ... | e

     This transformation is handled by the eliminate_direct_left_recursion function, which creates the new nonterminal and its corresponding rules. The empty string e is always included for the new nonterminal to terminate the recursion.

## Input Format
The input must be given via **standard input (stdin)**.
Like the next one:

n
k
A -> α1 α2 ...
B -> β1 β2 ...

Where:
* `n` = number of test cases  
* `k` = number of nonterminals in the current grammar  
* Each production rule is written in one line, alternatives separated by spaces.  

Example:

1
1
S -> Sa b

---
## Output Format
The output grammar (for each test case) is printed to **standard output (stdout)** with the same format:

S -> bZ
Z -> aZ e

Each test case is separated by a blank line.

## How to Run

1. Run the script:
Bash
python main.py

2. The program will wait for input. Type or paste the grammar input directly into the terminal.
3. Press Ctrl+D (Linux/macOS) or Ctrl+Z followed by Enter (Windows) to signal the end of the input.

# References: 

1. Aho, A. V., Sethi, R., & Ullman, J. D. (2006). *Compilers: Principles, Techniques, and Tools* (2nd Edition). Addison-Wesley. Section 4.3.3, pp. 212-214.
2. Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D. (2006). *Compilers: Principles, Techniques, and Tools* (2nd Edition, "Dragon Book"). Pearson Education.
