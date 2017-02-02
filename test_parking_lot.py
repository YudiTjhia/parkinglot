from parking_lot import parking_lot
import mylog

class test_parking_lot:
    def __init__(self):
        self.parking_lot = parking_lot()
        self.results = []
        self.c = test_parking_lot.__name__
    

    def test_create_slots(self, n):
        
        m = self.test_create_slots.__name__
        result = False
        try:
            result = self.parking_lot.create_slots(n)
        except:
            pass
        self.results.append(self.c + m + "=" + str(result))
        
        
    def test_park(self, reg_no, color):
        m = self.test_park.__name__
        result = False
        try:
            index = self.parking_lot.park(reg_no, color)
            if index>0:
                result = True
        except:
            pass        
        self.results.append(self.c + m + "=" + str(result))

        
        
    def test_get_register_no_wcolor(self, color):
        m = self.test_get_register_no_wcolor.__name__
        result = False
        try:
            r = self.parking_lot.get_register_no_wcolor(color)
            if len(r) >0:
                result = True
        except:
            pass        
        self.results.append(self.c + m + "=" + str(result))


    def test_get_slot_no_wcolor(self, color):
        m = self.test_get_slot_no_wcolor.__name__
        result = False
        try:
            r = self.parking_lot.get_slot_no_wcolor(color)
            if len(r) >0:
                result = True
        except:
            pass        
        self.results.append(self.c + m + "=" + str(result))
        

    def test_get_slot_no_car_wregister(self, reg_no):
        m = self.test_get_slot_no_car_wregister.__name__
        result = False
        try:
            r = self.parking_lot.get_slot_no_wregister_no(reg_no)
            if r >0:
                result = True
        except:
            pass        
        self.results.append(self.c + m + "=" + str(result))


    def test_slot_no_wregno_not_found(self, reg_no):
        m = self.test_slot_no_wregno_not_found.__name__
        result = False
        try:
            r = self.parking_lot.get_slot_no_wregister_no(reg_no)
            if int(r) == 0:
                result = True
        except:
            pass        
        self.results.append(self.c + m + "=" + str(result))


    def test_leave(self, n):
        m = self.test_leave.__name__
        try:
            result = self.parking_lot.leave(n)
        except:
            pass        
        self.results.append(self.c + m + "=" + str(result))

        
    def print_results(self):
        for i in range(len(self.results)):
            msg = self.results[i]
            mylog.info(msg)
            print msg



    
if __name__ == "__main__":
    
    test = test_parking_lot()
    test.test_create_slots(6)
    test.test_park("KA-01-HH-2701", "Blue")
    test.test_get_register_no_wcolor("Blue")
    test.test_get_slot_no_wcolor("Blue")
    test.test_get_slot_no_car_wregister("KA-01-HH-2701")
    test.test_slot_no_wregno_not_found("MH-04-AY-1111")
    test.test_leave(1)
    test.print_results()
        
