import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class PetRegistrationPage extends StatefulWidget {
  const PetRegistrationPage({super.key});

  @override
  State<PetRegistrationPage> createState() => _PetRegistrationPageState();
}

class _PetRegistrationPageState extends State<PetRegistrationPage> {
  final TextEditingController _nomeController = TextEditingController();
  final TextEditingController _idadeController = TextEditingController();
  final TextEditingController _especieController = TextEditingController();
  final TextEditingController _racaController = TextEditingController();

  Future<void> _submitPetForm() async {
    final String nome = _nomeController.text;
    final int idade = int.parse(_idadeController.text);
    final String especie = _especieController.text;
    final String raca = _racaController.text;

    final response = await http.post(
      Uri.parse('http://127.0.0.1:8000/crud_mobile/apipet/'),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(<String, dynamic>{
        'nome': nome,
        'idade': idade,
        'especie': especie,
        'raca': raca,
      }),
    );

    if (response.statusCode == 201) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Pet cadastrado com sucesso!')),
      );
    } else {
      ScaffoldMessenger.of(
        context,
      ).showSnackBar(const SnackBar(content: Text('Falha ao cadastrar pet.')));
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Cadastro de Pet')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            TextField(
              controller: _nomeController,
              decoration: const InputDecoration(labelText: 'Nome'),
            ),
            TextField(
              controller: _idadeController,
              decoration: const InputDecoration(labelText: 'Idade'),
              keyboardType: TextInputType.number,
            ),
            TextField(
              controller: _especieController,
              decoration: const InputDecoration(labelText: 'Espécie'),
            ),
            TextField(
              controller: _racaController,
              decoration: const InputDecoration(labelText: 'Raça'),
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: _submitPetForm,
              child: const Text('Cadastrar Pet'),
            ),
          ],
        ),
      ),
    );
  }
}
