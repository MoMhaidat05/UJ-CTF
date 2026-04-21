#include <iostream>
#include <vector>

using namespace std;

// Decrypt this cipher text with was encrypted using the algorithm below
vector<int> cipherText = {2784, 2496, 2880, 2064, 1296, 1200, 2568, 2400, 2688, 1272, 2016, 1584, 1488, 3000, 2952, 840, 2808, 1848, 2280, 864, 888, 2448, 2400, 936, 1344, 2472, };

vector<int> encryptionAlgorithm(string plainText)
{
    vector<int> cipher = {};

    for (int i = 0; i < plainText.size(); i++)
    {
        int encryptedCharacter = plainText[i] ^ (i + 1);
        for (int j = 1; j < 5; j++){
            encryptedCharacter *= j;
        }
        cipher.push_back(encryptedCharacter);
    }

    return cipher;
}

string decryptionAlgorithm(vector<int> cipherInput) {
    string flag = "";
    // YOUR CODE GOES HERE:
    
    return flag;
}

int main()
{
    // Print the flag...
    cout << decryptionAlgorithm(cipherText);
    return 0;
}