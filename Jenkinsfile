pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/DianaDimla/WebServices_Assignment1_B00150982.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t inventory-api .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 8000:8000 --name inventory-container inventory-api'
            }
        }

        stage('Run API Tests') {
            steps {
                sh 'newman run tests/collection.json'
            }
        }

        stage('Stop Container') {
            steps {
                sh 'docker stop inventory-container'
                sh 'docker rm inventory-container'
            }
        }

        stage('Create ZIP File') {
            steps {
                sh 'zip -r complete-$(date +%Y%m%d-%H%M%S).zip .'
            }
        }
    }
}