import time
def create_order_id(user_id):
    id = str(user_id) +'_'+ str(int(time.time()*1000))
    return id