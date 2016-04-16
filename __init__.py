from os import path,mkdir
from glob import glob
import re
class mocaText:
    def __init__(self,address="/data"):
        ##below part gets the valid folder path
        cur_folder=""
        print("block Generated")
        cur_path = cur_folder+address
        assert path.exists(cur_path),"no valid folder occurs"
        ##get file names
        self.files = sorted(glob(address+"/*.txt"))
        self.cleanFiles()
    def cleanFiles(self):
        for item in self.files:
            f_open=open(item,'r')
            lines=self.findLines(f_open)
            print(lines)
            f_open.close()

    def findLines(self,f_handle):
        lines=[]
        flag=False
        interviewID=""
        for line in f_handle:
            if line.find("tell me about")!=-1:
                flag=True
                semiconIndex=line.find(':')
                interviewID=line[:semiconIndex]
            elif line.find("this final passage for you to read")!=-1 or line.find("read this passage")!=-1:
                flag=False
            else:
                pass
            if not flag:
                continue
            else:
                if not line.strip() or line.startswith(interviewID):
                    pass
                else:
                    lines.append(line)
        return lines





if __name__=="__main__":
    absAddress="/Users/shuai_mac/Pycharm/MeganNZ/Original_data"
    Instance = mocaText(address=absAddress)
    Instance.cleanFiles()
