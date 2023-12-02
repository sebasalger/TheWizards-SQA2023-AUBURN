#simple1 change
import os
import random
import json
import graphtaint

# Get the current script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load naughty strings from the JSON file
def load_naughty_strings():
    json_file_path = os.path.join(script_dir, "blns.json")
    with open(json_file_path, "r", encoding="utf-8") as json_file:
        naughty_strings = json.load(json_file)
    return naughty_strings

def fuzz_method_1(input_val, output_file):
    """
    Fuzzing method 1: get_yaml_files
    """
    output_file.write("Fuzzing get_yaml_files\n")
    try:
        result = graphtaint.get_yaml_files(input_val)
        return result
    except Exception as error:
        output_file.write(f"Input: {input_val} --> Error: {error}\n")
    output_file.write("\n")

def fuzz_method_2(input_val, output_file):
    """
    Fuzzing method 2: get_valid_taints
    """
    output_file.write("Fuzzing get_valid_taints\n")
    try:
        result = graphtaint.get_valid_taints(input_val)
        return result
    except Exception as error:
        output_file.write(f"Input: {input_val} --> Error: {error}\n")
    output_file.write("\n")

def fuzz_method_3(val1, val2, val3, output_file):
    """
    Fuzzing method 3: mine_secret_graph
    """
    output_file.write("Fuzzing mine_secret_graph\n")
    try:
        result = graphtaint.mine_secret_graph(val1, val2, val3)
        return result
    except Exception as error:
        output_file.write(
            f"Input: {val1}, {val2}, {val3} --> Error: {error}\n"
        )
    output_file.write("\n")

def fuzz_method_4(val1, val2, output_file):
    """
    Fuzzing method 4: get_matching_templates
    """
    output_file.write("Fuzzing get_matching_templates\n")
    try:
        result = graphtaint.get_matching_templates(val1, val2)
        return result
    except Exception as error:
        output_file.write(
            f"Input: {val1}, {val2} --> Error: {error}\n"
        )
    output_file.write("\n")

def fuzz_method_5(input_val, output_file):
    """
    Fuzzing method 5: get_sh_files
    """
    output_file.write("Fuzzing get_sh_files\n")
    try:
        result = graphtaint.get_sh_files(input_val)
        return result
    except Exception as error:
        output_file.write(f"Input: {input_val} --> Error: {error}\n")
    output_file.write("\n")

def fuzzer():
    naughty_strings = load_naughty_strings()

    with open("fuzzed_errors.txt", "w", encoding="utf-8") as output_file:
        for i in range(len(naughty_strings)):
            fuzz_method_1(naughty_strings[i], output_file)
            fuzz_method_2(naughty_strings[i], output_file)
            fuzz_method_3(naughty_strings[i], naughty_strings[i], naughty_strings[i], output_file)
            fuzz_method_4(naughty_strings[i], naughty_strings[i], output_file)
            fuzz_method_5(naughty_strings[i], output_file)

if __name__ == "__main__":
    fuzzer()
