pipeline {
    agent any

    stages {
        stage('Stage 1') {
            steps {
                git url: "https://git.wmi.amu.edu.pl/s495719/ium_495719.git"
                sh './data_processing.sh'
                archiveArtifacts artifacts: './*'
            }
        }
    }
}