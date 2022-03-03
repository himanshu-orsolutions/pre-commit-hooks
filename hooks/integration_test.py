import os

def main():
    os.system("mvnw failsafe:integration-test")

if __name__ == '__main__':
    raise SystemExit(main())