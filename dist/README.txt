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
                                                                                
                                                                                

TO USE:
    -Install folder and open in IDE of your choice, preferrably VSCode.
    -Install dependencies as detailed below
    -Run sim.py to start the simulation. You will be asked to choose which engine you want to simulate with.
        Right now, the simulation only uses D12-5 and F15-4 engines.
        The simulation is currently limited to engines that have written reports from NAR about the thrust curve. 
        However, thrust vs time data could be imputted into the thrust curve analysis in the future.

This simulation was created to get rough estimates for design specs for the Florida Tech Rocketry Club rocket.

This folder contains a python program that runs the simulation, as well as an Excel Spreadsheet which contains rudimentary
geometry calculations and values that were looked up online. The sym.py program is the main program, 
where thrustCurveAnalysis_UPDATED.py is an auxillary program which fetches data on the thrust curve of the inquired engine.

A few concessions:
    This assumes a roughly constant air density. Since the rocket will likely not breach 1 km, 
it is fair to assume that air density will be roughly uniform.
    This simulation assumes a conical rocket, with two rings of engines on the bottom, which total 30 in number. 
These engine specs are assumed to be Estes D12-5 engines. If a different engine is chosen, the stats would need
to be changed on the excel Spreadsheet as well as a new thrust curve be defined
    The fetching of thrust curve data is very limited, ideally there would be an API or database I can draw the
information from, however I found no such database. Instead, it looks up NAR reports and parses data from there.
    The aerodynamic calculations do not concern the aerodynamic fins, or any protrusions/indents made for ease of access.
    The structure of the rocket was determined geometrically in the Excel Sheet. However, it is missing the mass of the fins, 
as well as having a very rough estimate of 3D-printing mass, with innacuracies due to infill, material, etc.
    There were also no mass estimates made for any metal components or parachute components. More reasearch is needed.

    In order to run the simulation, the local system needs to have Python, Pip, matplotlib, and openpyxl. These can be installed with the following:

    Python: Can be installed from online .exe or through a VSCode extension
        -https://www.python.org/downloads/

    Pip: run-> python -m pip install -U pip
        -https://pip.pypa.io/en/stable/installation/

    matplotlib: pip install -U matplotlib
        -https://matplotlib.org/stable/users/installing/index.html

    openpyxl: pip install openpyxl
        -https://pypi.org/project/openpyxl/

    In order to run the thrust curve analysis, your local system also needs requests and PyPDF2. These can be installed with the following:

    requests: pip install requests
        -https://pypi.org/project/requests/

    PyPDF2: pip install PyPDF2
        -https://pypi.org/project/PyPDF2/

    -Do not under any circumstances delete coconut.jpg.

    -Mathieu Cote
    Florida Tech Rocketry Club

                                                                                    
