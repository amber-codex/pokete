import subprocess

def test_ruff_formats_intent_correctly(tmp_path):
    bad_code_intent = "def indent():\n                              print('Hello World!')\n"
    expected_fixed_intent = 'def indent():\n    print("Hello World!")\n'

    test_file_intent = tmp_path / "bad_format_intent.py" # tmp_path in pytest makes a temporary path, that pytest cleans afterwards
    test_file_intent.write_text(bad_code_intent)

    # Running Ruff as it would be done in the terminal:
    result_intent = subprocess.run(
        ["python", "-m","ruff", "format", str(test_file_intent), "--config=ruff.toml"],
        capture_output=True,
        text=True
    )

    assert result_intent.returncode in (0, 1) # checking ruff is running well when it returns 0 it exits the program successfully
    # and in the cases it returned 1 it often cause by formatting errors ruff could not fix. 
    
    formatted = test_file_intent.read_text()
    assert formatted == expected_fixed_intent # testing implemented indexing and that is correctly formatted

def test_ruff_formats_line_length_correctly(tmp_path):
    bad_code_string = "def line_length():\n    print('0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100')\n"

    expected_fixed_string = (
    "def line_length():\n"
    "    print(\n"
    '        "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100"\n'
    "    )\n" # edge case of allowing long lines to surpass the line limit 
)

    test_file_string = tmp_path / "bad_format_string.py" # tmp_path in pytest makes a temporary path, that pytest cleans afterwards
    test_file_string.write_text(bad_code_string)

    # Running Ruff as it would be done in terminal
    result_string = subprocess.run(
        ["python", "-m","ruff", "format", str(test_file_string), "--config=ruff.toml"],
        capture_output=True,
        text=True
    )

    assert result_string.returncode in (0, 1) # checking ruff is running well when it returns 0 it exits the program successfully
    # and in the cases it returned 1 it often cause by formatting errors ruff could not fix. 
    
    formatted = test_file_string.read_text()
    assert formatted == expected_fixed_string # testing implemented if a string is seperated or not (result is not)
    
    bad_code_num = (
    "my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, "
    "13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]\n"
)

    expected_fixed_num = '''my_list = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
]\n'''
    test_file_num = tmp_path / "bad_format_num.py" # tmp_path in pytest makes a temporary path, that pytest cleans afterwards
    test_file_num.write_text(bad_code_num)
    
    result_num = subprocess.run(
        ["python", "-m","ruff", "format", str(test_file_num), "--config=ruff.toml"],
        capture_output=True,
        text=True
    )

    assert result_num.returncode in (0, 1) # checking ruff is running well when it returns 0 it exits the program successfully
    # and in the cases it returned 1 it often cause by formatting errors ruff could not fix. 
    
    formatted = test_file_num.read_text()
    assert formatted == expected_fixed_num # testing implemented line length limitations 
