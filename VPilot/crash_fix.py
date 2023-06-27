import os
from file_manage import clip_seq
from shutil import rmtree, copy

def crash_fix(seq):
    clip_seq("0")
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
            if s=="0099":
                target=os.path.join(tempdir,"00"+seq)
                seqdir=os.path.join(tempdir,"0099")
                for f in os.listdir(seqdir):
                    os.chdir(seqdir)
                    filename=f.split('.')
                    newfilename='{0:06d}'.format(int(filename[0])+500)+'.'+filename[1]
                    os.rename(f,newfilename)
                    copy(os.path.join(seqdir,newfilename),target)
def forgot_99():
    basedir = 'F:\Datasets\PreSIL_Dataset\\tracking'
    for f in os.listdir(basedir):
        if not os.path.isdir(os.path.join(basedir, f)):
            continue # Not a directory
        tempdir=basedir+"\\"+f
        for s in os.listdir(tempdir):
            if s=="0099":
                seqdir=os.path.join(tempdir,"0099")
                for f in os.listdir(seqdir):
                    os.chdir(seqdir)
                    filename=f.split('.')
                    if int(filename[0])>499:
                        os.remove(f)
forgot=False
if forgot==False:
    seq=input("Sequence? ")
    crash_fix(seq)
else:
    forgot_99()