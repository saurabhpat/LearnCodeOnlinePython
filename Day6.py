# Question :
# A floppy disk shows f bytes of free and u bytes of used.
# If you delete a file of size o bytes and create a new file of size n bytes,
# how many free bytes will the floppy disk have?
# f,u,o,n are the user-entered value

f = int(input("Enter free bytes in disk : "))

u = int(input("Enter used bytes in disk : "))

o = int(input("Enter deleted file size in bytes : "))

n = int(input("Enter created file size in bytes : "))

print("Total free size : ", f + o - n)
