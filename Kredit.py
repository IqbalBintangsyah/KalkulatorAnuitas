import numpy as np
import pandas as pd
from sympy import *

def HitungBunga(harga, dp, a, t):
	'''
	Inisialisasi Variabel
	'''
	i = symbols("i")						#bunga -> yang dicari
	p = harga - dp							#pinjaman pokok
	'''
	Manipulasi aljabar
	'''
	f = expand((1+i)**t)
	g = f-1
	f = p*f
	g, r = div(g, i, domain='QQ')
	g = a*g
	eq = f - g
	coeff = Poly(eq, i)
	res = np.poly1d(coeff.coeffs())
	sol = res.r

	for s in sol:
		if(np.isreal(s)):
			bunga = np.real(s)
			bunga = bunga*100
			bunga = round(bunga, 2)
			return (str(bunga) + "%")

def main():
	#Membuka file excel
	data = pd.read_excel(r'file_here')
	#mengasosiasikan header kolom jangka waktu dengan integer
	time11 = pd.DataFrame(data, columns=['11'])
	time17 = pd.DataFrame(data, columns=['17'])
	time23 = pd.DataFrame(data, columns=['23'])
	time29 = pd.DataFrame(data, columns=['29'])
	time35 = pd.DataFrame(data, columns=['35'])
	time47 = pd.DataFrame(data, columns=['47'])
	time = {"time11":11, "time17":17, "time23":23, "time29":29, "time35":35, "time47":47}
	for index, row in data.iterrows():
		bunga = []
		for key in time:
			jangka_waktu = time[key]
			harga = row['Harga']
			dp = row['DP']
			angsuran = row[jangka_waktu]
			bunga.append(HitungBunga(harga, dp, angsuran, jangka_waktu))
		print(bunga)

if __name__ == "__main__":
	main()