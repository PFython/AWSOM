#!python3

# Version 0.1 created 2018-04-18
#
# This script is a web front end for the
# AWSOM video automation toolkit.
# Currently based on bottle and simple html.
# Peter Fison, covering mainly:
#
# Author: peter@southwestlondon.tv
# © MMXVIII, South West London TV Ltd.

import os
# import gevent.tests.test__systemerror
import time
import pprint
import requests
import functools
import subprocess
from pathlib import Path

import multiprocessing
session = None
def set_global_session():
    global session
    if not session:
        session = requests.Session()

dir_path = Path(__file__).parent
ffmpeg_path = Path(r"c:\program files\ffmpeg\bin\ffmpeg.exe")

def timer(func):
    """
    Starts the clock, runs func(), stops the clock. Simples.
    Designed to work as a decorator... just put @timer in front of
    the original function.
    """
    # Preserve __doc__ and __name__ information of the main function
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        data = func(*args, **kwargs)
        print(f"Function {func.__name__!r} took {round(time.perf_counter()-start,2)} seconds to complete.")
        return (data)
    return wrapper

def get_output_file(call_type, input_path, input_path2="", start="", end=""):
    """
    Determine the name of the output file based on rules per call type.
    """
    def strip_audio():
        stem = input_path.stem.replace("[AV]","[A]")
        stem = stem.replace("[720]","")
        stem = stem.replace("[1080]","")
        return input_path.parent / (stem + ".m4a")
    def combine_av():
        stem = input_path.stem.replace("[1080][V]","[1080][AV]")
        return input_path.parent / (stem + input_path.suffix)
    def trim():
        # Desired format: lQmJr9kvPT0[1080][AV][10-20].mp4
        # Start and end use round number of seconds currently
        # Which may prove limiting in future, but reads much better
        stem = input_path.stem +"[" + str(round(start)) + "-" + str(round(end)) + "]"
        return Path(dir_path) / "static" / "Subclips" / (stem + input_path.suffix)
    trim0 = trim1 = trim2 = trim
    def detect():
        stem = input_path.stem + "[scenes]"
        return input_path.parent / (stem +".txt")
    def file_to_mp4():
        return input_path.with_suffix(".mp4")
    try:
        return eval(call_type)()
    except:
        stem = input_path.stem + "[new]"
        return input_path.parent / (stem + input_path.suffix)

def ffmpeg_args(call_type="mkv_to_mp4",input_path="Idlib Offensive-N0hqPmbUbgQ.mkv", input_path2="lQmJr9kvPT0[A].aac", start=5, end=10):
    """
    Generates ffmpeg command line args using presets based on desired call_type.
    """
    input_path = Path(input_path)
    output_file = get_output_file(call_type, input_path, input_path2, start, end)
    # Convert Paths to strings so ffmeg can digest the arguments
    output_file = str(output_file)
    input_path = str(input_path)
    calls = {"strip_audio":["-i",input_path,"-vn","-acodec","copy",output_file],
             "combine_av":["-i",input_path,"-i",input_path2,"-c","copy",output_file],
             "trim0":["-ss",str(start),"-i",input_path,"-to",str(end-start),"-c","copy",output_file],
             "trim1":["-i",input_path,"-ss",str(start),"-to",str(end),"-c","copy",output_file],
             "trim2":["-ss",str(start),"-i",input_path,"-to",str(end),"-c","copy","-copyts",output_file],
             "detect":["-i",input_path,"-filter:v","\"select='gt(scene,0.4)',showinfo\"","-f","null","-","2>",output_file],
             "file_to_mp4":('-i "' + input_path + '" -c:v copy "' + output_file +'"'),
             }
    # "trim2" is currently the most accurate/reliable preset for trimming
    # For different examples of "trim", see Notes section of
    # https://trac.ffmpeg.org/wiki/Seeking#Cuttingsmallsections
    #
    # {calls} can be extended over time to include all desired
    # presets for running ffmpeg without the need for a intermediate wrapper
    # or library.  Just need to master the ffmpeg syntax!
    args=calls[call_type]
    # Add (in REVERSE) common configuration args
    # Might want to toggle loglevel between "info" and "warning"
    common_args = ["repeat+level+warning","-loglevel","-hide_banner","-y", '"' + str(ffmpeg_path) + '"']
    for arg in common_args:
        if type(args) == list:
            args.insert(0,arg)
        elif type(args) == str:
            args = arg +" " + args

    return(args)

@timer
def call_ffmpeg(args=[str(ffmpeg_path)]):
    """
    Runs ffmpeg.exe using a list of basic [args]
    """
    try:
      if type(args)==list:
        call=subprocess.call(args)
      elif type(args)==str:
        subprocess.call(args,shell=True)
    except Exception as E:
        print(E)
        print("\n> Problem running ffmpeg with the following args:\n")
        pprint.pprint(args)
    return

def start_multiprocessing(function_list, data_list):
    """
    Creates and runs a multiprocessing pool for (1..n) functions all of which
    use the same data_list (e.g. YouTube video links).  Returns a dictionary
    of results indexed by function.
    """
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        results = {}
        for function in function_list:
            print(f"\n* Setting up multiprocessing for: {function.__name__} ({len(data_list)} items).\n")
            results[function] = pool.map(function, data_list)
            print(f"\n* {function.__name__}: multiprocessing complete.\n")
        return(results)

def file_to_mp4(path):
    print(f"\n* Converting {path.name} to .mp4")
    try:
        call_ffmpeg(ffmpeg_args("file_to_mp4",path))
        os.remove(path)
    except Exception as E:
        print("⚠", E)

@timer
def all_to_mp4(directory = ""):
    """
    FFmpeg sometimes reports that 'requested formats are incompatible' and
    merges audio/video streams into a .mkv or .webm format instead of .mp4.
    This function prompts FFmpeg to do the conversion to .mp4 for all video
    files in a given directory.
    """
    if directory == "":
        from AWSOM_helpers import DOWNLOAD_PATH
        directory = DOWNLOAD_PATH
    else:
        directory = Path(directory)
    mkv_files = list(directory.glob('*.mkv'))
    webm_files = list(directory.glob('*.webm'))
    all_files = mkv_files + webm_files
    start_multiprocessing([file_to_mp4],all_files)

def assemble_clips(subclips,filename,preset="720"):
    os.chdir(subclip_path)
    filename=filename.replace(".mp4","["+preset+"].mp4")
    filename=final_path+"\\"+filename
    clips=[]
    for subclip in subclips:
        try:
            clips+=[VideoFileClip(subclip)]
        except OSError as error:
            pass
            #print(error)
    try:
        final_video = concatenate_videoclips(clips)
        final_video.write_videofile(filename,progress_bar=False,verbose=False)
        os.startfile(filename)
        try:
            # Kill Zombie processes
            final_video.reader.close()
            final_video.audio.reader.close_proc()
        except:
            del final_video
    except:
        print(sys.exc_info()[0])
        print("Error: previous version of video is currently open,")
        print("OR final video not created (no matching material?).")
    return
