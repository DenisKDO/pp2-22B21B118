import os
print('EXIST: ', os.access(r"C:\Users\Денис\Documents\python_programs\unik\rep\pp2-22B21B118\tsis6\Builtin", os.F_OK))
print('READABLE: ', os.access(r"C:\Users\Денис\Documents\python_programs\unik\rep\pp2-22B21B118\tsis6\Builtin", os.R_OK))
print('WRITABLE: ', os.access(r"C:\Users\Денис\Documents\python_programs\unik\rep\pp2-22B21B118\tsis6\Builtin", os.W_OK))
print('EXECUTABLE: ', os.access(r"C:\Users\Денис\Documents\python_programs\unik\rep\pp2-22B21B118\tsis6\Builtin", os.X_OK))