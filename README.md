monochrome
==========
Monochrome is an image to ascii art convertor.
It uses Python and PIL.

Usage:
    monochrome [source] [destination] [dictionary(optional)]
    
    source:
          Path to an image file.
    
    destination:
          Path of the output file.
    
    dictionary:
          Path to the dictionary file.
          
          format of the dictionary:
          <char1><\n>
          <char2><\n>
          <char3>    ......
          
          Formed list : [char1,char2,char3]
          Make sure to have no *wild* whitespace lurking around.
          
          Its just characters seperated by newline.
          
          
     Note: It does not resize the image. If required please remove "#" (comment) from the image.resize(<width>,<height>) 
     
     Example : http://rawgithub.com/chinmay1/monochrome/master/example.html
