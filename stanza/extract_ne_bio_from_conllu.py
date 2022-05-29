import sys


def extract_ne_bio(fin, fout):
    for line in fin:
        line = line.rstrip("\n")
        if not line:
            print(file=fout)
            continue
        elif line.startswith("#"):
            continue
        f = line.split("\t")
        misc = dict(_.split("=", maxsplit=1) for _ in f[9].split("|")) if f[9] else {}
        ne = misc.get("NE", "O")
        if ne.startswith("U"):
            ne = "B" + ne[1:]
        elif ne.startswith("L"):
            ne = "I" + ne[1:]
        print(f[1], ne, sep="\t", file=fout)


def main():
    extract_ne_bio(sys.stdin, sys.stdout)


if __name__ == "__main__":
    main()
