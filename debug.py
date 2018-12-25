# -*- coding: utf-8 -*-
import sys
sys.path.append('app');
from app import app

if __name__ == "__main__":
    #NOTE: Não é seguro esse host, coloquei so para usar meu computador para
    #NOTE: hospedar o site temporariamente
    #NOTE: TIRAR
    app.run(debug=True, host='0.0.0.0')
    app.run(debug=True)
