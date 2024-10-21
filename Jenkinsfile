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
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest tests/'  // Assuming you have a tests folder
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t your-docker-image-name .'
            }
        }
        stage('Push Docker Image') {
            steps {
                sh 'docker login -u your-username -p your-password'
                sh 'docker push your-docker-image-name'
            }
        }
        stage('Deploy') {
            steps {
                // Add this line to run your deployment script
                sh 'python deploy.py'  // This will execute your deploy.py script
            }
        }
    }
}
