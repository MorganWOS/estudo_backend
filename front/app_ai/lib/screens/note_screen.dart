// lib/screens/note_screen.dart
import 'package:flutter/material.dart';

class NoteScreen extends StatefulWidget {
  @override
  _NoteScreenState createState() => _NoteScreenState();
}

class _NoteScreenState extends State<NoteScreen> {
  final TextEditingController _messageController = TextEditingController();
  final List<String> mensagens = [];

  void _enviarMensagem() {
    if (_messageController.text.trim().isEmpty) return;
    setState(() {
      mensagens.add(_messageController.text.trim());
      _messageController.clear();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Anotação")),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              reverse: true,
              itemCount: mensagens.length,
              itemBuilder: (context, index) => ListTile(
                title: Text(mensagens[mensagens.length - 1 - index]),
              ),
            ),
          ),
          Row(
            children: [
              IconButton(
                icon: Icon(Icons.mic),
                onPressed: () {}, // Implementar gravação de áudio
              ),
              IconButton(
                icon: Icon(Icons.image),
                onPressed: () {}, // Implementar seleção de imagem
              ),
              IconButton(
                icon: Icon(Icons.videocam),
                onPressed: () {}, // Implementar gravação de vídeo
              ),
              Expanded(
                child: TextField(
                  controller: _messageController,
                  decoration: InputDecoration(hintText: 'Escreva uma nota...'),
                ),
              ),
              IconButton(
                icon: Icon(Icons.send),
                onPressed: _enviarMensagem,
              ),
            ],
          ),
        ],
      ),
    );
  }
}
