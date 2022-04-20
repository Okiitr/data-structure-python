pipeline {
  agent any
  stages {
    stage('1st ') {
      parallel {
        stage('1st ') {
          steps {
            sh '''echo this is the 1st stage 
ls 

'''
          }
        }

        stage('1stp') {
          steps {
            sh '''echo hello world
'''
          }
        }

      }
    }

    stage('2nd') {
      steps {
        sh '''pwd 
ls
python3 palindrome.py'''
      }
    }

    stage('3rd') {
      parallel {
        stage('3rd') {
          steps {
            echo 'you are here now in third stage'
          }
        }

        stage('3rdp') {
          steps {
            sleep 5
          }
        }

      }
    }

    stage('4th ') {
      steps {
        sh 'touch jenkin.py'
      }
    }

  }
}