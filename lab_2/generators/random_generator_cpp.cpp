#include <iostream>
#include <random>
#include <bitset>

using namespace std;

/**
 * This function generates a random binary sequence and prints it to the standard output.
 * It uses a random number generator initialized with the current time.
 * @return A string representing the random binary sequence.
 */
string generateRandomBinarySequence() {
    random_device rd; // Initialize random number generator with current time
    mt19937_64 eng(rd()); // Create Mersenne Twister engine
    uniform_int_distribution<unsigned long long> distr; // Uniform distribution of unsigned long long integers

    string result;
    result.reserve(128); // Pre-allocate memory for efficiency

    // Generate 2 random 64-bit numbers and convert them to binary strings
    for (int i = 0; i < 2; ++i) {
        unsigned long long random_num = distr(eng);
        result += std::bitset<64>(random_num).to_string();
    }

    return result; // Return the generated binary sequence
}

/**
 * The main function that generates a random binary sequence and prints it.
 * @return 0 indicating successful execution.
 */
int main() {
    string random_sequence = generateRandomBinarySequence(); // Generate random binary sequence
    cout << "Random binary sequence: " << random_sequence << std::endl; // Print the sequence
    return 0; // Return 0 indicating successful execution
}