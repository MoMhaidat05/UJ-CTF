from Crypto.Util.number import getPrime, bytes_to_long

p = getPrime(2048)
q = getPrime(2048)
N = p * q
e = 65537
phi = (p - 1) * (q - 1)

flag = b"uj{y0u_d0nt_n33d_p_4nd_q_1f_y0u_h4v3_ph1}"
m = bytes_to_long(flag)
c = pow(m, e, N)

print("--- Give these to the students ---")
print("Description: My N is unbreakable. FactorDB will cry. I'm so confident, I'll even give you the totient value to prove how mathematically perfect my keys are.")
print(f"N = {N}")
print(f"e = {e}")
print(f"phi = {phi}")
print(f"c = {c}\n")