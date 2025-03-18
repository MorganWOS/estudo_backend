import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'cadastro_page.dart';
import 'cadastro_tutor_page.dart';
import 'cadastro_detalhes_page.dart';
import 'cadastro_localizacao_page.dart';
import 'cadastro_pet_page.dart';
import 'home_page.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Hospedagem Pet',
      theme: ThemeData(primarySwatch: Colors.blue),
      initialRoute: '/',
      routes: {
        '/': (context) => const LoginPage(),
        '/cadastro': (context) => const CadastroPage(),
        '/cadastro_tutor': (context) => const CadastroTutorPage(),
        '/cadastro_detalhes': (context) => const CadastroDetalhesPage(),
        '/cadastro_localizacao': (context) => const CadastroLocalizacaoPage(),
        '/cadastro_pet': (context) => const CadastroPetPage(),
        '/home': (context) => const HomePage(),
      },
    );
  }
}

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();
  bool _rememberMe = false;

  void _login() {
    final String email = _emailController.text;
    final String password = _passwordController.text;

    // Aqui você pode adicionar a lógica de autenticação
    if (email.isNotEmpty && password.isNotEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Login realizado com sucesso!')),
      );
      Navigator.pushNamed(
        context,
        '/home',
      ); // Navegue para a tela home após o login
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Por favor, preencha todos os campos.')),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Hospedagem Pet')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              const Text(
                'Bem vindo',
                style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 20),
              SizedBox(
                width: 300,
                child: TextField(
                  controller: _emailController,
                  decoration: const InputDecoration(
                    labelText: 'Email',
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.all(Radius.circular(12.0)),
                    ),
                  ),
                  keyboardType: TextInputType.emailAddress,
                ),
              ),
              const SizedBox(height: 20),
              SizedBox(
                width: 300,
                child: TextField(
                  controller: _passwordController,
                  decoration: const InputDecoration(
                    labelText: 'Senha',
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.all(Radius.circular(12.0)),
                    ),
                  ),
                  obscureText: true,
                ),
              ),
              const SizedBox(height: 20),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: <Widget>[
                  Row(
                    children: <Widget>[
                      Checkbox(
                        value: _rememberMe,
                        onChanged: (bool? value) {
                          setState(() {
                            _rememberMe = value ?? false;
                          });
                        },
                      ),
                      const Text('Lembrar-me'),
                    ],
                  ),
                  TextButton(
                    onPressed: () {
                      // Adicione a lógica para "Esqueci minha senha"
                    },
                    child: const Text('Esqueci minha senha'),
                  ),
                ],
              ),
              const SizedBox(height: 20),
              ElevatedButton(onPressed: _login, child: const Text('Login')),
              const SizedBox(height: 20),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  const Text("Não tem uma conta?"),
                  TextButton(
                    onPressed: () {
                      Navigator.pushNamed(context, '/cadastro');
                    },
                    child: const Text('Cadastre-se'),
                  ),
                ],
              ),
              const SizedBox(height: 20),
              const Text("Logar com"),
              const SizedBox(height: 10),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  IconButton(
                    icon: const FaIcon(FontAwesomeIcons.google),
                    iconSize: 24,
                    onPressed: () {
                      // Adicione a lógica para login com Google
                    },
                  ),
                  IconButton(
                    icon: const FaIcon(FontAwesomeIcons.facebook),
                    iconSize: 24,
                    onPressed: () {
                      // Adicione a lógica para login com Facebook
                    },
                  ),
                  IconButton(
                    icon: const FaIcon(FontAwesomeIcons.apple),
                    iconSize: 24,
                    onPressed: () {
                      // Adicione a lógica para login com Apple
                    },
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
