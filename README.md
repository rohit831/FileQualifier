# FileQualifier

A Python based Text Qualifier which can be used for importing documents according to your organizational standards.

USE CASE:

1) Whenever we receive any file which contains delimited data. The delimeter may be any character. 
   Also the strings are represented, suppose, inside "double-quotes".
   Strings may also contain delimeter inside them. So we need to first remove all the unwanted characters and after that
   split and import our data based on the no of columns and delimiter.

2) This text qualifier aims at first removing all the unwanted characters inside the file.
   For e.g. Input:  5~"Ro~hit"~"Some Data which ~ contains~ delimiter"
            Output: 5~Rohit"~Some Data which contains delimeter
            
3)  Now this data can be splitted and imported according to your policy.
    Also, Suppose if our file should have N delimeted columns.
    So Text Qualifier divides the file into two output files. One which contains the valid 
    data &Other tagged according to the issue with each row of data which can further be handled manually.
    
    
    
