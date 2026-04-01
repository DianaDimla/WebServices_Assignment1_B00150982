pipeline {
    agent any
    
    stages {
        stage('1. Clone') {
            steps {
                sh 'rm -rf * .??* && git clone https://github.com/DianaDimla/WebServices_Assignment1_B00150982.git .'
            }
        }
        
        stage('2. Build') {
            steps {
                sh 'docker build -t inventory-api .'
            }
        }
        
        stage('3. Run API') {
            steps {
                sh '''
                    docker stop api-test || true
                    docker rm api-test || true
                    docker run -d --network host --name api-test inventory-api
                    sleep 5
                '''
            }
        }
        
        stage('4. Tests') {
            steps {
                sh '''
                    cat tests/collection.json | docker run --rm -i --network host postman/newman:alpine run /dev/stdin \\
                        --global-var "base_url=http://localhost:8000" \\
                        --bail false \\
                        -r cli
                '''
            }
        }
        
        stage('5. README & ZIP') {
            steps {
                sh '''
                    echo "Inventory API Endpoints" > README.txt
                    echo "/getSingleProduct?id=ID - GET single product" >> README.txt
                    echo "/getAll - GET all products" >> README.txt
                    echo "/addNew - POST new product" >> README.txt
                    echo "/deleteOne?id=ID - DELETE product" >> README.txt
                    echo "/startsWith?letter=a - GET products by letter" >> README.txt
                    echo "/paginate?start=1&end=10 - GET paginated" >> README.txt
                    echo "/convert?id=ID - GET price USD to EUR" >> README.txt
                    echo "" >> README.txt
                    echo "FastAPI Docs: http://localhost:8000/docs" >> README.txt
                    cat README.txt
                    
                    DATE_TIME=$(date +%Y%m%d-%H%M%S)
                    tar -czf "complete-${DATE_TIME}.tar.gz" README.txt Dockerfile app tests requirements.txt
                    ls -la complete-*.tar.gz
                '''
            }
        }
    }
    
    post {
        always {
            sh 'docker stop api-test || true && docker rm api-test || true && docker rmi inventory-api || true'
        }
    }
}

