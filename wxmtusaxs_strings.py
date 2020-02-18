'''wxmtusaxs_strings: define strings used in USAXS macro creation

########### SVN repository information ###################
# $Date: 2017-06-15 10:05:09 -0500 (Thu, 15 Jun 2017) $
# $Author: jemian $
# $Revision: 1411 $
# $URL: https://subversion.xray.aps.anl.gov/small_angle/USAXS/wxmtusaxs/trunk/wxmtusaxs_strings.py $
# $Id: wxmtusaxs_strings.py 1411 2017-06-15 15:05:09Z jemian $
########### SVN repository information ###################
'''
from ca_util import caget, caput  

class USAXSStrings:
    
    def GetMacroHeaderPart1(self):
        return """    
    """
    def GetMacroHeaderPart2(self):
        return """
                      
    # This file runs USAXS, SAXS and WAXS scans according to the syntax shown below
    #       
    # Scan Type      sx         sy   Thickness  Sample Name
    # ------------------------------------------------------  
    # USAXSscan    45.07       98.3     0      "Water Blank"
    # saxsExp      45.07       98.3     0      "Water Blank"
    # waxsExp      45.07       98.3     0      "Water Blank"  
    #      Use a space (not a tab) to separate arguments (i.e., 45.07 <space> 98.3 in the examples above)  

    # Run this file by typing the following command in the spec window:   USAXS> CollectData usaxs.mac              
                                    
    # Stop the run using the "Stop after this scan?" checkbox in USAXS user main intf and waiting until the USAXS> prompt reappears
              
    ############ PLACE ALL USER COMMANDS AFTER THIS LINE ############                

          #SAXS measurements
    """    
    def GetMacroUSAXSPinSwitch(self):
        return """
    #USAXS measurements
    """
    
    def GetMacroFooter(self):
        return """
    """
    
class SAXSStrings:
    
    def GetMacroHeaderPart1(self):
        return """
        '''Pinhole instrument control script.  P. Beaucage 2011.06.10
        
        expose image using  :  pinhole.PinholeExp(sx, sy, time, name, thickness)
        
        example of more complicated controls by changing PV in epics: 
        epics.caput("EPLinkam1:TEMP",1500)

        while(epics.caget("EPLinkam1:T1")<1490):
            sleep(5)
    
        for i in range(1000):
            pinhole.PinholeExp(100,30,1.0, "Linkam Stage 1500C" + i,0)  

        pinhole.PinholeExp(100,30,1.0,"Linkam Stage 1500C",0)'''
    """
    def GetMacroHeaderPart2(self):
        return """
    epics.caput("15iddSAXS:string2",EXPERIMENT)
    ###################################################################################
  
    """    
    
    def GetMacroFooter(self):
        return """
    ###################################################################################

    """
