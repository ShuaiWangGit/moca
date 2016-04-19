from os import path,mkdir
from glob import glob
import re
import tools
class mocaText:
    def __init__(self,address="/data"):
        ##below part gets the valid folder path
        cur_folder=""
        print("block Generated")
        cur_path = cur_folder+address
        assert path.exists(cur_path),"no valid folder occurs"
        ##get file names
        #self.fillers=["umm","mmm","uh"]
        self.files = sorted(glob(address+"/*.txt"))
        self.cleanFiles()
    def cleanFiles(self):
        for item in self.files:
            location=item.rfind('/')
            formatLocation=item.rfind('.txt')
            subjectID=item[(location+1):formatLocation]
            print (subjectID)
            f_open=open(item,'r')
            lines=self.findLines(f_open)
            #clean those lines to write to the text later
            cleanLines=self.cleanLine(lines,subjectID)
            if not cleanLines:
                f_open.close()
            else:
                tools.write_to_txt(cleanLines,subjectID,'./','processed')
                f_open.close()
    def cleanLine(self,lineList,ID):
        clean_list=[]
        ID = ID+":"
        for line in lineList:
            line=line.replace(ID,"")
            line = line.strip()
            clean_list.append(self.removeAnnotation(line))
        return clean_list
    def removeAnnotation(self,oneLine):
        final_line = re.sub('\w+\~|\<.*?\>', " ", oneLine)
        final_line = re.sub('[-_]'," ",final_line)
        return final_line
    def getFillerOneLine(line):
        count = 0
        for filler in self.fillers:
            count = count + len(re.findall(filler,line))
        return count
    def getFillerTotal():
        count = 0
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
    absAddress="./Original_data"
    Instance = mocaText(address=absAddress)
    Instance.cleanFiles()
