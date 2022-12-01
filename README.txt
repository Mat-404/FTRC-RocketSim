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
      ##,,  .#    %    %  &.,/%, & (,   #  #.,.&      %   ,(.... %/    (/..,(*  
      &(     &&&&  %&%&   &   #/ & /&&&&  %.    &     &.  .&&&&& .%&&& (#   (#  
                                                                                
             &&&&&   /&&&&#  /#&&&# &* ,&# %&&&&& &&&&&&. &&&&&. &.  %/         
             #&.,*&  &/   #& &#     &/&(   %.,..    &#    &.,/%,  .%&           
             #& .&%   &%(%&  #&%##( &* /&( %&###(   &#    &   #/    &            
                                                                                
                                                                                

TO USE:

    For Dev work:

    -Install folder and open in IDE of your choice, preferrably VSCode, however any python environment with pip can work.
    -Install dependencies as detailed below
    -Run sim.py to start the simulation. You will be asked to choose which engine you want to simulate with.
        Right now, the simulation only uses D12-5, F15-4, and H31-P engines.
        In order to test other engines, Force/Time data must be added to EngineDataSheet.xlsx, and 
        the physical properties must be added in Mk1 Data Sheet.xlsx in the Engines sheet.

    For users:

    - An alternate method to run the simulation is available through a .exe program created by Auto Py To Exe,
        created by brentvollebregt on GitHub. This program was used to compress the simulation into a single .exe file.
        The compression program is listed below:
            https://github.com/brentvollebregt/auto-py-to-exe
        The simulation program is located in the dist zipped folder.
        Download the folder, unzip, and run "run.exe".

This simulation was created to get rough estimates for design specs for the Florida Tech Rocketry Club rocket.
It determines the thrust, mass, and velocity of the rocket at any given time, and plots the data for the user to see.
As of right now, the simulation works only in one dimension, however it is possible to add a second dimension to the simulation
as well as launch angles. The simulation is also able to calculate the drag force on the rocket, however it is currently only using
an approximation of the geometry of the rocket.


This folder contains a python program that runs the simulation, as well as a pair of Excel Spreadsheets which contain rudimentary
geometry calculations and values that were looked up online. The run.py program is the frontend program, using pyEasyGUI. The
program uses an additional two programs to calculate the simulation, and interpolate thrust data. The programs chain in series like so:

  run.py      ->     sim.py      ->      thrustCurveAnalysis_UPDATED.py   ->   sim.py   ->    run.py

[User Input] [Pull Requested Engine Data]  [Interpolate Thrust Data]   [Calculate Simulation]  [Plot Data]

An additional mode of the program is in progress, which allows the user to test different numbers of engines and find the optimal
configuration based on user criteria. This mode is not yet complete, however is included in this folder. It will tentatively follow this order:

    run.py -> optimization.py -> sim.py -> thrustCurveAnalysis_UPDATED.py -> sim.py -> optimization.py -> run.py

A few concessions:
    This assumes an air density following a linear curve below 11 km. This is justified due to us most likely not breaching 11 km in the immediate future.
    The aerodynamic calculations do not concern the aerodynamic fins, or any protrusions/indents made for ease of access.
    The structure of the rocket was determined rudimentarily in Mk 1 Data Sheet.xlsx. However, it is missing calculations for the fins, 
as well as having a very rough estimate of 3D-printing mass, with innacuracies due to infill, material, sanding, paint, etc.
    There were also no mass estimates made for any metal components or parachute components. More reasearch is needed.

    In order to run the simulation in dev mode, the local system needs to have Python, Pip, matplotlib, and openpyxl. These can be installed with the following:

    Python: Can be installed from online .exe or through a VSCode extension
        -https://www.python.org/downloads/

    Pip: run-> python -m pip install -U pip
        -https://pip.pypa.io/en/stable/installation/

    matplotlib: pip install -U matplotlib
        -https://matplotlib.org/stable/users/installing/index.html

    openpyxl: pip install openpyxl
        -https://pypi.org/project/openpyxl/

    -Do not under any circumstances delete coconut.jpg.

    -Mathieu Cote
    Florida Tech Rocketry Club

                                                                                    
