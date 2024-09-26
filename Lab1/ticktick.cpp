// La primera línea de entrada contiene la hora actual en formato hh:mm:ss (horas, minutos, segundos). Las horas estarán entre 
// 0
// 0 y 
// 23
// 23 (inclusive) y los minutos y segundos entre 
// 0
// 0 y 
// 59
// 59. La segunda línea contiene la hora de la explosión en el mismo formato.

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    string hora;
    cin >> hora;
    string horaExplosion;
    cin >> horaExplosion;

    if (hora == horaExplosion){
        cout << "24:00:00" << endl;
        return 0;
    }
    
    int horas = stoi(hora.substr(0, 2));
    int minutos = stoi(hora.substr(3, 2));
    int segundos = stoi(hora.substr(6, 2));

    int horasExplosion = stoi(horaExplosion.substr(0, 2));
    int minutosExplosion = stoi(horaExplosion.substr(3, 2));
    int segundosExplosion = stoi(horaExplosion.substr(6, 2));

    string horasOutput;
    string minutosOutput;
    string segundosOutput;

    
    
    
    if (segundosExplosion < segundos) {
        segundosOutput = to_string(60 - segundos + segundosExplosion);
        minutosExplosion -=1 ;
    
    } else {
        segundosOutput = to_string(segundosExplosion - segundos);
    }

    if (minutosExplosion < minutos) {
        minutosOutput = to_string(60 - minutos + minutosExplosion);
        horasExplosion -= 1;
    } else {
        minutosOutput = to_string(minutosExplosion - minutos);
    }

    if (horasExplosion < horas) {
        horasOutput = to_string(24 - horas + horasExplosion);
    } else {
        horasOutput = to_string(horasExplosion - horas);
    }


    if (horasOutput.size() == 1) {
        horasOutput = "0" + horasOutput;
    }
    if (minutosOutput.size() == 1) {
        minutosOutput = "0" + minutosOutput;
    }

    if (segundosOutput.size() == 1) {
        segundosOutput = "0" + segundosOutput;
    }

    cout << horasOutput << ":" << minutosOutput << ":" << segundosOutput << endl;
    return 0;
}









