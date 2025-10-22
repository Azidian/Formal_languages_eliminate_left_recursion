import sys
import string

def new_nonterminal_generator():
    for nt in reversed(string.ascii_uppercase):
        yield nt

def get_new_nonterminal(existing_nts):
    while True:
        new_nt = next(new_nt_gen)
        if new_nt not in existing_nts:
            return new_nt

def eliminate_direct_left_recursion(nonterminal, derivations, existing_nts):
    alphas, betas = [], []

    for derivation in derivations:
        if derivation.startswith(nonterminal):
            alpha = derivation[len(nonterminal):].strip()
            if alpha:
                alphas.append(alpha)
        else:
            betas.append(derivation)

    if not alphas:
        return {nonterminal: derivations}, None

    new_nt = get_new_nonterminal(existing_nts.union({nonterminal}))

    new_a_derivations = [f"{b}{new_nt}" for b in betas]
    new_nt_derivations = [f"{a}{new_nt}" for a in alphas] + ["e"]

    return {nonterminal: new_a_derivations}, {new_nt: new_nt_derivations}

def get_nonterminal_from_derivation(derivation):
    if not derivation:
        return None
    ch = derivation[0]
    return ch if 'A' <= ch <= 'Z' else None

def eliminate_left_recursion(grammar, nt_order):
    current_grammar = {nt: list(grammar[nt]) for nt in nt_order}
    existing_nts = set(nt_order)

    for i in range(len(nt_order)):
        Ai = nt_order[i]
        for j in range(i):
            Aj = nt_order[j]
            new_Ai_derivations = []
            for prod in current_grammar[Ai]:
                if prod.startswith(Aj):
                    gamma = prod[len(Aj):].strip()
                    for delta in current_grammar[Aj]:
                        new_Ai_derivations.append((delta + gamma).strip())
                else:
                    new_Ai_derivations.append(prod)
            current_grammar[Ai] = new_Ai_derivations

        Ai_result, new_nt_result = eliminate_direct_left_recursion(Ai, current_grammar[Ai], existing_nts)
        current_grammar.update(Ai_result)
        if new_nt_result:
            new_nt_name = list(new_nt_result.keys())[0]
            existing_nts.add(new_nt_name)
            current_grammar.update(new_nt_result)

    return current_grammar

def format_output(grammar_output):
    lines = []
    nts_to_print = sorted(grammar_output.keys(), key=lambda x: (0 if x == 'S' else 1, x))
    for nt in nts_to_print:
        derivations = ' '.join(grammar_output[nt])
        lines.append(f"{nt} -> {derivations}")
    return '\n'.join(lines)

def parse_input(input_lines):
    n = int(input_lines.pop(0).strip())
    cases = []

    for _ in range(n):
        k = int(input_lines.pop(0).strip())
        grammar = {}
        nt_order = []
        for _ in range(k):
            line = input_lines.pop(0).strip()
            nt, rhs = line.split('->')
            nt = nt.strip()
            nt_order.append(nt)
            derivations = [p.strip() for p in rhs.split(' ') if p.strip()]
            grammar[nt] = derivations
        cases.append((grammar, nt_order))
    return cases

def main():
    print("Introduzca la entrada de la gramática (Ctrl+Z en Windows y Ctrl+D en Linux, para finalizar la cadena del Imput):")
    input_data = sys.stdin.read().splitlines()
    input_lines = [line for line in input_data if line.strip()]
    cases = parse_input(input_lines)

    for i, (grammar, nt_order) in enumerate(cases):
        global new_nt_gen
        new_nt_gen = new_nonterminal_generator()
        result = eliminate_left_recursion(grammar, nt_order)
        print(format_output(result))
        if i < len(cases) - 1:
            print()

if __name__ == "__main__":
    main()