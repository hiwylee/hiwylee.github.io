package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
	"strconv"
	"strings"
	"time"
)

const pub_folder string = "https://securesites-prodapp.cec.ocp.oraclecloud.com/documents/folder"
const root_folder string = "https://securesites-prodapp.cec.ocp.oraclecloud.com/documents/folder/F77790F8151A323321386D76F6C3FF17C1177E4725F3"
const pub_file string = ""
const root_id string = "F77790F8151A323321386D76F6C3FF17C1177E4725F3"

var folder_id = map[string]string{
	"00_솔루션 Overview":                           "F55D8DA7DF37C8A5A5239951F6C3FF17C1177E4725F3",
	"01_고객별 지원 자료":                              "F3027F04EA4A5BAA23D289DDF6C3FF17C1177E4725F3",
	"02_이벤트 지원 자료":                              "F77790F8151A323321386D76F6C3FF17C1177E4725F3",
	"03_교육 자료":                                  "FF8C2CAA8A0E15DCBAD194BF0F6C3FF17C1177E4725F3",
	"04_팀세미나":                                   "F105B2C240D41BE0CDA4BE32F6C3FF17C1177E4725F3",
	"05_고객사례":                                   "F5069FE589FA93E0467A043DF6C3FF17C1177E4725F3",
	"06_기술가이드":                                  "FEEB80D22275F399210DDDE3F6C3FF17C1177E4725F3",
	"09_기타":                                     "F23463E84CECF98D4AA647C8F6C3FF17C1177E4725F3",
	"ODP TECH KOREA SALES ASSET (Heejung Jang)": "FD0DAF378141B9D40789753FF6C3FF17C1177E4725F3",
	"SC_ASSET (Myeongjin Lee)":                  "F27E95CB2754593C2052183EF6C3FF17C1177E4725F3",
	"SC_ASSET_TECH (SJ Han)":                    "F71F8F8C75282B0D29A2E955F6C3FF17C1177E4725F3",
	"SC_ASSET_TECH_2020 (Haje Kim)":             "F77790F8151A323321386D76F6C3FF17C1177E4725F3",
}

var parent_id = map[string]string{
	"ODP TECH KOREA SALES ASSET (Heejung Jang)": "FD0DAF378141B9D40789753FF6C3FF17C1177E4725F3",
	"SC_ASSET (Myeongjin Lee)":                  "F27E95CB2754593C2052183EF6C3FF17C1177E4725F3",
	"SC_ASSET_TECH (SJ Han)":                    "F71F8F8C75282B0D29A2E955F6C3FF17C1177E4725F3",
	"SC_ASSET_TECH_2020 (Haje Kim)":             "F77790F8151A323321386D76F6C3FF17C1177E4725F3",
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func Is_valid_folder(name string) bool {
	switch name {
	case
		"Bigdata Team",
		"00.고려해운 제안 폴더 (KwangSik Jeong)",
		"Workspace",
		".tmp",
		"01.계양전기 (KwangSik Jeong)",
		"외부공유",
		"Shared-Folder Website Confidential Files (peo-scs-troubleshooter_ww peo-scs-troubleshooter_ww)":
		return false
	}
	return true
}

func Is_valid_file(name string) bool {
	switch name {
	case
		"gen_v6.py",
		"gen_v5.py",
		"JTree-WIP2.html",
		"desktop.ini",
		"JTree_Candidate.html",
		"main.exe",
		"tree_json.js",
		"tree_json2.js",
		"main.go":

		return false
	}
	return true
}

func scan_dir(dir string, pid string, parent_url string, f io.Writer) {
	files, err := ioutil.ReadDir(dir)
	if err != nil {
		log.Fatal(err)
	}

	// filepath.Join("dir1//", "filename")
	var name, path, my_id, tmp_purl, my_fold_id string
	var seq int = 0
	var id_exists bool = false
	for _, file := range files {
		name = file.Name()
		path = filepath.Join(dir, name)
		if file.IsDir() && !Is_valid_folder(name) {
			//fmt.Println("DIR : " + file.Name())
			continue
		}
		if !file.IsDir() && !Is_valid_file(name) {
			//fmt.Println("FILE: " + file.Name())
			continue
		}

		seq += 1
		if pid == "#" {
			my_id = "lvl_" + strconv.Itoa(seq)
		} else {
			my_id = pid + "_" + strconv.Itoa(seq)
		}
		if file.IsDir() {
			my_fold_id, id_exists = get_folder_id(name)
			tmp_purl = ""

			if id_exists {
				tmp_purl = pub_folder + "/" + my_fold_id + "/_" + strings.Replace(name, " ", "_", -1)
			} else {
				tmp_purl = root_folder
			}
			fmt.Fprintf(f, `      { "id" : "`+my_id+`",  "parent" : "`+pid+`", "text" : "`+name+`" ,"a_attr" : {"href":"`+tmp_purl+`"}},`)
			fmt.Fprintln(f,"")
			scan_dir(path, my_id, tmp_purl, f)

		} else {
			fmt.Fprintf(f, `      { "id" : "`+my_id+`",  "parent" : "`+pid+`", "text" : "`+name+`" ,"icon":"jstree-file","a_attr" : {"href":"` + parent_url + `"}},`)
			fmt.Fprintln(f,"")
		}
	}
}

func get_folder_id(name string) (string, bool) {
	val, exists := folder_id[name]
	return val, exists
}

func say(s string) {
	for i := 0; i < 10; i++ {
		fmt.Println(s, "***", i)
	}
}

func main() {

	if len(os.Args) != 3 {
		fmt.Printf("usage : %s  [root_dir] [output] ", os.Args[0])
		os.Exit(3)
	}
	file_path := os.Args[1]
	file_name := os.Args[2]

	// f, err := os.Create(file_name,"w+")
	f, err := os.OpenFile(file_name, os.O_RDWR|os.O_CREATE|os.O_TRUNC, 0666)
	// w := bufio.NewWriter(file)
	check(err)
	defer f.Close()

	fmt.Fprintln(f,"// Generated Time : ", time.Now().Format("2006-01-02 15:04:05"))
	fmt.Fprintln(f, "function getTreeJson ()")
	fmt.Fprintln(f, "{")
	fmt.Fprintln(f, "var json_data =")
	fmt.Fprintln(f, "   [\n")
	scan_dir(file_path, "#", root_folder, f)
	fmt.Fprintln(f, "   ];")
	fmt.Fprintln(f, "")
	fmt.Fprintln(f, "return json_data;")
	fmt.Fprintln(f, "};\n")

}
