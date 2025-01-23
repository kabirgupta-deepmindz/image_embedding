pipeline {
    agent any

    tools {
        nodejs "node"
    }

    environment {
        ARCHIVE_NAME = 'image.tar.gz'
        FOLDER_NAME = 'curry/image'
        DEMO_SERVER = 'demo.pharynxai.com'
    }
 
    stages {
        stage('Environment') {
            steps {
                echo "Deploy User: ${env.UBUNTU_USER}"
                echo "Deploy Server: ${env.DEMO_SERVER}"
                echo "Deploy Path: ${env.DEPLOY_PATH}"
                echo "DEMO_SERVER: ${env.DEMO_SERVER}"
            }
        }

        stage('Archive Code') {
            steps {
                script {
                    sh """
                        tar -czvf ${env.ARCHIVE_NAME} .[!.]* * 
                        echo "Successfully created archive ${env.ARCHIVE_NAME}"
                    """
                }
            }
        }
 
        stage('Deploy to EC2') {
            steps {
                script {
                        sh """
                            scp ${env.ARCHIVE_NAME} ${env.UBUNTU_USER}@${env.DEMO_SERVER}:${env.DEPLOY_PATH}/${env.DEMO_SERVER}/
                            echo "Successfully copied archive to server"
 
                            ssh ${env.UBUNTU_USER}@${env.DEMO_SERVER} '
                                cd ${env.DEPLOY_PATH}/${env.DEMO_SERVER}/ &&
                                tar -xzf ${env.ARCHIVE_NAME} -C ${env.FOLDER_NAME} &&
                                rm ${env.ARCHIVE_NAME} &&
                                echo "Successfully extracted archive on server"
                            '
                        """
                }
            }
        }
 
        stage('Start Application') {
            steps {
                script {
                        sh """
                            ssh ${env.UBUNTU_USER}@${env.DEMO_SERVER} '
                                source ~/.nvm/nvm.sh &&
                                cd ${env.DEPLOY_PATH}/${env.DEMO_SERVER}/${env.FOLDER_NAME}/ &&
                                chmod +x start.sh &&
                                chmod 777 start.sh &&
                                ./start.sh
                            '
                        """
                }
            }
        }
    }
 
    post {
        always {
            // Clean up local archive
            sh "rm -f ${env.ARCHIVE_NAME}"
        }
    }
}