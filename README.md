# Ansible-Gitlab-List-of-changed-devices-for-pipeline
This will take a merge request and loop through the changes via an API call to GitLab, finding which are network configurations based on our predefined folder, and pass those to a file to be called in a CI/CD pipeline. This can be beneficial if you do not want to call groups and want it to specifically call only changed devices based on a certain rule.

<h1>Be sure to:</h1><br>
Replace <b>URL</b> with your url of your GitLab server.<br>
Update the <b>PRIVATE-TOKEN</b> with your Private Token.<br>
Update Project ID in URL (from GitLab).<br>
Have all the required modules installed.

Futher explanation in code comments!

