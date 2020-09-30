def formatdecorator(**kwargs):
    def wrapper(func):
        def wrapped_function(*args):
            print('Formats the string using decorator')
            print('Before formatting : '+kwargs['message'])
            bolded_string = "\033[1m" + kwargs['message'] + "\033[0m"
            undeline_string = "\033[4m" + bolded_string + "\033[0m"
            italic_string = "\033[3m" + undeline_string + "\033[0m"
            print('After formatting : '+italic_string)
            func(*args)
        return wrapped_function

    return wrapper


@formatdecorator(message="hello")
def wish(*args):
    print("Arguments in function: "+args.__str__())


wish("welcome", "to", "Redi", "school")

