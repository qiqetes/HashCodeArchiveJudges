import numpy as np

name_of_file = "f"
NUM_BOOKS = 0
NUM_LIB = 0
DAYS = 0
LIB = {}

# Read input
with open("./input/{}.txt".format(name_of_file)) as f:
    content = f.readlines()

content = [x.strip() for x in content]
NUM_BOOKS = int(content[0].split(" ")[0])
NUM_LIB = int(content[0].split(" ")[1])
DAYS = int(content[0].split(" ")[2])


BOOKS = np.zeros((NUM_BOOKS))
BOOKS = BOOKS.astype(int)
for i, book in enumerate(content[1].split(" ")):
    BOOKS[i] = book


for i in range(2, len(content), 2):
    lib = content[i].split(" ")
    books = content[i+1].split(" ")
    LIB[(i-2)/2] = {}
    LIB[(i-2)/2]["n_books"] = int(lib[0])
    LIB[(i-2)/2]["su"] = int(lib[1])
    LIB[(i-2)/2]["bpd"] = int(lib[2])
    LIB[(i-2)/2]["books"] = list(map(int, books))


# Read output
with open("./output/{}_out.txt".format(name_of_file)) as f:
    content = f.readlines()

content = [x.strip() for x in content]
NUM_LIB_SU = content[0]
LIB_SU = []
for i in range(1, len(content), 2):
    lib = content[i].split(" ")
    books = content[i+1].split(" ")
    lib_su = {}
    lib_su["id"] = int(lib[0])
    lib_su["books"] = list(map(int, books))
    LIB_SU.append(lib_su)


# evaluation
q = 0  # queue days
lib_avail = []
books_done = []
q_lib = None
score = 0
for day in range(DAYS):
    q -= 1
    if(q <= 0):
        if(q_lib):
            lib_avail.append(q_lib)
            q_lib = None
        # All libraries are signedup, get the next one
        if LIB_SU:
            lib = LIB_SU.pop(0)
            q += LIB[lib["id"]]["su"]
            q_lib = lib
    for lib in lib_avail:
        for _ in range(LIB[lib["id"]]["bpd"]):
            if lib["books"]:
                book = lib["books"].pop(0)
                if book not in books_done:
                    books_done.append(book)
                    score += BOOKS[book]
            else:
                break

print(BOOKS)
print("SCORE: ", score)
