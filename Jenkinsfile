pipeline {
    agent any

    stages {
        stage('Stage 1') {
            steps {
                git(
                    url: "https://git.wmi.amu.edu.pl/s495719/ium_495719.git",
                    branch: "main"
                )
                sh 'chmod 777 ./data_processing.sh'
                sh './data_processing.sh'
                archiveArtifacts artifacts: 'processed_data.txt'
            }
        }
    }
}