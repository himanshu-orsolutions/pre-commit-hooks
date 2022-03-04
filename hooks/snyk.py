from subprocess import check_output, CalledProcessError, STDOUT
import sys

def execute_command(command):
    try:
        check_output(command, stderr=STDOUT, shell=True)
        success = True 
    except CalledProcessError as e:
        success = False
    return success

def main():
    success = execute_command('snyk test --severity-threshold=high')
    return 0 if success else 1

if __name__ == '__main__':
    sys.exit(main())