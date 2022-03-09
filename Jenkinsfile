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
                        # docker build -t setup-jitx .
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
        // stage ('Tests on Windows') {
        //     steps {
        //         node ('Windows') {
        //             // Clean before build
        //             cleanWs()
        //             checkout scm
        //             powershell 'pwd'
        //             powershell '''
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
                        #echo $JITPCB_VERSION
                        # Check if empty directory
                        dir_path="$(pwd)"
                        cd $HOME/.jitx/
                        ls -la
                        ls -la current/
                        current_jitx_path="$(readlink "current")"
                        echo $current_jitx_path
                        if [ -d $current_jitx_path ]; then 
                            if [ -z "$(ls -A $current_jitx_path)" ]; then 
                                rm -r $current_jitx_path; 
                            fi 
                        fi               
                        cd $dir_path          
                        wget https://jitx-staging.s3.amazonaws.com/public/macos-catalina/jitx.zip
                        unzip -p jitx.zip jitpcb.release/scripts/install.sh > install.sh
                        #cat install.sh
                        bash install.sh jitx.zip
                        cp license ~/.jitx/
                        cp refresh_license ~/.jitx/
                        cp user.params ~/.jitx/  
                        echo $PATH
                        export PATH=$PATH:~/.jitx/current/
                        ls -a ~/.jitx/0.11.5-rc.2
                        echo $PATH
                        ls ~/.jitx/
                        ls ~/.jitx/current/
                        chmod +x jitx.sh
                        ./jitx.sh ./
                    '''
                        }
                    }
                }
    }
}
