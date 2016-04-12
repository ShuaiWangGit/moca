from os import path,mkdir
def write_to_txt(string_list,id,folder_address,sub_name):
    directoryPath=folder_address+sub_name# ]
    if not path.exists(directoryPath):
        mkdir(directoryPath)
    order=0
    full_file_name=directoryPath+id+'_'+str(order)+'_processed.txt'
    while path.isfile(full_file_name):
        order+=1
        full_file_name=directoryPath+id+'_'+str(order)+'_processed.txt'
    f=open(full_file_name,'w')
    l1=map(lambda x:x+'\n', string_list)
    f.writelines(l1)
    f.close()
def cleanFiles():
	pass