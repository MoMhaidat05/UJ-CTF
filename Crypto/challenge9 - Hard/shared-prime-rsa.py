from Crypto.Util.number import bytes_to_long, getPrime, long_to_bytes

p = getPrime(2048)
q = getPrime(2048)
r = getPrime(2048)

N1 = p * q
N2 = p * r
e = 65537
phi = (p-1) * (q-1)
d = pow(e, -1, phi)
flag = "uj{L34ky_Tw1ns_F34rs_GCD}".encode('utf-8')
flag_bytes = bytes_to_long(flag)
cipher = pow(flag_bytes, e, N1)
print(f"N1 = {N1}")
print(f"N2 = {N2}")
print(f"e = {e}")
print(f"cipher = {cipher}\n")