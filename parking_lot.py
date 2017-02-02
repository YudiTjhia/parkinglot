import cmd_type
import mylog
from car import car as car_class

class parking_lot:
    def __init__(self):
        self.n_lots = 0
        self.lots = []

    def __str__(self):
        return "parking_lot.py"

        
    def create_slots(self, n):
        mylog.info("parkinglot.create_slots()")
        mylog.info("[n]=" + str(n))

        
        if self.n_lots>0:
            raise Exception("Parking lots already created.")
        
        try:
            self.n_lots = int(n)
        except ValueError:
            raise Exception("Invalid Argument:" + str(n))
        

        if self.n_lots <=0:
            raise Exception("None(0) parking lot created.")

        self.lots = []        
        for index in range(self.n_lots):            
            self.lots.append(None)

        mylog.info("[RETURN]=" + str(True))
        return True


    def has_parking(self):
        if self.n_lots == 0:
            raise Exception("No Parking!.Try create_parking_lot 6")

        return True
    

    def slot_exists(self):
        mylog.info("parkinglot.slot_exists()")

        self.has_parking()

        for index in range(self.n_lots):
            if self.lots[index] == None:
                mylog.info("[RETURN][index]=" + str(index))
                return index

        
        raise Exception("Sorry, parking lot is full")

    def is_reg_no_exists(self, reg_no):
        for index in range(self.n_lots):
            car = self.lots[index]
            if car:
                if(car.number.lower() == reg_no.lower()):
                    raise Exception("Car Number=" + reg_no + " already exists.")
                    


    def park(self, reg_no, color):
        mylog.info("parkinglot.park()")
        mylog.info("[reg_no]=" + reg_no)
        mylog.info("[color]=" + color)

        self.is_reg_no_exists(reg_no)
        
        index = self.slot_exists()
        
        car_obj = car_class(reg_no, color)
        return self.park_car(car_obj, index)
    


    def park_car(self, car, index):
        mylog.info("parkinglot.park_car()")
        mylog.info("[car]=" + str(car))
        mylog.info("[index]=" + str(index))
        self.lots[index]=car
        mylog.info("[RETURN][index]=" + str(index+1))
        return (index+1)

    
    def leave(self, index):
        
        mylog.info("parkinglot.leave()")

        self.has_parking()
        
        idx = 0
        try:
            idx = int(index)
        except ValueError:
            raise Exception("Invalid Argument: " + str(index))
                            
        if(idx > self.n_lots):
            raise Exception("Invalid slot number. " +
                            " Total slot's number :" + str(self.n_lots))
        idx = idx-1
        if  self.lots[idx]:
            self.lots[idx] = None
            mylog.info("[RETURN]=True")
            return True
        else:
            raise Exception("No Car parked at slot " + str(index))


    def status(self):
        mylog.info("parkinglot.status()")

        self.has_parking()
        
        msg =       "----------------------------------------------------\n"
        msg = msg + "Slot No.\tRegistration No.\tColour\n"
        msg = msg + "----------------------------------------------------\n"
        
        for index in range(self.n_lots):
            if self.lots[index]:
                car = self.lots[index]
                if car:
                    mylog.info("[car]=" + str(car))
                    str_index = str((index+1))                
                    msg = msg + str_index.ljust(8,' ') + "\t" + car.number.ljust(16,' ') + "\t" + car.color + "\n"
        msg = msg + "----------------------------------------------------"

        mylog.info("[RETURN][msg]" + msg)
        return msg


    def get_register_no_wcolor(self, color):

        mylog.info("parkinglot.get_register_no_wcolor()")
        mylog.info("[color]=" + color)

        self.has_parking()
        
        result = []
        for index in range(self.n_lots):
            if self.lots[index]:
                car = self.lots[index]
                if car:
                    if car.color.lower() == color.lower():
                        result.append(car.number)

        mylog.info("[RETURN]=" + str(result))            
        return result
   

    def print_registration_no_car_wcolor(self, color):

        mylog.info("parkinglot.print_registration_no_car_wcolor()")
        mylog.info("[color]=" + color)

        self.has_parking()
        
        msg = ""
        car_numbers = self.get_register_no_wcolor(color)
        if len(car_numbers)>0:
            for n in car_numbers:
                msg = msg + n + ", "
            msg = msg[0:len(msg)-2]
            
        else:
            msg = "Not found"

        mylog.info("[RETURN][msg]=" + msg)            
        return msg


    def get_slot_no_wcolor(self, color):
        mylog.info("parkinglot.get_slot_no_wcolor()")
        mylog.info("[color]=" + color)

        self.has_parking()
        
        result = []
        for index in range(self.n_lots):
            if self.lots[index]:
                car = self.lots[index]
                if car:
                    if car.color.lower() == color.lower():
                        result.append(str(index+1))

        mylog.info("[RETURN]=" + str(result))   
        return result

        
    def print_slot_no_car_wcolor(self, color):
        mylog.info("parkinglot.get_slot_no_wcolor()")
        mylog.info("[color]=" + color)

        self.has_parking()
        
        msg = ""
        slot_no = self.get_slot_no_wcolor(color)
        if len(slot_no)>0:
            for n in slot_no:
                msg = msg + n + ", "
            msg = msg[0:len(msg)-2]
        else:
            msg = "Not found"

        mylog.info("[RETURN][msg]=" + msg)   
        return msg

               
    def get_slot_no_wregister_no(self, reg_no):
        mylog.info("parkinglot.get_slot_no_wregister_no()")
        mylog.info("[reg_no]=" + reg_no)

        self.has_parking()
        
        slot  = 0
        for index in range(self.n_lots):
            if self.lots[index]:
                car = self.lots[index]
                if car:
                    if car.number == reg_no:
                        slot =(index+1)

        mylog.info("[RETURN][slot]=" + str(slot))   
        return slot

        
    def print_slot_no_car_wregister(self, reg_no):
        mylog.info("parkinglot.get_slot_no_wregister_no()")
        mylog.info("[reg_no]=" + reg_no)

        self.has_parking()
        
        slot = self.get_slot_no_wregister_no(reg_no)
        if slot>0:
            msg = str(slot)
        else:
            msg= "Not found"

        mylog.info("[RETURN][msg]=" + msg)   
        return msg



    def execute(self, cmd):
        """
        CREATE_PARKING = "create_parking_lot"
        PARK = "park"
        LEAVE = "leave"
        STATUS = "status"
        PRINT_REGISTERNO_WCOLOR = "registration_numbers_for_cars_with_colour"
        PRINT_SLOTNO_WCOLOR = "slot_numbers_for_cars_with_colour"
        PRINT_SLOTNO_WREGISTERNO = "slot_numbers_for_registration_number"
        """
        mylog.info("parking_lot.execute()")
        
        msg = ""
        try:
            if cmd.cmd_type == cmd_type.CREATE_PARKING:
                if self.create_slots(cmd.argument[0]):
                    msg = "Created a parking lot with " + str(cmd.argument[0]) + " slots"
                
            elif cmd.cmd_type == cmd_type.PARK:
                index = self.park(cmd.argument[0], cmd.argument[1])
                if index>0:
                    msg = "Allocated slot number: " + str(index)

            elif cmd.cmd_type == cmd_type.LEAVE:
                if self.leave(cmd.argument[0]):
                    msg = "Slot number " + str(cmd.argument[0]) + " is free"

            elif cmd.cmd_type == cmd_type.STATUS:
                msg = self.status()

            elif cmd.cmd_type == cmd_type.PRINT_REGISTERNO_WCOLOR:
                msg = self.print_registration_no_car_wcolor(cmd.argument[0])

            elif cmd.cmd_type == cmd_type.PRINT_SLOTNO_WCOLOR:
                msg = self.print_slot_no_car_wcolor(cmd.argument[0])

            elif cmd.cmd_type == cmd_type.PRINT_SLOTNO_WREGISTERNO:
                msg = self.print_slot_no_car_wregister(cmd.argument[0])

            
        except Exception as ex:
            msg = str(ex)

        mylog.info("[Return][msg]=" +  msg)
        
        return msg + "\n"



                    
                
            

        
