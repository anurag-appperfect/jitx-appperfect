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
                        docker build -t jitx-image .
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
                        #docker rm --force test-jitx
                        docker volume create myvol3
                        docker run -dit -v $(pwd):/myvol3 --name test-jitx jitx-image
                        docker exec --workdir /myvol3 test-jitx chmod +x jitx.sh
                        docker exec test-jitx ls root/.jitx/
                        # docker exec --workdir /myvol3 test-jitx ./jitx.sh ./ 
                        # docker exec --workdir /myvol3 test-jitx ./jitx.sh ./ JITX-QA
                    '''
                }
            }
        }
    }
}
