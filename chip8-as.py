import sys
from typing import BinaryIO

def main(source: str, target: str) -> None:
    source = open(source, "r").read().splitlines()
    source = remove_comments(source)
    
    target = open(target, "wb")
    parse(source, target)
    

def remove_comments(source: list[str]) -> list[str]:
    return [line[:line.find(';')] for line in source]


def parse(source: list[str], target: BinaryIO):
    for line in source:
        if not line:
            continue
        print(line.lower().split())
        match line.lower().split():
            case ["clearscreen"]:
                target.write(bytes.fromhex("00E0"))
            case ["return"]:
                target.write(bytes.fromhex("00EE"))
            case ["jump", address]:
                target.write(bytes.fromhex('1' + address))
            case ["call", address]:
                target.write(bytes.fromhex('2' + address))
            case ["jmpeq", 'v', vx, nn]:
                target.write(bytes.fromhex('3' + vx + nn))
            case ["jmpneq", 'v', vx, nn]:
                target.write(bytes.fromhex('4' + vx + nn))
            case ["jmpeq", 'v', vx, 'v', vy]:
                target.write(bytes.fromhex('5' + vx + vy + '0'))
            case ["set", 'v', vx, nn]:
                print('6' + vx + nn)
                target.write(bytes.fromhex('6' + vx + nn))
            case ["add", 'v', vx. nn]:
                target.write(bytes.fromhex('7' + vx + nn))
            case ["set", 'v', vx, 'v', vy]:
                target.write(bytes.fromhex('8' + vx + vy + '0'))
            case ["|=", 'v', vx, 'v', vy]:
                target.write(bytes.fromhex('8' + vx + vy + '1'))
            case ["&=", 'v', vx, 'v', vy]:
                target.write(bytes.fromhex('8' + vx + vy + '2'))
            case ["^=", 'v', vx, 'v', vy]:
                target.write(bytes.fromhex('8' + vx + vy + '3'))
            case ["+=", 'v', vx, 'v', vy]:
                target.write(bytes.fromhex('8' + vx + vy + '4'))
            case ["-=", 'v', vx, 'v', vy]:
                target.write(bytes.fromhex('8' + vx + vy + '5'))
            case ["rshift", 'v', vx, 'v', vy]:
                target.write(bytes.fromhex('8' + vx + vy + '6'))
            case ["-=", 'v', vx, 'v', vy]:
                target.write(bytes.fromhex('8' + vx + vy + '7'))
            case ["lshift", 'v', vx, 'v', vy]:
                target.write(bytes.fromhex('8' + vx + vy + 'E'))
            case ["jmpneq", 'v', vx, 'v', vy]:
                target.write(bytes.fromhex('9' + vx + vy + '0'))
            case ['seti', nnn]:
                target.write(bytes.fromhex('A' + nnn))
            case ['jmpoffset', nnn]:
                target.write(bytes.fromhex('B' + nnn))
            case ['random', 'v', vx, nn]:
                target.write(bytes.fromhex('C' + vx + nn))
            case ['display', 'v', vx, 'v', vy, n]:
                target.write(bytes.fromhex('D' + vx + vy + n))
            case ['jmpifpressed', 'v', vx]:
                target.write(bytes.fromhex('E' + vx + "9E"))
            case ['jmpnotpressed', 'v', vx]:
                target.write(bytes.fromhex('E' + vx + "A1"))
            case ['getdelay', 'v', vx]:
                target.write(bytes.fromhex('F' + vx + "07"))
            case ['setdelay', 'v', vx]:
                target.write(bytes.fromhex('F' + vx + "15"))
            case ['setsoundtimer', 'v', vx]:
                target.write(bytes.fromhex('F' + vx + "18"))
            case ['incrementpc', 'v', vx]:
                target.write(bytes.fromhex('F' + vx + "1E"))
            case ["waitinput"]:
                target.write(bytes.fromhex('F00A'))
            case ["seti", 'v', vx]:
                target.write(bytes.fromhex('F' + vx + "29"))
            case ["splitreg", 'v', vx]:
                target.write(bytes.fromhex('F' + vx + "33"))
            case ["store", x]:
                target.write(bytes.fromhex('F' + x + "55"))
            case ["load", x]:
                target.write(bytes.fromhex('F' + x + "65"))


if __name__ == "__main__":
    # TODO: match block

    if len(sys.argv) == 2:
        if sys.argv[1] == "--help":
            print("TODO")
        else:
            sys.exit(f"Unknown argument {sys.argv[1]}, see --help")

    if len(sys.argv) != 3:
        sys.exit("wrong usage provided. see --help")

    # TODO: more error handling
    main(sys.argv[1], sys.argv[2])
