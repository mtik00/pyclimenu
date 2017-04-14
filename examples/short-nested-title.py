import climenu

@climenu.group(title='Build Menu')
def build_group(): pass


@build_group.menu(title='Build the package')
def build_package():
    # TODO: Add the actual code here
    print("I built the package!")

@build_group.menu(title='Build the release')
def build_release():
    '''
    Do a bunch of stuff to build the release.

        * Copy the files
        * Run some scripts
        * Build the release
        * Copy the release to X/Y/Z
    '''
    # TODO: Add the actual code here
    print("I built the release!")

def main():
    climenu.run()

if __name__ == '__main__':
    main()