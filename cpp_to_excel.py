import pandas as pd
import subprocess

excel_file = "data.xlsx"
# Put your path for tp here
relative_tp_path = "../logic-expressions/bin/"

# Change if is not tp1.out
executable_name = "tp1.out"

df = pd.read_excel(excel_file)

failed_tests_count = 0


def execute_cpp(row):
    global failed_tests_count
    cpp_executable = relative_tp_path + executable_name

    row_values = [str(value) for value in row]

    expression = row_values[0]
    expression_values = row_values[1]
    expected_result = row_values[2]

    cmd = [cpp_executable, "-s", expression, expression_values]
    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text="True"
    )
    stdout, stderr = process.communicate()

    if stdout.strip() == expected_result.strip():
        row[3] = "pass"
    else:
        row[3] = "failed"
        print(
            'Test "%s" %s failed, expect result was %s and your output is %s'
            % (expression, expression_values, expected_result, stdout.strip())
        )
        failed_tests_count += 1

    row[4] = stdout.strip()

    # Check for any errors
    if process.returncode != 0:
        print("C++ Program Error:")
        print(stderr)


for index, row in df.iterrows():
    execute_cpp(row)

print("Number of failed tests", failed_tests_count)
df.to_excel(excel_file, index=False)
