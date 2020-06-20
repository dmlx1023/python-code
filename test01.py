import os
import shutil
import random
base_path='E:\\xxx\\38499'
dst_path='E:\\xxx\\36666\\video'
for fpathe,dirs,fs in os.walk(base_path):
  for f in fs:
    # print( os.path.splitext(f)[1])
    if (os.path.splitext(f)[1]=='.mp4'):
        print(os.path.join(fpathe,f))
        os.rename(os.path.join(fpathe,f),os.path.join(dst_path,str(random.randint(10,10000))+'.mp4'))
        # shutil.move(os.path.join(fpathe,f),'E:\\xxx\\36666\\video')