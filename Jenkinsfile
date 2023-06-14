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
    }
}
