#!/usr/bin/env python

"""my_run_shell_0.py:
Simple shell to start programs, e.g., try "PShell>ps" and "PShell>ls".

The purpose of this script is to give you simple functions
for locating an executable program in common locations in Linux/UNIX
(PATH environmental variable).

You are meant to paste your code from your solution in Part A
into the relevant points in this script.

Try to stick to Style Guide for Python Code and Docstring Conventions:
see https://peps.python.org/pep-0008 and https://peps.python.org/pep-0257/

(Note: The breakdown into Input/Action/Output in this script is just a suggestion.)
"""

import grp
import os
import pwd
import shutil
import sys
import time

# Here the path is hardcoded, but you can easily optionally get your PATH environ variable
# by using: path = os.environ['PATH'] and then splitting based on ':' such as the_path = path.split(':')
THE_PATH = ["/bin/", "/usr/bin/", "/usr/local/bin/", "./"]

def run_external_cmd(fields):
    global THE_PATH
    cmd = fields[0]

    execname = None
    #constructs potential paths until it finds a file that exists and is executable
    for dir in THE_PATH:
        potential_path = os.path.join(dir, cmd)
        #if the file exists and is executable, we set execname to the path
        if os.path.isfile(potential_path) and os.access(potential_path, os.X_OK):
            execname = potential_path
            break

    if execname is None:
        print(f"Executable '{cmd}' not found")
        return

    #the child process with pid of 0 executes the command, while the parent waits for the child to finish
    pid = os.fork()
    if pid == 0:
        try:
            #The child process attempts to execute the external command
            os.execv(execname, fields)
        except Exception as e:
            print(f"Error executing command: {e}")
            os._exit(1)
    else:
        #parent process waits for the child process to finish execution (we ignore returned pid and only care about status)
        _, status = os.wait()
        if os.WIFEXITED(status):
            print(f"Command '{cmd}' exited normally with status {os.WEXITSTATUS(status)}")
        else:
            print(f"Command '{cmd}' exited abnormally")

# ========================
#   Constructs the full path used to run the external command
#   Checks to see if an executable file can be found in one of the provided directories.
#   Returns None on failure.
# ========================
def add_path(cmd, executable_dirs):
    """Returns command with full path when possible and None otherwise.
    
    Input: takes a command and a list of paths to search
    Action: no actions
    Output: returns external command prefaced by full path
            (returns None if executable file cannot be found in any of the paths)
    """
    if cmd[0] not in ['/', '.']:
        for dir in executable_dirs:
            execname = dir + cmd
            if os.path.isfile(execname) and os.access(execname, os.X_OK):
                return execname
        return None
    else:
        return cmd

# ========================
#   files command
#   List file and directory names
#   No arguments
# ========================
def files_cmd(fields):
    """Return nothing after printing names/types of files/dirs in working directory.
    
    Input: takes a list of text fields
    Action: prints for each file/dir in current working directory their type and name
            (unless list is non-empty in which case an error message is printed)
    Output: returns no return value
    """
    
    if checkArgs(fields, 0):
        for filename in os.listdir('.'):
            if os.path.isdir(os.path.abspath(filename)):
                print("dir:", filename)
            else:
                print("file:", filename)

# ========================
#  info command
#   List file information
#   1 argument: file name
# ========================
#this fucntion lists information about a file or directory 
def info_cmd(fields):
    #makes sure only one arg is passed
    if checkArgs(fields, 1):
        filename = fields[1]
        if not os.path.exists(filename):
            print(f"'{filename}' does not exist.")
            return
        print(f"File Name: {filename}")
        print("Directory/File:", "directory" if os.path.isdir(filename) else "file")
        stats = os.stat(filename)
        owner = pwd.getpwuid(stats.st_uid).pw_name
        group = grp.getgrgid(stats.st_gid).gr_name
        permissions = oct(stats.st_mode & 0o777)
        inode = stats.st_ino
        mtime = time.ctime(stats.st_mtime)
        atime = time.ctime(stats.st_atime)
        ctime = time.ctime(stats.st_ctime)
        print(f"Owner: {owner}")
        print(f"Group: {group}")
        print(f"Permissions: {permissions}")
        print(f"Inode Number: {inode}")
        print(f"Last Edited (mtime): {mtime}")
        print(f"Last Accessed (atime): {atime}")
        print(f"Metadata Change (ctime): {ctime}")
        # if the file is not a directory, we print the size and if it is executable
        if not os.path.isdir(filename):
            size = stats.st_size
            executable = os.access(filename, os.X_OK)
            print(f"Size (bytes): {size}")
            print(f"Executable?: {executable}")

#this function deletes a file if it exists
def delete_cmd(fields):
    if checkArgs(fields, 1):
        filename = fields[1]
        if os.path.isfile(filename):
            try:
                os.remove(filename)
                print(f"Deleted file '{filename}'")
            except Exception as e:
                print(f"Error deleting file: {e}")
        else:
            print(f"File '{filename}' does not exist")

#copies source file to destination
def copy_cmd(fields):
    if checkArgs(fields, 2):
        src, dst = fields[1], fields[2]
        if not os.path.isfile(src):
            print(f"Source file '{src}' does not exist.")
        # if the destination file already exists, we print an error message
        elif os.path.exists(dst):
            print(f"Destination file '{dst}' already exists.")
        else:
            shutil.copyfile(src, dst)
            print(f"Copied '{src}' to '{dst}'")

# make file
def make_cmd(fields):
    if checkArgs(fields, 1):
        filename = fields[1]
        if os.path.exists(filename):
            print(f"File '{filename}' already exists.")
        else:
            open(filename, 'w').close()
            print(f"File '{filename}' created.")

# moves down to a directory
def down_cmd(fields):
    if checkArgs(fields, 1):
        dirname = fields[1]
        if os.path.isdir(dirname):
            os.chdir(dirname)
            print(f"Moved into directory '{dirname}'")
        else:
            print(f"Directory '{dirname}' does not exist.")

# moves up the directory
def up_cmd(fields):
    if checkArgs(fields, 0):
        parent = os.path.abspath(os.path.join(os.getcwd(), '..'))
        if os.getcwd() == parent:
            print("Already at the top directory.")
        else:
            os.chdir(parent)
            print(f"Moved up to directory '{os.getcwd()}'")

# rename file
def rename_cmd(fields):
    if checkArgs(fields, 2):
        old, new = fields[1], fields[2]
        if os.path.exists(old):
            os.rename(old, new)
            print(f"Renamed '{old}' to '{new}'")
        else:
            print(f"File '{old}' does not exist.")

# make directory
def mkdir_cmd(fields):
    if checkArgs(fields, 1):
        dirname = fields[1]
        if not os.path.exists(dirname):
            os.mkdir(dirname)
            print(f"Directory '{dirname}' created.")
        else:
            print(f"Directory '{dirname}' already exists.")

#current directory
def pwd_cmd(fields):
    if checkArgs(fields, 0):
        print(f"Current directory: {os.getcwd()}")

# finish shell
def finish_cmd(fields):
    if checkArgs(fields, 0):
        print("Exiting PShell.")
        sys.exit(0)
        
        
def help_cmd(fields):
    """Displays a list of available commands"""
   
    if checkArgs(fields, 0):
        print("\nCommands in PShell:\n")
        commands_info = [
            ("files", "Lists all files/Directories."),
            ("info <filename>", "Shows specific file metadata."),
            ("delete <filename>", "Deletes the specified file."),
            ("copy <source> <destination>", "Copies a file from <source> file to <destination> file."),
            ("make <filename>", "Creates a new empty file."),
            ("down <directory>", "Moves into the subdirectory."),
            ("up", "Moves up one directory level."),
            ("rename <oldname> <newname>", "Renames a file from <oldname> to <newname>."),
            ("mkdir <directory>", "Creates a new directory."),
            ("pwd", "Displays the current working directory."),
            ("<Linux Command>", "Executes an external shell command."),
            ("finish", "Exits the shell."),
        ]

        for cmd, desc in commands_info:
            print(f"{cmd.ljust(20)} - {desc}")
        print("\n")



# ----------------------
# Other functions
# ----------------------
def checkArgs(fields, num):
    """Returns if len(fields)-1 == num (prints error to shell if not).
    
    Input: takes a list of text fields and how many non-command fields are expected
    Action: prints an error message if the number of fields is unexpected
    Output: returns boolean value to indicate if it was expected number of fields
    """
    
    numArgs = len(fields) - 1
    if numArgs == num:
        return True
    if numArgs > num:
        print("Unexpected argument", fields[num+1], "for command", fields[0])
    else:
        print("Missing argument for command", fields[0])
    
    return False

# ---------------------------------------------------------------------

def main():
    commands = {
        "files": files_cmd,
        "info": info_cmd,
        "delete": delete_cmd,
        "copy": copy_cmd,
        "make": make_cmd,
        "down": down_cmd,
        "up": up_cmd,
        "rename": rename_cmd,
        "mkdir": mkdir_cmd,
        "pwd": pwd_cmd,
        "help": help_cmd,
        "finish": finish_cmd,
    }

    while True:
        line = input("PShell>")
        fields = line.strip().split()

        if not fields:
            continue
        #match the command to the appropriate function, and if it doesn't exist, run the external command
        command = fields[0]
        if command in commands:
            commands[command](fields)
        else:
            run_external_cmd(fields)

if __name__ == '__main__':
    sys.exit(main())
