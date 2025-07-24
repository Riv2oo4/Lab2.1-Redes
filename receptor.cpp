#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

// Función para verificar y corregir errores en una trama Hamming 
tuple<string, bool, int> verificar_y_corregir_hamming(const string& trama) {
    vector<int> bits;
    for (char c : trama) {
        bits.push_back(c - '0');
    }

    // Posiciones de bits
    vector<int> posiciones_paridad = {0, 1, 3, 7};

    int error_pos = 0;
    for (int i = 0; i < posiciones_paridad.size(); ++i) {
        int p = posiciones_paridad[i];
        int suma = 0;
        for (int j = 0; j < bits.size(); ++j) {
            if (j != p && ((j + 1) & (1 << i))) {
                suma ^= bits[j];
            }
        }
        if (suma != bits[p]) {
            error_pos += (1 << i);
        }
    }

    bool corregido = false;
    if (error_pos > 0 && error_pos <= bits.size()) {
        cout << "Error detectado en la posición " << error_pos << ". Corrigiendo..." << endl;
        bits[error_pos - 1] ^= 1;
        corregido = true;
    }

    // Extraer los bits de datos
    string mensaje_original = "";
    for (int i = 0; i < bits.size(); ++i) {
        if (find(posiciones_paridad.begin(), posiciones_paridad.end(), i) == posiciones_paridad.end()) {
            mensaje_original += to_string(bits[i]);
        }
    }

    return {mensaje_original, corregido, error_pos};
}

void procesar_receptor(const string& archivo) {
    ifstream file(archivo);
    if (!file) {
        cerr << "No se pudo abrir el archivo receptor.txt" << endl;
        return;
    }

    string linea;
    int num_trama = 1;

    while (getline(file, linea)) {
        if (linea.empty()) continue;

        auto [mensaje, corregido, posicion] = verificar_y_corregir_hamming(linea);

        cout << "Trama " << num_trama << ": " << linea << endl;
        if (corregido) {
            cout << "- Error corregido en bit " << posicion << ". Mensaje original: " << mensaje << endl << endl;
        } else {
            cout << "- Sin errores. Mensaje original: " << mensaje << endl << endl;
        }

        num_trama++;
    }

    file.close();
}

int main() {
    procesar_receptor("receptor.txt");
    return 0;
}

// Ejecutar:
// g++ receptor.cpp -std=c++17 -o receptor
// ./receptor
