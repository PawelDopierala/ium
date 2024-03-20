pipeline {
    agent any

    stages {
        stage('Stage 1') {
            steps {
                echo 'Hello world!'
                checkout scm
                sh './data_processing.sh'
                archiveArtifacts artifacts: './*'
            }
        }
    }
}