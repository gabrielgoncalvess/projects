import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import 'home_page.dart';

class LoginPage extends StatefulWidget {
  @override
  _LoginPageState createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  String email = '';
  String password = '';

  Widget _body() {
    return SingleChildScrollView(
      child: SizedBox(
        width: MediaQuery.of(context).size.width,
        height: 500, //MediaQuery.of(context).size.width,
        child: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Container(
                  margin: const EdgeInsets.all(
                      15.0), // jogar os outros elementos pra baixo
                  width: 125,
                  height: 125,
                  child: Image.asset('assets/images/android-icon-192x192.png')),
              //Container(height: 20),   OUTRA MANEIRA DE ESPAÇAR OS ELEMENTOS
              Card(
                color: Colors.white.withOpacity(0.8),
                child: Padding(
                  padding: const EdgeInsets.only(
                      top: 10.0, right: 8.0, left: 8.0, bottom: 8.0),
                  child: Column(
                    children: [
                      TextField(
                        onChanged: (text) {
                          email = text;
                        },
                        keyboardType: TextInputType.emailAddress,
                        decoration: InputDecoration(
                            labelText: 'Email', border: OutlineInputBorder()),
                      ),
                      SizedBox(
                        height: 10,
                      ),
                      TextField(
                          onChanged: (text) {
                            password = text;
                          },
                          obscureText: true,
                          decoration: InputDecoration(
                              labelText: 'Password',
                              border: OutlineInputBorder())),
                      SizedBox(
                        height: 15, //15
                      ),
                      Container(
                        height: 50,
                        width: 150, //double.infinity
                        child: RaisedButton(
                          color: Colors.yellow,
                          onPressed: () {
                            if (email == 'gabreeuu@hotmail.com' &&
                                password == '123') {
                              Navigator.of(context)
                                  .pushReplacementNamed('/home');
                            } else {
                              print('incorreto');
                            }
                          },
                          child: Text(
                            'Entrar',
                            style: TextStyle(
                                fontSize: 20,
                                color: Colors.blue.withOpacity(1)),
                            textAlign: TextAlign.center,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          SizedBox(
              height: MediaQuery.of(context).size.height,
              child: Image.asset(
                'assets/images/Imagem1.png',
                fit: BoxFit.cover,
              )),
          Container(
            color: Colors.black.withOpacity(0.01), // CRIAR UMA MÁSCARA
          ),
          _body(),
        ],
      ),
    );
  }
}
