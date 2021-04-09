def swAP():
    blehblehbleh = input("First File Name : ")
    dorarora = input("Second File Name : ")
    with open (blehblehbleh, "r") as a:
        ba = a.read()
    with open (dorarora, "r") as b:
        da = b.read()
    with open (blehblehbleh, "w") as a:
        a.write(da)
    with open (dorarora, "w") as b:
        b.write(ba)

swAP()  