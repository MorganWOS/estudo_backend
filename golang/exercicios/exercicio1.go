package main

import (
  "fmt"
  "strings"
)

var listap map[string]int

func soma(x []int) int {
  sum := 0
  for _, number := range x {
    sum += number
  }
  return sum
}

func maior(x []int) int{
  maior := 0
  for _, number := range x {
    //fmt.Println(number)
    if number >= maior {
      maior = number
    }
  }
  return maior
}

func palavras(x string,) map[string]int{
  lista := strings.Fields(x)
  listap = make(map[string]int)
  //index := 0
  for _, palavra := range lista{
    if _, existe := listap[palavra]; existe{
      listap[palavra] += 1
    } else {
      listap[palavra] = 1
    }
  }
  return listap

}



func main(){
  slice1 := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
  slice2 := []int{1, 22, 3, 4, 15, 6, 69, 8, 9}
  fmt.Print("Soma: ")
  fmt.Println(soma(slice1))
  fmt.Print("Maior: ")
  fmt.Println(maior(slice2))
  fmt.Println(palavras("banana é muito bom, banana com queijo não é bom, mas banana sem queijo é bom"))
}
