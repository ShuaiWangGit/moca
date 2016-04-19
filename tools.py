from os import path,mkdir,remove
def write_to_txt(string_list,id,folder_address,sub_name):
    directoryPath=folder_address+sub_name
    if not path.exists(directoryPath):
        mkdir(directoryPath)
    else:
        pass
    order=0
    full_file_name=directoryPath+'/'+id+'_'+str(order)+'_processed.txt'
    if path.exists(full_file_name):
        remove(full_file_name)
    else:
        pass
    #while path.isfile(full_file_name):
     #   order+=1
      #  full_file_name=directoryPath+'/'+id+'_'+str(order)+'_processed.txt'
    f=open(full_file_name,'w')
    l1=map(lambda x:x+'\n', string_list)
    f.writelines(l1)
    f.close()