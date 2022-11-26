                                       ,****,                                   
                                       (&&&&%                                   
                                       (&&&&%                                   
                                       (&&&&%                                   
                                       (&&&&%                                   
                                       (&&&&%                                   
                                       (&&&&%                                   
                                       (&&&&%                                   
                                       (&&&&%                                   
                            /&&&&&     (&&&&%     %&&&&#                        
                            /&&&&&     (&&&&%     %&&&&#                        
                            /&&&&&     (&&&&%     %&&&&#                        
                            /&&&&&     (&&&&%     %&&&&#                        
                            /&&&&&     (&&&&%     %&&&&#                        
                            /&&&&&     (&&&&%     %&&&&#                        
                            /&&&&&     (&&&&%     %&&&&#                        
                            /&&&&&     (&&&&%     %&&&&#                        
                            /&&&&&     (&&&&%     %&&&&%                        
                            (&&&&&     (&&&&&     (&&&&&                        
                           ,*&&&&&*    /&&&&&*    *&&&&&%                       
                          .**%&&&&%   **#&&&&&   ,*/&&&&&(                      
                         ****/&&&&&* ****%&&&&%  ***/&&&&&&                     
                       ,*****//&&&&&/*****&&&&&&*****,%&&&&&#                   
                     ******/.  #&&&&&/***  %&&&&&/***  .&&&&&&&,                
                 ,/******/      #&&&&&/*    (&&&&&%*      &&&&&&&&#             
         .,***********/.       ,*#&&&&&/    ./&&&&&&%       ,&&&&&&&&&&&#/,..   
      .***********/,         *****(&&&&&&  ****/&&&&&&&,        /&&&&&&&&&&&&/  
      .///***.            *******/  %&&&&&%****/  %&&&&&&&,           *(%&&&&/  
                     .*/******/,      &&&&&&%/.     ,&&&&&&&&&,                 
               .*/**********.        /*/&&&&&&&.       .%&&&&&&&&&&%/.          
      .***************/*.         ********%&&&&&&&.        .#&&&&&&&&&&&&&&&&/  
       ***********            ./*******,    ,&&&&&&&&/           .#&&&&&&&&&&/  
                          ,********/,          *&&&&&&&&&(.                     
                    ,**********/*                  #&&&&&&&&&&%(.               
       **////*************/*,                          /&&&&&&&&&&&&&&&&&&&%%*  
      .*************/*,                                     ./%&&&&&&&&&&&&&&/  
       **,,..                                                          .*/(##*  
                                                                                
                                                                                
      &(%#  .#     %#*/   &&&&&. & (%#*#    #.%     /#%%/ ,/&##%  .#%  (,   /,  
      ##,,. .#    %    %  &.,/%, & (,   #  #.,.&      %   ,(.... %/    (/..,(*  
      &(     &&&&& %&%&   &   #/ & /&&&&  %.    &     &.  .&&&&& .%&&& (#   (#  
                                                                                
             &&&&&#  (&&&&&* *&&&&# &* ,&# %&&&&& &&&&&&. &&&&&. &.  %&         
             #&.,*&  &/   #& &#     &/&(   %.,..    &#    &.,/%, .&%&(          
             #& .&%  %&%(%&# #&%##( &* /&( %&###(   &#    &   #/    &(           
                                                                                
                                                                                



This simulation was created to get rough estimates for design specs for the Florida Tech Rocketry Club rocket.

This folder contains a python program that runs the simulation, as well as an Excel Spreadsheet which contains rudimentary
geometry calculations and values that were looked up online.

A few concessions:
    This assumes a roughly constant air density. Since the rocket will likely not breach 1 km, 
it is fair to assume that air density will be roughly uniform.
    This simulation assumes a conical rocket, with two rings of engines on the bottom, which total 30 in number. 
These engine specs are assumed to be Estes D12-5 engines. If a different engine is chosen, the stats would need
to be changed on the excel Spreadsheet as well as a new thrust curve be defined
    I found no good way to plot a function to the thrust curve, so I broke it into four roughly linear sections.
If someone thinks of a better way to do this, please let me know.
    The aerodynamic calculations do not concern the aerodynamic fins, or any protrusions/indents made for ease of access.
    The structure of the rocket was determined geometrically in the Excel Sheet. 
However, it is missing the mass of the fins, as well as having a rough estimate of 3D-printing mass.
    There were also no mass estimates made for any metal components or parachute components. More reasearch is needed.

    In order to run, the local system needs to have Python, Pip, matplotlib, and openpyxl. These can be installed with the following:

    Python: Can be installed from online .exe or through a VSCode extension
        -https://www.python.org/downloads/

    Pip: run-> python -m pip install -U pip
        -https://pip.pypa.io/en/stable/installation/

    matplotlib: pip install -U matplotlib
        -https://matplotlib.org/stable/users/installing/index.html

    openpyxl: pip install openpyxl
        -https://pypi.org/project/openpyxl/


    -Mathieu Cote
    Florida Tech Rocketry Club

                                                                                    
