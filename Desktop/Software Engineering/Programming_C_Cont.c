// This program takes a user value, being the number of terms from the Fibonacci Series they'd like to see,
// then calculates and returns each term up until the nth term.
// Inputs: Number of terms the user wants to see from the Fibonacci Series
// Outputs: All of the terms in the Fibonachi series until the user's number is met

#include <stdio.h> // import basic functions such as scanf
int main() { // open main program to be executed
    int n, i, a = 0, b = 1, nextTerm; // asign variables as integers; initialize a as 0 and b as 1
    printf("Enter the number of terms: "); // prompt user to enter number of terms
    scanf("%d", &n); // take input and store as integer n
    printf("Fibonacci Series: "); // display string to user
    printf("%d %d ", a, b); // 
    for (i = 3; i <= n; ++i) { // for loop starting at 3, and going until i is less than or equal to n; increment by 1 each pass
        nextTerm = a + b; // set next term equal to a + b
        printf("%d ", nextTerm);
        a = b; // set a equal to b
        b = nextTerm; // set b equal to nexTerm
    } // close for loop
} // close int main()