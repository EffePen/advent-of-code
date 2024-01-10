
def parse_input():
    with open("input.txt") as f:
        input_txt = f.read()

    wires = dict()
    for instr_txt in input_txt.splitlines():
        gate_info, output_wire_name = instr_txt.split(" -> ")
        wires[output_wire_name] = gate_info

    wire_names = list(wires.keys())
    for wire_name in wire_names:
        gate_info = wires[wire_name]
        try:
            wire_value = int(gate_info)
            gate_inputs = []
        except ValueError:
            wire_value = None
            gate_inputs = [wn for wn in wire_names if wn in gate_info.split()]
        wires[wire_name] = (gate_inputs, gate_info, wire_value)

    return wires


print("Part 1:", wire_a_value)


if __name__ == "__main__":
    pass
