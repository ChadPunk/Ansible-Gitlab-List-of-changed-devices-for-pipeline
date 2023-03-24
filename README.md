# Ansible-Gitlab-List-of-changed-devices-for-pipeline
This will take a merge request and loop through the changed file finding which are network configurations based on our predefined folder and pass those to a file to be called in a CI/CD pipeline. This can be beneficial if you do not want to call groups and want it to specifically call only changed devices.

<h1>Be sure to:</h1>
Replace <b>URL</b> with your url of your GitLab server.
Update the <b>PRIVATE-TOKEN</b> with your Private Token.
Have all the required modules installed.

