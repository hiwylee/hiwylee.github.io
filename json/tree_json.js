function getTreeJson ()
{
 var json_data =
  [
        { "id" : "root",        "parent" : "#",    "text" : "문서 공유 홈" },
        { "id" : "level_1_01",  "parent" : "root", "text" : "00_솔루션 Overview" },
        { "id" : "level_1_02",  "parent" : "root", "text" : "01_고객별 지원 자료" },
        { "id" : "level_1_03",  "parent" : "root", "text" : "02_이벤트 지원 자료" },
        { "id" : "level_1_04",  "parent" : "root", "text" : "03_교육 자료" },
        { "id" : "level_1_05",  "parent" : "root", "text" : "04_팀세미나" },
        { "id" : "level_1_06",  "parent" : "root", "text" : "05._고객사례" },
        { "id" : "level_1_09",  "parent" : "root", "text" : "01_고객별 지원 자료" },
        { "id" : "level_2_02_01", "parent" : "level_1_02", "text" : "김민수_대교CNS_OCI_ATP" },
        { "id" : "level_2_02_02", "parent" : "level_1_02", "text" : "김민수_태성에스엔이_OCI_HPC" },
  ];    // code to be executed
   return json_data;
};
