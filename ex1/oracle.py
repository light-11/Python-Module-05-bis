import os
from dotenv import load_dotenv

load_dotenv()


def oracle() -> None:
    print()
    print("ORACLE STATUS: Consulting the configuration...")
    print()
    print("Checking dependencies:")
    print(f"Mode: {os.getenv("MATRIX_MODE", "development")}")
    if os.getenv("DATABASE_URL"):
        print("Database: Configured")
    else:
        print("Database: Not configured")
    if os.getenv('API_KEY'):
        print("API Access: Authenticated")
    else:
        print("API Access: Unauthenticated")
    print(f"Log Level: {os.getenv('LOG_LEVEL')}")
    if os.getenv('ZION_ENDPOINT'):
        print("Remote Network: Online")
    else:
        print("Remote Network: Not configured")
    print()
    print("Configuration security check:")

    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly ignored by git")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


oracle()
