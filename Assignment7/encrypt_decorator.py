from cryptography.fernet import Fernet


def encryptdecorator(**kwargs):
    def wrapper(func):
        def wrapped_function(*args):
            print('Encrypts the string using decorator')
            key = Fernet.generate_key()
            message = kwargs['message'].encode()
            f = Fernet(key)
            encrypted = f.encrypt(message)
            print("Before Encryption", message)
            print("After Encryption", encrypted)
            print("After Decryption", f.decrypt(encrypted))
            func(*args)
        return wrapped_function

    return wrapper


@encryptdecorator(message="hello")
def wish(*args):
    print("Arguments in function: "+args.__str__())


wish("welcome", "to", "Redi", "school")
