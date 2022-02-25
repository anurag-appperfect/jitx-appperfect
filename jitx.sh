# This script is to execute the automated pytest test cases

usage() {
    echo "This script is to execute the automated pytest test cases"
    echo "usage: $0 test_case_dir_path test_case_dir_name"
    echo "arguments:"
    echo "  test_case_dir_path - path to the directory where all the test case folders are present"
    echo "  test_case_dir_name - (optional) To run the test cases in a particular directory"
    echo "  e.g:"
    echo "     $0 /myvol/qa/"
    echo "     $0 /myvol/qa/ Exporter-QA"
    echo "     $0 /myvol/qa/ Importer-QA"
    echo "     $0 /myvol/qa/ JITX-QA"
    echo "     $0 /myvol/qa/ OCDB-QA"
    echo "     $0 /myvol/qa/ Roundtrip-QA"
    echo "     $0 /myvol/qa/ Schematic-QA"
    exit 1
}

# Script Validation
if [[ $# -ne 1 && $# -ne 2 ]]; then
    echo "Invalid number of arguments"
    usage
fi

# Executing the test cases 
if [ $# -eq 1 ]; then
    dir_path="$1""Exporter-QA"
    cd $dir_path
    pytest test_exporter_jitx.py --html=Exporter_report.html
    cd ../Importer-QA
    pytest test_importer_jitx.py --html=Importer_report.html
    cd ../JITX-QA
    pytest test_jitxqa_jitx.py --html=JITX_report.html
    cd ../OCDB-QA
    pytest test_ocdb_jitx.py --html=OCDB_report.html
    cd ../Roundtrip-QA
    pytest test_roundtrip_jitx.py --html=Roundtrip_report.html
    cd ../Schematic-QA
    pytest test_schematic_jitx.py  --html=Schematic_report.html
else
    option="${2}" 
    case ${option} in 
        "Exporter-QA") dir_path="$1""Exporter-QA" 
            cd $dir_path
            pytest test_exporter_jitx.py --html=Exporter_report.html
            ;; 
        "Importer-QA") dir_path="$1""Importer-QA" 
            cd $dir_path
            pytest test_importer_jitx.py --html=Importer_report.html
            ;; 
        "JITX-QA") dir_path="$1""JITX-QA"
            cd $dir_path
            pytest test_jitxqa_jitx.py --html=JITX_report.html
            ;;
        "OCDB-QA") dir_path="$1""OCDB-QA"
            cd $dir_path
            pytest test_ocdb_jitx.py --html=OCDB_report.html
            ;;
        "Roundtrip-QA") dir_path="$1""Roundtrip-QA"
            cd $dir_path
            pytest test_roundtrip_jitx.py --html=Roundtrip_report.html
            ;;
        "Schematic-QA") dir_path="$1""Schematic-QA"
            cd $dir_path
            pytest test_schematic_jitx.py --html=Schematic_report.html
            ;;
        *)
            echo "Invalid directory name"
            usage
    esac 
fi
