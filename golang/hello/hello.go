package main

import (
  "fmt"
  "log"

  "example.com/greetings"
)

func main(){
  // Configura as propriedades do Logger padrão, incluindo
  // o prefixo das entradas de log e uma flag para desativar
  // a impressão de hora, arquivo fonte e número da linha.
  log.SetPrefix("greetings: ")
  log.SetFlags(0)

  // Uma lista (slice) de nomes.
  names := []string{"Gladys", "Samantha", "Darrin"}

  // Solicita mensagens de saudação para os nomes.
  messages, err := greetings.Hellos(names)
  // Se um erro for retornado, imprime no console e
  // encerra o programa.
  if err != nil {
    log.Fatal(err)
  }

  // Se nenhum erro for retornado, imprime o mapa de
  // mensagens retornado no console.
  fmt.Println(messages)
}
