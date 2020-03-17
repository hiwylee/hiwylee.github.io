import os


# pub_foler 뒤에 계층구조에 상관 없이 현재 폴더(_가 추가됨) 만 표시
# folder 마다 id 가 다름.
# 이름에 스페이스가 있으면 '_' 로 대체됨
# base/lvl1/lvl2 가 아니라 base/_lvl2 로 표시됨
from urllib import parse
pub_folder = 'https://publicdocs-corp.documents.us2.oraclecloud.com/documents/folder'
root_folder = 'https://publicdocs-corp.documents.us2.oraclecloud.com/documents/folder/F77790F8151A323321386D76F6C3FF17C1177E4725F3'
pub_file = ''
root_id='F77790F8151A323321386D76F6C3FF17C1177E4725F3'
folder_id = {
    "00_솔루션 Overview": "F55D8DA7DF37C8A5A5239951F6C3FF17C1177E4725F3",
    "01_고객별 지원 자료": "F3027F04EA4A5BAA23D289DDF6C3FF17C1177E4725F3",
    "02_이벤트 지원 자료": "F77790F8151A323321386D76F6C3FF17C1177E4725F3",
    "03_교육 자료": "FF8C2CAA8A0E15DCBAD194BF0F6C3FF17C1177E4725F3",
    "04_팀세미나": "F105B2C240D41BE0CDA4BE32F6C3FF17C1177E4725F3",
    "05_고객사례": "F5069FE589FA93E0467A043DF6C3FF17C1177E4725F3",
    "06_기술가이드": "FEEB80D22275F399210DDDE3F6C3FF17C1177E4725F3",
    "09_기타"     : "F23463E84CECF98D4AA647C8F6C3FF17C1177E4725F3",
 }

def get_folder_id(name) :
    # print('{} {}'.format(name,folder_id.get(name)))
    if name in folder_id :        
        return folder_id.get(name), True
    else :
        return root_id, False

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
        #
        #  폴더별로 아이디가 서로 다르게 할당 되어 있어 있음.
        #
        if os.path.isdir(path):    
            my_fold_id, id_exists  = get_folder_id(name)
            tmp_purl = ''
            
            if id_exists :
                tmp_purl = pub_folder + '/' + my_fold_id + '/_' + parse.quote(name.replace(' ', '_'))
            else:  # root folder 
                tmp_purl = root_folder
            # print ('{ "id" : "'  + my_id + '",  "parent" : "' + pid+ '", "text" : "' + name + '" ,"a_attr" : {"href":"' + tmp_purl + '"}},')            
            # scan_dir(path, my_id,tmp_purl)
            print ('{ "id" : "'  + my_id + '",  "parent" : "' + pid+ '", "text" : "' + name + '" ,"a_attr" : {"href":"' + tmp_purl + '"}},') 
            #print ('#################  : {} {} {}'.format(my_fold_id, id_exists, tmp_purl))
            scan_dir(path, my_id,tmp_purl)
        else:
            # my_path , my_file = os.path.split(path)
            # my_path = my_path[2:]
            # print ('{ "id" : "'  + my_id + '",  "parent" : "' + pid+ '", "text" : "' + name + '" ,"icon":"glyphicon glyphicon-leaf","a_attr" : {"href":"' + parent_url + '"}},')
            print ('{ "id" : "'  + my_id + '",  "parent" : "' + pid+ '", "text" : "' + name + '" ,"icon":"jstree-file","a_attr" : {"href":"' + parent_url + '"}},')
     
import sys
if __name__=="__main__":
    # tree_printer('../..')
    if len(sys.argv) != 2:
        print("Insufficient arguments: python gen.py dir")
        sys.exit()
    file_path = sys.argv[1]

    scan_dir(file_path, "#", root_folder)
