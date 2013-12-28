
#os imports
from os import path
#time imports
from time import gmtime
from time import time
#sys imports
from sys import argv


#file path
file_path = path.abspath(path.dirname(__file__))


def look_and_say(string):
    string = str(string)
    count = 1
    prev = string[0]
    result = ''

    for d in string[1:]:
        if d == prev:
            count += 1
            continue

        result += str(count) + prev
        count = 1
        prev = d

    return result + str(count) + prev


def count_digits(string):
    one, two, three = 0, 0, 0

    for d in string:
        if d == '1':
            one += 1
        elif d == '2':
            two += 1
        elif d == '3':
            three += 1

    return one, two, three


def read_file():
    with open('result_las.txt', 'r') as f:
        string = f.read()
        f.close()

    return string


def main():
    cycles = int(argv[1])

    if path.exists(path.join(file_path, 'result_las.txt')) is False:
        with open('result_las.txt', 'w') as f:
            f.write('1')
            f.close()

    init_time = '(%i/%i/%i) %i:%i:%i' % (gmtime().tm_mon, gmtime().tm_mday,
        gmtime().tm_year, gmtime().tm_hour, gmtime().tm_min, gmtime().tm_sec)

    start = time()
    for x in range(0, cycles):
        print 'Cycle [%i/%i] - (%i/%i/%i)[%i:%i:%i]' % (x + 1, cycles,
            gmtime().tm_mon, gmtime().tm_mday, gmtime().tm_year,
            gmtime().tm_hour, gmtime().tm_min, gmtime().tm_sec)

        print '\t[%i:%i:%i] Reading file...' % (gmtime().tm_hour,
                                            gmtime().tm_min, gmtime().tm_sec)

        string = read_file()

        print '\t[%i:%i:%i] Cycle...' % (gmtime().tm_hour,
                                         gmtime().tm_min, gmtime().tm_sec)
        result = look_and_say(string)

        print '\t[%i:%i:%i] Save file...' % (gmtime().tm_hour,
                                             gmtime().tm_min, gmtime().tm_sec)

        with open('result_las.txt', 'w') as f:
            f.write(result)
            f.close()

    end = time()
    end_time = '(%i/%i/%i) %i:%i:%i' % (gmtime().tm_mon, gmtime().tm_mday,
        gmtime().tm_year, gmtime().tm_hour, gmtime().tm_min, gmtime().tm_sec)

    print '\n' + '-' * 70
    print 'Initiated: %s' % init_time
    print 'Finalized: %s' % end_time
    du_t = gmtime(end - start)
    print 'Duration: %i:%i:%i' % (du_t.tm_hour, du_t.tm_min, du_t.tm_sec)
    print 'All cycles: %i' % cycles
    print 'File size: %iKiB' % (path.getsize(path.join(file_path, 'result_las.txt')) / 1024)

    print '\n' + '-' * 70
    print 'Analyzing file...'
    print '-' * 70

    string = read_file()

    print 'Digits:', len(string)

    count = count_digits(string)

    print 'All one: %i (%f%%)' % (count[0], (count[0]*100.0)/len(string))
    print 'All two: %i (%f%%)' % (count[1], (count[1]*100.0)/len(string))
    print 'All three: %i (%f%%)' % (count[2], (count[2]*100.0)/len(string))

main()
