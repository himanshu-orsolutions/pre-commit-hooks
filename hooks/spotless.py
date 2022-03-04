import subprocess

def main():
    result = subprocess.run('mvnw spotless:check', capture_output=True, shell=True)

    if result.returncode == 0:
        print(result.stdout)
        return 0
    else:
        print(result.stderr)
        return 1

if __name__ == '__main__':
    raise SystemExit(main())