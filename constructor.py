class employ:
    def __init__(self ):
        print("employ created")
    def __del__(self):
        print("destructor called employ deleted")
ob=employ()
del ob