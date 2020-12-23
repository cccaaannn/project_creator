from project_creator import python_project_creator, cpp_project_creator, c_project_creator
import sys



def menu(cfg_path):

    # Project Language selection menu
    print("<<< Project Creator >>>\n"
                "\n"
                "Python   (1)\n"
                "cpp      (2)\n"
                "c        (3)\n"
                "exit     (0)\n"
                "\n"
            "Select Project Language\n"
                )

    while True:
        try:
            project_language = int(input(": "))
            if not(project_language < 4 and project_language >= 0):
                raise ValueError
            else:
                if project_language == 0:
                    sys.exit(0)
                break
        except ValueError:
            print("Enter a valid value")


    # Project type selection menu
    if(project_language == 0):
        sys.exit(0)
    
    # python project creation
    elif(project_language == 1):

        creator = python_project_creator(cfg_path = cfg_path)

        print("\n<<< Create Python Project >>>\n"
                    "\n"
                    "standart project   (1)\n"
                    "git project        (2)\n"
                    "pypi project       (3)\n"
                    "exit               (0)\n"
                    "\n"
                    "Select Project Type\n"
                    )

        while True:
            try:
                project_type = int(input(": "))
                if not(project_type < 4 and project_type >= 0):
                    raise ValueError
                else:
                    if project_type == 0:
                        sys.exit(0)
                    break
            except ValueError:
                print("Enter a valid value")


        project_name = input("\nProject name: ")

        if project_type == 1:
            creator.standart_project(project_name)

        elif project_type == 2:
            creator.git_project(project_name)

        elif project_type == 3:
            creator.pypi_project(project_name)

        elif project_type == 0:
            sys.exit(0)

    # cpp project creation
    elif(project_language == 2):

        creator = cpp_project_creator(cfg_path = cfg_path)

        print("\n<<< Create cpp Project >>>\n"
                    "\n"
                    "standart project   (1)\n"
                    "git project        (2)\n"
                    "exit               (0)\n"
                    "\n"
                    "Select Project Type\n"
                    )

        while True:
            try:
                project_type = int(input(": "))
                if not(project_type < 3 and project_type >= 0):
                    raise ValueError
                else:
                    if project_type == 0:
                        sys.exit(0)
                    break
            except ValueError:
                print("Enter a valid value")


        project_name = input("\nProject name: ")

        if project_type == 1:
            creator.standart_project(project_name)

        elif project_type == 2:
            creator.git_project(project_name)

        elif project_type == 0:
            sys.exit(0)

    # c project creation
    elif(project_language == 3):

        creator = c_project_creator(cfg_path = cfg_path)

        print("\n<<< Create cProject >>>\n"
                    "\n"
                    "standart project   (1)\n"
                    "git project        (2)\n"
                    "exit               (0)\n"
                    "\n"
                    "Select Project Type\n"
                    )

        while True:
            try:
                project_type = int(input(": "))
                if not(project_type < 3 and project_type >= 0):
                    raise ValueError
                else:
                    if project_type == 0:
                        sys.exit(0)
                    break
            except ValueError:
                print("Enter a valid value")


        project_name = input("\nProject name: ")

        if project_type == 1:
            creator.standart_project(project_name)

        elif project_type == 2:
            creator.git_project(project_name)

        elif project_type == 0:
            sys.exit(0)


