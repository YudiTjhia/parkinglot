#!/usr/local/bin/python

import sys
from cmd_registry import cmd_registry as cmd_reg
import cmd_registry as mod_cmd_reg
from cmd_out import cmd_out

class my_program:
    
    def __init__(self):
        self.cmd_registry = cmd_reg(False)
        
        #init all commands here
        mod_cmd_reg.init(self.cmd_registry)
        self.cmd_out = cmd_out(self.cmd_registry, False)
        
        try:
            if len(sys.argv)==2:
                self.parse_file(sys.argv[1])
            else:
                self.shell()
                
        except Exception as ex:
            print str(ex)

        
    def parse_file(self, filename):
        f = None
        try:
            f = open(filename)
            for line in f:
                line = line.strip()                
                if len(line)>0:
                    self.cmd_registry.add_cmd_q(line)
                    
        except:
            raise
        finally:
            
            if f:
                f.close()
                f = None

                            
    def shell(self):
        cmd_str = ""
        print "Type command ['exit' to end]:"

        try:
            while(cmd_str!="exit"):
                cmd_str = raw_input("")
                if(cmd_str!="exit"):
                    self.cmd_registry.add_cmd_q(cmd_str.strip())
        except:
            raise
        
            
            

if __name__ == "__main__":
    
    p = my_program()
