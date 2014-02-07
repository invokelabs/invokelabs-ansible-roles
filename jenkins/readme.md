# Jenkins Role

### Description

This role installs Jenkins on a server. Jenkins is a popular continuous integration service.

Currently this role works on OS X only. _Please read through this entire document before beginning._

This document assumes that you've already installed Ansible on your local machine. It also assumes that you are familiar with public key authentication. It also assumes that you're familiar with Ansible.

You should configure public-key authentication for a user that has the right to run sudo on the target machine. You should also configure that user to be able to run sudo without entering a password, at least temporarily during this set-up.

Otherwise you will need to rely on the sshpass program, which could potentially cause a kernel panic on your OS X machine.

### Usage

The steps to use this role are roughly as follows:

1. Create a plain text file called ``jenkins.inventory``, which will allow Ansible to find the server on the internet. The file should look like this:

        [jenkins]
        ip.address.or.fqdn.of.OSX.machine.you'll.be.installing.jenkins.on
            
2. Decide on configuration details, such as
    1. What should be the domain name of the jenkins installation?
    	* This domain name must be reachable at the time you run the playbook, since it will be used by the CLI to install the Xcode, TestFlight, and CocoaPods plugins.
    	* If you don't know what the DNS name will be, then you can just use the IP address of the machine that you specified in the jenkins.inventory file.
    2. Do I have an SSL certificate signed by a known CA, or will I use a self-signed certificate?
       * If you change the domain name of the service, you'll need a new self-signed certificate for that domain name.
    3. My default user _needs_ an SSH key pair. Should I generate one or use the included default?
    4. My default user _needs_ an API token. Should I generate one or use the included default?
    5. Do I have a mail relay host from through which Jenkins can send out e-mail? This is an important one to avoid Jenkins' mails to you or your team members from ending up in spam folders.
    
3. Open up the file ./playbooks/jenkins_osx.yml in your favorite text editor (hopefully one that provides YAML syntax highlighting) and edit the values of the variables to match the answers from the last step.
        
4. Because Ansible communicates with the OS X machine via SSH, you'll need to have configured SSH on the server machine on which you'll be installing Jenkins. The simplest explanation of how to do so is available [here](http://bluishcoder.co.nz/articles/mac-ssh.html). If that site ever goes off-line, the very short text is roughly:

        The Apple Mac OS X operating system has SSH installed by default but the SSH daemon is not enabled. This means you can’t login remotely or do remote copies until you enable it.

        To enable it, go to ‘System Preferences’. Find the‘Sharing’ icon. Run that. In the list that appears, check the ‘Remote Login’ option.

        This starts the SSH daemon immediately and you can remotely login using your username. The ‘Sharing’ window shows at the bottom the name and IP address to use. You can also find this out using ‘whoami’ and ‘ifconfig’ from the Terminal application.
        

5. You should confirm that you can log in to the OS X Server via SSH.

6.  Once you've confirmed that you have all of you can SSH into the OS X Server, you can use the playbook to install Jenkins. Here are three different command line versions that you could use depending on the state of your SSH login.

    If you need to type your password to use sudo:  

        ansible-playbook -K -i jenkins.inventory ./playbooks/jenkins_osx.yml

    If you don't need to type your password to use sudo:
    
        ansible-playbook -i jenkins.inventory ./playbooks/jenkins_osx.yml
       
   7. The final piece of information about which you should be aware is that this playbook will overwrite your existing Jenkins configuration if and only if you already have Jenkins installed on a machine. You might find this useful if, for example, you've locked yourself out of your Jenkins installation and you need to allow yourself access again with a new user. 
   8. The default user that it creates will have the following password: BhPPvtmaD9  You should log in and change it as soon as you have installed Jenkins.


   

