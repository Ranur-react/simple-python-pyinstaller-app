// node{
//     checkout scm
//     stage('Build'){
//         docker.image('python:2-alpine').inside{
//                 sh 'python -m py_compile sources/add2vals.py sources/calc.py'
//                   stash(name: 'compiled-results', includes: 'sources/*.py*')
//         }
//     }

//     stage('Test'){
//         docker.image('qnib/pytest').inside{
//                 sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
//                 junit 'test-reports/results.xml'
//         }
//     }
//     stage('Deploy') {
//         docker.image('cdrx/pyinstaller-linux:python2').inside{
//             checkout scm
//             sh 'pyinstaller --onefile sources/add2vals.py'
//         }
//         input message: 'Finished using the website? (Click "Proceed" to continue)'

//     }
// }

//pasrt2

// node {
//     try {
//         // Checkout source code from SCM
//         checkout scm

//         // Build stage
//         stage('Build') {
//             docker.image('python:2-alpine').inside {
//                 sh 'python -m py_compile sources/add2vals.py sources/calc.py'
//             }
//         }

//         // Test stage
//         stage('Test') {
//             docker.image('qnib/pytest').inside {
//                 sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
//                 junit 'test-reports/results.xml'
//             }
//         }

//         // Deploy stage
//         stage('Deploy') {
//             def container = docker.image('cdrx/pyinstaller-linux:python2')
//             .run("-d", "--name", "pyinstallerContainer", "/bin/sh", "-c",
//              "while true; do sleep 60; done")

//                 sh "docker exec pyinstallerContainer pyinstaller --onefile sources/add2vals.py"

//             input message: 'Finished using the website? (Click "Proceed" to continue)'
//         }


//     } catch (Exception e) {
//         // Catch any exceptions and log them
//         echo "Error occurred: ${e.message}"
//         currentBuild.result = 'FAILURE' // Mark the build as failed
//     }
// }
// 

// pipeline {
//     agent none
//     stages {
//         stage('Build') {
//             agent {
//                 docker {
//                     image 'python:2-alpine'
//                 }
//             }
//             steps {
//                 sh 'python -m py_compile sources/add2vals.py sources/calc.py'
//             }
//         }
//         stage('Test') {
//             agent {
//                 docker {
//                     image 'qnib/pytest'
//                 }
//             }
//             steps {
//                 sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
//             }
//             post {
//                 always {
//                     junit 'test-reports/results.xml'
//                 }
//             }
//         }
//         stage('Deploy') {
//             agent {
//                 docker {
//                     image 'cdrx/pyinstaller-linux:python2'
//                 }
//             }
//             steps {
//                 script {
//                     // Run pyinstaller to package the script
//                     sh 'pyinstaller --onefile sources/add2vals.py'

//                     // Copy the packaged executable to a known location
//                     sh 'cp dist/add2vals /tmp/'
//                 }
//             }
//             // post {
//             //     success {
//             //         // Archive the packaged executable
//             //         archiveArtifacts '/tmp/add2vals'
//             //     }
//             // }
//         }
//         stage('Input') {
//             steps {
//                 // Wait for user input to proceed
//                 input message: 'Finished using the website? (Click "Proceed" to continue)'
//             }
//         }
//     }
// }
pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'python -m py_compile sources/add2vals.py sources/calc.py'
                  stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('Deliver') {
            agent {
                docker {
                    image 'cdrx/pyinstaller-linux:python2'
                }
            }
            steps {
                sh 'pyinstaller --onefile sources/add2vals.py'
            }
            post {
                success {
                    archiveArtifacts 'dist/add2vals'
                }
            }
        }
    }
}
