class student:
    
    #initializing constructor
    def __init__(self):
        print('student called')

    

    def __del__(self):
        print('constructor called,student deleted')

obj=student()
del obj
