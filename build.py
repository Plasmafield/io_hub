import sys

target_dir = sys.argv[1]
fw_name = sys.argv[2]

file = open(target_dir + "/" + fw_name, "w")
file.write("This is the firmware\n")
file.close()
