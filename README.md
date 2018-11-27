Overview
========

astr8300_rappture is a sample package for Astr8300 rappture projects

Installation
------------

You will need a computer with [rappture](https://nanohub.org/infrastructure/rappture/) installed.

You can do this by first logging on to AWS. Start an instance of the Webnucleo1 AMI. Then to log in, in the terminal type,
* ssh -X -i "key_name.pem" ubuntu@ec2-18-234-137-202.compute-1.amazonaws.com  
Change the path by typing, 
* export PATH=$PATH:/usr/local/rappture/bin

Now that rappture is installed on this computer, 
 Type the following:

* git clone http://github.com/samalkapiy/astr8300_rappture.git
* cd astr8300_rappture
* rappture

Authors
-------

- Bradley S. Meyer <mbradle@clemson.edu>
