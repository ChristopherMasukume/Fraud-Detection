pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/ChristopherMasukume/Fraud-Detection'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'pytest tests/'  // Assuming you have a tests folder
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t your-docker-image-name .'
            }
        }
        stage('Push Docker Image') {
            steps {
                bat 'docker login -u your-username -p your-password'
                bat 'docker push your-docker-image-name'
            }
        }
        stage('Deploy') {
            steps {
                bat 'python deploy.py'  // This will execute your deploy.py script
            }
        }
    }
}
