import rekins
print("programma rekina sagatavosana")

def lietotaja_ievadi():
    vards = input()
    veltijuma_teksts = input()
    platums = input("platums")
    garums = input ()
    augstums = input ()
    materialcena = input

    return vards,veltijuma_teksts, platums, garums, augstums, materialcena

if __name__ == '__rekins__':
    print_info()
    while 1>0:
        lietotaja_ievadi()
        rekins = rekins.Rekins()
        run_again = input()
        if run_again == 1:
            continue
        else:
            exit(0)