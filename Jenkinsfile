pipeline {
  agent any

  environment {
    DOCKER_IMAGE = "devender29/python-app"
    TAG = "${BUILD_NUMBER}"
  }

  stages {

    stage('Checkout Code') {
      steps {
        checkout scm
      }
    }

    stage('Build & Push Image') {
      steps {
        sh '''
        docker build -t $DOCKER_IMAGE:$TAG .
        docker push $DOCKER_IMAGE:$TAG
        '''
      }
    }

    stage('Deploy to Kubernetes') {
      steps {
        withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
          sh '''
          export KUBECONFIG=$KUBECONFIG
          kubectl set image deployment/python-app python-app=$DOCKER_IMAGE:$TAG -n jenkins
          '''
        }
      }
    }

  }
}