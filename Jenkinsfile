pipeline {
    agent any

    stages {
        stage("Clone") {
            steps {
                echo "Cloning the repo"
                git url: "https://github.com/Arjun4522/IEMSIS.git", branch: "main"
            }
        }
        stage("Build") {
            steps {
                echo "Building the image"
                sh "docker build -t app ."
            }
        }
        stage("Deploy") {
            steps {
                echo "Deploying the container"
                sh "docker-compose down && docker-compose up -d"
            }
        }
    }
}
