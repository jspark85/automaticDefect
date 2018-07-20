# automaticDefect

This code was written by Ji-Sang to run [sxdefectalign](https://sxrepo.mpie.de/projects/sphinx-add-ons/files) easily.

Input parameters:

(1) Dielectric constant
* (e.g.) eps = '10' 

(2) Location of folders
* bulk = 'bulk' 
* charged = '1' 
* neutral = '0'

(3) Direction (0, 1, or 2)
* direction = 0

(4) Index of defect
* center = map(float,getCenter(defect,**-1**))
* -1 = last atom # 
* integer i = ith atom
