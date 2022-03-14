pipeline {
    agent none
    options {
        skipDefaultCheckout(true)
    }
    stages {
        stage ('Running tests on several platforms'){
            parallel {
                // stage ('Tests on MacOS') {
                //     steps {
                //         node ('MacMini') {
                //             cleanWs()
                //             checkout scm
                //             sh 'pwd'
                //             // slackSend color: "good", message: "Message from Jenkins Pipeline"
                //             sh '''
                //                 ls
                //                 wget https://jitx-staging.s3.amazonaws.com/public/macos-catalina/jitx.zip
                //                 unzip -p jitx.zip jitpcb.release/scripts/install.sh > install.sh
                //                 unzip -p jitx.zip jitpcb.release/scripts/install-info.sh > install-info.sh
                //                 source install-info.sh
                //                 # Check if empty directory
                //                 current_jitx_path=~/.jitx/$JITPCB_VERSION
                //                 echo $current_jitx_path
                //                 if [ -d $current_jitx_path ]; then 
                //                     if [ -z "$(ls -A $current_jitx_path)" ]; then 
                //                         rm -r $current_jitx_path; 
                //                     fi 
                //                 fi
                //                 bash install.sh jitx.zip
                //                 cp license ~/.jitx/
                //                 cp refresh_license ~/.jitx/
                //                 cp user.params ~/.jitx/  
                //                 echo $PATH
                //                 export PATH=$PATH:~/.jitx/current/
                //                 echo $PATH
                //                 chmod +x jitx.sh
                //                 ./jitx.sh ./
                //             '''
                //         }
                //     }
                // }
                stage ('Tests on Ubuntu bionic') {
                    steps {
                        node ('slave-node01||master') {
                            // Clean before build
                            cleanWs()
                            checkout scm
                            sh 'pwd'
                            sh '''
                                ls
                                docker build . --file ./ubuntu-bionic-image.dockerfile --tag setup-jitx-bionic
                                docker rm --force test-jitx-bionic
                                docker run -dit -v $(pwd):/myvol3 --name test-jitx-bionic setup-jitx-bionic
                                docker exec --workdir /myvol3 test-jitx-bionic chmod +x jitx.sh
                                docker exec --workdir /myvol3 test-jitx-bionic ./jitx.sh ./ 
                                # docker exec --workdir /myvol3 test-jitx-bionic ./jitx.sh ./ JITX-QA
                            '''
                        }
                    }
                }
                stage ('Tests on Ubuntu xenial') {
                    steps {
                        node ('slave-node01||master') {
                            // Clean before build
                            cleanWs()
                            checkout scm
                            sh 'pwd'
                            sh '''
                                ls
                                docker build . --file ./ubuntu-xenial-image.dockerfile --tag setup-jitx-xenial
                                docker rm --force test-jitx-xenial
                                docker run -dit -v $(pwd):/myvol3 --name test-jitx-xenial setup-jitx-xenial
                                docker exec --workdir /myvol3 test-jitx-xenial chmod +x jitx.sh
                                docker exec --workdir /myvol3 test-jitx-xenial ./jitx.sh ./ 
                                # docker exec --workdir /myvol3 test-jitx-xenial ./jitx.sh ./ JITX-QA
                            '''
                        }
                    }
                }
            }
        }
    }
}