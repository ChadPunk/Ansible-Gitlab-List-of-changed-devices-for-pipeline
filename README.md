# Ansible-Gitlab-List-of-changed-devices-for-pipeline
This will take a merge request and loop through the changes via an API call to GitLab, finding which are network configurations based on our predefined folder, and pass those to a file to be called in a CI/CD pipeline. This can be beneficial if you do not want to call groups and want it to specifically call only changed devices based on a certain rule. If you have hundreds of devices this will save so much time not having to loop through each device to determine if the devices actually have a change.

<h1>Be sure to:</h1><br>
Replace <b>URL</b> with your url of your GitLab server.<br>
Update the <b>PRIVATE-TOKEN</b> with your Private Token.<br>
Update Project ID in URL (from GitLab).<br>
Modify the compiled folder regex to look for your own folder.<br>
Have all the required modules installed.<br><br>

This assumes you can follow along and is not a full write up. You will need to break this open and know how to change this to fit your needs.
A little further explanation in code comments!

