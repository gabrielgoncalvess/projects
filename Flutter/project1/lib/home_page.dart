import 'package:flutter/material.dart';
import 'package:project1/app_controller.dart';

class HomePage extends StatefulWidget {
  @override
  State<HomePage> createState() {
    return HomePageState();
  }
}

//Icons.arrow_back
//Icons.highlight_remove

class HomePageState extends State<HomePage> {
  int counter = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      drawer: Drawer(
        // BOTÃO COM OPÇÕES
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start, //alinhar tudo ao centro
          children: [
            UserAccountsDrawerHeader(
                currentAccountPicture: ClipRRect(
                  borderRadius: BorderRadius.circular(40),
                  child: Image.network(
                      'https://upload.wikimedia.org/wikipedia/commons/4/49/Chris_Evans_-_Captain_America_2_press_conference_headshot.jpg'),
                ),
                accountName: Text('Gabriel Gonçalves'),
                accountEmail: Text('gabreeuu@hotmail.com')),
            ListTile(
              leading: Icon(
                Icons.home,
                size: 40,
              ),
              title: Text('Início'),
              subtitle: Text('Tela de início'),
              onTap: () {
                print('HOME');
              },
            ),
            ListTile(
              leading: Icon(
                Icons.exit_to_app,
                size: 40,
              ),
              title: Text('Logout'),
              subtitle: Text('Finalizar sessão'),
              onTap: () {
                print('LOGOUT');
                Navigator.of(context)
                    .pushReplacementNamed('/'); //VOLTAR PARA TELA DE LOGIN
              },
            ),
          ],
        ),
      ),
      appBar: AppBar(
        title: Text('Home Page'),
        actions: [CustomSwitch()],
      ),
      body: Container(
        width: double.infinity,
        height: double.infinity,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          //scrollDirection: Axis.horizontal,
          children: [
            Text(
              'Contador: $counter',
              style: TextStyle(fontSize: 25),
            ),
            Container(
              height: 30,
            ),
            CustomSwitch(),
            Container(
              height: 30,
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                Container(
                  width: 50,
                  height: 50,
                  color: Colors.black,
                ),
                Container(
                  width: 50,
                  height: 50,
                  color: Colors.black,
                ),
                Container(
                  width: 50,
                  height: 50,
                  color: Colors.black,
                )
              ],
            )
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.add),
        onPressed: () {
          setState(() {
            counter++;
          });
        },
      ),
    );
  }
}

class CustomSwitch extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Switch(
      value: AppController.instance.isDartTheme,
      onChanged: (value) {
        AppController.instance.changeTheme();
      },
    );
  }
}
