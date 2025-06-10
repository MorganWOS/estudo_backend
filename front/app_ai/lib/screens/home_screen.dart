// lib/screens/home_screen.dart
import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget {
  final List<String> notas = ['Meu notebook', 'Fone de ouvido', 'Câmera'];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Minhas Anotações')),
      body: ListView.builder(
        itemCount: notas.length,
        itemBuilder: (context, index) {
          return ListTile(
            title: Text(notas[index]),
            onTap: () => Navigator.pushNamed(context, '/note'),
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => Navigator.pushNamed(context, '/note'),
        child: Icon(Icons.add),
      ),
    );
  }
}