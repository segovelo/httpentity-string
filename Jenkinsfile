pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
      }
    triggers {
        pollSCM '* * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building..."
                sh '''
                echo "Building some stuff..."
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing..."
                sh '''
                echo "Testing http-entity.py program..."
                python3 httpentity.py test
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver...'
                sh '''
                echo "doing delivery stuff..."
                '''
            }
        }
    }
}