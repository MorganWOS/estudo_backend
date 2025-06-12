package greetings

import (
  "fmt"
  "errors"
  "math/rand"
)

// Hello retorna uma saudação para a pessoa nomeada.
// Retorna uma string com a mensagem e um possível erro.
func Hello(name string) (string, error){
  // Se nenhum nome for fornecido, retorna um erro com mensagem
  if name == "" {
    return "", errors.New("nome vazio!")
  }

  // Cria uma mensagem usando um formato aleatório
  message := fmt.Sprintf(randomFormat(), name)
  // message := fmt.Sprint(randomFormat())
  return message, nil
}

// Hellos retorna um mapa que associa cada pessoa nomeada
// com uma mensagem de saudação.
// Recebe uma lista de nomes e retorna um mapa ou erro.
func Hellos(names []string) (map[string]string, error){
  // Um mapa para associar nomes com mensagens
  messages := make(map[string]string)
  // Percorre a lista de nomes recebida, chamando
  // a função Hello para obter uma mensagem para cada nome
  for _, name := range names {
    message, err := Hello(name)
    if err != nil {
      return nil, err
    }
    // No mapa, associa a mensagem obtida com
    // o respectivo nome
    messages[name] = message
  }
  return messages, nil
}

// randomFormat retorna uma de várias mensagens de saudação pré-definidas.
// A mensagem retornada é selecionada aleatoriamente.
func randomFormat() string{
  // Uma lista de formatos de mensagem
  formats := []string{
    "Oi, %v. Bem-vindo!",
    "Ótimo te ver, %v",
    "Saudações, %v! Bem-vindo!",
  }

  // Retorna um formato de mensagem selecionado aleatoriamente
  // especificando um índice aleatório para a lista de formatos
  return formats[rand.Intn(len(formats))]
}
