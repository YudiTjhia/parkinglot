import threading
import Queue
import time
import mylog

class cmd_registry(threading.Thread):
#class cmd_registry:
    
    def __init__(self, use_thread):
        threading.Thread.__init__(self)
        self.cmds = []
        self.programs = []
        self.use_thread = use_thread
        
        self.running = False
        self.cmd_q = Queue.Queue()
        self.output = Queue.Queue()
        self.on_output_added = None

        self.on_exit = None
        
    def add_program(self, program):
        self.programs.append(program)
        mylog.info("cmd_registry.add_program>" + str(program))

        
    def add_cmd_q(self, cmd_str):
        self.cmd_q.put_nowait(cmd_str)
        mylog.info("cmd_registry.add_cmd_q>cmd_str=" + cmd_str)
        if not self.use_thread:
            self.dequeue_cmd_q()
            
        
    def add_cmd(self, cmd):
        mylog.info("cmd_registry.add_cmd>cmd=>" + str(cmd))
        for c in self.cmds:
            if c.cmd_type == cmd.cmd_type:
                raise Exception("Command Type already registered: " + str(cmd.cmd_type))

        self.cmds.append(cmd)


    def stop(self):
        self.running = False
        
        
    def run(self):
        self.running = True
        mylog.info("cmd_registry thread started.")
        while self.running==True:
            try:
                
                cmd_str = self.cmd_q.get_nowait()
                if cmd_str=="exit":
                    self.running =False
                    if self.on_exit:
                        self.on_exit()
                else:
                    self.parse_cmd(cmd_str)                

            except Queue.Empty:
                pass
            except Exception as ex:
                self.add_output(str(ex))
                

            #print "cmd_registry.running=true"
            time.sleep(0.1)            

            
    def dequeue_cmd_q(self):
        mylog.info("cmd_registry.dequeue_cmd_q()")
        try:
            cmd_str = self.cmd_q.get_nowait()
            self.parse_cmd(cmd_str)                
        except:
            pass


    def add_output(self, msg):
        mylog.info("cmd_registry.add_output=" + msg)
        self.output.put_nowait(msg)
        if self.on_output_added:
            self.on_output_added()
        


    def parse_cmd(self, cmd_str):        
        mylog.info("cmd_registry.parse_cmd")
        mylog.info("[cmd_str]=" + cmd_str)

        found = False
        for cmd in self.cmds:
            if cmd.parse(cmd_str)==True:                
                self.parse_cmd_(cmd)
                found = True
                break

        if not found:
            self.add_output("Invalid Command : " + cmd_str)

        
    def parse_cmd_(self, s_cmd):        
        mylog.info("cmd_registry.parse_cmd_()")
        mylog.info("[s_cmd]=" + str(s_cmd))

        """
        if s_cmd.cmd_type == cmd_type.EXIT:
            self.add_output(s_cmd.cmd_type)
            self.running = False
            if self.on_exit:
                self.on_exit()
            return
        """
        
        for i, p in enumerate(self.programs):
            mylog.info("prgram=" + str(p))
            msg = p.execute(s_cmd)
            if len(msg)>0:
                self.add_output(msg)


    
"""
CREATE_PARKING = "create_parking_lot"
PARK = "park"
LEAVE = "leave"
STATUS = "status"
PRINT_REGISTERNO_WCOLOR = "registration_numbers_for_cars_with_colour"
PRINT_SLOTNO_WCOLOR = "slot_numbers_for_cars_with_colour"
PRINT_SLOTNO_WREGISTERNO = "slot_numbers_for_registration_number"
"""
def init(cmd_registry):
    import cmd_type
    from cmd import cmd
    from parking_lot import parking_lot
    
    cmd_registry.add_cmd(cmd(cmd_type.CREATE_PARKING,1))
    cmd_registry.add_cmd(cmd(cmd_type.PARK,2))
    cmd_registry.add_cmd(cmd(cmd_type.LEAVE,1))
    cmd_registry.add_cmd(cmd(cmd_type.STATUS,0))
    cmd_registry.add_cmd(cmd(cmd_type.PRINT_REGISTERNO_WCOLOR,1))
    cmd_registry.add_cmd(cmd(cmd_type.PRINT_SLOTNO_WCOLOR,1))
    cmd_registry.add_cmd(cmd(cmd_type.PRINT_SLOTNO_WREGISTERNO,1))
    cmd_registry.add_cmd(cmd(cmd_type.EXIT,0))


    cmd_registry.add_program(parking_lot())
        



