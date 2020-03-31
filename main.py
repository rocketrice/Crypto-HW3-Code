from aes import AES_128

if __name__=="__main__":
    key = "2b7e151628aed2a6abf7158809cf4f3c".decode('hex')
    #key = "000102030405060708090a0b0c0d0e0f".decode('hex')
    check = (
            #("00112233445566778899aabbccddeeff", "69c4e0d86a7b0430d8cdb78070b4c55a"),
            ("6bc1bee22e409f96e93d7e117393172a", "3ad77bb40d7a3660a89ecaf32466ef97"),
            ("ae2d8a571e03ac9c9eb76fac45af8e51", "f5d3d58503b9699de785895a96fdbaaf"),
            ("30c81c46a35ce411e5fbc1191a0a52ef", "43b1cd7f598ece23881b00e3ed030688"),
            ("f69f2445df4f9b17ad2b417be66c3710", "7b0c785e27e8ad3f8223207104725dd4"),
            )
    crypt = AES_128()
    crypt.key = key
    for c in check:
        p = c[0].decode('hex')
        v = c[1].decode('hex')
        t = crypt.cipher(p)
        if t == v:
            print("yay!")
        else:
            print("{0} != {1}".format(t.encode('hex'), c[1]))
        t = crypt.inv_cipher(v)
        if t == p:
            print("yay!")
        else:
            print("{0} != {1}".format(t.encode('hex'), c[1]))
