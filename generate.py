import sys


def main():
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    with open('00_ytmnd_{}_{}.txt'.format(start, end), 'w') as f:
        f.write('\n'.join(['ytmnd:{}-{}'.format(i, i+99)
                           for i in range(start, end, 100)]))

if __name__ == '__main__':
    main()

