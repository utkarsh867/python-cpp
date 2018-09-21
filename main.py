import sys
import os
import subprocess
import json

def main():
    subprocess.call("g++ helloworld.cpp -o helloworld")
    x = input()
    y = input()
    z = input()
    str = x + " " + y + " " + z
    p = subprocess.run(["helloworld"], input=str.encode("utf-8"), capture_output = True)
    j = p.stdout.decode("utf-8")
    result = json.loads(j)
    print(result["key1"])

if __name__ == '__main__':
    main()
