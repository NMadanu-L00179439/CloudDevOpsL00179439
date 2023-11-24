pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/NMadanu-L00179439/CloudDevOpsL00179439.git']]])
                sh 'pwd'
                sh 'ls'
                sh '/Library/Frameworks/Python.framework/Versions/3.12/bin/pip install -r requirements.txt'
            }
        }
        stage('Build') {
            steps {
                script{
                    sh 'tar -cvf cloudDevops.tar Dockerfile app.py requirements.txt templates/home.html'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh '/Library/Frameworks/Python.framework/Versions/3.12/bin/coverage run -m pytest'
                    sh '/Library/Frameworks/Python.framework/Versions/3.12/bin/coverage report -m '
                    sh '''/Library/Frameworks/Python.framework/Versions/3.12/bin/pytest -v --junitxml=junit.xml \
                            --cov-report html --cov .
                        '''
                    }
                }
        }
        stage('Deploy') {
            steps {
                script{
                    sh 'chmod 600 ec2creationkey.pem'
                    sh 'scp -i ec2creationkey.pem -o StrictHostKeyChecking=no cloudDevops.tar ec2-user@52.212.114.97:/home/ec2-user/docker-data'
                }
            }
        }
    }
}
