"""
12/27/2025 - Puzzle 10

structure example:

[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
^ indicator light
        ^ qutton writing schematics
                                        ^ joltage requirements


"""
import ast
from functools import lru_cache

def read_input(file_path = "input.txt"):
    with open(file_path, "r") as file:
        return file.read().splitlines()

def parse_machine_info(line):
    indicator_lights_info, rest_of_line = line.split("]")
    indicator_lights_status = indicator_lights_info[1:]  # Ex: '.##.'
    indicator_lights_goal = indicator_lights_status  # Keep as string, e.g. '.##.'

    button_info, joltage_requirements = rest_of_line.split("{")
    joltage_requirements = joltage_requirements[:-1].split(",")
    joltage_requirements = [int(joltage_requirement) for joltage_requirement in joltage_requirements]

    button_infos = button_info.split(" ")
    button_infos = [button for button in button_infos if button != ""]
    processed_buttons = []
    for button in button_infos:
        parsed = ast.literal_eval(button)
        if isinstance(parsed, int):
            processed_buttons.append((parsed,))
        else:
            processed_buttons.append(tuple(parsed))
    return indicator_lights_goal, processed_buttons, joltage_requirements


def current_state_matches_goal(current_machine_state, indicator_lights_goal):
    # current_machine_state: string, e.g. '.##.'
    # indicator_lights_goal: string, e.g. '.#..'
    return current_machine_state == indicator_lights_goal

def toggle_lights(current_machine_state, button_info):
    # current_machine_state: string of '.' and '#'
    # button_info: tuple/list of indices
    state_as_list = list(current_machine_state)
    for idx in button_info:
        # toggle the bit at idx
        state_as_list[idx] = '#' if state_as_list[idx] == '.' else '.'
    return ''.join(state_as_list)

# Make machine_infos a global variable by defining it at the module level
machine_infos = []

@lru_cache(maxsize=None)
def find_least_button_presses(machine_info_index, current_machine_state = None, current_button_presses = 0):
    # machine_info_index: int
    # current_machine_state: string, e.g. '....'
    # current_button_presses: int
    global machine_infos
    indicator_lights_goal, button_infos_tuple, joltage_requirements = machine_infos[machine_info_index]
    num_lights = len(indicator_lights_goal)
    if current_machine_state is None:
        current_machine_state = '.' * num_lights

    if current_state_matches_goal(current_machine_state, indicator_lights_goal):
        return current_button_presses
    elif current_button_presses > 100:
        return int(1e9)

    least_button_presses = int(1e9)
    for button_info in button_infos_tuple:
        new_machine_state = toggle_lights(current_machine_state, button_info)
        new_button_presses = current_button_presses + 1
        result = find_least_button_presses(
            machine_info_index,
            new_machine_state,
            new_button_presses,
        )
        least_button_presses = min(least_button_presses, result)

    return least_button_presses

def main():
    input_lines = read_input()
    total_least_button_presses = 0
    global machine_infos
    machine_infos = []
    for line in input_lines:
        indicator_lights_goal, button_infos, joltage_requirements = parse_machine_info(line)
        machine_infos.append((indicator_lights_goal, button_infos, joltage_requirements))

    for machine_info_index in range(len(machine_infos)):
        indicator_lights_goal, button_infos_tuple, joltage_requirements = machine_infos[machine_info_index]
        least_button_presses = find_least_button_presses(machine_info_index)
        total_least_button_presses += least_button_presses
        print("for machine info", machine_info_index, "the least number of button presses is", least_button_presses)
    print(total_least_button_presses)



if __name__ == "__main__":
    main()