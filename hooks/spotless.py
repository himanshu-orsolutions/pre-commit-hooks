import os

def main():
    os.system("mvnw spotless:check")

if __name__ == '__main__':
    raise SystemExit(main())