

with open("a_input.txt") as f:
    input_txt = f.read()


instructions_str, products_str = input_txt.split("\n\n")

products = []
for product_str in products_str.splitlines():
    p_splits = product_str.strip("{}").strip("}").split(",")
    product = {e.split("=")[0]: int(e.split("=")[1]) for e in p_splits}
    products.append(product)

instructions_dict = {}
for instruction_str in instructions_str.splitlines():
    instr_id, instruction_str = instruction_str.split("{")
    instructions = instruction_str.strip("}").split(",")
    instructions_dict[instr_id] = instructions


accepted = []
score = 0
for p in products:
    x, m, a, s = p["x"], p["m"], p["a"], p["s"]
    tmp_score = x + m + a + s
    instr_id = "in"
    returned = False

    while instr_id not in ("A", "R"):
        for instruction in instructions_dict[instr_id]:
            cond = False
            if ":" in instruction:
                cond_str, dst_id = instruction.split(":")
                exec(f"cond = {cond_str}")
                if cond:
                    instr_id = dst_id
                    break
            else:
                instr_id = instruction
                break

    if instr_id == "A":
        accepted.append(p)
        score += tmp_score

print(score)


if __name__ == "__main__":
    pass