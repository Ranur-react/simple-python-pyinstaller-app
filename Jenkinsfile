node{
    stage('Build'){
        checkout scm
        docker.image('python:2-alpine')
        sh 'python -m py_compile sources/add2vals.py sources/calc.py'


    }
}