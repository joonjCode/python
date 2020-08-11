import sys
import argparse
from typing import Optional
from typing import Sequence

def main(argv: Optional[Sequence[str]] =None)-> int:
    # print(f'Hello {sys.argv[-1]}')
    parser = argparse.ArgumentParser()
    parser.add_argument('person')
    args = parser.parse_args(argv)

    if args.person == '':
        print("Persons's name must not be empty", file= sys.stderr)
        return 1

    print(f'Hello {args.person}')
    return 0
    

if __name__ =='__main__':
    exit(main())
    # raise SystemExit(main())