import os
import threading
import shutil

class Scanner():
    def __init__(self, dir, dest):
        self.dir = dir
        self.dest = dest
        print("IF YOU ARE READING THIS AND ARE NOT TRYING TO DEBUG /n YOU ARE RUNNING THIS WRONG!")
        print(self.dir)
        print(self.dest)

    def copy_file(self, file):
        shutil.copy2(file, self.dest)
    def find_dir(self):
        if os.path.exists(self.dir) and os.path.isdir(self.dir):
            print("FOUND " + self.dir)
            threads = []

            for file in os.listdir(self.dir):
                full_path = os.path.join(self.dir, file)

                if os.path.isfile(full_path):
                    t = threading.Thread(target=self.copy_file,args=(full_path,))
                    t.start()
                    threads.append(t)

            for t in threads:
                t.join()

    def __call__(self, *args, **kwargs):
        self.find_dir()

