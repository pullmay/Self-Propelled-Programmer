def is_valid(name):
    return name.endswith('.txt')

def main():
    name = 'hoge.txt'
    if is_valid(name):
        print('The file is valid')
    else:
        print('The file is not valid')
    return 0

if __name__ == "__main__":
    main()