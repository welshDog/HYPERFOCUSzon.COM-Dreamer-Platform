package com.hyperfocus.example;

import org.junit.Test;
import org.junit.Before;
import static org.junit.Assert.*;

/**
 * Unit tests for the App class
 *
 * Demonstrates JUnit 4 testing patterns and best practices
 * for the HyperFocus Zone development environment.
 */
public class AppTest {

    private App app;

    /**
     * Set up test fixtures before each test method
     */
    @Before
    public void setUp() {
        app = new App();
    }

    /**
     * Test the greeting generation with valid names
     */
    @Test
    public void testGenerateGreeting_WithValidName() {
        // Test with a normal name
        String result = app.generateGreeting("Developer");
        assertEquals("Hello, Developer! Welcome to Java development!", result);

        // Test with a name that has extra whitespace
        String resultWithSpaces = app.generateGreeting("  Code Ninja  ");
        assertEquals("Hello, Code Ninja! Welcome to Java development!", resultWithSpaces);
    }

    /**
     * Test the greeting generation with invalid inputs
     */
    @Test
    public void testGenerateGreeting_WithInvalidInputs() {
        // Test with null
        String resultNull = app.generateGreeting(null);
        assertEquals("Hello, anonymous developer!", resultNull);

        // Test with empty string
        String resultEmpty = app.generateGreeting("");
        assertEquals("Hello, anonymous developer!", resultEmpty);

        // Test with whitespace only
        String resultWhitespace = app.generateGreeting("   ");
        assertEquals("Hello, anonymous developer!", resultWhitespace);
    }

    /**
     * Test sum calculation with valid arrays
     */
    @Test
    public void testCalculateSum_WithValidArrays() {
        // Test with positive numbers
        int[] positiveNumbers = {1, 2, 3, 4, 5};
        int result = app.calculateSum(positiveNumbers);
        assertEquals(15, result);

        // Test with mixed positive and negative numbers
        int[] mixedNumbers = {-2, -1, 0, 1, 2};
        int resultMixed = app.calculateSum(mixedNumbers);
        assertEquals(0, resultMixed);

        // Test with single element
        int[] singleElement = {42};
        int resultSingle = app.calculateSum(singleElement);
        assertEquals(42, resultSingle);
    }

    /**
     * Test sum calculation with edge cases
     */
    @Test
    public void testCalculateSum_WithEdgeCases() {
        // Test with null array
        int resultNull = app.calculateSum(null);
        assertEquals(0, resultNull);

        // Test with empty array
        int[] emptyArray = {};
        int resultEmpty = app.calculateSum(emptyArray);
        assertEquals(0, resultEmpty);
    }

    /**
     * Test sum calculation with large numbers
     */
    @Test
    public void testCalculateSum_WithLargeNumbers() {
        int[] largeNumbers = {1000000, 2000000, 3000000};
        int result = app.calculateSum(largeNumbers);
        assertEquals(6000000, result);
    }

    /**
     * Performance test for sum calculation
     */
    @Test(timeout = 1000) // Test should complete within 1 second
    public void testCalculateSum_Performance() {
        // Create a large array
        int[] largeArray = new int[100000];
        for (int i = 0; i < largeArray.length; i++) {
            largeArray[i] = i + 1;
        }

        // This should complete quickly
        int result = app.calculateSum(largeArray);

        // Verify the result (sum of 1 to 100000)
        long expected = 100000L * 100001L / 2;
        assertEquals((int) expected, result);
    }
}
