Overview
========

astr8300_rappture is a sample package for Astr8300 rappture projects.

Installation
------------

You will need a computer with [rappture](https://nanohub.org/infrastructure/rappture/) installed.

You can do this by first logging on to AWS. Start an instance of the Webnucleo1 AMI.To log in type,
* ssh -X -i "Samalka2.pem" ubuntu@ec2-18-234-137-202.compute-1.amazonaws.com  
Change the path by typing, 
* export PATH=$PATH:/usr/local/rappture/bin

Now that rappture is installed on this computer, 
 Type the following:

* git clone http://github.com/samalkapiy/IMF.git
* cd IMF
* rappture

<h2> Brief Introduction </h2>

The Initial Mass Function(IMF) gives the fraction of stars with masses m to m+dm in a generation of stars at birth. This function is expressed as a <i> probabability density function</i>(pdf). There are different IMFs in literature over the years with some of the popular ones being Salpeter(1955), Kroupa(2002) and Chabrier(2003). 

The standard normalization condition is:

&int;<sub>m<sub>l</sub></sub><sup>mu</sup> &xi;(m) dm = 1
&int;<sub(m<subl>)><sup>

<img src="integral.gif" align="middle" alt=
"the integral of exp(x**2) for x from 0 to infinity"></p>





Authors
-------

- Samalka Anandagoda <iananda@g.clemson.edu>
- Bradley S. Meyer <mbradle@clemson.edu>
