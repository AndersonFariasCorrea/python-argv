import sys
print ('argument list', sys.argv)
name = sys.argv[1]
print ("Hello {}. How are you?".format(name))

# ubuntu: run as python3 main.py <arg>
