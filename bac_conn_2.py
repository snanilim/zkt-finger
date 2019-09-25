from zk import ZK, const

conn201 = None
conn202 = None
# create ZK instance
zk201 = ZK('192.168.1.201', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)
zk202 = ZK('192.168.1.202', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)
try:
    # connect to device
    conn201 = zk201.connect()
    conn202 = zk202.connect()
    # disable device, this method ensures no activity on the device while the process is run
    conn201.disable_device()
    conn202.disable_device()

    # another commands will be here!
    # Example: Get All Users
    users = conn202.get_users()
    finger = conn202.get_user_template(uid=5, temp_id=5)
    print('finger', finger.template)

    for user in users:
        print('user', user)
        privilege = 'User'

        print ('+ UID #{}'.format(user.uid))
        print ('  Name       : {}'.format(user.name))
        print ('  Privilege  : {}'.format(privilege))
        print ('  Password   : {}'.format(user.password))
        print ('  Group ID   : {}'.format(user.group_id))
        print ('  User  ID   : {}'.format(user.user_id))

        if user.user_id == '123':
            print('201 call')
            # conn201.set_user(uid=user.uid, name=user.name, privilege=user.privilege, password=user.password, group_id=user.group_id, user_id=user.user_id, card=user.card)
            conn201.save_user_template(user, finger)

    # Test Voice: Say Thank You
    # re-enable device after all commands already executed
    conn201.test_voice()
    conn201.enable_device()

    conn202.test_voice()
    conn202.enable_device()
except Exception as e:
    print('eeee', e)
    print ("Process terminate : {}".format(e))
finally:
    if conn201:
        conn201.disconnect()
    if conn202:
        conn202.disconnect()