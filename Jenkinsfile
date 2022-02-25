pipeline {
    agent none
    options {
        skipDefaultCheckout(true)
    }
    stages {
        stage ('Installing jitx') {
            steps {
                node ('slave-node01||master') {
                    cleanWs()
                    checkout scm
                    // My comment
                    sh 'pwd'
                    sh '''
                        # authenticate to AWS
                        # launch container with a script as command
                        ls
                        docker build -t setup-jitx .
                    '''
                }
            }
        }
        stage ('Tests on Ubuntu bionic') {
            steps {
                node ('slave-node01||master') {
                    // Clean before build
                    cleanWs()
                    checkout scm
                    sh 'pwd'
                    sh '''
                        ls
                        docker volume create myvol3
                        docker run -dit -v $(pwd):/myvol3 --name check-jitx setup-jitx
                        docker start check-jitx
                        docker exec check-jitx mv /myvol3/license /root/.jitx/
                        docker exec check-jitx mv /myvol3/refresh_license /root/.jitx/
                        docker exec check-jitx mv /myvol3/user.params /root/.jitx/
                        docker exec --workdir /myvol3/Importer-QA check-jitx pytest test_importer_jitx.py --html=report.html
                        docker exec --workdir /myvol3/Exporter-QA check-jitx pytest test_exporter_jitx.py --html=report.html
                        docker exec --workdir /myvol3/Roundtrip-QA check-jitx pytest test_roundtrip_jitx.py --html=report.html
                        docker exec --workdir /myvol3/JITX-QA check-jitx pytest test_jitxQA_jitx.py --html=report.html
                        docker exec --workdir /myvol3/OCDB-QA check-jitx pytest test_ocdb_jitx.py --html=report.html
                        docker exec --workdir /myvol3/Schematic-QA check-jitx pytest test_schematic_jitx.py --html=report.html
                        docker stop check-jitx
                        ls
                    '''
                }
            }
        }
    }
}
