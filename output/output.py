frame = "output.txt"
file = open(frame, "w")
for i in range(10):
    file.write(f"This is the first line{i}.\n")
file.close()
