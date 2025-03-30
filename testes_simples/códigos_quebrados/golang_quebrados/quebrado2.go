// Quebrado ainda
package main

import (
    "errors"
    "fmt"
)

type Usuario struct {
    Nome  string
    Idade int
}

type GerenciadorUsuarios struct {
    usuarios []Usuario
}

func (g *GerenciadorUsuarios) AdicionarUsuario(u Usuario) {
    g.usuarios = append(g.usuarios, u)
}

func (g *GerenciadorUsuarios) RemoverUsuario(nome string) error {
    for i, usuario := range g.usuarios {
        if usuario.Nome == nome {
            g.usuarios = append(g.usuarios[:i], g.usuarios[i+1:]...)
            return nil
        }
    }
    return errors.New("Usuário não encontrado")
}

func (g *GerenciadorUsuarios) MediaIdades() float64 {
    soma := 0
    for _, usuario := range g.usuarios {
        soma += usuario.Idade
    }
    return float64(soma) / float64(len(g.usuarios))
}