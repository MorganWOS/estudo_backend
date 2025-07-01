package main

import (
	"fmt"
	"time"
)

func main() {
	// Canal bufferizado com capacidade 2
	ch := make(chan string, 2)

	// Podemos enviar 2 valores sem bloqueio
	ch <- "primeiro"
	ch <- "segundo"

	// Este terceiro envio bloquearia (deadlock) se não tivesse buffer suficiente
	// ch <- "terceiro" // Descomente para ver o erro

	go func() {
		time.Sleep(1 * time.Second)
		fmt.Println("Recebido:", <-ch)
	}()

	fmt.Println("Enviei dois valores")
	time.Sleep(2 * time.Second)
}
