from distiller import Distiller
from brain import Brain
from guard import LogicGuard
import os

def main():
    print("--- Sentinel Orchestrator Started ---")

    # Initialize components
    distiller = Distiller()
    brain = Brain()
    guard = LogicGuard()

    # Simulated input
    target_file = "example.py"
    issue_query = "Fix off-by-one error in loop"

    # Create dummy file for demonstration
    if not os.path.exists(target_file):
        with open(target_file, "w") as f:
            f.write("def do_something():\n    pass")

    print(f"\nStep 1: Reading File -> {target_file}")

    print("\nStep 2: Distilling Context")
    context = distiller.distill_context(issue_query, target_file)

    print("\nStep 3: Generating Fix")
    fix_data = brain.generate_fix(context, issue_query)

    print("\nStep 4: Verifying Logic")
    is_valid = guard.verify_logic(
        code=fix_data["code"],
        pre_conditions=fix_data["pre_conditions"],
        post_conditions=fix_data["post_conditions"]
    )

    if is_valid:
        print("\n[SUCCESS] Code mathematically verified. Ready for deployment.")
        print(f"Proposed Code:\n{fix_data['code']}")
    else:
        print("\n[FAILURE] Guard rejected the AI's code due to logic constraints.")

    # Cleanup dummy file
    if os.path.exists(target_file):
        os.remove(target_file)

if __name__ == "__main__":
    main()
