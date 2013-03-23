import os
import getpass

def copyDistribution(dist):
  usb = [f for f in os.listdir("/dev/disk/by-id/") if f.find("usb")!= -1 ]
  if(len(usb)!=0):
    homedir = os.environ['HOME']
    base=homedir+"/.the-gnu-distro/distribution/"+dist
    result= os.popen("udisks --show-info /dev/disk/by-id/usb*part1|grep -i 'mount paths'").read()
    target=result[result.find("/"):len(result)-1]
    for f in os.listdir(base):
		src=os.path.join(base,f)
		tgt=os.path.join(target,f)
		shutil.copy(src,tgt)
    return True
  else:
    return False
