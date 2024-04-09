#include <iostream>
#include <random>
#include <bitset>

using namespace std;

string generateRandomBinarySequence() {
    random_device rd;
    mt19937_64 eng(rd());
    uniform_int_distribution<unsigned long long> distr;

    string result;
    result.reserve(128);

    for (int i = 0; i < 2; ++i) {
        unsigned long long random_num = distr(eng);
        result += std::bitset<64>(random_num).to_string();
    }

    return result;
}

int main() {
    string random_sequence = generateRandomBinarySequence();
    cout << "Random binary sequence: " << random_sequence << std::endl;
    return 0;
}