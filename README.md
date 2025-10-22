# Formal_languages_eliminate_left_recursion

## Introduction
This program implements a systematic algorithm to eliminate left recursion from context-free grammars. Left recursion occurs when a nonterminal A can derive a string that begins with A itself (A ⇒+ Aα). This is problematic for top-down parsers, which can enter infinite loops when encountering left-recursive productions

## Authors

* Isabella Cadavid Posada
* Wendy Vanessa Atehortua Chaverra

## Description
This program eliminates **left recursion** (both direct and indirect) from a context-free grammar, following the algorithm described in **Aho, Sethi & Ullman – _Compilers: Principles, Techniques, and Tools (2nd Edition)_, Section 4.3.3**.

Given a grammar in which:
* Nonterminals are **uppercase letters** (e.g., `S`, `A`, `B`)
* Terminals are **lowercase letters** ( a, b, c)
* `e` denotes the **empty string** (ε)
* There are **no ε-productions** or **cycles** in the input

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

---

## How to Run

### Option 1: Direct execution
```bash
python main.py
Then type or paste the grammar input.
Press Ctrl +D (Linux/macOS) or Ctrl + Z followed by Enter (Windows) to end input.

The program outputs an equivalent grammar **without left recursion**, formatted as described in the assignment specification.


# References: 

1. Aho, A. V., Sethi, R., & Ullman, J. D. (2006). *Compilers: Principles, Techniques, and Tools* (2nd Edition). Addison-Wesley. Section 4.3.3, pp. 212-214.
2. Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D. (2006). *Compilers: Principles, Techniques, and Tools* (2nd Edition, "Dragon Book"). Pearson Education.
