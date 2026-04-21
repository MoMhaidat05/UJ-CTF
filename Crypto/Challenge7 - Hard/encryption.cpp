#include <iostream>
#include <vector>
#include <string>

using namespace std;

// I had chose a random number between 0-255. Good luck guessing it ;)
const int RANDOM_NUMBER = 0; // 0 is dummy and not correct, only to avoide the code from being broke.
vector<int> cipherText = {172,198,189,239,220,191,202,184,203,250,140,191,224,173,153,253,206,145,220,239,176,248,204,184,139,212,144,195,190};


void encryptRecursive(const string& plainText, int index, int prev, vector<int>& cipher) {
    // base case
    if (index >= plainText.size()) {
        return;
    }

    int current;

    if (index == 0) {
        current = plainText[index] ^ RANDOM_NUMBER;
    } else {
        current = plainText[index] ^ prev;
    }

    cipher.push_back(current);

    // recursive call
    encryptRecursive(plainText, index + 1, current, cipher);
}

void decryptionAlgorithm(vector<int>& cipher) {
    // YOUR CODE GOES HERE:
    string flag = "";
    
    /* 
    This is a helping line, this function searches for "uj{" in the flag, 
    if found, then your solution is correct. If not, then your solution is not.
    Only to help you avoide noise that will be printed in terminal. 
    */
    if (flag.rfind("uj{", 0) == 0) {
        cout << flag << endl;
    }
}

int main() {
    decryptionAlgorithm(cipherText);
    return 0;
}