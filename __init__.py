import os
class mocaText:
    def __init__(self,address=""):
        ##below part gets the valid folder path
        cur_folder=os.getwd()
        print("block Generated")
        cur_path = cur_folder+address
        assert os.path.exists(cur_path),"no valid folder occurs"
        ##
        
if __name__=="__main__":
    Instance = mocaText()
