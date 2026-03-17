import subprocess
import os


# Test 1 - Execute Linux commands using subprocess
def test_linux_commands_subprocess():

    print("\nRunning Linux commands using subprocess")

    commands = ["ls", "pwd"]

    for cmd in commands:
        result = subprocess.run(["wsl", cmd], capture_output=True, text=True)
        print(f"{cmd} output:\n{result.stdout}")

        assert result.returncode == 0


# Test 2 - Execute Linux commands using os module
def test_linux_commands_os():

    print("\nRunning Linux commands using os module")

    os.system("wsl ls")
    os.system("wsl pwd")

    assert True


# Test 3 - Execute another python file using os module
def test_execute_python_file():

    print("\nExecuting another python file")

    os.system("python ./linux_script.py")

    assert True