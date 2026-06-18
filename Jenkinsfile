// pipeline {
//   agent any

//   environment {
//     IMAGE = "devender29/python-app"
//     TAG = "${BUILD_NUMBER}"
//   }

//   stages {

//     stage('Checkout') {
//       steps {
//         checkout scm
//       }
//     }

//     stage('Build & Push Image using Kaniko') {
//       steps {
//         sh '''
//         docker run --rm \
//           -v $(pwd):/workspace \
//           -v /root/.docker:/kaniko/.docker \
//           gcr.io/kaniko-project/executor:latest \
//           --dockerfile=/workspace/Dockerfile \
//           --context=/workspace \
//           --destination=$IMAGE:$TAG
//         '''
//       }
//     }

//     stage('Deploy') {
//       steps {
//         withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
//           sh '''
//           export KUBECONFIG=$KUBECONFIG
//           kubectl set image deployment/python-app python-app=$IMAGE:$TAG -n jenkins
//           '''
//         }
//       }
//     }
//   }
// }


pipeline {
  agent {
    kubernetes {
      label 'dind-agent'
    }
  }

  stages {
    stage('Test Docker') {
      steps {
        container('docker') {
          sh '''
            docker version
            docker run hello-world
          '''
        }
      }
    }
  }
}