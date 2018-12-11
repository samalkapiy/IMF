Overview
========

astr8300_rappture is a sample package for Astr8300 rappture projects.

Installation
------------

You will need a computer with [rappture](https://nanohub.org/infrastructure/rappture/) installed.

You can do this by first logging on to AWS. Start an instance of the Webnucleo1 AMI.To log in type,
* ssh -X -i "Samalka2.pem" ubuntu@ec2-18-234-137-202.compute-1.amazonaws.com

This is an example. The URL will change for different computers. 

Change the path by typing, 
* export PATH=$PATH:/usr/local/rappture/bin

Now that rappture is installed on this computer, 
 Type the following:

* git clone http://github.com/samalkapiy/IMF.git
* cd IMF
* cd final_project
* rappture

<<<<<<< HEAD
<h2> Brief Introduction </h2>
----------------

The Initial Mass Function(IMF) gives the fraction of stars with masses m to m+dm in a generation of stars at birth. This function is expressed as a <i> probabability density function</i>(pdf). There are different IMFs in literature over the years with some of the popular ones being Salpeter(1955), Kroupa(2002) and Chabrier(2003). 

The standard normalization condition is:

&int;<sub>m<sub>l</sub></sub><sup>m<sub>u</sub></sup> &xi;(m) dm = 1

where, m<sub>l</sub> and m<sub>u</sub> are the lower and upper mass limits respectively.  

<h2> Method </h2>
------------------

In this project, the Initial Mass Function(IMF) by Kroupa(2002) was used. This is a piecewise function for different mass ranges. 

For mass ranges between,
<br>0.01 Mo <= m > 0.08 Mo:</br>
       &xi;(m) = A m<sup>-0.3</sup> 

0.08 Mo <= m > 0.5 Mo:
      <br> &xi;(m) = A (0.08) m<sup>-1.3</sup> </br>
      
0.5 Mo <=m > 100 Mo:
      <br> &xi;(m) = A (0.5) (0.08) m<sup>-2.3</sup> </br>

Where, A is the normalization constant. 

<h3>Result 1 </h3>

In the <b>tool.xml</b> file, 3 inputs were created to type in the piecewise Initial mass function. Each input also have two inputs to enter the lower and upper mass limits.

The python code that is used for the tool.xml file is <b>imf.py.</b> In this file, these inputs are used and integrated over the whole mass range as shown in equation given below. To find the normalization constant(A), 1 was divided by the total value obtained by integrating over the whole mass range.

A{&int;<sub>0.01</sub><sup>0.08</sup>m<sup>-0.3</sup> + (0.08) &int;<sub>0.08</sub><sup>0.5</sup>m<sup>-1.3</sup> + (0.08)(0.5) &int;<sub>0.5</sub><sup>100</sup>m<sup>-2.3</sup>} = 1

The normalization constant is displayed in the drop down list in the GUI.

<h3>Result 2</h3>

From the GUI, a fourth function can be entered. This could be a function of mass like the Luminosity function or simply mass. Inorder to calculate the average value of the function that is entered into the GUI. 

The integration looks like the following:

<br>As an example, if the Function that is enetered is mass, then the average mass in a population of stars is given by:</br>

<m> = A &int;<sub>m<sub>l</sub></sub><sup>m<sub>u</sub></sup>  m  &xi;(m) dm 

This result is deplayed as the second result in the drop down list in the GUI.

<h3>Result 3</h3>

As the third result, the change in the Initial mass function with varying mass was graphed. 
We know, 

&int; &xi;(m) dm = N

since, &xi;(m) &prop; m<sup>-&alpha;</sup>

dN/dm = m<sup>-&alpha;</sup>
log<sub>10</sub>(dN/dm) = -&alpha; log<sub>10</sub>m

The quantity of log<sub>10</sub>(dN/dm) vs log<sub>10</sub>m was plotted and displayed as result 3. 



Authors
-------

- Samalka Anandagoda <iananda@g.clemson.edu>
- Bradley S. Meyer <mbradle@clemson.edu>
