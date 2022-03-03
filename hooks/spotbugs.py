import os

def main():
    os.system("mvnw spotbugs:check")

if __name__ == '__main__':
    raise SystemExit(main())