
def loading() -> None:
    print()
    print("REAGENT STATUS: Loading reagents...")
    print()
    print("Checking dependencies:")
    print()
    true_count = 0
    try:
        import pandas
        print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
        true_count += 1
    except ImportError:
        print("Install with pip: pip install pandas")
        print("Install with Poetry: poetry add pandas")
    try:
        import numpy
        print(f"[OK] numpy ({numpy.__version__}) - Numerical "
              "computation ready")
        true_count += 1
    except ImportError:
        print("Install with pip: pip install numpy")
        print("Install with Poetry: poetry add numpy")
    print()
    print("pip vs Poetry:")
    print("  requirements.txt declares what to install;"
          " pip resolves it at install time.")
    print("  pyproject.toml declares the same constraints,"
          " and Poetry pins the resolved")
    print("  versions in poetry.lock so every install is identical.")
    print()
    if true_count == 2:
        print("All reagents present and accounted for.")


loading()
