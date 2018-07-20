# automaticDefect

This code was written by Ji-Sang to run [sxdefectalign](https://sxrepo.mpie.de/projects/sphinx-add-ons/files) easily.

Input parameters:

(1) Dielectric constant (string)
* (e.g.) eps = '10' 

(2) Location of folders (string)
* bulk (e.g) 'bulk' 
* charged (e.g.) '1' 
* neutral (e.g.) '0'

(3) Direction (0, 1, or 2) (string or int)
* direction = 0

(4) Index of defect x (int)
* center = map(float,getCenter(defect,**x**))
* -1 = last atom  
* integer i = ith atom
