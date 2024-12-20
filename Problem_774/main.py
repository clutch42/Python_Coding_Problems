# Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.
# For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.
from Read7 import Read7
from ReadN import read_n

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_file = Read7("data.txt")
    seven = read_file.read7()
    print(seven)
    while seven != "":
        seven = read_file.read7()
        print(seven)
    read_file.close()

    print(read_n(10))
    print(read_n(11))
    print(read_n(100))
    print(read_n(0))
    print(read_n(20))
    print(read_n(40))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
