package main

import (
	"fmt"
)

type Retangulo struct {
	base, altura float64
}

func (r Retangulo) calculaArea() (float64, float64) {
	area := r.base * r.altura
	perimetro := (r.base * 2) + (r.altura * 2)
	return area, perimetro // Corrigido o nome da variável
}

type Contato struct {
  nome string
  idade string
  email string
}

func adicionar_contato(c Contato) []string{
  lista_contatos := []string{
    c.nome,
    c.idade,
    c.email,
  }
  return lista_contatos

}

func main() {
	r := Retangulo{
		base:   10.0,
		altura: 10.0,
	}

  c := Contato{
    nome: "Morgan",
    idade: "38",
    email: "Morgan@email.com",
  }

	area, perimetro := r.calculaArea()

	fmt.Printf("Área: %.2f, Perímetro: %.2f\n", area, perimetro)
  fmt.Println(adicionar_contato(c))
}
