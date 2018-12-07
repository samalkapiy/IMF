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

<<<<<<< HEAD
<h2> Brief Introduction </h2>

The Initial Mass Function(IMF) gives the fraction of stars with masses m to m+dm in a generation of stars at birth. This function is expressed as a <i> probabability density function</i>(pdf). There are different IMFs in literature over the years with some of the popular ones being Salpeter(1955), Kroupa(2002) and Chabrier(2003). 

The standard normalization condition is:

&int;<sub>m<sub>l</sub></sub><sup>m<sub>u</sub></sup> &xi;(m) dm = 1

where, m<sub>l</sub> and m<sub>u</sub> are the lower and upper mass limits respectively.  

<h2> Method </h2>

In this project, the Initial Mass Function(IMF) by Kroupa(2002) was used. This is a piecewise function for different mass ranges. 

In the Kroupa IMF, for mass ranges between 0.01 Mo to 0.08 Mo, the IMF is &xi;(m) = A m<sup>-0.3</sup> 
for mass ranges between, 0.08 Mo to 0.5 Mo, this function is, &xi;(m) = A (0.08) m<sup>-1.3</sup>
for mass ranges between, 0.5 M0 to 100 Mo, the function is, &xi;(m) = A (0.5) (0.08) m<sup>-2.3</sup>

Where, A is the normalization constant. 

In the tool.xml file, 3 inputs were created to type in the piecewise Initial mass function. Each input also have two inputs to obtain the lower and upper mass limits.



Authors
-------

- Samalka Anandagoda <iananda@g.clemson.edu>
- Bradley S. Meyer <mbradle@clemson.edu>
