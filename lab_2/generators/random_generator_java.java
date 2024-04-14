import java.util.Random;

public class Main {
    
    /**
     * Generates a binary sequence of the specified length.
     * @param length The length of the binary sequence to generate.
     * @return The generated binary sequence as a string.
     */
    public static String generateBinarySequence(int length) {
        Random random = new Random(); // Initialize a random number generator
        StringBuilder binarySequence = new StringBuilder(); // String builder to efficiently build the binary sequence
        
        // Generate random bits and append them to the binary sequence
        for (int i = 0; i < length; i++) {
            int bit = random.nextInt(2); // Generate a random bit (0 or 1)
            binarySequence.append(bit); // Append the bit to the binary sequence
        }
        
        return binarySequence.toString(); // Return the generated binary sequence
    }
    
    /**
     * The main method that generates a binary sequence and prints it.
     * @param args The command-line arguments (not used in this program).
     */
    public static void main(String[] args) {
        String binarySequence = generateBinarySequence(128); // Generate a binary sequence of length 128
        System.out.println("Random binary sequence: " + binarySequence); // Print the generated binary sequence
    }
    
}
