
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
#l1 = "P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<"
#l1 =  "P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<"
#l2= "L898902C36UTO7408122F1204159ZE184226B<<<<<<1"

#l1 = "P<CIVLYNN<<NEVEAH<BRAM<<<<<<<<<<<<<<<<<<<<<<"
#l2 = "W620126G54CIV5910106F9707302AJ010215I<<<<<<6"

record = "P<CIVLYNN<<NEVEAH<BRAM<<<<<<<<<<<<<<<<<<<<<<;W620126G54CIV5910106F9707302AJ010215I<<<<<<6"






def get_digit(string):
    #, length

    weight =[7,3,1,7,3,1,7,3,1]

    sum =0
    y =0

    for x in string:


        if x.isnumeric():
            prod1 = int(x)*weight[y]
            y =y+1
            sum = sum + prod1

        elif x == "<":
            y =y+1
            #sum = sum + prod1
 
        else:
            prod2 = letters[x]*weight[y]
            y =y+1
            sum = sum + prod2
   #print(sum%10)
    return sum%10


def check_digit(a,b):
    if int(b) == get_digit(a):
        return True

    else:
        return False
    pass


def scan():
    pass

def data_base():
    pass

def decode(record):
    l1 = record.split(";")[0]
    l2 = record.split(";")[1]
    l1c1 = l1.split("<<")
    #l2c = l2.split("")

    l1c2 = l1c1[0].split("<")
    doc_type = l1c2[0]
    #print("test: "+str(l1c2[1]))
    #l1c2_2 = str(l1c2[1]).split("")
    country =""
    for x in range(3):
        country = country + l1c2[1][x]
    
    last_name = ""

    for y in range(3, len(l1c2[1])):
        last_name = last_name + l1c2[1][y]

    l1c3 = l1c1[1].split("<")
    first_name = l1c3[0]
    #print (l1c3)
    if len(l1c3) == 1:
        middle_name = ""
    else:
        middle_name = l1c3[1]

    print ("Document Type: "+doc_type+", Country: "+country+ ", First Name: "+first_name+", Middle Name: "+middle_name+", Last Name: "+last_name)

    pn = l2[0:9]
    cd_pn = l2[9]
    cc = l2[10:13]
    bd = l2[13:19]
    cd_bd = l2[19]
    sex = l2[20]
    exp = l2[21:27]
    cd_exp = l2[27]
    prn = l2[28:37]

    #cd_prn = l2[:1]
    l2_last = l2.split("<")
    #cd_prn = l2[:1]
    cd_prn = l2_last[-1]

    print("passport_number: "+pn+", country_code: "+cc+", birth_date: "+bd+", sex: "+sex+", expiration_date: "+exp+", personal_number: "+prn)
    print("CD PN: "+cd_pn+" CD BD: "+cd_bd+ " CD EXP: "+cd_exp+" CD PRN: "+str(cd_prn))



def mismatch(record):
    l2 = record.split(";")[1]

    
    pn = l2[0:9]
    cd_pn = l2[9]
    cc = l2[10:13]
    bd = l2[13:19]
    cd_bd = l2[19]
    sex = l2[20]
    exp = l2[21:27]
    cd_exp = l2[27]
    prn = l2[28:37]
    l2_last = l2.split("<")
    #cd_prn = int(l2[:1])
    cd_prn = int(l2_last[-1])

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
        


#def encode(dt, c, ln, fn, mn, pn, cc, bd, s, ed, prn):

def encode(decoded_array):

    #decoded_array
    dt = "P"
    c = decoded_array["line1"]["issuing_country"]
    ln = decoded_array["line1"]["last_name"]

    name = decoded_array["line1"]["given_name"]
    if len(name.split(" ")) == 1:
        fn = name
        mn =""
    else:
        fn = name.split(" ")[0]
        mn = name.split(" ")[1]
    
    pn = decoded_array["line2"]["passport_number"]
    cc = decoded_array["line2"]["country_code"]
    bd = decoded_array["line2"]["birth_date"]
    s = decoded_array["line2"]["sex"]
    ed = decoded_array["line2"]["expiration_date"]
    prn = decoded_array["line2"]["personal_number"]


    #44
    l1_c = dt+c+ln+fn+mn
    emp_len = 44-4-len(l1_c)
    end = ""
    for r in range(emp_len):
        end = end + "<"

    ln1 = dt+"<"+c+ln+"<<"+fn+"<"+mn+end

    l2_c = pn+cc+bd+s+ed+prn


    emp2_len = 44-len(l2_c)-4
    end2 = ""
    for k in range(emp2_len):
        end2 = end2 + "<"


    ln2 = pn+str(get_digit(pn))+cc+bd+str(get_digit(bd))+s+ed+str(get_digit(ed))+prn+end2+str(get_digit(prn))

    #return ln1,ln2
    print(ln1+";"+ln2)
    return (ln1+";"+ln2)


decode(record)
mismatch(record)

decoded_array = {
            "line1": {
                "issuing_country": "CIV",
                "last_name": "LYNN",
                "given_name": "NEVEAH BRAM"
            },
            "line2": {
                "passport_number": "W620126G5",
                "country_code": "CIV",
                "birth_date": "591010",
                "sex": "F",
                "expiration_date": "970730",
                "personal_number": "AJ010215I"
            }
        }


encode(decoded_array)


#P<CIVLYNN<<NEVEAH<BRAM<<<<<<<<<<<<<<<<<<<<<<;W620126G54CIV5910106F9707302AJ010215I<<<<<<6
#P<CIVLYNN<<NEVEAH<BRAM<<<<<<<<<<<<<<<<<<<<<<;W620126G54CIV5910106F9707302AJ010215I<<<<<<6