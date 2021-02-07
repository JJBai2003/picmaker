def main():
    pic = open('final.ppm','w')
    pic.write('P3 500 500 255 \n')
    colors = ''
    for i in range(500):
        for j in range(500):
            if i > 0 and j >0 and i % j > 13:
                r = (i **2 + i // 10) % 256
                b = (j **2 + j // 20) % 256
                g = ((i + j) **2 + 5) % 256
            elif i >= j:
                r = i **2 % 256
                b = (i + j) **2 % 256
                g = j **2 % 256
            elif j >= i:
                r = ((i + j) **2 +25) % 256
                b = (i **2 + 25) % 256
                g =( j **2 +25) % 256
            else:
                r = 0
                b = 0
                g = 0 
            colors += str(r) + ' '+ str(b) +' '+str(g) + '\n'
        pic.write(colors)
    pic.close

main()
