import 'dart:ffi';

import 'package:flutter/material.dart';
import 'dart:math' as math;
import 'package:flutter_masked_text/flutter_masked_text.dart';

import 'package:flutter/services.dart';

//import 'package:google_fonts/google_fonts.dart';

/*

SCRIPT CRIADO POR GABRIEL DA SILVA GONÇALVES

*/

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

var controller = new MaskedTextController(mask: '000.000.000-00'); //MOEDA
final lowPrice = MoneyMaskedTextController(
    decimalSeparator: ',', thousandSeparator: '.', leftSymbol: 'R\$ ');

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  var controller = new MaskedTextController(mask: '000.000.000-00'); //MOEDA
  final lowPrice = MoneyMaskedTextController(
      decimalSeparator: ',', thousandSeparator: '.', leftSymbol: 'R\$ ');

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Stack(
      children: [
        Scaffold(
            body: SizedBox(
          width: MediaQuery.of(context).size.width,
          height: MediaQuery.of(context).size.height,
          child: Container(
            padding: const EdgeInsets.only(top: 80, left: 10),
            child: Column(
              //mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Row(
                  children: [
                    Container(
                      //padding: const EdgeInsets.only(top: 80, left: 10),
                      alignment: Alignment.topLeft,
                      child: Icon(
                        Icons.arrow_back,
                        color: Colors.black,
                        size: 55,
                      ),
                    ),
                  ],
                ),
                Row(
                  children: [
                    Container(
                        padding: const EdgeInsets.only(left: 10),
                        child: Text(
                          'Tipo de combustível',
                          style: TextStyle(fontSize: 17),
                        )),
                    SizedBox(
                      width: 40,
                    ),
                    MyStatefulWidget()
                  ],
                ),
                SizedBox(
                  height: 0,
                ),
                Row(
                  //Coluna 3
                  children: [
                    SizedBox(
                      width: 10,
                    ),
                    Container(
                        height: 80,
                        width: 250,
                        //padding: const EdgeInsets.only(left: 10),
                        child: TextField(
                          controller: lowPrice, //AQUI ESTÁ MEU CONTROLLER
                          style: TextStyle(
                              fontSize: 40, fontWeight: FontWeight.bold),
                          decoration: InputDecoration(
                            //labelText: 'Digite',
                            border: InputBorder.none,
                            focusedBorder: InputBorder.none,
                            enabledBorder: InputBorder.none,
                            errorBorder: InputBorder.none,
                            disabledBorder: InputBorder.none,
                          ),
                          keyboardType: TextInputType.number,
                        )),
                    SizedBox(
                      width: 40,
                    ),
                    Container(
                        height: 60,
                        width: 60,
                        child: ConstrainedBox(
                            constraints: BoxConstraints.expand(),
                            child: IconButton(
                                onPressed: () {
                                  double valor = double.parse(
                                      '${lowPrice.text.split(" ")[1].replaceAll(',', '.')}');
                                  double novovalor = 0;
                                  lowPrice.updateValue(novovalor);
                                },
                                icon: Image.network(
                                    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQeI99kpi7I_KuWkZ8-5uZJnb-RgjXuyVReR2c78zYCEI396flgRg63UFHIwrhe2LolVM&usqp=CAU'))))
                    // Container(
                    //   child: SizedBox(
                    //     height: 45,
                    //     width: 45,
                    //     child: FlatButton(
                    //       onPressed: () {},
                    //       child: Image.network(
                    //         'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQeI99kpi7I_KuWkZ8-5uZJnb-RgjXuyVReR2c78zYCEI396flgRg63UFHIwrhe2LolVM&usqp=CAU',
                    //         fit: BoxFit.contain,
                    //       ),
                    //     ),
                    //   ),
                    // ),
                    // Container(
                    //     child: SizedBox(
                    //   height: 45,
                    //   width: 45,
                    //   child: ElevatedButton(
                    //     onPressed: () {},
                    //     child: Container(
                    //       child: Image.network(
                    //           'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQeI99kpi7I_KuWkZ8-5uZJnb-RgjXuyVReR2c78zYCEI396flgRg63UFHIwrhe2LolVM&usqp=CAU'),
                    //     ),
                    //   ),
                    // )),
                    // ElevatedButton(
                    //   style: ElevatedButton.styleFrom(
                    //       primary: Colors.white,
                    //       side: BorderSide(
                    //         width: 0,
                    //         color: Colors.white,
                    //       )),
                    //   onPressed: () {},
                    //   child: Container(
                    //     height: 50,
                    //     width: 50,
                    //     child: Image.network(
                    //       'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQeI99kpi7I_KuWkZ8-5uZJnb-RgjXuyVReR2c78zYCEI396flgRg63UFHIwrhe2LolVM&usqp=CAU',
                    //       fit: BoxFit.contain,
                    //     ),
                    //   ),
                    // ),
                  ],
                ),
                SizedBox(
                  height: 40,
                ),
                Row(
                  children: [
                    SizedBox(
                      width: 5,
                    ),
                    // AQUI COMEÇA O BOTÃO
                    Container(
                      width: 101,
                      height: 45,
                      child: ElevatedButton(
                        onPressed: () {
                          double valor = double.parse(
                              '${lowPrice.text.split(" ")[1].replaceAll(',', '.')}');
                          double novovalor = valor + 30;
                          lowPrice.updateValue(novovalor);
                        },
                        child: Text(
                          '+ R\$ 30',
                          style: TextStyle(
                              color: Colors.black,
                              fontWeight: FontWeight.bold,
                              fontSize: 20),
                        ),
                        style: ElevatedButton.styleFrom(
                            shape: RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(10.0)),
                            side: BorderSide(
                              width: 2.0,
                              color: Colors.black,
                            ),
                            primary: Colors.white),
                      ),
                    ),
                    // AQUI TERMINA O BOTÃO
                    SizedBox(
                      width: 25,
                    ),
                    Container(
                      width: 101,
                      height: 45,
                      child: ElevatedButton(
                        onPressed: () {
                          double valor = double.parse(
                              '${lowPrice.text.split(" ")[1].replaceAll(',', '.')}');
                          double novovalor = valor + 50;
                          lowPrice.updateValue(novovalor);
                        },
                        child: Text(
                          '+ R\$ 50',
                          style: TextStyle(
                              color: Colors.black,
                              fontWeight: FontWeight.bold,
                              fontSize: 20),
                        ),
                        style: ElevatedButton.styleFrom(
                            shape: RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(10.0)),
                            side: BorderSide(
                              width: 2.0,
                              color: Colors.black,
                            ),
                            primary: Colors.white),
                      ),
                    ),
                    SizedBox(
                      width: 25,
                    ),
                    Container(
                      width: 113,
                      height: 45,
                      child: ElevatedButton(
                        onPressed: () {
                          double valor = double.parse(
                              '${lowPrice.text.split(" ")[1].replaceAll(',', '.')}');
                          double novovalor = valor + 100;
                          lowPrice.updateValue(novovalor);
                        },
                        child: Text(
                          '+ R\$ 100',
                          style: TextStyle(
                              color: Colors.black,
                              fontWeight: FontWeight.bold,
                              fontSize: 20),
                        ),
                        style: ElevatedButton.styleFrom(
                            shape: RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(10.0)),
                            side: BorderSide(
                              width: 2.0,
                              color: Colors.black,
                            ),
                            primary: Colors.white),
                      ),
                    ),
                  ],
                ),
                SizedBox(
                  height: 138,
                ),
                // Container(
                //   child: Center(
                //     child: Text(
                //       'Avançar',
                //       style: TextStyle(
                //           fontSize: 20,
                //           color: Colors.black,
                //           fontWeight: FontWeight.bold),
                //       textAlign: TextAlign.center,
                //     ),
                //   ),
                //   color: Colors.grey,
                //   height: 90.0,
                //   width: MediaQuery.of(context).size.width,
                // ),
              ],
            ),
          ),
        )),
        Padding(
          padding: const EdgeInsets.only(top: 500.0),
          child: Container(
            child: Center(
              child: Text(
                'Avançar',
                style: TextStyle(
                    fontSize: 20,
                    color: Colors.grey.shade700,
                    fontWeight: FontWeight.bold,
                    decorationColor: Colors.grey.shade300),
                textAlign: TextAlign.center,
              ),
            ),
            color: Colors.grey.shade300,
            height: 80,
            width: MediaQuery.of(context).size.width,
          ),
        ),
      ],
    );
  }
}

class MyStatefulWidget extends StatefulWidget {
  const MyStatefulWidget({key}) : super(key: key);

  @override
  _MyStatefulWidgetState createState() => _MyStatefulWidgetState();
}

class _MyStatefulWidgetState extends State<MyStatefulWidget> {
  String dropdownValue = 'Gasolina Original';

  @override
  Widget build(BuildContext context) {
    return DropdownButton<String>(
      value: dropdownValue,
      icon: Transform.rotate(
        angle: -90 * math.pi / 180,
        child: Container(
          padding: const EdgeInsets.only(left: 10),
          child: const Icon(
            Icons.arrow_back_ios,
            color: Colors.black,
          ),
        ),
      ),
      iconSize: 24,
      elevation: 16,
      style: const TextStyle(
          color: Colors.black, fontWeight: FontWeight.bold, fontSize: 17),
      underline: Container(
        height: 2,
        color: Colors.white10,
      ),
      onChanged: (String newValue) {
        setState(() {
          var s = dropdownValue = newValue;
        });
      },
      items: <String>[
        'Gasolina Original',
        'Gasolina DT Clean',
        'Gasolina Octapro',
        'Etanol',
        'Etanol Aditivado',
        'Diesel',
        'Diesel RendMax',
        'Gás Natural'
      ].map<DropdownMenuItem<String>>((String value) {
        return DropdownMenuItem<String>(
          value: value,
          child: Text(
            value,
            textAlign: TextAlign.center,
          ),
        );
      }).toList(),
    );
  }
}
