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
                        docker rm --force test-jitx
                        docker volume create myvol3
                        docker run -dit -v $(pwd):/myvol3 --name test-jitx setup-jitx
                        docker start test-jitx
                        docker exec test-jitx mv /myvol3/machine-id /etc/
                        docker exec test-jitx mv /myvol3/license /root/.jitx/
                        docker exec test-jitx mv /myvol3/refresh_license /root/.jitx/
                        docker exec test-jitx mv /myvol3/user.params /root/.jitx/
                        docker exec --workdir /myvol3/Exporter-QA test-jitx pytest test_exporter_jitx.py --html=report.html || true
                        docker exec --workdir /myvol3/JITX-QA test-jitx pytest test_jitxQA_jitx.py --html=report.html || true
                        docker exec --workdir /myvol3/OCDB-QA test-jitx pytest test_ocdb_jitx.py --html=report.html
                        docker stop test-jitx
                        ls
                    '''
                }
            }
        }
    }
}
