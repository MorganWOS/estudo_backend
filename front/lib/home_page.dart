import 'package:flutter/material.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Home')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            ElevatedButton(
              onPressed: () {
                // Navegar para a tela de Hospedagem
              },
              child: const Text('Hospedagem'),
            ),
            ElevatedButton(
              onPressed: () {
                // Navegar para a tela de Passeio
              },
              child: const Text('Passeio'),
            ),
            ElevatedButton(
              onPressed: () {
                // Navegar para a tela de Pet Sitter
              },
              child: const Text('Pet Sitter'),
            ),
          ],
        ),
      ),
      bottomNavigationBar: BottomNavigationBar(
        backgroundColor:
            Colors.grey[850], // Define a cor de fundo da barra de navegação
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(icon: Icon(Icons.home), label: 'Home'),
          BottomNavigationBarItem(icon: Icon(Icons.business), label: 'Chat'),
          BottomNavigationBarItem(icon: Icon(Icons.school), label: 'Serviços'),
          BottomNavigationBarItem(icon: Icon(Icons.egg), label: 'Perfil'),
        ],
        selectedItemColor: Colors.amber[800],
        unselectedItemColor:
            Colors.black, // Define a cor dos itens não selecionados
      ),
      backgroundColor: Colors.grey, // Define a cor de fundo da tela
    );
  }
}
