import pytest
import subprocess
import sys
import importlib

from brain import Brain
from guard import LogicGuard
from distiller import Distiller
import main

def test_brain_generate_fix():
    brain = Brain()
    result = brain.generate_fix("context", "instruction")
    assert "code" in result
    assert "pre_conditions" in result
    assert "post_conditions" in result
    assert result["code"] == "def example_fix(x):\n    return x + 1"

def test_guard_verify_logic():
    guard = LogicGuard()
    result = guard.verify_logic("code", ["pre"], ["post"])
    assert result is True

def test_distiller_distill_context():
    distiller = Distiller()
    result = distiller.distill_context("query", "file_path")
    assert "file_path" in result
    assert "query" in result

def test_main(capsys):
    main.main()
    captured = capsys.readouterr()
    assert "[SUCCESS] Code mathematically verified. Ready for deployment." in captured.out

def test_main_failure(capsys, monkeypatch):
    monkeypatch.setattr(LogicGuard, "verify_logic", lambda *args, **kwargs: False)
    main.main()
    captured = capsys.readouterr()
    assert "[FAILURE] Guard rejected the AI's code due to logic constraints." in captured.out

def test_main_script():
    # Use the correct path based on project structure. The script is run from project root.
    result = subprocess.run([sys.executable, "src/main.py"], capture_output=True, text=True)
    assert "[SUCCESS] Code mathematically verified. Ready for deployment." in result.stdout

def test_main_name_main(monkeypatch):
    # runpy.run_module or similar executes the code in a new namespace.
    # Mocking main.main won't work that way.
    # Instead, we can just execute the script using run_path and provide a mocked globals dict
    # or just use the simplest approach: import the module and manually run the block.
    # But to get coverage on `if __name__ == "__main__":` we can use runpy.run_path

    import runpy
    import os

    # We want to run src/main.py but mock the main() function so it doesn't do all the work again,
    # though it doesn't really matter since it's just printing.
    # Actually, we can just run it using runpy and let it execute. The subprocess test already tests
    # the script execution, but runpy ensures coverage tool sees it.

    # We can use runpy.run_path to execute the file as __main__ within the current process
    # so coverage can track it.
    runpy.run_path("src/main.py", run_name="__main__")
