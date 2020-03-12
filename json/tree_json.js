
function getTreeJson ()
{
 var json_data =
  [
        { "id" : "ajson1", "parent" : "#", "text" : "Simple root node" },
        { "id" : "ajson2", "parent" : "#", "text" : "Root node 2" },
        { "id" : "ajson3", "parent" : "ajson2", "text" : "Child 1" },
        { "id" : "ajson4", "parent" : "ajson2", "text" : "Child 2" },
  ];    // code to be executed
   rerurn json_data;
};
    var tree_json2 = 
    [
          { "id" : "ajson1", "parent" : "#", "text" : "Simple root node" },
          { "id" : "ajson2", "parent" : "#", "text" : "Root node 2" },
          { "id" : "ajson3", "parent" : "ajson2", "text" : "Child 1" },
          { "id" : "ajson4", "parent" : "ajson2", "text" : "Child 2" },
    ];

    function getTreeJson2()   
    {
        return tree_json2;
    }

function a(){
 alert("aaa");
}
