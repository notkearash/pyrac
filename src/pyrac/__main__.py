#!/usr/bin/env python3
def main():
    try:
        from rac import main
        main()
    except KeyboardInterrupt:
        print('Interrupted...')
        exit(1)
    except ModuleNotFoundError:
        print('\033[91msome modules not found')
        print('try: pip install requests\033[0m')


if __name__ == '__main__':
    main()

