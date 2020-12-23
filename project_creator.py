from pathlib import Path
import shutil
import json
import sys
import os


class project_creator(object):
    """base project creator class"""
    def __init__(self, cfg_path="cfg/options.cfg"):
        self.cfg_path = cfg_path
        self.__set_options_from_cfg()
    
    def __set_options_from_cfg(self):
        cfg_dict = self.__read_cfg_file()
        if(cfg_dict):
            # general options
            self.default_project_path = cfg_dict["general"]["default_project_path"]
            self.init_vscode = cfg_dict["general"]["init_vscode"]

            # python options
            self.python_vscode_files = cfg_dict["python"]["vscode_files"]
            self.python_git_files = cfg_dict["python"]["git_files"]
            self.python_pypi_files = cfg_dict["python"]["pypi_files"]
            self.python_main_file_name = cfg_dict["python"]["main_file_name"]
            
            # cpp options
            self.cpp_vscode_files = cfg_dict["cpp"]["vscode_files"]
            self.cpp_git_files = cfg_dict["cpp"]["git_files"]
            self.cpp_files = cfg_dict["cpp"]["cpp_files"]
            self.cpp_main_file_name = cfg_dict["cpp"]["main_file_name"]
            
            # c options
            self.c_vscode_files = cfg_dict["c"]["vscode_files"]
            self.c_git_files = cfg_dict["c"]["git_files"]
            self.c_files = cfg_dict["c"]["c_files"]
            self.c_main_file_name = cfg_dict["c"]["main_file_name"]

        else:
            print("cfg file is broken")
            sys.exit(0)

    def __read_cfg_file(self):
        try:
            with open(self.cfg_path,"r") as file:
                dict = json.load(file)
            return dict
        except:
            return 0


    def _copy_all_files_from_dir(self, src, dest):
        src_files = os.listdir(src)
        for file_name in src_files:
            full_file_name = os.path.join(src, file_name)
            shutil.copy(full_file_name, dest)

    def _create_dir_if_not_exists(self, path):
        if(not os.path.exists(path)):
            os.makedirs(path)

    def _create_file_if_not_exists(self, file_name, content = ""):
        with open(file_name,"a") as file:
            file.write(content)

    def _init_git(self, project_path):
        os.system("{0} {1} && {2}".format("cd",project_path,"git init"))

    def _start_vscode(self, project_path):
        os.system("{0} {1} && {2}".format("cd",project_path,"code ."))



class python_project_creator(project_creator):
    def __init__(self, cfg_path):
        super().__init__(cfg_path)

    def standart_project(self, project_name):

        # set main file name
        if(self.python_main_file_name):
            python_main_file_name = self.python_main_file_name
        else:
            python_main_file_name = project_name + ".py"

        # set paths
        project_path = os.path.join(self.default_project_path, project_name)
        vscode_file_path = os.path.join(project_path, ".vscode")
        main_file_full_name = os.path.join(project_path, python_main_file_name)

        # create required dirs
        self._create_dir_if_not_exists(project_path)
        self._create_dir_if_not_exists(vscode_file_path)

        # copy required files
        self._copy_all_files_from_dir(self.python_vscode_files, vscode_file_path)

        # create files
        self._create_file_if_not_exists(main_file_full_name)

        # start vs code
        if(self.init_vscode):
            self._start_vscode(project_path)

        # exit
        sys.exit(0)

    def git_project(self, project_name):

        # set main file name
        if(self.python_main_file_name):
            python_main_file_name = self.python_main_file_name
        else:
            python_main_file_name = project_name + ".py"
        
        # set paths
        project_path = os.path.join(self.default_project_path, project_name)
        vscode_file_path = os.path.join(project_path, ".vscode")
        main_file_full_name = os.path.join(project_path, python_main_file_name)

        # create required dirs
        self._create_dir_if_not_exists(project_path)
        self._create_dir_if_not_exists(vscode_file_path)

        # copy required files
        self._copy_all_files_from_dir(self.python_vscode_files, vscode_file_path)
        self._copy_all_files_from_dir(self.python_git_files, project_path)

        # create files
        self._create_file_if_not_exists(main_file_full_name)

        # init git
        self._init_git(project_path)

        # start vs code
        if(self.init_vscode):
            self._start_vscode(project_path)

        # exit
        sys.exit(0)

    def pypi_project(self, project_name):
        
        # set main file name
        if(self.python_main_file_name):
            python_main_file_name = self.python_main_file_name
        else:
            python_main_file_name = project_name + ".py"

        # set paths
        project_path = os.path.join(self.default_project_path, project_name)
        vscode_file_path = os.path.join(project_path, ".vscode")
        inner_project_path = os.path.join(project_path, project_name)
        gitignore_path = os.path.join(project_path, ".gitignore")
        init_file_full_name = os.path.join(inner_project_path, "__init__.py")
        main_file_full_name = os.path.join(inner_project_path, python_main_file_name)

        # create required dirs
        self._create_dir_if_not_exists(project_path)
        self._create_dir_if_not_exists(vscode_file_path)
        self._create_dir_if_not_exists(inner_project_path)
        
        # copy required files
        self._copy_all_files_from_dir(self.python_vscode_files, vscode_file_path)
        self._copy_all_files_from_dir(self.python_pypi_files, project_path)

        # init git
        self._init_git(project_path)

        # create files
        self._create_file_if_not_exists(main_file_full_name)
        self._create_file_if_not_exists(init_file_full_name)
        self._create_file_if_not_exists(gitignore_path, content="{0}{1}\n".format(project_name, ".egg-info"))

        # start vs code
        if(self.init_vscode):
            self._start_vscode(project_path)

        # exit
        sys.exit(0)



class cpp_project_creator(project_creator):
    def __init__(self, cfg_path):
        super().__init__(cfg_path)

    def standart_project(self, project_name):

        # set main file name
        if(self.cpp_main_file_name):
            cpp_main_file_name = self.cpp_main_file_name
        else:
            cpp_main_file_name = project_name + ".cpp"

        # set paths
        project_path = os.path.join(self.default_project_path, project_name)
        vscode_file_path = os.path.join(project_path, ".vscode")
        main_file_full_name = os.path.join(project_path, cpp_main_file_name)
        temp_cpp_main_file_path = os.path.join(project_path, "main.cpp")

        # create required dirs
        self._create_dir_if_not_exists(project_path)
        self._create_dir_if_not_exists(vscode_file_path)

        # copy required files
        self._copy_all_files_from_dir(self.cpp_vscode_files, vscode_file_path)
        self._copy_all_files_from_dir(self.cpp_files, project_path)

        # rename temp main.cpp file
        os.rename(temp_cpp_main_file_path, main_file_full_name)

        # start vs code
        if(self.init_vscode):
            self._start_vscode(project_path)

        # exit
        sys.exit(0)

    def git_project(self, project_name):

        # set main file name
        if(self.cpp_main_file_name):
            cpp_main_file_name = self.cpp_main_file_name
        else:
            cpp_main_file_name = project_name + ".cpp"
        
        # set paths
        project_path = os.path.join(self.default_project_path, project_name)
        vscode_file_path = os.path.join(project_path, ".vscode")
        main_file_full_name = os.path.join(project_path, cpp_main_file_name)
        temp_cpp_main_file_path = os.path.join(project_path, "main.cpp")

        # create required dirs
        self._create_dir_if_not_exists(project_path)
        self._create_dir_if_not_exists(vscode_file_path)

        # copy required files
        self._copy_all_files_from_dir(self.cpp_vscode_files, vscode_file_path)
        self._copy_all_files_from_dir(self.cpp_git_files, project_path)
        self._copy_all_files_from_dir(self.cpp_files, project_path)

        # rename temp main.cpp file
        os.rename(temp_cpp_main_file_path, main_file_full_name)

        # init git
        self._init_git(project_path)

        # start vs code
        if(self.init_vscode):
            self._start_vscode(project_path)

        # exit
        sys.exit(0)



class c_project_creator(project_creator):
    def __init__(self, cfg_path):
        super().__init__(cfg_path)

    def standart_project(self, project_name):

        # set main file name
        if(self.c_main_file_name):
            c_main_file_name = self.c_main_file_name
        else:
            c_main_file_name = project_name + ".c"

        # set paths
        project_path = os.path.join(self.default_project_path, project_name)
        vscode_file_path = os.path.join(project_path, ".vscode")
        main_file_full_name = os.path.join(project_path, c_main_file_name)
        temp_c_main_file_path = os.path.join(project_path, "main.c")

        # create required dirs
        self._create_dir_if_not_exists(project_path)
        self._create_dir_if_not_exists(vscode_file_path)

        # copy required files
        self._copy_all_files_from_dir(self.c_vscode_files, vscode_file_path)
        self._copy_all_files_from_dir(self.c_files, project_path)

        # rename temp main.c file
        os.rename(temp_c_main_file_path, main_file_full_name)

        # start vs code
        if(self.init_vscode):
            self._start_vscode(project_path)

        # exit
        sys.exit(0)

    def git_project(self, project_name):

        # set main file name
        if(self.c_main_file_name):
            c_main_file_name = self.c_main_file_name
        else:
            c_main_file_name = project_name + ".c"
        
        # set paths
        project_path = os.path.join(self.default_project_path, project_name)
        vscode_file_path = os.path.join(project_path, ".vscode")
        main_file_full_name = os.path.join(project_path, c_main_file_name)
        temp_c_main_file_path = os.path.join(project_path, "main.c")

        # create required dirs
        self._create_dir_if_not_exists(project_path)
        self._create_dir_if_not_exists(vscode_file_path)

        # copy required files
        self._copy_all_files_from_dir(self.c_vscode_files, vscode_file_path)
        self._copy_all_files_from_dir(self.c_git_files, project_path)
        self._copy_all_files_from_dir(self.c_files, project_path)

        # rename temp main.c file
        os.rename(temp_c_main_file_path, main_file_full_name)

        # init git
        self._init_git(project_path)

        # start vs code
        if(self.init_vscode):
            self._start_vscode(project_path)

        # exit
        sys.exit(0)

