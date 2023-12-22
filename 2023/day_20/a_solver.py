

with open("a_input.txt") as f:
    input_txt = f.read()

mod_types = {}
mod_inputs = {}
mod_outputs = {}
mod_status = {}

for row in input_txt.splitlines():
    module_info, destinations_str = row.split(" -> ")

    # update map of module types and their status
    if module_info == "broadcaster":
        mod_type = mod_id = module_info
    else:
        mod_type, mod_id = module_info[0], module_info[1:]
        # if flip-flop, set initial status to false
        if mod_type == "%":
            mod_status[mod_id] = False
    mod_types[mod_id] = mod_type

    # for each destination module
    for dst_mod_id in destinations_str.split(", "):
        # update list of mod outputs
        if mod_id not in mod_outputs:
            mod_outputs[mod_id] = []
        mod_outputs[mod_id].append(dst_mod_id)

        # update list of destination mod inputs
        if dst_mod_id not in mod_inputs:
            mod_inputs[dst_mod_id] = {}
        mod_inputs[dst_mod_id][mod_id] = False

# remove input statuses for non-conj types
for mod_id, mod_type in mod_types.items():
    if mod_type != "&" and mod_id != "broadcaster":
        del mod_inputs[mod_id]

# add button module
mod_types["button"] = "button"
mod_outputs["button"] = ["broadcaster"]

# init num pulses
num_low = num_high = 0

for idx in range(1, 1000):
    pulses = [("button", "broadcaster", False)]
    while pulses:
        # count pulses
        num_pulses = len(pulses)
        num_high_pulses = len([p for p in pulses if p[2]])
        num_low_pulses = num_pulses - num_high_pulses
        num_low += num_low_pulses
        num_high += num_high_pulses

        # propagate pulses
        new_pulses = []
        for pulse in pulses:
            # calculate new pulse and sed to destinations
            src_mod_id, mod_id, pulse_is_high = pulse

            # if module has no outputs, skip
            if mod_id not in mod_outputs:
                continue

            mod_type = mod_types[mod_id]
            new_pulse_is_high = None

            # if flip-flop
            if mod_type == "%":
                # if pulse is low
                if not pulse_is_high:
                    # update status
                    mod_status[mod_id] = not mod_status[mod_id]
                    new_pulse_is_high = mod_status[mod_id]

            # if module is a conjuction
            elif mod_type == "&":
                # update input status
                mod_inputs[mod_id][src_mod_id] = pulse_is_high

                # get new pulse status
                new_pulse_is_high = True
                if all(mod_inputs[mod_id].values()):
                    new_pulse_is_high = False

            # if module is a broadcaster, keep same pulse
            elif mod_type == "broadcaster":
                new_pulse_is_high = pulse_is_high

            else:
                raise RuntimeError

            # send pulse to all outputs, if any
            if new_pulse_is_high is not None:
                for dst_mod_id in mod_outputs[mod_id]:
                    new_pulses.append((mod_id, dst_mod_id, new_pulse_is_high))

        # update pulses
        pulses = new_pulses


print(num_high * num_low)


if __name__ == "__main__":
    pass