pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t inventory-api .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 8000:8000 --name inventory-container inventory-api'
            }
        }

        stage('Run API Tests') {
            steps {
                bat 'newman run tests/collection.json'
            }
        }

        stage('Stop Container') {
            steps {
                bat 'docker stop inventory-container'
                bat 'docker rm inventory-container'
            }
        }

        stage('Create ZIP File') {
            steps {
                bat 'powershell Compress-Archive -Path * -DestinationPath complete.zip'
            }
        }
    }
}