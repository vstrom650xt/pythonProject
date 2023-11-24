#1 y 2
if __name__ == '__main__':
 nm = 'X-DSPAM-Confidence: 0.8475'
 enc= nm.find(' ')
 a= float(nm[enc+1:len(nm)])
 print(a)
 b = round(a,2)
 print(b)
#3
if __name__ == '__main__':
 nm = 'X-DSPAM-Confidence: 0.8475'
 a= nm[2:len(nm)]
 print(a)
