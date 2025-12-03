import subprocess
import sys
import os


def test_sample_run():
    # run the main script with sample email and check exit code 0
    script = os.path.join(os.path.dirname(__file__), "..", "main.py")
    cmd = [sys.executable, script, "--file", "samples/email1.txt"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    assert res.returncode == 0
    assert "SUMMARY" in res.stdout
