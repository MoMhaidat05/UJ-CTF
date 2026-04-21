from Crypto.Util.number import getPrime, bytes_to_long

N = getPrime(2048) * getPrime(2048)
e = 3
message = "uj{3v3n_W1th_B1g_K3ys??!}"
message_bytes = bytes_to_long(message.encode('utf-8'))
cipher = pow(message_bytes, e, N)

print("Cipher", cipher)
print("N", N)