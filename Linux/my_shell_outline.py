#!/usr/bin/env python

"""my_shell_outline.py:
Simple shell that interacts with the filesystem, e.g., try "PShell>files".

Try to stick to Style Guide for Python Code and Docstring Conventions:
see https://peps.python.org/pep-0008 and https://peps.python.org/pep-0257/

(Note: The breakdown into Input/Action/Output in this script is just a suggestion.)
"""

import glob
import grp
import os
import pwd
import shutil
import sys
import time
import stat

# ========================
#    files command
#    List file and directory names
#    No command arguments
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
#     List file information
#     1 command argument: file name
# ========================
def info_cmd(fields):
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
        if not os.path.isdir(filename):
            size = stats.st_size
            executable = os.access(filename, os.X_OK)
            print(f"Size (bytes): {size}")
            print(f"Executable?: {executable}")

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

def copy_cmd(fields):
    if checkArgs(fields, 2):
        src, dst = fields[1], fields[2]
        if not os.path.isfile(src):
            print(f"Source file '{src}' does not exist.")
        elif os.path.exists(dst):
            print(f"Destination file '{dst}' already exists.")
        else:
            shutil.copyfile(src, dst)
            print(f"Copied '{src}' to '{dst}'")

def make_cmd(fields):
    if checkArgs(fields, 1):
        filename = fields[1]
        if os.path.exists(filename):
            print(f"File '{filename}' already exists.")
        else:
            open(filename, 'w').close()
            print(f"File '{filename}' created.")

def down_cmd(fields):
    if checkArgs(fields, 1):
        dirname = fields[1]
        if os.path.isdir(dirname):
            os.chdir(dirname)
            print(f"Moved into directory '{dirname}'")
        else:
            print(f"Directory '{dirname}' does not exist.")

def up_cmd(fields):
    if checkArgs(fields, 0):
        parent = os.path.abspath(os.path.join(os.getcwd(), '..'))
        if os.getcwd() == parent:
            print("Already at the top directory.")
        else:
            os.chdir(parent)
            print(f"Moved up to directory '{os.getcwd()}'")

def rename_cmd(fields):
    if checkArgs(fields, 2):
        old, new = fields[1], fields[2]
        if os.path.exists(old):
            os.rename(old, new)
            print(f"Renamed '{old}' to '{new}'")
        else:
            print(f"File '{old}' does not exist.")

def mkdir_cmd(fields):
    if checkArgs(fields, 1):
        dirname = fields[1]
        if not os.path.exists(dirname):
            os.mkdir(dirname)
            print(f"Directory '{dirname}' created.")
        else:
            print(f"Directory '{dirname}' already exists.")

def pwd_cmd(fields):
    if checkArgs(fields, 0):
        print(f"Current directory: {os.getcwd()}")

def finish_cmd(fields):
    if checkArgs(fields, 0):
        print("Exiting PShell.")
        sys.exit(0)


# ----------------------
# Other functions
# ----------------------
def checkArgs(fields, num):
    """Returns if len(fields)-1 == num and print an error in shell if not.
    
    Input: takes a list of text fields and how many non-command fields are expected
    Action: prints error to shell if the number of fields is unexpected
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
            ("finish", "Exits the shell."),
        ]

        for cmd, desc in commands_info:
            print(f"{cmd.ljust(20)} - {desc}")
        print("\n")

# ---------------------------------------------------------------------

def main():
    """Returns exit code 0 (after executing the main part of this script).
    
    Input: no function arguments
    Action: run multiple user-inputted commands
    Output: return zero to indicate regular termination
    """
    
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

        command = fields[0]
        if command in commands:
            commands[command](fields)
        else:
            print(f"Unknown command '{command}'")

if __name__ == '__main__':
    sys.exit( main() ) # run main function and then exit
