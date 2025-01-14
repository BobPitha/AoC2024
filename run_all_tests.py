import unittest

def main():
    # Discover and run all tests in AoC2024 subdirectories
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="AoC2024", pattern="*_test.py")
    
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    main()
