pipeline {
  agent {
    kubernetes {
      yamlFile 'kaniko-pod.yaml'
    }
  }

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
        container('kaniko') {
          sh """
          /kaniko/executor \
            --dockerfile=Dockerfile \
            --context=\$(pwd) \
            --destination=${DOCKER_IMAGE}:${TAG}
          """
        }
      }
    }

    stage('Deploy to Kubernetes') {
      steps {
        container('kubectl') {   // ✅ use kubectl container
          withCredentials([file(credentialsId: 'kubeconfig-file', variable: 'KUBECONFIG')]) {
            sh """
            export KUBECONFIG=\$KUBECONFIG
            kubectl set image deployment/python-app python-app=${DOCKER_IMAGE}:${TAG}
            """
          }
        }
      }
    }

  }
}