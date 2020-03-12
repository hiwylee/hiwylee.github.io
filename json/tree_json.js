function getTreeJson ()
{
 var json_data =
  [
        { "id" : "root",        "parent" : "#",    "text" : "문서 공유 홈" },
        { "id" : "level_1_01",  "parent" : "root", "text" : "00_솔루션 Overview" , "a_attr" : {"href":"https://publicdocs-corp.documents.us2.oraclecloud.com/documents/folder/F55D8DA7DF37C8A5A5239951F6C3FF17C1177E4725F3/_00_%EC%86%94%EB%A3%A8%EC%85%98_Overview"} },
        { "id" : "level_1_02",  "parent" : "root", "text" : "01_고객별 지원 자료" ,  "a_attr" : {"href":"https://publicdocs-corp.documents.us2.oraclecloud.com/documents/folder/F3027F04EA4A5BAA23D289DDF6C3FF17C1177E4725F3/_01_%EA%B3%A0%EA%B0%9D%EB%B3%84_%EC%A7%80%EC%9B%90_%EC%9E%90%EB%A3%8C"} },
        { "id" : "level_1_03",  "parent" : "root", "text" : "02_이벤트 지원 자료" ,  "a_attr" : {"href":"https://publicdocs-corp.documents.us2.oraclecloud.com/documents/folder/F77790F8151A323321386D76F6C3FF17C1177E4725F3/_02_%EC%9D%B4%EB%B2%A4%ED%8A%B8_%EC%A7%80%EC%9B%90_%EC%9E%90%EB%A3%8C"} },
        { "id" : "level_1_04",  "parent" : "root", "text" : "03_교육 자료" ,        "a_attr" : {"href":"https://publicdocs-corp.documents.us2.oraclecloud.com/documents/folder/F8C2CAA8A0E15DCBAD194BF0F6C3FF17C1177E4725F3/_03_%EA%B5%90%EC%9C%A1_%EC%9E%90%EB%A3%8C"} },
        { "id" : "level_1_05",  "parent" : "root", "text" : "04_팀세미나" ,         "a_attr" : {"href":"https://publicdocs-corp.documents.us2.oraclecloud.com/documents/folder/F105B2C240D41BE0CDA4BE32F6C3FF17C1177E4725F3/_04_%ED%8C%80%EC%84%B8%EB%AF%B8%EB%82%98"} },
        { "id" : "level_1_06",  "parent" : "root", "text" : "05._고객사례" ,        "a_attr" : {"href":"https://publicdocs-corp.documents.us2.oraclecloud.com/documents/folder/F5069FE589FA93E0467A043DF6C3FF17C1177E4725F3/_05._%EA%B3%A0%EA%B0%9D%EC%82%AC%EB%A1%80"} },
        { "id" : "level_1_09",  "parent" : "root", "text" : "06_기술가이드" ,        "a_attr" : {"href":"https://publicdocs-corp.documents.us2.oraclecloud.com/documents/folder/FEEB80D22275F399210DDDE3F6C3FF17C1177E4725F3/_06_%EA%B8%B0%EC%88%A0%EA%B0%80%EC%9D%B4%EB%93%9C"} },        
        { "id" : "level_1_09",  "parent" : "root", "text" : "09_기타" ,             "a_attr" : {"href":"https://publicdocs-corp.documents.us2.oraclecloud.com/documents/folder/F23463E84CECF98D4AA647C8F6C3FF17C1177E4725F3/_09_%EA%B8%B0%ED%83%80"}},                                                                                      
        { "id" : "level_2_02_01", "parent" : "level_1_02", "text" : "김민수_대교CNS_OCI_ATP" , "a_attr" : {"href":"https://publicdocs-corp.documents.us2.oraclecloud.com/documents/folder/F695F5AE79798476EDA4E633F6C3FF17C1177E4725F3/_%EA%B9%80%EB%AF%BC%EC%88%98_%EB%8C%80%EA%B5%90CNS_OCI_ATP"} },
        { "id" : "level_2_02_01_01", "parent" : "level_2_02_01", "text" : "오라클클라우드인프라소개_대교CNS_202001.pptx" , "li_attr": {"icon":"glyphicon glyphicon-leaf"}, "a_attr" : {"href":"https://publicdocs-corp.documents.us2.oraclecloud.com/documents/folder/F695F5AE79798476EDA4E633F6C3FF17C1177E4725F3/_%EA%B9%80%EB%AF%BC%EC%88%98_%EB%8C%80%EA%B5%90CNS_OCI_ATP"} },
        { "id" : "level_2_02_02", "parent" : "level_1_02", "text" : "김민수_태성에스엔이_OCI_HPC" , "li_attr": {"icon":"glyphicon glyphicon-leaf"}, "a_attr" : {"href":"https://publicdocs-corp.documents.us2.oraclecloud.com/documents/folder/FDE5F71B2838194FF68EEED5F6C3FF17C1177E4725F3/_%EA%B9%80%EB%AF%BC%EC%88%98_%ED%83%9C%EC%84%B1%EC%97%90%EC%8A%A4%EC%97%94%EC%9D%B4_OCI_HPC"} },
  ];    // code to be executed
  return json_data;
};
