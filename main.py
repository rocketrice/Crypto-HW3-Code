from aes import AES_128

if __name__=="__main__":
    key = "0f1571c947d9e8591cb7add6af7f6798".decode('hex')

    crypt = AES_128()
    crypt.key = key

    # encrypt
    p = "0123456789abcdeffedcba9876543210".decode('hex')
    c = crypt.cipher(p)
    print c.encode('hex')

    # decrypt
    p = crypt.inv_cipher(c)
    print p.encode('hex')

    print "\n\nThis is for the Avalanche Compare:"

    base = "8123456789abcdeffedcba9876543210"
    trial1 = "8123456789abcdeffedcba9876543211"
    trial2 = "8123456789abcdeffedcba9876543212"
    trial3 = "8123456789abcdeffedcba9876543214"

    print "Base\t: {0} : {1}".format(base, crypt.cipher(base.decode('hex')).encode('hex'))
    print "Round 1\t: {0} : {1}".format(base, crypt.cipher(trial1.decode('hex')).encode('hex'))
    print "Round 2\t: {0} : {1}".format(base, crypt.cipher(trial2.decode('hex')).encode('hex'))
    print "Round 3\t: {0} : {1}".format(base, crypt.cipher(trial3.decode('hex')).encode('hex'))