# with open("Python\\File_Handling\\f1.txt", "w+") as f:
#     f.write("kamalesh")
#     f.seek(0)
#     a = f.read()
#     print(a)



# obj = A().__enter__()
# try:
#     # block
# finally:
#     A().__exit__()


with open("f1.txt","w+") as f:
    f.write("siva perumal")
    f.seek(0)
    a = f.read()
    print(a)