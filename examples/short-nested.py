import climenu

@climenu.group()
def build_group():
    '''Build Menu'''
    pass

@build_group.menu()
def build_package():
    '''Build the package'''
    # TODO: Add the actual code here
    print("I built the package!")

@build_group.menu()
def build_release():
    '''Build the release'''
    # TODO: Add the actual code here
    print("I built the release!")

def main():
    climenu.run()

if __name__ == '__main__':
    main()