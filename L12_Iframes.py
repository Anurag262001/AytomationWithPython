#switch_to_frame(webelement)
#switch_to_frame(0)
#switch_to_frame(id of the frame)
#switch_to_frame(name of the frame)
from idlelib.debugger_r import frametable

defaultpage---> parentframe---> child frametable (innerframe)
child back to parent frame
driver.switch_to.parent_frame()  #this will directly switch to the parent frame
driver.switch_to.default_content() #this will directly switch to default page

