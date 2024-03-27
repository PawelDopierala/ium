pipeline {
    agent any

    stages {
        stage('Git') {
            steps {
                git(
                    url: "https://git.wmi.amu.edu.pl/s495719/ium_495719.git",
                    branch: "main"
                )
            }
        }
        stage('Shell') {
            steps {
                sh 'chmod 777 ./data_processing.sh'
                sh './data_processing.sh'
            }
        }
        stage('Artifacts') {
            steps {
                archiveArtifacts artifacts: 'processed_data.txt'
            }
        }
    }
}