import os
import shutil
from pathlib import Path
from pprint import pprint
import PySimpleGUI as sg
import hashlib
import PySimpleGUI as sg

IMPORTS = ["os", "shutil", "Path", "pprint", "PySimpleGUI", "sg", "hashlib", "print", "input",]
NAS = r"\\Serverlan\Serverlan - SWLTV"
WORK_IN_PROGRESS = "E:\\"
RECENT_WORK = "D:\\Videos"
ARCHIVE1 = "H:\\"
ARCHIVE2 = "L:\\"
ARCHIVE3 = "P:\\"
LOCAL_STORAGE = [ARCHIVE1, ARCHIVE2, ARCHIVE3, RECENT_WORK, WORK_IN_PROGRESS]
LOCATIONS = LOCAL_STORAGE + [NAS]
EXCLUSIONS = ("Adobe Premiere Pro Auto-Save",
            "$RECYCLE.BIN",
            "Media Cache Files",
            "Media Cache",
            "Peak Files",
            "Team Projects Cache",
            "System Volume Information",
            'SWLTV - Stock Footage',
            'SWLTV - Tutorials',)

def get_folders(path="E://"):
    path = Path(path)
    contents = [x for x in path.glob("*") if x.is_dir()]
    return [x for x in contents if x.is_dir() and x.name not in EXCLUSIONS]

def get_disk_usage():
    GB = 1024**3
    for location in LOCATIONS:
        try:
            print(f"\n{Path(location).drive}")
            usage = [f"{x/GB:.2f}" for x in shutil.disk_usage(location)]
            print(f"Total: {usage[0]} GB", end=" | ")
            print(f"Used: {usage[1]} GB", end=" | ")
            print(f"Free: {usage[2]} GB")
        except FileNotFoundError:
            print(f"Path not found - perhaps drive is disconnected?")

def copy_WIP():
    """
    Copies WORK_IN_PROGRESS (directories) to RECENT_WORK as a backup,
    overwriting if necessary.
    """
    i=input("Press ENTER or click Yes to overwrite D: with E:")
    if i != "Yes":
        return
    for source in get_folders(WORK_IN_PROGRESS):
        destination = Path(RECENT_WORK) / source.name
        print(str(source).upper())
        files = len([x for x in os.listdir(source) if (Path(source)/x).is_file()])
        directories = len([x for x in os.listdir(source) if (Path(source)/x).is_dir()])
        print(f"{files} (top level) files | {directories} (top level) directories\n")
        try:
            shutil.copytree(source, destination)
            print(f"ⓘ Copied everything in {source} to\n  {destination}\n")
        except FileExistsError:
            os.makedirs(destination, exist_ok = True)
            _check_for_essential_files(source, destination)
    print(f"\n✓ Work In Progress backed up ({WORK_IN_PROGRESS} -> {RECENT_WORK})")


def _get_file_hash(file_list):
    """
    Gets an MD5 Hash value for each file in a list.
    Returns a dictionary of {file: hash} items
    """
    if type(file_list) != list:
        file_list = [file_list]
    BLOCKSIZE = 65536
    file_dict = {}
    for file in file_list:
        hasher = hashlib.md5()
        with open(file, 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        file_dict[file] = hasher.hexdigest()
        # print(file.name, ":", hasher.hexdigest())
    return file_dict

def _check_for_essential_files(source, destination):
    """
    Looks for identical/changed files of particular types in source and
    destination folders; compares the hashes to decide.
    """
    essential_files = "prproj srt mp4 wav jpg png".split()
    for file_type in essential_files:
        source_files = list(k for k in source.glob("*."+ file_type))
        destination_files = list(k for k in destination.glob("*."+ file_type))
        for file in source_files:
            in_destination = file.name in [x.name for x in destination_files]
            match = [x for x in destination_files if x.name == file.name]
            if match:
                up_to_date = all([
                    file.stat().st_size == match[0].stat().st_size,
                    file.stat().st_mtime == match[0].stat().st_mtime,
                ])
            else:
                up_to_date = False
            if not up_to_date or not in_destination:
                shutil.copy(file, destination / file.name)
                shutil.copystat(file, destination / file.name)
                print(f"ⓘ Copied: {file.name} to\n  {destination}\n")


def archive_folder(archive_type = "swltv", folder = None):
    """
    Copy folder to Archive (Local Drive)
    Copy folder to NAS
    Delete folder
    """
    archive_drive = {"swltv": ARCHIVE1,
                     "project": ARCHIVE2,
                     "police": ARCHIVE3,
                     "military": ARCHIVE3}[archive_type]
    if folder is None:
        for folder in WORK_FOLDERS:
            pass
    return "Not yet implemented"

def rename_folder(old = None, new = None):
    """
    Searches LOCATIONS for folders named {old} and renames them as {new}
    """
    if old is None:
        old = Path(sg.popup_get_folder("",
                                       default_path="DATA (D:)",
                                       no_window=True,
                                       keep_on_top=True)).name
        if not old:
            print("> No directory selected.")
            return
    if new is None:
        new = sg.popup_get_text("",title="Rename Directory:",
                                     default_text = str(old),
                                     keep_on_top=True)
        if not new:
            print("> Replacement cancelled.")
            return
        if new == old:
            print("> Old and new directory name are the same.")
            return
    print(f"Renaming: {old}")
    print(f"To:       {new}\n")
    for location in LOCATIONS:
        old_path = Path(location) / old
        if old_path.is_dir():
            new_path = Path(location) / new
            i=input(f"Press ENTER or click Yes to rename: {str(old_path)} >  ")
            if i == 'Yes' or i == "":
                os.rename(old_path, new_path)
                print(f"> {new_path}\n")

def compare_folder(location1= WORK_IN_PROGRESS, location2=RECENT_WORK, reverse=True):
    """
    Compares first level directories/folders of two different locations
    """
    names1 = {x.name for x in set(get_folders(location1))}
    names2 = {x.name for x in set(get_folders(location2))}
    difference = names1 - names2
    if difference:
        print(f"\nDirectories in {location1} but not in (-) {location2}:")
    if reverse:
        difference = names2 - names1
        if difference:
            print(f"\nDirectories in {location2} but not in (-) {location1}:")
    pprint(difference)

def compare_folders():
    """
    Loops through a custom list of folders to compare and show differences
    """
    comparisons = [(WORK_IN_PROGRESS, RECENT_WORK, True),
                   (RECENT_WORK, ARCHIVE1, True),
                   (ARCHIVE1, NAS, False),
                   (RECENT_WORK, NAS, False)]
    for location1, location2, reverse in comparisons:
        compare_folder(location1, location2, reverse)

def _sg_input(text, **kwargs):
    return sg.popup_yes_no(text, title="AWSOM Backup", keep_on_top=True)

_input = input
_print = print
input = _sg_input
print = sg.Print
sg.change_look_and_feel('DarkAmber')
sg.set_options(message_box_line_width=80, debug_win_size=(80,30))
print(do_not_reroute_stdout=False, keep_on_top = True)  # Redirect stdout and stderr to Debug Window

FOLDERS = {k.split(":")[0]: get_folders(k) for k in LOCATIONS}
FOLDERS['NAS'] = FOLDERS.pop(NAS)
RESOURCES = {k:type(v).__name__ for k,v in list(locals().items()) if k not in IMPORTS and not k.startswith("_")}
print("Summary of Resources in AWSOM_Backup")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
pprint(RESOURCES)
print()
# input = _input
# print = _print
