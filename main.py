from pathlib import Path
import shutil
import sys
import os
import json


def __copy_all_files_from_dir(src, dest):
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        shutil.copy(full_file_name, dest)

def __create_dir_if_not_exists(path):
    if(not os.path.exists(path)):
        os.makedirs(path)

def __create_file_if_not_exists(file_name, content = ""):
    with open(file_name,"a") as file:
        file.write(content)

def __init_git(project_path):
    os.system("{0} {1} && {2}".format("cd",project_path,"git init"))

def __start_vscode(project_path):
    os.system("{0} {1} && {2}".format("cd",project_path,"code ."))

def __read_cfg_file(cfg_path="default_options.cfg"):
    try:
        with open(cfg_path,"r") as file:
            dict = json.load(file)
        return dict
    except:
        return 0




def standart_project(project_name, default_project_path, main_file_name):
    
    # set paths
    project_path = os.path.join(default_project_path, project_name)
    vscode_file_path = os.path.join(project_path, ".vscode")
    main_file_full_name = os.path.join(project_path, main_file_name)

    # create required dirs
    __create_dir_if_not_exists(project_path)
    __create_dir_if_not_exists(vscode_file_path)

    # copy required files
    __copy_all_files_from_dir(vscode_files, vscode_file_path)

    # create files
    __create_file_if_not_exists(main_file_full_name)
    
    __start_vscode(project_path)


def github_project(project_name, default_project_path, main_file_name):
    
    # set paths
    project_path = os.path.join(default_project_path, project_name)
    vscode_file_path = os.path.join(project_path, ".vscode")
    main_file_full_name = os.path.join(project_path, main_file_name)

    # create required dirs
    __create_dir_if_not_exists(project_path)
    __create_dir_if_not_exists(vscode_file_path)

    # copy required files
    __copy_all_files_from_dir(vscode_files, vscode_file_path)
    __copy_all_files_from_dir(github_project_files, project_path)

    # init git
    __init_git(project_path)

    # create files
    __create_file_if_not_exists(main_file_full_name)
    
    __start_vscode(project_path)


def pypi_project(project_name, default_project_path):

    # set paths
    project_path = os.path.join(default_project_path, project_name)
    vscode_file_path = os.path.join(project_path, ".vscode")
    inner_project_path = os.path.join(project_path, project_name)
    gitignore_path = os.path.join(project_path, ".gitignore")
    init_file_full_name = os.path.join(inner_project_path, "__init__.py")
    main_file_full_name = os.path.join(inner_project_path, project_name+".py")

    # create required dirs
    __create_dir_if_not_exists(project_path)
    __create_dir_if_not_exists(vscode_file_path)
    __create_dir_if_not_exists(inner_project_path)
    
    # copy required files
    __copy_all_files_from_dir(vscode_files, vscode_file_path)
    __copy_all_files_from_dir(pypi_project_files, project_path)

    # init git
    __init_git(project_path)

    # create files
    __create_file_if_not_exists(main_file_full_name)
    __create_file_if_not_exists(init_file_full_name)
    __create_file_if_not_exists(gitignore_path, content="{0}{1}\n".format(project_name, ".egg-info"))
    
    __start_vscode(project_path)





cfg_dict = __read_cfg_file()
if(cfg_dict):
    vscode_files = cfg_dict["vscode_files"]
    github_project_files = cfg_dict["github_project_files"]
    pypi_project_files = cfg_dict["pypi_project_files"]
    default_project_path = cfg_dict["default_project_path"]
    default_file_name = cfg_dict["default_file_name"]
else:
    print("cfg file is broken")
    sys.exit(0)


print("Python Project Creator\nProject will be created on {0}\nTo change default options see default_options.cfg file\n\n".format(default_project_path))

while True:
    try:
        project_type = int(input("Project type\n(1) standart\n(2) standart with git\n(3) pypi\n(0) exit\n:"))
        if not(project_type <= 3 and project_type > 0):
            raise ValueError
        else:
            break
    except ValueError:
        print("Enter a valid value")


project_name = input("Project name: ")

if project_type == 1:
    standart_project(project_name, default_project_path, default_file_name)

elif project_type == 2:
    github_project(project_name, default_project_path, default_file_name)

elif project_type == 3:
    pypi_project(project_name, default_project_path)

elif project_type == 0:
    sys.exit(0)






