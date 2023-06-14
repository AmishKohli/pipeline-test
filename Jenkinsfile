pipeline {
    
    parameters {
					choice(name: 'myenv', choices: ['sbx', 'dev', 'prd'], description: 'Select environment')
					string(name: 'showtext', defaultValue: 'DUMMY', description: 'test param value')
					password(
					    name: 'SECRET_DATA', 
					    defaultValue: '', 
					    description: 'Enter secrets in JSON format ex:'
                    )
	}
				
    agent any

    stages {
        stage('validate data') {
            steps {
                script {
                    println(params.myenv)
                    println(params.showtext)
                    println(params.SECRET_DATA)
                    
                }
            }
        }

        stage('validate data in shell') {
            steps {
                println(params.SECRET_DATA)
                sh '''
                        chmod +x entry.sh
                        echo ${SECRET_DATA}
                        ./entry.sh ${myenv}  ${showtext}  ${SECRET_DATA}
                    '''
            }
        }

        stage('validate data in Python') {
            steps {
                script {
                    sh '''
                        python --version
                        is_pip_install=$(pip --version)
                        echo $is_pip_install
                        curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
                        ls -ltr
                        pwd
                        whoami
                        python get-pip.py
                        pip install getopts
                        python readparam.py -c ${myenv} -t ${showtext}  -s ${SECRET_DATA}
                    '''
                    // println(params.myenv)
                    // println(params.showtext)
                    // println(params.SECRET_DATA)
                    
                }
            }
        }
    }
}
