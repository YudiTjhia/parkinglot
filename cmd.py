class cmd:
    def __init__(self,cmd_type, n_argument):        
        self.cmd_type = cmd_type
        self.argument = []
        self.n_argument = n_argument
        
    
    def parse(self, cmd_str):        
        words = cmd_str.split(" ")
        self.argument = []
        if len(words)>0:
            for w in words:
                w = w.strip()

            cmd_ = words[0]
            if cmd_ == self.cmd_type:

                len_words = len(words)
                if len_words <> (self.n_argument+1):
                    raise Exception(cmd_ + " needs " + str(self.n_argument) + " argument(s)")
                
                for i, p in enumerate(words):
                    if i>0:
                        self.argument.append(p)

                return True
                    

        return False


    
    def __str__(self):
        return "cmd_type=" + self.cmd_type + ", argument=" + str(self.argument)
        
    
    
    
