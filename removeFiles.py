import os
import shutil
import time

path = input("Enter the path of the folder/directory to be organised:")
day = 0
seconds = time.time() - (day * 24 * 60 * 60)

if (os.path.exists(path)):
    for root, dirs, files in os.walk(path, topdown = True):
        for name in files:
            path = os.path.join(root,name)
            ctime = os.stat(path).st_ctime

            if (seconds >= ctime):
                os.remove(path)
                print("Deleted the path " + path + "successfully.")

        for name in dirs:
            path = os.path.join(root,name)
            ctime = os.stat(path).st_ctime

            if (seconds >= ctime):
                shutil.rmtree(path)
                print("Deleted the path " + path + "successfully.")

else:
    print("Path not found!")