from zk import ZK, const

conn = None
# create ZK instance
zk = ZK('192.168.1.202', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)
try:
    # connect to device
    conn = zk.connect()
    # disable device, this method ensures no activity on the device while the process is run
    conn.disable_device()
    # another commands will be here!
    # Example: Get All Users
    users = conn.get_users()
    finger = conn.get_user_template(uid=6, temp_id=5)
    fing1 = finger.template
    print('finger', fing1)

    # conn.set_user(uid=5, name='Fanani M. Ihsan', privilege=const.USER_ADMIN, group_id='', user_id='123', card=0)
    
    for user in users:
        print('user', dir(user))
        privilege = 'User'
        if user.privilege == const.USER_ADMIN:
            privilege = 'Admin'
        print ('+ UID #{}'.format(user.uid))
        print ('  Name       : {}'.format(user.name))
        print ('  Privilege  : {}'.format(privilege))
        print ('  Password   : {}'.format(user.password))
        print ('  Group ID   : {}'.format(user.group_id))
        print ('  User  ID   : {}'.format(user.user_id))
        print('user', user)
        if user.user_id == '123':
            print('call')
            # user.repack_only = ''
            conn.save_user_template(user, finger)

    # Test Voice: Say Thank You
    conn.test_voice()
    # re-enable device after all commands already executed
    conn.enable_device()
except Exception as e:
    print('eeee', e)
    print ("Process terminate : {}".format(e))
finally:
    if conn:
        conn.disconnect()