import os
import sys
import subprocess

def run_tests():
    subprocess.run(["behave", "features"])

if __name__ == "__main__":
    run_tests()
