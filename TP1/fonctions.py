def prime_numbers(un_entier):
    liste = []
    for num in range(1, un_entier) :
        for div in range(2, num) :
            if num%div == 0 :
                break
        else :
            liste.append(num)
    return liste



def factorial(n):
    if n < 2 :
        return n
    return factorial(n-1)*n



def display_file(filename):
    f = open(filename)
    count = 1
    for line in f:
        print(count," : ", line)
        count += 1;
        

        
def stat_file(filename):
    f = open(filename)
    text = f.read()
    tableauMot = {}
    
    mots = text.split()    
    for unMot in mots:
        if unMot in tableauMot:
            tableauMot[unMot] += 1
        else:
            tableauMot[unMot] = 1
            
    return tableauMot



def main():
    #print(stat_file("test.txt"))
    #result = [i*i for i in range(100)] #B1
    #result = [i*i for i in range(100) if i*i < 100] #B2
    #result = [i for i in range(100) if i%7 == 0] #B4
    result = [(float(line.split(";")[0])) for line in open("test.txt")]
    print(result)

if __name__ == "__main__":main()
            