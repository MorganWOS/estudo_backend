package main

import(
  "fmt"
  "time"
)

func hello_world(x bool){
  var hello string
  if x == true{
    hello = "Hello World! com go"
  }else{
    hello = "Hello World! normal"
  }

  fmt.Println(hello)
}

func sum(x []int, c chan int) {
  sum := 0
  for _, n := range x{
    sum += n
  }
  c <- sum
}

func divide(x int, y int) int{
  divides := x / y
  fmt.Println(divides)
  return divides
}

func main(){
  listnumber := []int{
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
  }

  listnumbers := []int{
    123, 1241, 12, 14, 15, 10, 100, 88, 99, 1003,
  }



  go hello_world(true)
  hello_world(false)

  c := make(chan int)
  go sum(listnumber, c)
  go sum(listnumbers, c)
  x, y := <-c, <-c
  go divide(x, y)

  fmt.Println(x)
  fmt.Println(y)

  time.Sleep(100 * time.Millisecond)

  fmt.Println("Todas as goroutines acabaram!")
}
