from os import path,mkdir
from glob import glob

class mocaText:
    def __init__(self,address="/data"):
        ##below part gets the valid folder path
        cur_folder=""
        print("block Generated")
        cur_path = cur_folder+address
        assert path.exists(cur_path),"no valid folder occurs"
        ##get file names
        files = sorted(glob(address+"/*.txt"))
        cleanFiles(files)


if __name__=="__main__":
    absAddress="/Users/shuai_mac/Pycharm/MeganNZ/Original_data"
    Instance = mocaText(address=absAddress)

