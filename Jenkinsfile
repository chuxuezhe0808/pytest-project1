pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install and Run') {
            steps {
                // 1. 使用电脑上Python的绝对路径来安装依赖和运行测试
                // 注意：路径中的反斜杠需要转义，或者用正斜杠
                bat 'cmd /c C:\\Users\\54095\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe -m pip install -r requirements.txt'

                // 2. 同样用绝对路径运行pytest
                bat 'cmd /c C:\\Users\\54095\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe -m pytest tests/ -v'

                // 3. 如果还需要生成Allure报告
                bat 'cmd /c C:\\Users\\54095\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe -m pip install allure-pytest'
                bat 'cmd /c C:\\Users\\54095\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe -m pytest tests/ --alluredir=allure-results -v'
            }
        }
    }
}