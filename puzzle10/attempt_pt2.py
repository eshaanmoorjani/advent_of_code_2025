"""
12/27/2025 - Puzzle 10

structure example:

[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
^ indicator light
        ^ button writing schematics
                                        ^ joltage requirements


"""
import ast
from functools import lru_cache
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, value

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


def find_least_button_presses_joltage(machine_info_index):
    # machine_info_index: int
    # current_machine_state: string, e.g. '....'
    # current_button_presses: int
    global machine_infos
    indicator_lights_goal, button_infos_tuple, joltage_requirements = machine_infos[machine_info_index]
    num_lights = len(indicator_lights_goal)

    # linear programming to solve this
    problem = LpProblem("Least Button Presses", LpMinimize)
    button_constraints = []
    button_vectors = []
    for index, button_info in enumerate(button_infos_tuple):
        button_constraint = LpVariable(f"button_presses_for_button_{index}", lowBound=0, cat='Integer')
        button_constraints.append(button_constraint)

        button_vector = [0] * num_lights
        for j in button_info:
            button_vector[j] = 1
        button_vectors.append(button_vector)

    problem += lpSum(button_constraints), "Total Button Presses"

    for i in range(num_lights):
        problem += (
            lpSum(
                button_constraints[j] * button_vectors[j][i]
                for j in range(len(button_vectors))
            )
            == joltage_requirements[i]
        )



    problem.solve()
    print(problem)
    print(value(problem.objective))
    return value(problem.objective)



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
        least_button_presses = find_least_button_presses_joltage(machine_info_index)
        total_least_button_presses += least_button_presses
        print("for machine info", machine_info_index, "the least number of button presses is", least_button_presses)
    print(total_least_button_presses)



if __name__ == "__main__":
    main()