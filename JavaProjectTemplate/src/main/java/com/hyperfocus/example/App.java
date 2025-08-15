package com.hyperfocus.example;

/**
 * HyperFocus Zone Java Application
 *
 * A simple example application demonstrating Java 8 features
 * and best practices for the HyperFocus Zone development environment.
 */
public class App {

    /**
     * Application entry point
     *
     * @param args Command line arguments
     */
    public static void main(String[] args) {
        System.out.println("🌟 Welcome to HyperFocus Zone Java Development! 🌟");
        System.out.println("☕ Running on Java " + System.getProperty("java.version"));

        // Demonstrate Java 8 features
        App app = new App();
        app.demonstrateJava8Features();
    }

    /**
     * Demonstrates Java 8 lambda expressions and streams
     */
    private void demonstrateJava8Features() {
        System.out.println("\n🚀 Java 8 Features Demo:");

        // Lambda expressions
        Runnable task = () -> System.out.println("  ⚡ Lambda expression executed!");
        task.run();

        // Method references
        String message = "  💎 Method reference works!";
        System.out.println(message);

        // Optional usage
        java.util.Optional<String> optionalValue = java.util.Optional.of("HyperFocus Zone");
        optionalValue.ifPresent(value -> System.out.println("  🎯 Optional value: " + value));

        System.out.println("\n✅ Java environment is ready for development!");
    }

    /**
     * Utility method for generating greeting messages
     *
     * @param name The name to greet
     * @return A formatted greeting message
     */
    public String generateGreeting(String name) {
        if (name == null || name.trim().isEmpty()) {
            return "Hello, anonymous developer!";
        }
        return String.format("Hello, %s! Welcome to Java development!", name.trim());
    }

    /**
     * Calculates the sum of an array of integers
     *
     * @param numbers Array of integers to sum
     * @return The sum of all numbers in the array
     */
    public int calculateSum(int[] numbers) {
        if (numbers == null || numbers.length == 0) {
            return 0;
        }

        int sum = 0;
        for (int number : numbers) {
            sum += number;
        }
        return sum;
    }
}
