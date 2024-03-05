// node{
//     checkout scm
//     stage('Build'){
//         docker.image('python:2-alpine').inside{
//                 sh 'python -m py_compile sources/add2vals.py sources/calc.py'
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
//             sh 'pyinstaller --onefile sources/add2vals.py'
//         }
//         input message: 'Finished using the website? (Click "Proceed" to continue)'

//     }
// }
node {
    try {
        // Checkout source code from SCM
        checkout scm

        // Build stage
        stage('Build') {
            docker.image('python:2-alpine').inside {
                sh 'python -m py_compile sources/add2vals.py sources/calc.py'
            }
        }

        // Test stage
        stage('Test') {
            docker.image('qnib/pytest').inside {
                sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
                junit 'test-reports/results.xml'
            }
        }

        // Deploy stage
       // Deploy stage
        stage('Deploy') {
            // Run the Docker container and keep it running until deployment is done
            def container = docker.image('cdrx/pyinstaller-linux:python2')
            .run('-d --name pyinstallerContainer')
            // .run('-d', '--name', 'pyinstaller', '/bin/sh', '-c', 'while true; do sleep 60; done')
            try {
                // Execute deployment commands inside the Docker container
                // container.inside {
                // Execute deployment commands inside the Docker container
                sh "docker exec pyinstallerContainer pyinstaller --onefile sources/add2vals.py"
                // Additional deployment steps can be added here
                    // Additional deployment steps can be added here
                // }
            } finally {
                // Stop and remove the Docker container after deployment is done
                container.stop()
                // container.remove()
            }
            // Wait for user input to proceed
            input message: 'Finished using the website? (Click "Proceed" to continue)'
        }


    } catch (Exception e) {
        // Catch any exceptions and log them
        echo "Error occurred: ${e.message}"
        currentBuild.result = 'FAILURE' // Mark the build as failed
    }
}
