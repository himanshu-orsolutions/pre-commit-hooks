import os

def main():
    res = os.system("snyk test --severity-threshold=high")
    return 0 if res == 0 else 1

if __name__ == '__main__':
    raise SystemExit(main())