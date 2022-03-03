import os

def main():
    os.system("snyk test --severity-threshold=high")

if __name__ == '__main__':
    raise SystemExit(main())