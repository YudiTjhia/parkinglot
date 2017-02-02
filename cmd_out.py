import threading
import time
import mylog

class cmd_out(threading.Thread):
    
    def __init__(self, cmd_registry, use_thread):
        
        threading.Thread.__init__(self)
        
        self.use_thread= use_thread
        self.cmd_registry = cmd_registry
        
        if not self.use_thread:
            self.cmd_registry.on_output_added = self.on_output_added
            
        self.running = False
        self.on_exit = None


    def run(self):
        self.running = True
        mylog.info('cmd_out thread started')
        
        while self.running==True:
            try:
                output = self.cmd_registry.output.get_nowait()
                if output == "exit":
                    self.running=False
                    if self.on_exit:
                        self.on_exit()
                else:
                    print output
            except:
                pass
            
            #print "cmd_out.running=true"
            time.sleep(0.1)
            
    
    def stop(self):
        self.running = False

    def on_output_added(self):
        output = self.cmd_registry.output.get_nowait()
        print output
