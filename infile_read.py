def main():
    infile = open("SchoolIT.txt")

    file_contents = infile.read()

    infile.close()

    print(file_contents)

if __name__ == '__main__':
    main()
