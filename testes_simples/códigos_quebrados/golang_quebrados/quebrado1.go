//Qubrado ainda
package main

import "fmt"

// Calcula o fatorial de um número
func fatorial(n int) int {
    if n == 0 {
        return 1
    }
    return n * fatorial(n-1)
}

// Verifica se um número é primo
func isPrimo(num int) bool {
    if num < 2 {
        return false
    }
    for i := 2; i < num; i++ {
        if num%i == 0 {
            return false
        }
    }
    return true
}

// Inverte uma string
func reverseString(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}