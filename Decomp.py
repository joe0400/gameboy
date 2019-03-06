def bytesToHex(input):
	str = ""
	for i in input:
		hexn = b'0123456789'
		hexc = b'abcdef'
		for j in range(len(hexn)):
			if i == hexn[j]:
				str += chr(ord('0')+j)
		for k in range(len(hexc)):
			if i == hexc[k]:
				str += chr(ord('a')+k)
	return str


instdic = {b'00':"NOP",b'01':"LD BC 0x{}",b'02':"LD BC A",b'03':"INC BC",
b'04':"INC B",b'05':"DEC B", b'06':"LD B 0x{}",b'07':"RLCA",b'08':"LD 0x{}, SP",
b'09':"ADD HL, BC",b'0a':"LD A,(BC)",b'0b':"DEC BC",b'0c':"INC C",b'0d':"DEC C",
b'0e':"LD C,0x{}",b'0f':"RRCA",b'10':"STOP",b'11':"LD DE,0x{}",
b'12':"LD (DE),A",b'13':"INC DE",b'14':"INC D",b'15':"DEC D",b'16':"LD D,0x{}",
b'17':"RLA",b'18':"JR 0x{}",b'19':"ADD HL, DE",b'1a':"LD A, (DE)",b'1b':"DEC DE",
b'1c':"INC E",b'1d':"DEC E",b'1e':"LD E,0x{}",b'1f':"RRA",b'20':"JR NZ,0x{}",
b'21':"JD HL, 0x{}",b'22':"LD (HL+),A",b'23':"INC HL",b'24':"INC H",b'25':"DEC H",
b'26':"LD H,0x{}",b'27':"DAA",b'28':"JR Z,0x{}",b'29':"ADD HL,HL",
b'2a':"LD A,(HL+)",b'2b':"DEC HL",b'2c':"INC L",b'2d':"DEC L",b'2e':"LD L,0x{}",
b'2f':"CPL",b'30':"JR NC,0x{}",b'31':"LD SP,0x{}",b'32':"LD (HL-),A",
b'33':"INC SP",b'34':"INC HL",b'35':"DEC HL",b'36':"LD HL,0x{}",b'37':"SCF",
b'38':"JR C,0x{}",b'39':"ADD HL,SP",b'3a':"LD A,(HL-)",b'3b':"DEC SP",
b'3c':"INC A",b'3d':"DEC A",b'3e':"LD A,0x{}",b'3f':"CCF",
b'40':"LD B,B",b'41':"LD B,C",b'42':"LD B,D",b'43':"LD B,E",b'44':"LD B,H",b'45':"LD B,L",b'46':"LD B,(HL)",b'47':"LD B,A",
b'48':"LD C,B",b'49':"LD C,C",b'4a':"LD C,D",b'4b':"LD C,E",b'4c':"LD C,H",b'4d':"LD C,L",b'4e':"LD C,(HL)",b'4f':"LD C,A",
b'50':"LD D,B",b'51':"LD D,C",b'52':"LD D,D",b'53':"LD D,E",b'54':"LD D,H",b'55':"LD D,L",b'56':"LD D,(HL)",b'57':"LD D,A",
b'58':"LD E,B",b'59':"LD E,C",b'5a':"LD E,D",b'5b':"LD E,E",b'5c':"LD E,H",b'5d':"LD E,L",b'5e':"LD E,(HL)",b'5f':"LD E,A",
b'60':"LD H,B",b'61':"LD H,C",b'62':"LD H,D",b'63':"LD H,E",b'64':"LD H,H",b'65':"LD H,L",b'66':"LD H,(HL)",b'67':"LD H,A",
b'68':"LD L,B",b'69':"LD L,C",b'6a':"LD L,D",b'6b':"LD L,E",b'6c':"LD L,H",b'6d':"LD L,L",b'6e':"LD L,(HL)",b'6f':"LD L,A",
b'70':"LD (HL),B",b'71':"LD (HL),C",b'72':"LD (HL),D",b'73':"LD (HL),E",b'74':"LD (HL),H",b'75':"LD (HL),L",b'76':"HALT",b'77':"LD (HL),A",
b'78':"LD A,B",b'79':"LD A,C",b'7a':"LD A,D",b'7b':"LD A,E",b'7c':"LD A,H",b'7d':"LD A,L",b'7e':"LD A,(HL)",b'7f':"LD A,A",
b'80':"ADD A,B",b'81':"ADD A,C",b'82':"ADD A,D",b'83':"ADD A,E",b'84':"ADD A,H",b'85':"ADD A,L",b'86':"ADD A,(HL)",b'87':"ADD A,A",
b'88':"ADC A,B",b'89':"ADC A,C",b'8a':"ADC A,D",b'8b':"ADC A,E",b'8c':"ADC A,H",b'8d':"ADC A,L",b'8e':"ADC A,(HL)",b'8f':"ADC A,A",
b'90':"SUB B",b'91':"SUB C",b'92':"SUB D",b'93':"SUB E",b'94':"SUB H",b'95':"SUB L",b'96':"SUB (HL)",b'97':"SUB A",
b'98':"SBC A,B",b'99':"SBC A,C",b'9a':"SBC A,D",b'9b':"SBC A,E",b'9c':"SBC A,H",b'9d':"SBC A,L",b'9e':"SBC A,(HL)",b'9f':"SBC A,A",
b'a0':"AND B",b'a1':"AND C",b'a2':"AND D",b'a3':"AND E",b'a4':"AND H",b'a5':"AND L",b'a6':"AND (HL)",b'a7':"AND A",
b'a8':"XOR B",b'a9':"XOR C",b'aa':"XOR D",b'ab':"XOR E",b'ac':"XOR H",b'ad':"XOR L",b'ae':"XOR (HL)",b'af':"XOR A",
b'b0':"OR B",b'b1':"OR C",b'b2':"OR D",b'b3':"OR E",b'b4':"OR H",b'b5':"OR L",b'b6':"OR (HL)",b'b7':"OR A",
b'b8':"LD B",b'b9':"LD C",b'ba':"LD D",b'bb':"LD E",b'bc':"LD H",b'bd':"LD L",b'be':"LD (HL)",b'bf':"LD A",
b'c0':"RET NZ",b'c1':"POP BC",b'c2':"JP NZ 0x{}",b'c3':"JP 0x{}",
b'c4':"CALL NZ, 0x{}",b'c5':"PUSH BC",b'c6':"ADD A,0x{}",b'c7':"RST 00H",
b'c8':"RET Z",b'c9':"RET",b'ca':"JP Z, 0x{}",b'cb':"CB PREFIXES",
b'cc':"CALL Z,0x{}",b'cd':"CALL 0x{}",b'ce':"ADC A,0x{}",b'cf':"RST 00H",
b'd0':"RET NC",b'd1':"POP DE",b'd2':"JP NC,0x{}",b'd4':"CALL NC,0x{}",
b'd5':"PUSH DE",b'd6':"SUB 0x{}",b'd7':"RST 10H",b'd8':"RET C",b'd9':"RETI",
b'da':"JP C, 0x{}",b'dc':"CALL C,0x{}",b'de':"SBC A,0x{}",b'df':"RST 18H",
b'e0':"LDH (0x{}),A",b'e1':"POP HL",b'e2':"LD (C+0x{}),A",b'e5':"PUSH HL",
b'e6':"AND 0x:{}",b'e7':"RST 20H",b'e8':"ADD SP, 0x{}",b'e9':"JP (HL)",
b'ea':"LD (0x{}), A",b'ee':"XOR 0x{}",b'ef':"RST 20H",
b'f0':"LDH A,(0x{})",b'f1':"POP AF",b'f2':"LD A,(c+0x{}",b'f3':"DI",
b'f5':"PUSH AF",b'f6':"OR 0x{}",b'f7':"RST 30H",b'f8':"LD HL, SP+0x{}",
b'f9':"LD SP,HL",b'fa':"LD A,(0x{})",b'fb':"EI",b'fe':"CP 0x{}",b'ff':"RST 38H"
}
size1 = [b'10',b'20',b'30',b'06',b'16',b'26',b'36',b'18',b'28',b'38',b'0e',b'1e',b'2e',b'3e',b'c6',b'd6',b'e6',b'f6',b'ce',b'de',b'ee',b'fe',b'e0',b'f0',b'e2',b'f2',b'e8',b'f8',b'c8']
size2 = [b'01',b'11',b'21',b'31',b'08',b'c2',b'd2',b'c3',b'c4',b'd4',b'ca',b'da',b'ea',b'fa',b'cc',b'dc',b'cd']


f = open('DMG_ROM.bin',"rb")

bytes = bytes(f.read().hex(),'utf-8')
i = 0
#print(bytes)
dat = True
while(i < len(bytes)):
	if(dat):
		try:
			if not (bytes[i:i+2] in size1 or bytes[i:i+2] in size2):
				print(instdic[bytes[i:i+2]])
				i += 2
			elif bytes[i:i+2] in size1:
				print(instdic[bytes[i:i+2]].format(bytesToHex(bytes[i+2:i+4])))
				i += 4
			else:
				print(instdic[bytes[i:i+2]].format(bytesToHex(bytes[i+2:i+6])))
				i += 6
		except:
			dat = not dat
	else:
		try:
			instdic[bytes[i:i+2]]
		except:
			dat = not dat
		print(bytesToHex(bytes[i:i+2]),end=', ')
		i += 2
		#print("failed here")
f.close()
