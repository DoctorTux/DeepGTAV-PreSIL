import os
from shutil import rmtree

def rename_dir(seq):
    if len(seq)==1:
        seq="0"+seq
    basedir = 'F:\Datasets\PreSIL_Dataset\\tracking'
    for f in os.listdir(basedir):
        if not os.path.isdir(os.path.join(basedir, f)):
            continue # Not a directory
        tempdir=basedir+"\\"+f
        for s in os.listdir(tempdir):
            if s=="0000":
                target=os.path.join(tempdir,"00"+seq)
                if os.path.isdir(target):
                    rmtree(target)
                os.rename(os.path.join(tempdir,s), os.path.join(tempdir, "00"+seq))

def clip_seq(seq):
    if len(seq)==1:
        seq="0"+seq
    basedir = 'F:\Datasets\PreSIL_Dataset\\tracking'
    for f in os.listdir(basedir):
        if not os.path.isdir(os.path.join(basedir, f)):
            continue # Not a directory
        tempdir=basedir+"\\"+f+"\\00"+seq
        if os.path.isdir(tempdir):
            for f in os.listdir(tempdir):
                if f.__contains__("-"):
                    os.remove(os.path.join(tempdir,f))

def clear_seq(seq):
    if len(seq)==1:
        seq="0"+seq
    basedir = 'F:\Datasets\PreSIL_Dataset\\tracking'
    for f in os.listdir(basedir):
        if not os.path.isdir(os.path.join(basedir, f)):
            continue # Not a directory
        tempdir=basedir+"\\"+f+"\\00"+seq
        if os.path.isdir(tempdir):
            rmtree(tempdir)