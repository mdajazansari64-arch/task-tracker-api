
pipeline {
    agent any

    options {
        timestamps()
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
                echo 'GitHub code checkout successful'
            }
        }

        stage('Test') {
            steps {
                bat '"C:\\Users\\User\\AppData\\Local\\Python\\bin\\python.exe" -m pip install -r requirements.txt pytest'
                bat '"C:\\Users\\User\\AppData\\Local\\Python\\bin\\python.exe" -m pytest -v'
            }
        }

        stage('Build') {
            steps {
                bat 'docker build -t ajazaj/task-tracker-api:%BUILD_NUMBER% -t ajazaj/task-tracker-api:latest .'
            }
        }

        stage('Verify') {
            steps {
                bat 'docker image inspect ajazaj/task-tracker-api:%BUILD_NUMBER%'
                echo 'Docker image verification successful'
            }
        }

        stage('Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'docker-credentials',
                    usernameVariable: 'DOCKERHUB_USERNAME',
                    passwordVariable: 'DOCKERHUB_PASSWORD'
                )]) {
                    bat 'docker login -u %DOCKERHUB_USERNAME% -p %DOCKER_PASSWORD%'
                    bat 'docker push ajazaj/task-tracker-api:%BUILD_NUMBER%'
                    bat 'docker push ajazaj/task-tracker-api:latest'
                }
            }
        }
    }

    post {
        always {
            bat 'docker logout'
        }
    }
}
