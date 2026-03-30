import paramiko
import pexpect
import subprocess
import argparse
from concurrent.futures import ThreadPoolExecutor


HOST = "test.rebex.net"
USERNAME = "demo"
PASSWORD = "password"

def ssh_paramiko(command):

    print("\nRunning using Paramiko:", command)

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(HOST, username=USERNAME, password=PASSWORD)

    stdin, stdout, stderr = client.exec_command(command)

    output = stdout.read().decode()
    print(output)

    client.close()

    return output


# Pexpect SSH login

def ssh_pexpect():

    print("\nRunning SSH using Pexpect")

    child = pexpect.spawn(f"wsl ssh {USERNAME}@{HOST}")

    child.expect("password:")
    child.sendline(PASSWORD)

    child.expect("$")
    child.sendline("ls")

    child.expect("$")

    output = child.before.decode()
    print(output)

    child.close()

    return output


# Local commands using subprocess

def run_local(command):

    print("\nRunning Local Command:", command)

    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    print(result.stdout)

    return result.stdout


# Multithreading using concurrent.futures

def run_threads(command):

    print("\nRunning commands with 10 threads")

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(run_local, command) for i in range(10)]

        for f in futures:
            f.result()


# ---------------------------------
# PyTest Test Cases
# ---------------------------------

def test_subprocess_commands():

    output = run_local("ls")

    assert output is not None


def test_thread_execution():

    run_threads("ls")

    assert True


def test_paramiko_ssh():

    output = ssh_paramiko("ls")

    assert output is not None


def test_pexpect_ssh():

    output = ssh_pexpect()

    assert output is not None