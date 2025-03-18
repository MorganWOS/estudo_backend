import 'package:flutter/material.dart';

class CadastroPetPage extends StatelessWidget {
  const CadastroPetPage({super.key});

  @override
  Widget build(BuildContext context) {
    final TextEditingController _nomePetController = TextEditingController();
    final TextEditingController _racaController = TextEditingController();
    final TextEditingController _pesoController = TextEditingController();
    final TextEditingController _dataNascimentoPetController =
        TextEditingController();

    return Scaffold(
      appBar: AppBar(title: const Text('Nos conte sobre seu pet')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              const Text(
                'Nos conte sobre seu pet',
                style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 20),
              const Text('Qual o sexo do pet?'),
              const SizedBox(height: 10),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  ElevatedButton(
                    onPressed: () {
                      // Adicione a lógica para selecionar macho
                    },
                    child: const Text('Macho'),
                  ),
                  const SizedBox(width: 10),
                  ElevatedButton(
                    onPressed: () {
                      // Adicione a lógica para selecionar fêmea
                    },
                    child: const Text('Fêmea'),
                  ),
                ],
              ),
              const SizedBox(height: 20),
              TextField(
                controller: _nomePetController,
                decoration: const InputDecoration(
                  labelText: 'Nome',
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.all(Radius.circular(12.0)),
                  ),
                ),
              ),
              const SizedBox(height: 20),
              TextField(
                controller: _racaController,
                decoration: const InputDecoration(
                  labelText: 'Raça',
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.all(Radius.circular(12.0)),
                  ),
                ),
              ),
              const SizedBox(height: 20),
              TextField(
                controller: _pesoController,
                decoration: const InputDecoration(
                  labelText: 'Peso',
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.all(Radius.circular(12.0)),
                  ),
                ),
                keyboardType: TextInputType.number,
              ),
              const SizedBox(height: 20),
              TextField(
                controller: _dataNascimentoPetController,
                decoration: const InputDecoration(
                  labelText: 'Data de Nascimento',
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.all(Radius.circular(12.0)),
                  ),
                ),
              ),
              const SizedBox(height: 20),
              const Text('Tipo de pet:'),
              const SizedBox(height: 10),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  ElevatedButton(
                    onPressed: () {
                      // Adicione a lógica para selecionar cachorro
                    },
                    child: const Text('Cachorro'),
                  ),
                  const SizedBox(width: 10),
                  ElevatedButton(
                    onPressed: () {
                      // Adicione a lógica para selecionar gato
                    },
                    child: const Text('Gato'),
                  ),
                ],
              ),
              const SizedBox(height: 20),
              ElevatedButton(
                onPressed: () {
                  Navigator.pushNamed(context, '/home');
                },
                child: const Text('Cadastrar Pet'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
