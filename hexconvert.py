import numpy as np


###### CONVERTERS  ##################3
def decToHex(x, numHex):
	string = "{0:0" + str(numHex) + "x}";
	return string.format(x);

def decToBinary(x, numBits): # If 7 for example it can't be less than the bits it takes to represent 7. 
	string = "{0:0" + str(numBits) + "b}";
	return string.format(x)

def hexToDec(x):
	return int(x, 16)
def binaryToDec(x):
	return int(x, 16)

def countBits(xBinary):
	return len(xBinary)



############# Test vector

def convert_test_vector(bitstring):
	a = [bitstring[i:i+8] for i in range(0, len(bitstring), 8)] # slices them up 8 by 8 bits.
	return ''.join(i[::-1] for i in a) # Join them in backward direction (bits) # http://stackoverflow.com/questions/9027862/what-does-listxy-do x[startAt:endBefore:skip] -1 converts the list backwards



def testbench(): 
	f = open('test.txt', 'w')

	IVBits = [69]
	KeyBits = []

	Length = len(KeyBits) + len(IVBits);
	OffsetKey = 128

	k = 0
	offsetafter = 73;
	for i in range(0, len(IVBits)):
	
		f.write('"' + decToBinary(k,8) + '' + decToBinary(96-1 - IVBits[i], 8) + '" after period *' + str(73 + k*2)+',\n')
		k += 1
	for ii in range(0, len(KeyBits)):
		f.write('"' + decToBinary(k,8) + '' + decToBinary(96 + (128 -1) - KeyBits[ii], 8) + '" after period *' + str(73 + k*2)+',\n')
		k += 1

#testbench()




def hexResultConvert(hexString): # but in hex result here. 
	binofHex = bin(int(hexString,16))[2:].zfill(len(hexString)*8) # Removes first two 0b and adds up so the length becomes 32*8 =256 bits. 
	binofHex8bits = [binofHex[i:i+8] for i in range(0, len(binofHex), 8)] # slices them up 8 by 8 bits.
	binConvertString = ''.join(i[::-1] for i in binofHex8bits) # Join them in backward direction (bits) # http://stackoverflow.com/questions/9027862/what-does-listxy-do x[startAt:endBefore:skip] -1 converts the list backwards
	
	result = hex(int(binConvertString, 2));
	resultHex = result[2:len(result)-1];

	return resultHex.zfill(len(hexString)); # 64 hex = 64*4 bits. Our length of the bit convert adds a L for long at the end and 0x at the beginning. 

print("HexConvertResult: " + str(hexResultConvert("00000000000000000000000000000000000000000000602ac6e336d945ae3dcf"))  + "")



#####
print("" +hexResultConvert("000102030405060708090A0B0C0D0E0F"));

def convert():
	a = 0x1fffffffd3c0b1d3798e350d6ece80fb
	a_conv = bin(a)[2:].zfill(32*4)
	a_conv = convert_test_vector(a_conv)
	print a_conv
	a_conv = int(a_conv, 2)
	print hex(a_conv)
	b = 0xF8FFFFFFCB03CDE38C71EEF685F2168D
	print hex(a_conv ^ b)[2:].zfill(32)

#convert()


	
		


