import sys

print(sys.argv)  # prints out a list

# initialize a counter to print all available arguments
counter = 0
for i in sys.argv:
    counter += 1
    print("Argument {}: {}".format(counter, i))


# opening text file using commandline arguments
my_text_file = sys.argv[1]

with open(my_text_file, "r") as f:
    f_cont = f.read()

print(f_cont)
