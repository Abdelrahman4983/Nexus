from workers.organizer import Organizer
import time

start = time.time()
print('\n Phase4 \n')
org = Organizer('railway',
                'postgres',
                'ba**64B3f3*dd521Egef3g4*B-E-cA-3',
                'viaduct.proxy.rlwy.net',
                '36793')
org.create_tables()
end = time.time()
print("Calculated time for Organizer: ",end - start)
