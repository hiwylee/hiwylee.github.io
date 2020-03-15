import os

'''
def tree_printer(root):
    level = 1;
    for root, dirs, files in os.walk(root):
        for d in dirs:
            print ('Dir Level %d : %s : '%(level, os.path.join(root, d))    
        for f in files:
            print ('File Level %d : %s  : '%(level, os.path.join(root, f))    
        level += 1
 '''
def tree_printer(root):
    level = 1;
    parnet_id = '#';
    my_id = 'lvl'
    depth = 0
    for root, dirs, files in os.walk(root):
        depth = 0
        parnet_id = my_id 
        if depth == 0 :
            parnet_id = '#'
            
        cnt = 0
        for d in dirs:
            if depth == 0 :
                my_id = 'lvl' + '_' + str(cnt);
            else:
                my_id = parnet_id + '_' + str(cnt);
            cnt += 1
            print ("Dir pid [{}], my_id [{}] : {}".format(parnet_id, my_id, os.path.join(root, d)))
#        for f in files:
#            print (os.path.join(root, f))
        level += 1        
        depth += 1
pub_folder = 'https://publicdocs-corp.documents.us2.oraclecloud.com/documents/folder/F77790F8151A323321386D76F6C3FF17C1177E4725F3'
pub_file = ''
from urllib import parse

def scan_dir(dir, pid, parent_url):
    
    seq = 0
    my_id = ''
    for name in os.listdir(dir):
            
        path = os.path.join(dir, name)
        if os.path.isfile(path) and name  in ["JTree-WIP2.html", "desktop.ini"]:   
            continue
        my_folder = path[2:]
        
        seq += 1
        if pid == "#" :
            my_id = "lvl_" + str(seq)
        else :
            my_id = pid +"_" + str(seq)

        if os.path.isdir(path):    
            #print ('{ "id" : "'  + my_id + '",  "parent" : "' + pid+ '", "text" : "' + name + '" ,"a_attr" : {"href":"' + pub_folder + '/' + parse.quote(my_folder.replace("\\","/"), )+ '"}},')            
            
            print ('{ "id" : "'  + my_id + '",  "parent" : "' + pid+ '", "text" : "' + name + '" ,"a_attr" : {"href":"' + pub_folder + '/' + my_folder.replace("\\","/")+ '"}},')            
            tmp_purl = pub_folder + '/' + my_folder.replace("\\","/")
            scan_dir(path, my_id,tmp_purl)
        else:
            my_path , my_file = os.path.split(path)
            my_path = my_path[2:]
            #print ('{ "id" : "'  + my_id + '",  "parent" : "' + pid+ '", "text" : "' + name + '" ,"icon":"glyphicon glyphicon-leaf","a_attr" : {"href":"' + pub_folder + '/' + parse.quote(my_path.replace("\\","/"), )+ '"}},')
            print ('{ "id" : "'  + my_id + '",  "parent" : "' + pid+ '", "text" : "' + name + '" ,"icon":"glyphicon glyphicon-leaf","a_attr" : {"href":"' + parent_url + '"}},')
                
  
import sys
if __name__=="__main__":
    # tree_printer('../..')
    if len(sys.argv) != 2:
        print("Insufficient arguments")
        sys.exit()
    file_path = sys.argv[1]

    scan_dir(file_path, "#", pub_folder)