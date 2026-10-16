import sys
import os
import site


def construct() -> None:
    print()
    if sys.prefix == sys.base_prefix:
        print("LABORATORY STATUS: You are working in the open")
    else:
        print("LABORATORY STATUS: The laboratory is sealed")
    print()
    print(f"Current Python: {sys.executable}")
    if sys.prefix == sys.base_prefix:
        print("Virtual Environment: None detected")
    else:
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}")
    print()
    if sys.prefix == sys.base_prefix:
        print("WARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.")
        print()
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print(r"lab_env\Scripts\activate # On Windows")
        print()
        print("Then run this program again.")
    else:
        print("SUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting")
        print("the global system.")
        print()
        print("Reagent installation path:")
        print(site.getsitepackages()[0])


construct()
