pipeline {
    agent none
    options {
        skipDefaultCheckout(true)
    }
    stages {
        // stage ('Installing jitx') {
        //     steps {
        //         node ('slave-node01||master') {
        //             cleanWs()
        //             checkout scm
        //             // My comment
        //             sh 'pwd'
        //             sh '''
        //                 # authenticate to AWS
        //                 # launch container with a script as command
        //                 #docker build -t setup-jitx .
        //             '''
        //         }
        //     }
        // }
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
        // stage ('Load AWS credentials') {
        //     steps {
        //         node ('slave-node01||master') {
        //             cleanWs()
        //             sh '''
        //                 echo "Write .env"
        //                 echo > .env
        //                 echo "AWS_ACCESS_KEY_ID=$(grep aws_access_key_id /home/jenkins/.aws/credentials | grep -oE '[^ =]+$')"         >> .env
        //                 echo "AWS_SECRET_ACCESS_KEY=$(grep aws_secret_access_key /home/jenkins/.aws/credentials | grep -oE '[^ =]+$')" >> .env
        //                 echo "AWS_REGION=$(grep region /home/jenkins/.aws/config | grep -oE '[^ =]+$')" >> .env
        //             '''
        //             stash name: "qa-ci", useDefaultExcludes: false
        //         }
        //     }
        // }
        // stage ('Tests on Windows') {
        //     steps {
        //         node ('Windows') {
        //             // Clean before build
        //             cleanWs()
        //             checkout scm
        //             unstash name: "qa-ci"
        //             powershell 'pwd'
        //             powershell '''
        //                 Get-Content .env | ForEach-Object {
        //                     if ($_) {
        //                         $kv = $_.Split("=")
        //                         Write-Host "Setting $($kv[0])=$($kv[1])"
        //                         Set-Item -Path "Env:$($kv[0])" -Value "$($kv[1])"
        //                     }
        //                 }
        //                 Invoke-Expression -Command (Get-ECRLoginCommand).Command
        //                 docker build -t test-image-jitx .
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
                        rm -r ~/.jitx/0.11.5-rc.2/
                        ls
                        #rm ~/.jitx/current
                        #wget https://jitx-staging.s3.amazonaws.com/public/macos-catalina/jitx.zip
                        #unzip -p jitx.zip jitpcb.release/scripts/install.sh > install.sh
                        #bash install.sh jitx.zip
                        
                        wget https://jitx-staging.s3.amazonaws.com/public/macos-catalina/jitx.zip
                        unzip -p jitx.zip jitpcb.release/jitx > jitx
                        chmod +x ./jitx
                        ./jitx install-from-zip jitx.zip
                        export PATH=$PATH:~/.jitx/current/
                        jitx version

                        cp license ~/.jitx/
                        cp refresh_license ~/.jitx/
                        cp user.params ~/.jitx/
                        echo $PATH
                        export PATH=$PATH:~/.jitx/current/
                        echo $PATH
                        ls -la ~/.jitx/0.11.5-rc.2/
                        ls -la ~/.jitx/
                        jitx check-install
                        # chmod +x jitx.sh
                        # ./jitx.sh ./
                    '''
                        }
                    }
                }
    }
}
