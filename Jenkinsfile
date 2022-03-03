pipeline {
    agent none
    options {
        skipDefaultCheckout(true)
    }
    stages {
        stage ('Installing jitx') {
            steps {
                node ('MacMini') {
                    cleanWs()
                    checkout scm
                    // My comment
                    sh 'pwd'
                    sh '''
                        # authenticate to AWS
                        # launch container with a script as command
                        #docker build -t setup-jitx .
                    '''
                }
            }
        }
        // stage ('Tests on Ubuntu bionic') {
        //     steps {
        //         node ('slave-node01||master') {
        //             // Clean before build
        //             cleanWs()
        //             checkout scm
        //             sh 'pwd'
        //             sh '''
        //                 docker rm --force test-jitx
        //                 docker run -dit -v $(pwd):/myvol3 --name test-jitx setup-jitx
        //                 docker exec --workdir /myvol3 test-jitx chmod +x jitx.sh
        //                 docker exec --workdir /myvol3 test-jitx ./jitx.sh ./ 
        //                 # docker exec --workdir /myvol3 test-jitx ./jitx.sh ./ JITX-QA
        //             '''
        //         }
        //     }
        // }
        stage ('Tests on MacOS') {
            steps {
                node ('MacMini') {
                    cleanWs()
                    checkout scm
                    sh 'pwd'
                    sh '''
                        ls
                        #echo "installing pip, pytest using $($PYTHON_ALIAS --version)"
                        #curl https://bootstrap.pypa.io/pip/3.6/get-pip.py | $PYTHON_ALIAS
                        #pip3 install pytest
                        #pip3 install pytest-html
                        #pip install pytest --user
                        #pip install pytest-html --user
                        #/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
                        #brew install wget
                        #wget https://jitx-staging.s3.amazonaws.com/public/ubuntu-bionic/jitx.zip
                        #unzip -p jitx.zip jitpcb.release/scripts/install.sh > install.sh
                        #bash install.sh jitx.zip
                        echo $PATH
                        ls -a ~/
                        echo "~/.jitx/current/" > ~/.bash_profile
                        cat ~/.bash_profile
                        ls ~/.jitx/current
                        ~/.jitx/current/jitx check-install
                        echo $PATH
                        jitx check-install
                        #export PATH=$PATH:~/.jitx/current/
                        #echo $PATH
                        #chmod +x jitx.sh
                        #./jitx.sh ./ JITX-QA
                        #echo $PATH
                    '''
                        }
                    }
                }
    }
}
