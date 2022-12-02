
letters = {
    "A":10,
    "B":11,
    "C":12,
    "D":13,
    "E":14,
    "F":15,
    "G":16,
    "H":17,
    "I":18,
    "J":19,
    "K":20,
    "L":21,
    "M":22,
    "N":23,
    "O":24,
    "P":25,
    "Q":26,
    "R":27,
    "S":28,
    "T":29,
    "U":30,
    "V":31,
    "W":32,
    "X":33,
    "Y":34,
    "Z":35

}

#test
l1 = "P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<"
l2=""




def get_digit(string, length):

    weight =[7,3,1,7,3,1,7,3,1]

    sum =0
    y =0

    for x in string:


        if x.isnumeric():
            prod1 = x*weight[y]
            y =y+1
            sum = sum + prod1

        elif x == "<":
            y =y+1
            #sum = sum + prod1
 
        else:
            letters[x]*weight[y]
            y =y+1
            sum = sum + prod1
    
    return sum%10


def check_digit(a,b):
    if a == get_digit(b):
        return True

    else:
        return False
    pass




def decode(l1,l2):
    l1c1 = l1.split("<<")
    #l2c = l2.split("")

    l1c2 = l1c1[0].split("<")
    doc_type = l1c2[0]
    print("test: "+str(l1c2[1]))
    #l1c2_2 = str(l1c2[1]).split("")
    country =""
    for x in range(3):
        country = country + l1c2[1][x]
    
    last_name = ""

    for y in range(3, len(l1c2[1])):
        last_name = last_name + l1c2[1][y]

    l1c3 = l1c1[1].split("<")
    first_name = l1c3[0]
    middle_name = l1c3[1]

    print ("Document Type: "+doc_type+", Country: "+country+ ", First Name: "+first_name+", Middle Name: "+middle_name+", Last Name: "+last_name)

    pn = l2[0:8]
    cd_pn = l2[9]
    cc = l2[10:12]
    bd = l2[13:18]
    cd_bd = l2[19]
    sex = l2[20]
    exp = l2[21:26]
    cd_exp = l2[27]
    prn = l2[28:36]
    cd_prn = l2[:1]

    if check_digit(pn,cd_pn) and check_digit(bd,cd_bd) and check_digit(exp,cd_exp) and check_digit(prn,cd_prn):

        print("Check digits have matched")
        
    else:
        print("Check digits did NOT match")
        if not check_digit(pn,cd_pn):
            print("Passport number and its check digits did NOT match")

        if not check_digit(bd,cd_bd):
            print("Birth date and its check digits did NOT match")

        if not check_digit(exp,cd_exp):
            print("Expiration date and its check digits did NOT match")

        if not check_digit(prn,cd_prn):
            print("Personal number and its check digits did NOT match")
        


def encode(dt, c, ln, fn, mn, pn, cc, bd, s, ed, prn):

    #44
    l1_c = dt+c+ln+fn+mn
    emp_len = 44-4-len(l1_c)
    end = ""
    for r in range(emp_len):
        end = end + "<"

    ln1 = dt+"<"+c+ln+"<<"+fn+"<"+mn+end

    l2_c = pn+cc+bd+s+ed+prn+4


    emp2_len = 44-len(l2_c)
    end2 = ""
    for k in range(emp2_len):
        end2 = end2 + "<"


    ln2 = pn+str(get_digit(pn,9))+cc+bd+str(get_digit(bd,6))+s+ed+str(get_digit(ed,6))+prn+end2+str(get_digit(prn,9))

    return ln1,ln2


    




 
        
        


    


decode(l1,l2)


    

    