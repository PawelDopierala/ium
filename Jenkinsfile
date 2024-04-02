pipeline {
    agent {
        dockerfile true
    }

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
        stage('Download data') {
            steps {
                withEnv(["KAGGLE_USERNAME=${params.KAGGLE_USERNAME}",
                  "KAGGLE_KEY=${params.KAGGLE_KEY}" ]) {
                    sh 'chmod 777 ./data_processing.py'
                    sh "./data_processing.py ${params.CUTOFF}"
                }
            }
        }
        stage('Artifacts') {
            steps {
                def artifactsList = ['hp_train.csv', 'hp_dev.csv', 'hp_test.csv']
                artifactsList.each { artifact ->
                    archiveArtifacts artifacts: artifact
                }
            }
        }
    }
}