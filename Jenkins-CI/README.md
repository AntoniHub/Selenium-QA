<h3 align="center"> Continuous Integration - Automated Testing </h3>
<h4> Tools: </h4>
<li> .- Install  <a href="https://www.python.org/downloads/"> Python </a></li>
<li> .- Install  <a href="https://www.jenkins.io/doc/book/installing/"> Jenkins  </a></li>
<li> .- Java requirements: <a href="https://www.jenkins.io/doc/administration/requirements/java/"> Java Development Kits </a></li>
<li> .- Install Jenkins Plugins: <i><a href="https://plugins.jenkins.io/"> Plugins Index </a></i></li>
<i>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Some plugins: ShiningPanda (virtualenv), Selenium, Python.</i>
<li>.- See <a href="https://www.jenkins.io/doc/pipeline/tour/getting-started/"> Guided Tour </a> Jenkins tutorial. </li>
&nbsp;&nbsp;


With the freestyle project can create a Windows/Shell execution:
<pre><blockquote>
cd "path/to/project"
python -m AntonioRodriguezFarias.py
</blockquote></pre>
&nbsp;
Also run a Pipeline:
&nbsp;&nbsp;
<pre><blockquote>
Jenkinsfile (Declarative Pipeline)
/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'python:3.10.7-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}
</blockquote></pre>