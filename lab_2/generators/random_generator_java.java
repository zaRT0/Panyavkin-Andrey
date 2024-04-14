import java.util.Random;

public class Main {
    
    public static String generateBinarySequence(int length) {
        Random random = new Random();
        StringBuilder binarySequence = new StringBuilder();
        
        for (int i = 0; i < length; i++) {
            int bit = random.nextInt(2);
            binarySequence.append(bit);
        }
        
        return binarySequence.toString();
    }
    
    public static void main(String[] args) {
        String binarySequence = generateBinarySequence(128);
        System.out.println("Случайная последовательность: " + binarySequence);
    }
    
}