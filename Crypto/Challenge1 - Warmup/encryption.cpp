#include <iostream>
#include <vector>

using namespace std;

// Decrypt this cipher text with was encrypted using the algorithm below
vector<int> cipherText = {114, 108, 126, 92, 51, 112, 94, 49, 124, 81, 67, 60, 127, 85, 93, 96, 35, 98, 74, 89, 106, 97, 101, 35, 109, 47, 45, 105, 104, 103};

vector<int> encryptionAlgorithm(string plainText)
{
    vector<int> cipher = {};

    for (int index = 0; index < plainText.size(); index++)
    {
        int encryptedCharacter = (plainText[index] ^ (index ^ 7));
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