//Quebrado ainda
package main

import (
    "fmt"
    "sync"
)

type Contador struct {
    valor int
    mu    sync.Mutex
}

func (c *Contador) Incrementar() {
    c.mu.Lock()
    c.valor++
    c.mu.Unlock()
}

func (c *Contador) Valor() int {
    c.mu.Lock()
    defer c.mu.Unlock()
    return c.valor
}

func main() {
    var wg sync.WaitGroup
    contador := Contador{}

    for i := 0; i < 1000; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            contador.Incrementar()
        }()
    }

    wg.Wait()
    fmt.Println("Valor final:", contador.Valor())
}