pipeline {
    agent any

    parameters {
        string(
            defaultValue: '',
            description: 'Kaggle username',
            name: 'KAGGLE_USERNAME',
            trim: false
        )
        password(
            defaultValue: '',
            description: 'Kaggle token taken from kaggle.json file, as described in https://github.com/Kaggle/kaggle-api#api-credentials',
            name: 'KAGGLE_KEY'
        )
        string(
            defaultValue: '50',
            description: 'number of truncated examples',
            name: 'CUTOFF'
        )
    }

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
                sh "./data_processing.sh ${params.CUTOFF}"
            }
        }
        stage('Artifacts') {
            steps {
                archiveArtifacts artifacts: 'processed_data.txt'
            }
        }
        stage('Kaggle') {
            steps {
                withEnv(["KAGGLE_USERNAME=${params.KAGGLE_USERNAME}",
                  "KAGGLE_KEY=${params.KAGGLE_KEY}" ]) {
                    sh 'echo KAGGLE_USERNAME: $KAGGLE_USERNAME'
                    sh 'kaggle datasets list'
                }
            }
        }
    }
}