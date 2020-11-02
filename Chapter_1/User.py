class User:
    def __init__(self, name, mail=None):
        self.name = name
        self.mail = mail

def main():
    # User('miruca', email='miruca@example.com') # エラーになる
    User('miruca', mail='miruca@example.com')

if __name__ == "__main__":
    main()