import os
cmd = 'date'

cwd = os.getcwd()
print("current working directory : " + cwd)
ping ="ping"
# pingFoo = os.system(ping)

#os.mkdir("new")
# os.system("touch new.py")
print(os.stat("os.py"))
print(os.listdir())
os.chdir("/Users/Lenovo/Downloads/vscNew/ethical/new")
# os.rename("new","one")


# for dirpath ,dirnames,filenames in os.walk("/Users/Lenovo/Downloads/vscNew/ethical/"):
#     print("dirpath" , dirpath)
#     print("dirnames" , dirnames)
#     print("filename" , filenames)
#     print("!!!")


path = os.environ.get('os.py')
print(path)